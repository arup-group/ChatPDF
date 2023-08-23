# Deployment Guide

# Dependencies

*`provide a list of dependencies that are required for the project`*

# Deployment Strategy

*`provide an overview of the deployment strategy being used as aprt of the development process`*

# Pipelines

*`provide the CI/CD methodology being used as part of the project`*

| Section           | Information                       |
|---------------    |-------------------------------    |
| CI/CD Method      | *`E.g. Azure DevOps`*             |
| Pipeline URL  | *`url to the Build pipeline`*     |

# Triggers

*`list the triggers that invoke the deployment pipeline`*

E.g.

triggers are set on the following branches

| Branches          | Environment deployed too                      | Rules|
|---------------    |-------------------------------    | - |
| All Feature branches      |     Development environment       | Any commit to feature branch will rebuild in the development environment for solution |
| staging   | Staging environment   | feature branches are merged into staging only |
| production    | Production environment    | staging branch is only merged in production |

# Pull Requests

*`list the criteria for creation of PRs and what mandatory information is required`*

E.g.

- repo and branches
- JIRA ticket reference
- testing criteria

