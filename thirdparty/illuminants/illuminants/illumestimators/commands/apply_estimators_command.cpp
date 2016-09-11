#include <iostream>
#include <fstream>
#include <opencv2/highgui/highgui.hpp>

#include "apply_estimators_command.h"
#include "iic.h"
#include "iebv.h"
#include "felzenszwalb/felzenszwalbsegmentation.h"
#include "veksler/vekslersegmentation.h"
#include "normal_image.h"
#include "db_index_shida.h"
#include "grayworld/grayworldestimator.h"
#include "bayesian/bayesianestimator.h"
#include "gamutmapping/gamutmapping2destimator.h"
#include "evaluation/error2.h"
#include "illuminantestimator.h" // for cleanlyReadImage()

namespace illumestimators {


CommandApplyEstimators::CommandApplyEstimators()
 : vole::Command(
		"apIllEst",
		config,
		"Christian Riess",
		"christian.riess@informatik.uni-erlangen.de")
{
}

// TODO: Doppelung mit gt_multi_illum/commands/command_batch*.cpp
bool CommandApplyEstimators::read_normalized_16_bit(std::string filename, cv::Mat_<cv::Vec3d> &img, int &minVal, int &maxVal)
{
	img = cv::imread(filename, -1 /* read as-is (16 bit, breaks if image has alpha channel) */);
	if (img.data == NULL) {
		std::cerr << "unable to read 16 bit image " << img << " (note: image must be RGB, 16 bits, no alpha channel)" << std::endl;
		return false;
	}
	maxVal = -1;
	minVal = 56; // note that some values become negative due to this threshold
	img = vole::NormalImage::normalize((cv::Mat_<cv::Vec3s>)img, minVal, maxVal);
//	config.min_intensity = minVal;
//	config.max_intensity = maxVal;

	return true;
}


int CommandApplyEstimators::execute() {
	if (config.output_path.length() < 1) { std::cerr << "output path (--output) must be set; aborted." << std::endl; return 1; }
	if ((config.gamut || config.bayes) == false) { std::cerr << "select a method (--gamut or --bayes)" << std::endl; return 1; }

	if (config.gamut) {
		std::cout << "doing gamut mapping" << std::endl;
		cv::Mat_<double> gamut_error = completeGamutShida();
	}
	if (config.bayes) {
		std::cout << "doing bayesian stuff" << std::endl;
		cv::Mat_<double> bayes_error = completeBayesShida();
	}
	if (config.grayworld_vanilla) {
		std::cout << "doing gray world vanilla" << std::endl;
		cv::Mat_<double> gw_vanilla_error = completeGwShida(0);
	}
	if (config.grayworld_first_order) {
		std::cout << "doing 1st order gray world" << std::endl;
		cv::Mat_<double> gw_first_error = completeGwShida(1);
	}
	if (config.grayworld_second_order) {
		std::cout << "doing 2nd order gray world" << std::endl;
		cv::Mat_<double> gw_second_error = completeGwShida(2);
	}
	if (config.grayworld_best) {
		std::cout << "doing looking for best gray world" << std::endl;
		cv::Mat_<double> gw_best_error = completeGwShida(-1);
	}
	if (config.white_patch_retinex) {
		std::cout << "doing white patch retinex" << std::endl;
		cv::Mat_<double> wp_retinex_error = completeGwShida(-2);
	}

		return 0;
}

// returns: errors
cv::Mat_<double> CommandApplyEstimators::completeGwShida(int derivative) {
	// FIXME IMPLEMENT ME

	return cv::Mat_<double>();
}

// returns: errors
cv::Mat_<double> CommandApplyEstimators::completeGamutShida() {
	gtmi::DbIndexShida index;
	std::vector<gtmi::SCENE> scenes = index.getScenes();
	std::vector<gtmi::ILLUM> illums = index.getIllums();

	int minVal = 56; int maxVal = -1;
	cv::Mat_<cv::Vec3d> normalized_image, ground_truth;
	// leave-one-scene-out training
	for (int eval_scene_idx = 1; eval_scene_idx < (int)scenes.size(); ++eval_scene_idx) {
		GamutMapping2DEstimator est(GamutMapping2DEstimator::MAX, 0, 0); // vary method: MEAN, MEDIAN --- choose n, sigma
		for (int tr_scene_idx = 1; tr_scene_idx < (int)scenes.size(); ++tr_scene_idx) {
			if (eval_scene_idx == tr_scene_idx) continue;

			for (int i1_idx = 0; i1_idx < (int)illums.size(); ++i1_idx) {
				for (int i2_idx = 0; i2_idx < (int)illums.size(); ++i2_idx) {
					if (index.gtLookup(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]) == NULL) continue;

					read_normalized_16_bit(index.lookupWithPath(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]), normalized_image, minVal, maxVal);
					read_normalized_16_bit(index.gtLookupWithPath(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]), ground_truth, minVal, maxVal);

					superpixels::VekslerSegmentation segV(40);
					std::vector<superpixels::Superpixel> segmentation = segV.superpixels((cv::Mat_<cv::Vec3d>)normalized_image);

						// DELETE_ME_SOON
					cv::Mat_<cv::Vec3d> gt_image;

					// compute average ground truth for superpixels
					std::vector<cv::Vec3d> gt_values;
					getSuperpixelGroundTruth(ground_truth, segmentation, gt_values, gt_image);	

					// feed ground truth to training
					cv::Mat_<unsigned char> mask(normalized_image.rows, normalized_image.cols, (unsigned char)0);
					est.preprocessImage(normalized_image, mask);
					est.addTrainingData(normalized_image, segmentation, gt_values, mask);
				}
			}
		}
		est.finalizeTraining();
	
		// eval on last remaining scene

		for (int i1_idx = 0; i1_idx < (int)illums.size(); ++i1_idx) {
			for (int i2_idx = 0; i2_idx < (int)illums.size(); ++i2_idx) {
				if (index.gtLookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) == NULL) continue;

				read_normalized_16_bit(index.lookupWithPath(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]), normalized_image, minVal, maxVal);
				read_normalized_16_bit(index.gtLookupWithPath(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]), ground_truth, minVal, maxVal);

				superpixels::VekslerSegmentation segV(40);
				std::vector<superpixels::Superpixel> segmentation = segV.superpixels((cv::Mat_<cv::Vec3d>)normalized_image);

				// show ground truth image
					// DELETE_ME_SOON
				cv::Mat_<cv::Vec3d> gt_image;

				// compute average ground truth for superpixels
				std::vector<cv::Vec3d> gt_values;
				getSuperpixelGroundTruth(ground_truth, segmentation, gt_values, gt_image);	
					cv::imwrite("/tmp/test_gt.png", gt_image*255); // DELETE_ME_SOON

				// feed ground truth to training

				std::vector<cv::Vec3d> illuminants;
				cv::Mat_<unsigned char> mask(normalized_image.rows, normalized_image.cols, (unsigned char)0);
				est.preprocessImage(normalized_image, mask);
				est.estimateIlluminants(normalized_image, segmentation, illuminants, mask);
				cv::Mat_<double> errors(4, illuminants.size(), -1.0);
				compute_illuminant_error(illuminants, gt_values, errors);

				// write colorized image
				cv::Mat_<cv::Vec3b> estimationImage(normalized_image.rows, normalized_image.cols, cv::Vec3b(0, 0, 0));
				for (int i = 0; i < (int)segmentation.size(); ++i) {
					std::vector<cv::Point> &coord = segmentation[i].coordinates;
					double norm = illuminants[i][0] + illuminants[i][1] + illuminants[i][2];
					for (int j = 0; j < (int)coord.size(); ++j) {
						for (int c = 0; c < 3; ++c) 
							estimationImage[coord[j].y][coord[j].x][c] = 255 * illuminants[i][c] / norm;
					}
				}
				// get output image path
				std::string outfile;
				{	std::stringstream s;
					s << config.output_path << "/" << "est_gamut2d_" << *index.lookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) << ".png";
					outfile = s.str();
				}
				cv::imwrite(outfile, estimationImage);

				std::ofstream out;
				{	std::stringstream s;
					s << config.output_path << "/" << "est_gamut2d_" << *index.lookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) << "_numbers.txt";
					outfile = s.str();
				}
				out.open(outfile.c_str());
				for (int i = 0; i < (int)illuminants.size(); ++i) {
					out << illuminants[i][0] <<" "<< illuminants[i][1] <<" "<< illuminants[i][2] << " ";
					out << gt_values[i][0] <<" "<< gt_values[i][1] <<" "<< gt_values[i][2];
					for (int j = 0; j < errors.rows; ++j) out << " " << errors[j][i];
					out << std::endl;
				}
				out.close();
			}
		}
	}
	// FIXME
	return cv::Mat_<double>();

}

