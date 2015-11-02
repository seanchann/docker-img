FROM rh/jenkins-plugins
MAINTAINER The rongheTV jenkins image <www.ronghe.com> - seanchann

ENV JAVA_OPTS="-Djava.io.tmpdir=$JENKINS_HOME/tmp -Duser.timezone=Asia/Chongqing"

# Switch user to root so that we can install apps (jenkins image switches to user "jenkins" in the end)
USER root

# Install Docker prerequisites
RUN apt-get update -qq && apt-get install bc