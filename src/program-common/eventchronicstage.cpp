#include "eventchronicstage.h"
#include "eventformation.h"
#include "eventaidsstage.h"
#include "gslrandomnumbergenerator.h"
#include "jsonconfig.h"
#include <stdio.h>
#include <iostream>

EventChronicStage::EventChronicStage(Person *pPerson) : SimpactEvent(pPerson)
{
}

EventChronicStage::~EventChronicStage()
{
}

double EventChronicStage::getNewInternalTimeDifference(GslRandomNumberGenerator *pRndGen, const State *pState)
{
	const SimpactPopulation &population = SIMPACTPOPULATION(pState);
	Person *pPerson = getPerson(0);

	assert(pPerson != 0);
	assert(getNumberOfPersons() == 1);
	assert(pPerson->isInfected());

	assert(m_acuteTime > 0); 

	double tEvt = pPerson->getInfectionTime() + m_acuteTime;
	double dt = tEvt - population.getTime();
	
	assert(dt >= 0); // should not be in the past!

	// Here we'll add a small amount of randomness to make comparison between versions easier

	return dt + pRndGen->pickRandomDouble()*1.0/365.0;
}

std::string EventChronicStage::getDescription(double tNow) const
{
	Person *pPerson = getPerson(0);
	char str[1024];

	sprintf(str, "Chronic infection stage for %s", pPerson->getName().c_str());
	return std::string(str);

}

void EventChronicStage::writeLogs(double tNow) const
{
	Person *pPerson = getPerson(0);
	writeEventLogStart(true, "chronicstage", tNow, pPerson, 0);
}

void EventChronicStage::fire(State *pState, double t)
{
	SimpactPopulation &population = SIMPACTPOPULATION(pState);
	assert(getNumberOfPersons() == 1);

	Person *pPerson = getPerson(0);
	assert(pPerson->getInfectionStage() == Person::Acute);

	pPerson->setInChronicStage();

	// Schedule the event that will mark the start of the AIDS stage
	EventAIDSStage *pEvt = new EventAIDSStage(pPerson, false);
	population.onNewEvent(pEvt);
}

double EventChronicStage::m_acuteTime = -1;

void EventChronicStage::processConfig(ConfigSettings &config)
{
	if (!config.getKeyValue("chronicstage.acutestagetime", m_acuteTime, 0))
		abortWithMessage(config.getErrorString());
}

void EventChronicStage::obtainConfig(ConfigWriter &config)
{
	if (!config.addKey("chronicstage.acutestagetime", m_acuteTime))
		abortWithMessage(config.getErrorString());
}

JSONConfig chronicStageJSONConfig(R"JSON(
        "EventChronicStage": { 
            "depends": null,
            "params": [ ["chronicstage.acutestagetime", 0.25 ] ],
            "info": [ "Duration of the acute stage. 3 months = 3/12 = 0.25" ]
        })JSON");
