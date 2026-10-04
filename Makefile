.PHONY: install train test app clean

install:
	pip install -r requirements.txt

train:
	python -m src.models.train

test:
	pytest tests/ -v

app:
	streamlit run app/streamlit_app.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