// returns: errors
cv::Mat_<double> CommandApplyEstimators::completeBayesShida() {
	gtmi::DbIndexShida index;
	std::vector<gtmi::SCENE> scenes = index.getScenes();
	std::vector<gtmi::ILLUM> illums = index.getIllums();

	int minVal = 56; int maxVal = -1;
	cv::Mat_<cv::Vec3d> normalized_image, ground_truth;
	// leave-one-scene-out training
	for (int eval_scene_idx = 1; eval_scene_idx < (int)scenes.size(); ++eval_scene_idx) {
		if (eval_scene_idx > 1) break;
		BayesianEstimator est(BayesianEstimator::POSTERIOR_MEAN); // vary method: MIN_AVERAGE_LOSS_ANGULAR, MIN_AVERAGE_LOSS_EUCLIDEAN
		for (int tr_scene_idx = 1; tr_scene_idx < (int)scenes.size(); ++tr_scene_idx) {
			if (eval_scene_idx == tr_scene_idx) continue;

			for (int i1_idx = 0; i1_idx < (int)illums.size(); ++i1_idx) {
				for (int i2_idx = 0; i2_idx < (int)illums.size(); ++i2_idx) {
					if (index.gtLookup(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]) == NULL) continue;

					read_normalized_16_bit(index.lookupWithPath(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]), normalized_image, minVal, maxVal);
					read_normalized_16_bit(index.gtLookupWithPath(scenes[tr_scene_idx], illums[i1_idx], illums[i2_idx]), ground_truth, minVal, maxVal);

					superpixels::VekslerSegmentation segV(40);
					std::vector<superpixels::Superpixel> segmentation = segV.superpixels((cv::Mat_<cv::Vec3d>)normalized_image);

						// DELETE_ME_SOON
					cv::Mat_<cv::Vec3d> gt_image;

					// compute average ground truth for superpixels
					std::vector<cv::Vec3d> gt_values;
					getSuperpixelGroundTruth(ground_truth, segmentation, gt_values, gt_image);	

					// feed ground truth to training
					cv::Mat_<unsigned char> mask(normalized_image.rows, normalized_image.cols, (unsigned char)0);
					est.preprocessImage(normalized_image, mask);
					est.addTrainingData(normalized_image, segmentation, gt_values, mask);
				}
			}
		}
		est.finalizeTraining();
	
		// eval on last remaining scene

		for (int i1_idx = 0; i1_idx < (int)illums.size(); ++i1_idx) {
			for (int i2_idx = 0; i2_idx < (int)illums.size(); ++i2_idx) {
				if (index.gtLookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) == NULL) continue;

				read_normalized_16_bit(index.lookupWithPath(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]), normalized_image, minVal, maxVal);
				read_normalized_16_bit(index.gtLookupWithPath(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]), ground_truth, minVal, maxVal);

				superpixels::VekslerSegmentation segV(40);
				std::vector<superpixels::Superpixel> segmentation = segV.superpixels((cv::Mat_<cv::Vec3d>)normalized_image);

				// show ground truth image
					// DELETE_ME_SOON
				cv::Mat_<cv::Vec3d> gt_image;

				// compute average ground truth for superpixels
				std::vector<cv::Vec3d> gt_values;
				getSuperpixelGroundTruth(ground_truth, segmentation, gt_values, gt_image);	
					cv::imwrite("/tmp/test_gt.png", gt_image*255); // DELETE_ME_SOON

				// feed ground truth to training

				std::vector<cv::Vec3d> illuminants;
				cv::Mat_<unsigned char> mask(normalized_image.rows, normalized_image.cols, (unsigned char)0);
				est.preprocessImage(normalized_image, mask);
				est.estimateIlluminants(normalized_image, segmentation, illuminants, mask);
				cv::Mat_<double> errors(4, illuminants.size(), -1.0);
				compute_illuminant_error(illuminants, gt_values, errors);

				// write colorized image
				cv::Mat_<cv::Vec3b> estimationImage(normalized_image.rows, normalized_image.cols, cv::Vec3b(0, 0, 0));
				for (int i = 0; i < (int)segmentation.size(); ++i) {
					std::vector<cv::Point> &coord = segmentation[i].coordinates;
					double norm = illuminants[i][0] + illuminants[i][1] + illuminants[i][2];
					if (fabs(norm) <= std::numeric_limits<double>::epsilon()) norm = 1;
					for (int j = 0; j < (int)coord.size(); ++j) {
						for (int c = 0; c < 3; ++c) 
							estimationImage[coord[j].y][coord[j].x][c] = 255 * illuminants[i][c] / norm;
					}
				}
				// get output image path
				std::string outfile;
				{
					std::stringstream s;
					s << config.output_path << "/" << "est_bayes_" << *index.lookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) << ".png";
					outfile = s.str();
				}
				cv::imwrite(outfile, estimationImage);
				std::ofstream out;
				{
					std::stringstream s;
					s << config.output_path << "/" << "est_bayes_" << *index.lookup(scenes[eval_scene_idx], illums[i1_idx], illums[i2_idx]) << "_numbers.txt";
					outfile = s.str();
				}
				out.open(outfile.c_str());
				for (int i = 0; i < (int)illuminants.size(); ++i) {
					out << illuminants[i][0] <<" "<< illuminants[i][1] <<" "<< illuminants[i][2];
					for (int j = 0; j < errors.rows; ++j) {
						out << " " << errors[j][i];
					}
					out << std::endl;
				}
				out.close();
			}
		}
	}
	// FIXME
	return cv::Mat_<double>();
}


