"""
database.py — Single Source of Truth for Monarch Intelligence Network Projects

DATABASE STRATEGY:
  Local Dev  → SQLite  (automatic, no setup needed, set DATABASE_URL=sqlite:///./projects.db)
  Production → Supabase PostgreSQL (set DATABASE_URL in Vercel environment variables)

To add a new project:  append a new dict to PROJECTS_SEED below, redeploy.
To update a project:   edit the relevant dict, redeploy. On first deploy the table
                       is seeded automatically if empty.
"""

import os
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# ─── Database Connection ──────────────────────────────────────────────────────
# Supabase provides a postgres:// URL; SQLAlchemy 2.x requires postgresql://
_raw_url = os.getenv("DATABASE_URL", "sqlite:///./projects.db")
DATABASE_URL = _raw_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

# ─────────────────────────────────────────────────────────────────────────────
# MASTER DATA — Edit this list to manage all project content.
# Fields:
#   github_url    -> None means "in progress / no repo yet"
#   streamlit_url -> None means "not deployed"
# ─────────────────────────────────────────────────────────────────────────────
PROJECTS_SEED = [
    {
        "id": "001",
        "file_number": "FILE #001",
        "status": "THREAT: CRITICAL",
        "title": "OPERATION: SIGNAL TRACE",
        "description": "BBC News Multi-Class NLP Classification & Summarization System",
        "tech_stack": ["Python", "BiLSTM", "Word2Vec", "T5-small", "HuggingFace", "Keras", "Streamlit"],
        "github_url": "https://github.com/davidkumar355/News-Article-Classification-System",
        "streamlit_url": "https://news-article-classification-system.streamlit.app/",
        "bullets": [
            "Engineered an end-to-end NLP pipeline for automated news categorization and concise summarization.",
            "Trained a BiLSTM model with Word2Vec embeddings achieving 92% classification accuracy across 5 categories.",
            "Integrated T5-small via HuggingFace for real-time abstractive summarization of unstructured text.",
            "Deployed the solution as a high-performance interactive Streamlit application.",
        ],
    },
    {
        "id": "002",
        "file_number": "FILE #002",
        "status": "THREAT: ELEVATED",
        "title": "VISUAL THREAT IDENTIFICATION SYSTEM",
        "description": "CIFAR-10 Computer Vision Pipeline with Grad-CAM Explainability",
        "tech_stack": ["TensorFlow", "Keras", "EfficientNetV2M", "DenseNet121", "Custom CNN", "Grad-CAM", "Streamlit"],
        "github_url": "https://github.com/davidkumar355/CIFAR-10-Classifier",
        "streamlit_url": "https://sota-cifar-10-classifier.streamlit.app/",
        "bullets": [
            "Developed a robust image classification system using transfer learning and custom CNN architectures.",
            "Implemented Grad-CAM for visual explainability to highlight influential regions in image predictions.",
            "Benchmarked EfficientNetV2M and DenseNet121 against a custom baseline CNN.",
            "Deployed an interactive web interface for real-time visual analysis.",
        ],
    },
    {
        "id": "003",
        "file_number": "FILE #003",
        "status": "THREAT: HIGH",
        "title": "CASE FILE 003 - POPULATION PROFILING",
        "description": "Credit Card Customer Behavioral Segmentation",
        "tech_stack": ["Python", "K-Means", "GMM", "Agglomerative", "DBSCAN", "PCA", "Scikit-learn", "Streamlit"],
        "github_url": "https://github.com/davidkumar355/Credit-Card-Behavior-Segmentation-Clustering",
        "streamlit_url": None,
        "bullets": [
            "Applied advanced unsupervised learning techniques for customer segmentation.",
            "Utilized dimensionality reduction (PCA) to visualize high-dimensional financial data.",
            "Benchmarked four clustering algorithms: K-Means, GMM, Agglomerative, and DBSCAN.",
            "Identified distinct behavioral clusters to inform targeted marketing strategies.",
        ],
    },
    {
        "id": "004",
        "file_number": "FILE #004",
        "status": "THREAT: CRITICAL",
        "title": "OPERATION: SYNTHETIC HIVE",
        "description": "Enterprise Multi-Agent Customer Support Platform",
        "tech_stack": ["LangGraph", "FastAPI", "Gemini", "OpenAI", "Qdrant", "RAG", "SQLite"],
        "github_url": None,
        "streamlit_url": None,
        "bullets": [
            "Architected a multi-agent generative AI system for complex customer query resolution.",
            "Integrated Retrieval-Augmented Generation (RAG) with vector databases for knowledge grounding.",
            "Built scalable APIs utilizing state-of-the-art LLMs for autonomous problem solving.",
        ],
    },
    {
        "id": "005",
        "file_number": "FILE #005",
        "status": "THREAT: ELEVATED",
        "title": "CASE FILE 005 - ECONOMIC PRECOGNITION",
        "description": "Bank Marketing Ensemble Classification & SHAP Analysis",
        "tech_stack": ["Scikit-learn", "SMOTE", "Random Forest", "Gradient Boosting", "Stacking Ensembles", "SHAP"],
        "github_url": "https://github.com/davidkumar355/Bank-Marketing-Case-Study",
        "streamlit_url": None,
        "bullets": [
            "Constructed predictive models to forecast marketing campaign success rates.",
            "Handled severe class imbalance using SMOTE oversampling techniques.",
            "Employed SHAP (SHapley Additive exPlanations) for model transparency and feature importance.",
            "Stacked ensemble classifiers achieving significant uplift over single-model baselines.",
        ],
    },
]

