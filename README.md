# Sentry Platform

## Overview

Sentry is a full-stack platform designed to help school counselors assess violence risks, generate personalized support plans, and coordinate resources using AI, ML, and NLP.

## Executive Summary

### Problem and Impact
I’m solving the issue of violent incidents that often go unreported in public schools in the U.S. and Canada, which includes weapon possession, physical fights, and gang activity. This is caused by poverty, educational attainment, and mental health issue factors worsened by societal stigma and social dynamics leading to desires to find coping mechanisms to heal. When students engage less in school due to individual learning circumstances, their likelihood decreases for future career and university prospects for individual fulfillment and societal progression, along with less emotional resilience in navigating challenges.

### Gap Analysis
Existing solutions are security cameras, metal detectors, and training programs to increase awareness, social media monitoring, and those school-wide Microsoft Teams meetings school-wide emphasizing counselor reach-outs for struggling students. However, they don’t fully capture the environmental factors students grew up externally living in place, and behavioral issues in place. Plus, this would require so many resources all at once with a huge liability asset combating false positives and ensuring user privacy, along with bridging the divides between many different resources all at once making sure that the data is able to be accessed in the first place.

### Solution
Sentry is a full-stack platform leveraging AI to analyze diverse data sources, assess violence risks with ML and NLP, and provide personalized support plans for each student. We take in incident reports, student safety plans, family and student questionnaires from the past, external mental health screening reports from outside agencies, and student registration forms as the input that is though school owned, not too problematic to collect akin to public data sources. We are ensuring anecdotal evidence heavily collected stored from elementary to middle to inform the future for high school crowds. Next, we assess for violence risk indicators based on trained backed case studies and research emphasizing family dysfunction and past trauma, abuse, and mental disorders previously to be assessed with ML, NLP (probably open-sourced models) already implemented, and generate personalized support plan PDFs that are clean, easy to interpret, and actionable to read for counselors for justification and collaboration, all in for further understanding. As a result, we make sure that students are academically strong, live in healthier external environments securing enough resources to grow up effectively and well addressing their divides, and have overall greater self esteem during formative years where education is a often mandatory aspect of our lives for Canada and the United States.

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

## Requirements

1. bubble.io - for frontend development and workflow management
2. flask - backend framework for api development
3. sqlite - database for storing application data
4. pdf plugin - for generating support plan pdfs in bubble.io
5. cursor - for code editing and development
6. obsidian - for organizing project notes and information
7. python - main programming language for backend logic
8. github - for version control, deployment, and licensing

## Job to Be Done

When I am a school counselor aimed to take care of the students in my public high school I’m working at, I want to leverage AI-powered insights and personalized PDF support plans so that I can effectively reduce violence risks, improve the overall school climate for every student, bridging the stigma and social dynamics exacerbating poverty and especially mental health, and improving academic and emotional outcomes for future prospects.

## Success Criteria

1. Overall Success Criteria:
   - Completion of all phases at above 80% level with a few debugs before the time comes
   - Develop functional MVP with at least 70% accuracy
   - Create accessible Flask web interface for authorized school counselors, parents, external coordinators specialized in youth mental health
   - Document user feedback for validation and future outreach, and performance metrics of the trained model.

2. Minimum Results:
   - Deploy working MVP with flask using bubble.io or AWS services as infrastructure already set up
   - Implement basic violence risk assessment and emphasized personalized support plans and backed up with research with information flow on the datasets uploaded all throughout with machine learning and natural language processing
   - Document initial user usage with user feedback

3. Stretch Goals:
   - Achieve 80% accuracy in predicting students at risk of violence earlier for high school counselors
   - Implement real time alerts via SMS
   - Secure commitment from one social worker working in a public high school in the Lower Mainland to pilot the system
   - Develop basic mobile app prototype for at-risk violent student reporting

## Pre-Mortem

1. Difficulty obtaining real threat data due to working with such sensitive information along with how the information’s all collected and stored in the first place
   - Use with emphasis on anecdotal interviews, family and student conferences and interviews, safety plans, incident reports, student registration forms, and making it highly recommended for students and parents to open up with students for my input

2. False positives with AI and machine learning algorithms may not always accurately identify threats from input data with a low rate of false positives and negatives
   - Implemented human-in-the-loop mechanism by collaborations with students, parents, and especially counselors with decision logs on how the machine made the decision

## Key Assumptions

- Legal and Ethical consideration: Laws and ethical guidelines would permit widespread monitoring and analysis of teen databases for personalized pdfs
- Privacy and Data protection: Robust safeguards and protocols could be implemented to protect individuals’ privacy while still allowing for effective at-risk violence detection
- Behavioral assumptions: Potential students who do threats would consistently display these identifiable signs that are always on anecdotal evidence prior to an attack
- Technical feasibility: AI, NLP, and ML algorithms could accurately identify violent potentially students with a low rate of false positives and false negatives.

## Outlook

Bridge individual student fulfillment with societal gaps from elementary to post-graduate high school.

## Next Steps

