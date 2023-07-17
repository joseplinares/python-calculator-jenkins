pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/joseplinares/python-calculator-jenkins.git']])
            }
        }
       
        stage('build') {
            steps {
                git branch: 'master', url: 'https://github.com/joseplinares/python-calculator-jenkins.git'
                bat 'python calculator.py'
            }
        }
       
        stage('test') {
            steps {
                bat 'python -m pytest'
            }
        }
       
       
    }
}
