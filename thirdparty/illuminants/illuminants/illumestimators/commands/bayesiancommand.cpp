#include "bayesiancommand.h"
#include "bayesian/bayesianestimator.h"
#include "metadata/metadatastorage.h"
#include "pipeline/single_illuminant_pipeline.h"
#include <opencv2/highgui/highgui.hpp>

namespace illumestimators {

BayesianCommand::BayesianCommand():
	Command("Bayesian",
		config,
		"Tiago Carvalho",
		"tiagojc@gmail.com"
	)
{
}

int BayesianCommand::execute()
{
	illumestimators::BayesianEstimator estimator(config.n, config.p, config.sigma);

	SingleIlluminantPipeline::loadIlluminantEstimator(estimator, config.loadFile);

	MetadataStorage storage(config.metaFiles);

	Illum estimate;
	double error;

	if (!SingleIlluminantPipeline::runEstimator(estimate, error, estimator, config.inputFile, storage, config.verbosity)) {
		return -1;
	}

	SingleIlluminantPipeline::saveIlluminantEstimator(estimator, config.saveFile);

	return 0;
}

void BayesianCommand::printShortHelp() const
{
	std::cout << "Bayesian illuminant estimator." << std::endl;
}

void BayesianCommand::printHelp() const
{
	std::cout << "Bayesian illuminant estimator." << std::endl;
}

} // namespace illumestimators
