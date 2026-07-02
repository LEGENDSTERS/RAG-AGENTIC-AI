from backend.agents.policy_agent import policy_agent
from backend.agents.eligibility_agent import eligibility_agent
from backend.agents.benefit_agent import benefit_agent
from backend.agents.checklist_agent import checklist_agent
from backend.agents.grievance_agent import grievance_agent
from backend.agents.exclusion_agent import exclusion_agent

AGENTS = {
    "policy_agent": policy_agent,
    "eligibility_agent": eligibility_agent,
    "benefit_agent": benefit_agent,
    "checklist_agent": checklist_agent,
    "grievance_agent": grievance_agent,
    "exclusion_agent": exclusion_agent,
}