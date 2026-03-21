# SupervisAI — User Research Survey

> AI-Powered Clinical Supervision Support for DClinPsy Trainees  
> Built as part of the BiteLabs Digital Health, AI and Innovation Fellowship — Winter 2026

---

## About This Survey

This interactive survey was built to validate the core problem statement and solution concept behind **SupervisAI** — an AI-powered platform designed to support DClinPsy trainees with post-session reflection and competency tracking, with the goal of reducing supervisor burden and increasing NHS placement capacity.

### Three Hypotheses Being Tested

1. Supervisor time on direct clinical session support is a primary barrier to services taking on more DClinPsy trainees
2. Trainees currently lack adequate structured reflection between supervision sessions
3. Clinicians would be open to adopting an AI tool that addressed these gaps, provided their key concerns were met

### Survey Features

- **Branching logic** — supervisors and trainees see role-appropriate questions
- **15 unique questions** across 6 sections
- **Lean Canvas aligned** — every question maps to a named Lean Canvas block
- **Response saving** — answers stored locally to `responses.csv`
- **Anonymous** — no personally identifiable information collected

---

## How to Run Locally

### Prerequisites

- Python 3.9+
- Anaconda (recommended) or pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/supervisai-survey.git
cd supervisai-survey

# 2. Create a conda environment (recommended)
conda create -n supervisai python=3.11
conda activate supervisai

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The survey will open automatically at `http://localhost:8501`

---

## Deploy on Streamlit Cloud (Free)

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository and `app.py` as the entry point
5. Click **Deploy** — you'll get a public URL to share with respondents

---

## Viewing Responses

Responses are saved to `responses.csv` in the project root. Each row is one submission with a timestamp.

To view in Python:

```python
import pandas as pd
df = pd.read_csv("responses.csv")
print(df)
```

---

## Project Structure

```
supervisai-survey/
├── app.py              # Main Streamlit survey application
├── requirements.txt    # Python dependencies
├── responses.csv       # Generated automatically on first submission
└── README.md           # This file
```

---

## Survey Question Map

| Question | Audience | Lean Canvas Block | Hypothesis Tested |
|---|---|---|---|
| Q1 | All | Customer Segments | — |
| Q2 | All | Customer Segments | — |
| Q3 | Supervisors | Problem | H1 |
| Q4 | Supervisors | Problem | H1 |
| Q5a | Supervisors | Existing Alternatives | H2 |
| Q6a | Supervisors | Problem | H2 |
| Q5b | Trainees | Existing Alternatives | H2 |
| Q6b | Trainees | Problem | H2 |
| Q7 | Trainees | Existing Alternatives | H2 |
| Q8 | All | Existing Alternatives | — |
| Q9 | All | Customer Segments | H3 |
| Q10 | All | Unique Value Proposition | H3 |
| Q11 | All | Channels | H3 |
| Q12 | All | Revenue Streams | H3 |
| Q13 | All | Key Metrics | — |
| Q14 | All | Channels | — |
| Q15a | All | Unfair Advantage | — |
| Q15b | All | — | Open |

---

## About the Developer

Built by **Elif Mertan**, Band 8a Counselling Psychologist, NHS Community Mental Health Hub, London.  
As part of the **BiteLabs Digital Health, AI and Innovation Fellowship — Winter Cohort 2026**.

---

## Licence

MIT — free to use, adapt, and build upon.