void CommandApplyEstimators::compute_illuminant_error(std::vector<cv::Vec3d> &illuminants, std::vector<cv::Vec3d> &gt_values, cv::Mat_<double> &errors)
{
	int nMetrics = 5;
	errors = cv::Mat_<double>(nMetrics, illuminants.size());
	for (int i = 0; i < (int)illuminants.size(); ++i) {
		errors[0][i] = Error2::toAngularErrorDeg(illuminants[i], gt_values[i]);
		errors[1][i] = Error2::toRgError(illuminants[i], gt_values[i]);
		errors[2][i] = Error2::toRMSE(illuminants[i], gt_values[i]);
		errors[3][i] = Error2::toRError(illuminants[i], gt_values[i]);
		errors[4][i] = Error2::toGError(illuminants[i], gt_values[i]);
	}
}

void CommandApplyEstimators::getSuperpixelGroundTruth(
	cv::Mat_<cv::Vec3d> &ground_truth, std::vector<superpixels::Superpixel> &segmentation,
	std::vector<cv::Vec3d> &gt_values, cv::Mat_<cv::Vec3d> &sp_gt_image)
{
	gt_values.assign(segmentation.size(), cv::Vec3d(0, 0, 0));
	sp_gt_image = cv::Mat_<cv::Vec3d>(ground_truth.rows, ground_truth.cols, cv::Vec3d(0, 0, 0));

	for (int i = 0; i < (int)segmentation.size(); ++i) {
		int pixel_count = 0;
		cv::Vec3d sum;
		std::vector<cv::Point> &coordinates = segmentation[i].coordinates;
		for (int j = 0; j < (int)coordinates.size(); ++j) {
			cv::Point &p = coordinates[j];
			if (ground_truth[p.y][p.x][0] + ground_truth[p.y][p.x][1] + ground_truth[p.y][p.x][2] < 0.1) continue;
			pixel_count++;
			sum += ground_truth[p.y][p.x];
		}
		if (pixel_count > 0)
			for (int c = 0; c < 3; ++c)
				gt_values[i][c] = sum[c] / pixel_count;

		// DELETE_ME_SOON
		for (int j = 0; j < (int)coordinates.size(); ++j) {
			cv::Point &p = coordinates[j];
			sp_gt_image[p.y][p.x] = gt_values[i];
		}

	}
}

void CommandApplyEstimators::printShortHelp() const {
	std::cout << "Illuminant Estimation by Voting (modularized version)" << std::endl;
}

void CommandApplyEstimators::printHelp() const {
	std::cout << "Illuminant Estimation by Voting (modularized version)" << std::endl;
}



}
