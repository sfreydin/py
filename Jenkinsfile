#!/usr/bin/env groovy

pipeline {
    environment{
        REGISTRY=sh returnStdout: true, script: 'echo -n "${REGISTRY:=hub.krusche.cloud/demo/py}"'
        GIT_CODE=sh returnStdout: true, script: 'echo -n "${GIT_CODE=https://github.com/froggy777/py.git}"'
        IMAGE_TAG = "${RELEASE_NAME}.${BUILD_ID}"
        RELEASE_NAME=sh returnStdout: true, script: 'echo -n "${RELEASE_NAME=v0.1}"'
        REGISTRY_CRED=sh returnStdout: true, script: 'echo -n "${REGISTRY_CRED=hub_id}"'
        REPO_CRED=sh returnStdout: true, script: 'echo -n "${REPO_CRED=repo-cred-id}"'

    }
    agent any
//    options {
//        timestamps()
//        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
//    }
//    parameters {
//        gitParameter branchFilter: 'origin.*/(.*)', defaultValue: 'master', name: 'BRANCH_PY', type: 'PT_BRANCH', useRepository: env.GIT_CODE
//    }
    stages {
        stage('SCMs checkout') {
            parallel {
                stage('py') {
                    steps {
                          git branch: 'master', url: env.GIT_CODE
                    }
                }
            }
        }
        stage('BUILD') {
            parallel {
                stage('build and push docker') {
                    steps {
                        script {
                            sh "env"
                            docker.withRegistry('https://' + env.REGISTRY, env.REGISTRY_CRED) {
                                def DockerImagePy = docker.build("${REGISTRY}:${IMAGE_TAG}", "-f Dockerfile --build-arg IMAGE_TAG=${IMAGE_TAG} .")
                                def DockerImagePyLatest = docker.build("${REGISTRY}:latest", "-f Dockerfile --build-arg IMAGE_TAG=${IMAGE_TAG} .")
                                DockerImagePy.push()
                                DockerImagePyLatest.push()
                            }
                        }
                    }
                }

                stage('build and push helm') {
                    steps {
                        script {
                            sh """
                                 helm init --client-only
                                 helm package helm/py
                                 s3cmd put py-0.1.0.tgz s3://helm-repo-kc/py-0.1.0.tgz
                            """

                        }
                    }
                }
            }
        }
    }
}
