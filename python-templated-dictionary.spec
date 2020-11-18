%global srcname templated-dictionary

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%global with_python2 1
%endif

Name:       python-%{srcname}
Version:    1.1
Release:    1%{?dist}
Summary:    Dictionary with Jinja2 expansion

License:    GPLv2+
URL:        https://github.com/xsuchy/templated-dictionary

# Source is created by:
# git clone https://github.com/xsuchy/templated-dictionary && cd templated-dictionary
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch: noarch

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires:      python2-jinja2
%endif

%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-jinja2
%endif

%global _description\
Dictionary where __getitem__() is run through Jinja2 template.

%description %_description


%if %{with python2}
%package -n python2-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
%description -n python2-%{srcname} %_description
%endif


%if %{with python3}
%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname} %_description
%endif


%prep
%setup -q


%build
%if %{with python3}
version="%version" %py3_build
%endif

%if %{with python2}
version="%version" %py2_build
%endif


%install
%if %{with python3}
version=%version %py3_install
%endif

%if %{with python2}
version=%version %py2_install
%endif


%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/*
%endif


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%{python2_sitelib}/*
%endif


%changelog
* Wed Nov 18 2020 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- new package
