#include "grayworldestimator.h"
#include "common/color.h"
#include "common/derivative.h"
#include "common/mask.h"
#include "common/statistics.h"
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

namespace illumestimators {

GrayWorldEstimator::GrayWorldEstimator(int n, int p, double sigma) :
	m_n(n),
	m_p(p),
	m_sigma(sigma)
{

}

GrayWorldEstimator::~GrayWorldEstimator()
{

}

std::string GrayWorldEstimator::name() const
{
	std::stringstream name;
	name << "GrayWorldEstimator(n = " << m_n << ", p = " << m_p << ", sigma = " << m_sigma << ")";

	return name.str();
}

std::string GrayWorldEstimator::identifier() const
{
	std::stringstream identifier;
	identifier << "grayworld-" << m_n << "-" << m_p << "-" << m_sigma;

	return identifier.str();
}

Illum GrayWorldEstimator::minkowskiNorm(const std::vector<cv::Vec3d>& pixels, int p) const
{
	cv::Vec3d estimate;

	for (std::vector<cv::Vec3d>::const_iterator it = pixels.begin(); it != pixels.end(); it++) {
		for (int i = 0; i < 3; i++) {
			estimate[i] += pow((*it)[i], p);
		}
	}

	const int size = pixels.size();

	for (int i = 0; i < 3; i++) {
		estimate[i] = pow(estimate[i], 1 / (double) p) / size;
	}

	Illum result(estimate[2], estimate[1], estimate[0]); // attention: bgr for a rgb constructor

	return result;
}

void GrayWorldEstimator::preprocessImage(const cv::Mat_<cv::Vec3d>& image, const cv::Mat_<unsigned char>& mask, cv::Mat_<cv::Vec3d> &inputImage, cv::Mat_<unsigned char> &inputMask) const
{
	inputImage = image.clone();
	inputMask = mask.clone();
	if ((image.rows != mask.rows) || (image.cols != mask.cols)) {
		inputMask = cv::Mat_<unsigned char>(inputImage.rows, inputImage.cols, (unsigned char)0);
	}

	Mask::maskSaturatedPixels(inputImage, inputMask, 1);

	cv::Mat_<unsigned char> element = cv::Mat_<unsigned char>::ones(3, 3);
	cv::dilate(inputMask, inputMask, element);

	const double kernelsize = cvRound(m_sigma * 3 * 2 + 1) | 1;
	Mask::maskBorderPixels(inputImage, inputMask, (kernelsize + 1) / 2);

	if (m_sigma > 0) {
		if (m_n == 0) {
			const double kernelsize = cvRound(m_sigma * 3 * 2 + 1) | 1;
			cv::GaussianBlur(inputImage, inputImage, cv::Size(kernelsize, kernelsize), m_sigma, m_sigma);
		} else if (m_n > 0) {
			inputImage = Derivative::normDerivativeFilter(inputImage, m_n, m_sigma);
		}
	}
}

Illum GrayWorldEstimator::estimateIlluminant(const cv::Mat_<cv::Vec3d>& image, const cv::Mat_<unsigned char>& mask) const
{
	cv::Vec3d estimate;

	if ((image.rows != mask.rows) || (image.cols != mask.cols)) {
		return Illum();
	}

	if ((m_n < 0) || (m_n > 2) || (m_p < -1) || (m_p == 0) || (m_sigma < 0)) {
		std::cerr << "Bad parameters for calling GrayWorldEstimator!" << std::endl;
	}

	const std::vector<cv::Vec3d> pixels = Mask::unmaskedPixels(image, mask);

	if (m_p == -1) {
		estimate = Color::calculateChromaticities(Statistics::max(pixels));
	} else if (m_p == 1) {
		estimate = Color::calculateChromaticities(Statistics::mean(pixels));
	} else if (m_p > 0) {
		return Color::calculateChromaticities(minkowskiNorm(pixels, m_p));
	}
	return Illum(estimate[2], estimate[1], estimate[0]); // attention: bgr for a rgb constructor
}

Illum GrayWorldEstimator::estimateIlluminant(const cv::Mat_<cv::Vec3d>& image, const superpixels::Superpixel &superpixel, const cv::Mat_<unsigned char>& mask) const
{
	cv::Vec3d estimate;

	if ((m_n < 0) || (m_n > 2) || (m_p < -1) || (m_p == 0) || (m_sigma < 0)) {
		std::cerr << "Bad parameters for calling GrayWorldEstimator!" << std::endl;
	}

//	cv::Mat_<cv::Vec3d> inputImage = image.clone();
//	cv::Mat_<unsigned char> inputMask = mask.clone();

//	preprocessImage(inputImage, inputMask);

//	if (m_sigma > 0) {
//		if (m_n == 0) {
//			const double kernelsize = cvRound(m_sigma * 3 * 2 + 1) | 1;
//			cv::GaussianBlur(inputImage, inputImage, cv::Size(kernelsize, kernelsize), m_sigma, m_sigma);
//		} else if (m_n > 0) {
//			inputImage = Derivative::normDerivativeFilter(inputImage, m_n, m_sigma);
//		}
//	}

	const std::vector<cv::Vec3d> pixels = Mask::unmaskedPixels(image, superpixel, mask);
	if (pixels.size() == 0) return Illum();

	if (m_p == -1) {
		estimate = Color::calculateChromaticities(Statistics::max(pixels));
	} else if (m_p == 1) {
		estimate = Color::calculateChromaticities(Statistics::mean(pixels));
	} else if (m_p > 0) {
		Illum ill = Color::calculateChromaticities(minkowskiNorm(pixels, m_p));
		return ill;
	}

	return Illum(estimate[2], estimate[1], estimate[0]); // attention: bgr for a rgb constructor
}

bool GrayWorldEstimator::train(const std::vector<std::string>&, const std::vector<std::string>&, const std::vector<cv::Vec3d>&, const std::vector<std::string>&)
{
	return true;
}

bool GrayWorldEstimator::save(const std::string& filename) const
{
	cv::FileStorage	fs(filename, cv::FileStorage::WRITE);

	if (!fs.isOpened()) {
		return false;
	}

	fs << "name" << "GrayWorldEstimator";
	fs << "n" << m_n;
	fs << "p" << m_p;
	fs << "sigma" << m_sigma;

	return true;
}

bool GrayWorldEstimator::load(const std::string& filename)
{
	cv::FileStorage	fs(filename, cv::FileStorage::READ);

	if (!fs.isOpened()) {
		return false;
	}

	std::string name = fs["name"];

	if (name != "GrayWorldEstimator") {
		return false;
	}

	m_n = fs["n"];
	m_p = fs["p"];
	m_sigma = fs["sigma"];

	return true;
}

int GrayWorldEstimator::error() {
	return 0;
}

} // namespace illumestimators