- Data collection: Demographics and safety plans and risk factors at elementary/middle school levels, multi-year questionnaires and parents, obtain parental permission for medical/agency infrastructure,
- Collaboration: link schools with outside agencies and industries, coordinate with mental health, medical, counseling, and behavioral support systems, engage with students, parents, school admins, and counselors and external resources so often
- Compliance and ethics: Adherence to privacy regulations (CCPA, EU AI, FERPA), implement transparency and safeguards, maintain “human-in-the-loop approach”

## Expansion

- Incorporate real threat data, incident reports, and risk assessments
- Pilot with counselors, focusing on specialized centers for youth in the most need due to mental disorders, dysfunctional families, and external environment exposure to weapons (vape/weed/substances, and trauma or abuse or bullying with ACEs)
- Develop communication platform connecting external agencies from rehab centers, personalized counseling, and Covenant House
- For monetization and scaling: We’ll create a virtual boundary around a specific geographic area to analyze data and monitor teen activity that’s related to potential violence risk identified in students, counselors in that area have to pay to get access to those alerts, and then rinse and repeat to scale the product up across Canada and the United States, set up an LLC when accessing real teen databases complying with the VPD core principles of Privacy, Transparency, and Human-In-the-Loop

## Database Structure

The database is designed to store comprehensive information about students, counselors, support plans, and risk assessments. Below is an overview of the database models and their fields:

### Student

- **ID**: Unique identifier for each student.
- **Age**: Integer representing the student's age.
- **Violence Incidents**: List of numbers indicating recorded incidents.
- **Counselor Notes**: List of text entries for notes made by counselors.

### Counselor

- **ID**: Unique identifier for each counselor.
- **Specialization**: Text field describing the counselor's area of expertise.
- **Assigned Students**: Relationship to the `Student` model, indicating students assigned to the counselor.

### SupportPlan

- **ID**: Unique identifier for each support plan.
- **Student**: Foreign key linking to the `Student` model.
- **Interventions**: List of text entries detailing interventions for the student.
- **Stakeholders**: List of text entries identifying stakeholders involved in the support plan.

### RiskAssessment

- **ID**: Unique identifier for each risk assessment.
- **Student**: Foreign key linking to the `Student` model.
- **Poverty Level**: Text field indicating the student's poverty level.
- **Mental Health Issues**: List of text entries describing mental health issues.
- **Behavioral Patterns**: List of text entries detailing observed behavioral patterns.

## Plugins (PDF, Risk Prediction Algorithm)

The Sentry platform leverages plugins and APIs to enhance its functionality, particularly in generating personalized support plans and assessing risk levels. Below is an overview of the key plugins and their integration:

### PDF Generation Plugin

- **Plugin**: PDF Conjurer
- **Purpose**: Generate personalized support plan PDFs for students.
- **Integration Steps**:
  1. **Installation**: Install the PDF Conjurer plugin from the Bubble plugin marketplace.
  2. **Configuration**: Configure the plugin to work with the `SupportPlan` data structure, ensuring it can access and format the necessary data.
  3. **Workflow Integration**: Use the plugin's actions within the "Generate Support Plan" workflow to create PDFs based on stored data.
  4. **Formatting**: Ensure the PDF is properly formatted, including all necessary information for effective communication with stakeholders.
  5. **Testing**: Test the workflow to ensure successful generation and download of the Support Plan PDF.

### Risk Prediction Algorithm

- **Objective**: Implement a risk prediction algorithm to analyze student data for potential violence risk.
- **Integration Steps**:
  1. **Workflow Creation**: Create a workflow that triggers the risk prediction algorithm when a user submits the risk assessment form.
  2. **Data Analysis**: Utilize Bubble's workflow actions to analyze data inputs for poverty levels, mental health issues, and behavioral patterns.
  3. **Result Display**: Display the risk assessment results to the user, indicating the level of risk for violence.
  4. **Conditional Logic**: Incorporate conditional statements to ensure accurate risk assessment results.

### External API Integration

- **Purpose**: Enhance analysis capabilities using external APIs.
- **Integration Steps**:
  1. **Plugin Exploration**: Explore and install relevant plugins offering external APIs for data analysis.
  2. **API Integration**: Integrate these APIs into your Bubble app to leverage advanced data analysis capabilities for more accurate risk predictions.
  3. **Testing**: Test the integration thoroughly to ensure the external APIs are functioning correctly and providing valuable insights for risk assessment.


## Workflow

### Risk Assessment and Alert System Workflow

1. **Setup**: 
   - Open the Bubble editor and navigate to the Workflows tab.

2. **Create Workflow**: 
   - Name the workflow "Submit Risk Assessment".

3. **Trigger**: 
   - Activate when the "Submit" button is clicked on the Risk Assessment page.

