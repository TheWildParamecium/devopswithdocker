FROM ruby:2.6.0
RUN apt-get update && apt-get install -y curl git 
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt install -y nodejs
RUN gem install bundler
RUN git clone https://github.com/docker-hy/rails-example-project
WORKDIR /rails-example-project
RUN bundle install
RUN rails db:migrate
EXPOSE 3000
CMD ["rails",  "s"]