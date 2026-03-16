pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                  git branch: 'main', url: 'https://github.com/D-Shravani/ui-automation-framework.git'
           }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -n 3 --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

    }
}