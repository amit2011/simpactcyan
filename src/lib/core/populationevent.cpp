#include "populationevent.h"
#include "population.h"
#include "personbase.h"
#include <stdlib.h>
#include <assert.h>
#include <iostream>

void PopulationEvent::commonConstructor()
{
	// Since we'll be removing each event when executed, this
	// avoids the needless generation of a random number
	setWillBeRemoved(true); 

	m_eventID = -1;
	m_scheduledForRemoval = false;

	// only one person will have a reference to this event

	for (int i = 0 ; i < POPULATIONEVENT_MAXPERSONS ; i++)
	{
		m_pPersons[i] = 0;
		m_eventIndex[i] = -1;
	}
}

PopulationEvent::PopulationEvent()
{
	std::cerr << "Currently no support for events that have no reference to any person" << std::endl;
	exit(-1);
}

PopulationEvent::PopulationEvent(PersonBase *pPerson)
{
	assert(pPerson != 0);

	commonConstructor();

	m_pPersons[0] = pPerson;
	m_numPersons = 1;
}

PopulationEvent::PopulationEvent(PersonBase *pPerson1, PersonBase *pPerson2)
{
	assert(pPerson1 != 0 && pPerson2 != 0);

	commonConstructor();

	m_pPersons[0] = pPerson1;
	m_pPersons[1] = pPerson2;
	m_numPersons = 2;
}
	
PopulationEvent::~PopulationEvent()
{
}

bool PopulationEvent::isNoLongerUseful()
{
	int num = m_numPersons;

	for (int i = 0 ; i < num ; i++)
	{
		assert(m_pPersons[i] != 0);

		if (m_pPersons[i]->hasDied())
			return true;
	}

	return isUseless();
}


#ifndef NDEBUG
PersonBase *PopulationEvent::getPerson(int idx) const
{ 
	assert(m_numPersons >= 0 && m_numPersons <= POPULATIONEVENT_MAXPERSONS); 
	assert(idx < (int)m_numPersons); 

	PersonBase *pPerson = m_pPersons[idx];
	assert(pPerson != 0);
	assert(!pPerson->hasDied());
	return pPerson;
}
#endif