# ─── DDL ─────────────────────────────────────────────────────────────────────
_CREATE_TABLE_SQL = text("""
    CREATE TABLE IF NOT EXISTS projects (
        id            TEXT PRIMARY KEY,
        file_number   TEXT NOT NULL,
        status        TEXT NOT NULL,
        title         TEXT NOT NULL,
        description   TEXT NOT NULL,
        tech_stack    TEXT NOT NULL,
        github_url    TEXT,
        streamlit_url TEXT,
        bullets       TEXT NOT NULL
    )
""")

_INSERT_SQL = text("""
    INSERT INTO projects
        (id, file_number, status, title, description,
         tech_stack, github_url, streamlit_url, bullets)
    VALUES
        (:id, :file_number, :status, :title, :description,
         :tech_stack, :github_url, :streamlit_url, :bullets)
    ON CONFLICT (id) DO NOTHING
""")


def init_db() -> None:
    """Create the projects table if it does not already exist."""
    with engine.begin() as conn:
        conn.execute(_CREATE_TABLE_SQL)


def seed_db() -> None:
    """Insert seed data only when the table is empty (safe on every startup)."""
    with engine.begin() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM projects")).scalar()
        if count and count > 0:
            return
        for proj in PROJECTS_SEED:
            conn.execute(_INSERT_SQL, {
                "id":            proj["id"],
                "file_number":   proj["file_number"],
                "status":        proj["status"],
                "title":         proj["title"],
                "description":   proj["description"],
                "tech_stack":    json.dumps(proj["tech_stack"]),
                "github_url":    proj.get("github_url"),
                "streamlit_url": proj.get("streamlit_url"),
                "bullets":       json.dumps(proj["bullets"]),
            })


def get_all_projects() -> list:
    """Return all projects as a list of plain dicts, deserialising JSON fields."""
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM projects ORDER BY id ASC")).mappings().all()
    result = []
    for row in rows:
        proj = dict(row)
        proj["tech_stack"] = json.loads(proj["tech_stack"])
        proj["bullets"]    = json.loads(proj["bullets"])
        proj["github_url"]    = proj.get("github_url") or None
        proj["streamlit_url"] = proj.get("streamlit_url") or None
        result.append(proj)
    return result
