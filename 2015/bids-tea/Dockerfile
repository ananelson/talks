FROM                    ubuntu:latest
MAINTAINER              Ana Nelson <ana@ananelson.com>

### "localedef"
RUN locale-gen en_US.UTF-8

### "apt-defaults"
RUN echo "APT::Get::Assume-Yes true;" >> /etc/apt/apt.conf.d/80custom ; \
    echo "APT::Get::Quiet true;" >> /etc/apt/apt.conf.d/80custom ; \
    apt-get update

### "apt-installs"
RUN apt-get install \
      pkg-config \
      libfreetype6-dev \
      libpng-dev \
      python \
      python-dev \
      python-pip \
      python-scipy \
      ;

### "pip-installs"
RUN pip install \
        dexy \
        ipython[notebook] \
        matplotlib \
        pandas \
        statsmodels \
        xlsxwriter \
        ;

### "create-user"
RUN useradd -m repro && \
    echo "repro:password" | chpasswd ; \
    echo "repro ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/repro

### "activate-user"
ENV HOME /home/repro
USER repro
WORKDIR /home/repro
