%define prj     Horde_Editor

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:		horde-editor
Version:	0.0.2
Release:	%mkrel 1
Summary:	Horde Browser package
License:	LGPL
Group:		Networking/Mail
Url:		http://pear.horde.org/index.php?package=%{prj}
Source0:	%{prj}-%{version}.tgz
BuildArch:	noarch
Requires(pre):  php-pear
Requires:	horde-framework
Requires:	horde-util
Requires:	php-pear-channel-horde
BuildRequires:	php-pear
BuildRequires:	php-pear-channel-horde
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Horde_UI:: class provides an API for getting information about
the current user's userinterface and its capabilities.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%dir %{peardir}/Horde/Editor
%{peardir}/Horde/Editor.php
%{peardir}/Horde/Editor/fckeditor.php
%{peardir}/Horde/Editor/tinymce.php
%{peardir}/Horde/Editor/xinha.php