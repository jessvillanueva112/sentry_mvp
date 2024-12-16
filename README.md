# Sentry Platform

## Overview

Sentry is a full-stack platform designed to help school counselors assess violence risks, generate personalized support plans, and coordinate resources using AI, ML, and NLP.

## Problem and Impact

Violent incidents in schools often go unreported, exacerbated by factors like poverty and mental health issues. Sentry aims to address these challenges by providing data-driven insights and personalized interventions.

## Solution

Sentry leverages AI to analyze diverse data sources, assess risks, and generate support plans. It integrates incident reports, safety plans, and mental health screenings to provide actionable insights for counselors.

## Key Features

- **Data-Driven Insights**: Aggregates data for comprehensive student profiles.
- **Personalized Support Plans**: Generates tailored PDF documents for effective communication.
- **Risk Assessment**: Utilizes ML algorithms to predict and assess violence risks.

## Project Structure

sentry-platform/
│
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── routes.py
│ │ ├── utils.py
│ │ └── synthetic_data.py
│ ├── requirements.txt
│ └── config.py
│
├── frontend/ (Bubble.io interface)
│
├── tests/
│ ├── test_api.py
│ └── test_synthetic_data.py
│
└── README.md


## Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
5. Run the Flask application:
   ```bash
   python backend/app/main.py
   ```

## Bubble.io Workflow

### Data-Driven Insights and Risk Assessment

1. **Create a New Page**: Design the Risk Assessment feature.
2. **Set Up Workflow**:
   - Trigger: "Submit" button click.
   - Actions:
     - Create `RiskAssessment` entry.
     - Link to `Student` record.
     - Calculate risk score.
     - Update student’s risk level.
     - Alert counselor if necessary.

### Generate Support Plan

1. **Create a New Page**: Design the Support Plan feature.
2. **Set Up Workflow**:
   - Trigger: "Generate Plan" button click.
   - Actions:
     - Create `SupportPlan` entry.
     - Use PDF Conjurer plugin.
     - Save PDF URL.

## Synthetic Datasets

1. **Student Data**: Includes `Name`, `Age`, `Violence Incidents`, etc.
2. **Incident Reports**: Includes `Student ID`, `Incident Type`, etc.
3. **Risk Assessments**: Includes `Poverty Level`, `Risk Score`, etc.
4. **Support Plans**: Includes `Interventions`, `Stakeholders`, etc.

## Connecting Flask Backend to Bubble.io

1. Deploy the Flask app to a cloud service.
2. Use Bubble's API Connector to connect to the backend.
3. Create API calls for data operations.

## Success Criteria

- Develop a functional MVP with at least 70% accuracy.
- Implement basic violence risk assessment and support plans.
- Document user feedback and performance metrics.

## Deliverables

- Memo, article, and presentation explaining Sentry.
- Website detailing the problem, solution, and technical aspects.
- GitHub repository for deployability.

## Key Assumptions

- Legal and ethical guidelines permit monitoring.
- AI algorithms can accurately identify risks with low false positives.

## Next Steps

- Data collection and collaboration with schools and agencies.
- Compliance with privacy regulations.
- Pilot with counselors and expand the project.

## License

[Specify the license under which the project is released]