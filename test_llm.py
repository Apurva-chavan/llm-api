from llm_config import ask_llm

resume = """
Data Science Intern — The Entrepreneurship Network
- Built and trained 3 ML models (Linear Regression, Random Forest, LSTM) for weather prediction, stock forecasting, and house price prediction
- Implemented 5-fold cross-validation and hyperparameter tuning to improve generalization
- Documented model performance metrics in structured reports

Machine Learning Intern — Atharvo India Pvt. Ltd.
- Performed end-to-end data cleaning on 50K+ records using Python and SQL
- Built 4 interactive Power BI dashboards for internal decision-making
- Reduced manual preparation effort by 35% through automated preprocessing

Projects:
- Deep Deception Detector: CNN-based deepfake detection, 94% F1-score, 0.97 AUC-ROC
- FIFA Player Performance Analysis: EDA on 18,000+ records, 12 visualizations, 40% preprocessing time reduction
"""

job_description = """
Looking for AI/ML Engineer with experience in:
- Machine learning model development and deployment
- Deep learning and neural networks
- Python, TensorFlow, Scikit-learn
- Model evaluation and MLOps
- NLP and Computer Vision
"""

prompt = f"""
I have this resume:
{resume}

Tailor all bullet points for this job description:
{job_description}

Give me the complete tailored resume bullet points only.
"""

result = ask_llm(prompt)
print(result)