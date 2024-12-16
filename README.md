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
