#include "discretedistribution.h"
#include "gslrandomnumbergenerator.h"
#include <iostream>
#include <cmath>
#include <stdlib.h>

DiscreteDistribution::DiscreteDistribution(std::vector<double> &binStarts,
		                           std::vector<double> &histValues, 
		                           GslRandomNumberGenerator *pRndGen)
{
	m_histSums.resize(histValues.size());
	m_binStarts.resize(binStarts.size() + 1); // allocate one more for the start of the next one

	double lastValue = histValues[m_histSums.size()-1];

	if (std::abs(lastValue) > 1e-7) // last one should be about zero for everything to make sense
	{
		std::cerr << "DiscreteDistribution: ERROR: last value should be nearly zero, but is " << lastValue << std::endl;
		exit(-1);
	}
	double sum = 0;
	for (int i = 0 ; i < histValues.size() ; i++)
	{
		sum += histValues[i];
		m_histSums[i] = sum;
		m_binStarts[i] = binStarts[i];
	}

	int lastPos = histValues.size() - 1;
	m_binStarts[lastPos+1] = binStarts[lastPos] + (binStarts[lastPos] - binStarts[lastPos-1]); 

	for (int i = 0 ; i < histValues.size() ; i++)
	{
		// Check that the bin start values are ascending
		if (!(m_binStarts[i+1] > m_binStarts[i]))
		{
			std::cerr << "DiscreteDistribution: ERROR: bin start values must be increasing!" << std::endl;
			exit(-1);
		}
	}

//	std::cerr << "extra bin start: " << m_binStarts[lastPos+1] << std::endl;

	m_totalSum = sum;
	m_pRndGen = pRndGen;
}

DiscreteDistribution::~DiscreteDistribution()
{
}

double DiscreteDistribution::pickNumber() const
{
	double r = m_pRndGen->pickRandomDouble() * m_totalSum;
	int foundBin = -1;

	for (int i = 0 ; i < m_histSums.size() ; i++)
	{
		if (r < m_histSums[i] || i == m_histSums.size()-1)
		{
			foundBin = i;
			break;
		}
	}

	double startValue = 0;
	double endValue = m_histSums[foundBin]; // we've allocated one more for this

	if (foundBin > 0)
		startValue = m_histSums[foundBin-1];

	double frac = (r-startValue)/(endValue-startValue);

	if (frac < 0)
		frac = 0;
	else if (frac > 1.0)
		frac = 1.0;

	double binStart = m_binStarts[foundBin];
	double binEnd = m_binStarts[foundBin+1]; // we've allocated one position more, so this is ok
	double binSize = binEnd - binStart;

	return binStart + frac*binSize;
}