4. **Actions**:
   - **Create RiskAssessment Entry**: 
     - Use "Create a new thing" to add a `RiskAssessment` entry.
     - Populate fields like `poverty_level`, `mental_health_issues`, and `behavioral_patterns` from form inputs.
   - **Link to Student Record**: 
     - Use "Make changes to a thing" to associate the entry with the `Student` record.
   - **Calculate Risk Score**: 
     - Use custom states and conditions to calculate a risk score.
   - **Update Student's Risk Level**: 
     - Update the `Student` record with the risk level.
   - **Create Alert for Counselor**: 
     - If the risk score exceeds a threshold, generate an alert for the counselor.

### Generate Support Plan Workflow

1. **Setup**: 
   - Open the Bubble editor and navigate to the Workflows tab.

2. **Create Workflow**: 
   - Name the workflow "Generate Support Plan".

3. **Trigger**: 
   - Activate when the "Generate Plan" button is clicked on the student page.

4. **Actions**:
   - **Create SupportPlan Entry**: 
     - Use "Create a new thing" to add a `SupportPlan` entry.
     - Populate with student data, interventions, and stakeholders.
   - **Generate PDF**: 
     - Use the PDF Conjurer plugin to generate a PDF.
     - Ensure it includes all necessary information for stakeholders.
   - **Save PDF URL**: 
     - Save the PDF's URL to the `SupportPlan` record.

### Risk Assessment and Alert System Workflow

1. **Setup**: 
   - Open the Bubble editor and navigate to the Workflows tab.

2. **Create Workflow**: 
   - Name the workflow "Submit Risk Assessment".

3. **Trigger**: 
   - Activate when the "Submit" button is clicked on the Risk Assessment page.

4. **Actions**:
   - **Create RiskAssessment Entry**: 
     - Use "Create a new thing" to add a `RiskAssessment` entry.
     - Populate fields like `poverty_level`, `mental_health_issues`, and `behavioral_patterns` from form inputs.
   - **Link to Student Record**: 
     - Use "Make changes to a thing" to associate the entry with the `Student` record.
   - **Calculate Risk Score**: 
     - Use custom states and conditions to calculate a risk score.
   - **Update Student's Risk Level**: 
     - Update the `Student` record with the risk level.
   - **Create Alert for Counselor**: 
     - If the risk score exceeds a threshold, generate an alert for the counselor.

### Generate Support Plan Workflow

1. **Setup**: 
   - Open the Bubble editor and navigate to the Workflows tab.

2. **Create Workflow**: 
   - Name the workflow "Generate Support Plan".

3. **Trigger**: 
   - Activate when the "Generate Plan" button is clicked on the student page.

4. **Actions**:
   - **Create SupportPlan Entry**: 
     - Use "Create a new thing" to add a `SupportPlan` entry.
     - Populate with student data, interventions, and stakeholders.
   - **Generate PDF**: 
     - Use the PDF Conjurer plugin to generate a PDF.
     - Ensure it includes all necessary information for stakeholders.
   - **Save PDF URL**: 
     - Save the PDF's URL to the `SupportPlan` record.

## User Interface Overview

The Sentry platform's user interface is designed to facilitate risk assessments and generate personalized support plans. Below is an explanation of the key UI components and their relation to the platform's workflows and plugins:

### Risk Assessment UI

![Risk Assessment UI](/Users/jvillanueva112/Desktop/sentry_mvp/frontend/risk-assessment-ui.png)

1. **New Assessment Section**
   - **Student ID**: Input field for entering the student's unique identifier.
   - **Risk Factors**: Dropdown to select various risk factors affecting the student.
   - **Start Assessment Button**: Triggers the "Submit Risk Assessment" workflow.

2. **Assessment Results Section**
   - **Risk Score**: Displays the calculated risk level (e.g., Medium).
   - **Risk Factors Chart**: Visual representation of the risk factors contributing to the assessment.
   - **Generate Support Plan Button**: Initiates the "Generate Support Plan" workflow.

### Connection to Workflows and Plugins

- **Risk Assessment and Alert System Workflow**:
  - The UI allows users to input data and trigger the risk assessment process, which is automated through the workflow described in the `README.md`.
  - The workflow calculates the risk score and updates the student's record, as outlined in the "Risk Assessment and Alert System" section.

- **Generate Support Plan Workflow**:
  - The "Generate Support Plan" button in the UI triggers the workflow to create a personalized support plan PDF.
  - This process uses the PDF Conjurer plugin to format and generate the document, as detailed in the "PDF Generation Plugin" section.

### Integration with Plugins and APIs

- **PDF Generation**: The UI's "Generate Support Plan" button utilizes the PDF Conjurer plugin to create a PDF, ensuring it includes all necessary information for stakeholders.
- **Risk Prediction Algorithm**: The UI supports the risk prediction algorithm by allowing data input and displaying results, aligning with the workflow steps for data analysis and result display.

This UI effectively supports the functionalities described in your `README.md`, providing a user-friendly interface for conducting risk assessments and generating support plans.

## Testing and Validation

- **Test Each Workflow**: Ensure workflows function as expected with accurate data processing.
- **Validate Plugin Integration**: Confirm the PDF Conjurer plugin works seamlessly.
- **User Feedback**: Collect feedback to refine workflows for better usability and effectiveness.