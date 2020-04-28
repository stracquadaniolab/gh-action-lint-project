FROM stracquadaniolab/vanilla:latest

LABEL org.stracquadaniolab.maintainer="gh-action-lint-project"
LABEL org.stracquadaniolab.version="0.0.1"
LABEL org.stracquadaniolab.platform="github-action"

ADD ./entrypoint.sh /usr/bin/entrypoint.sh
ADD ./layoutcheck.py /usr/bin/layoutcheck.py
ADD ./namecheck.py /usr/bin/namecheck.py
ADD ./dir.ignore /etc/dir.ignore
ADD ./file.ignore /etc/file.ignore
RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]