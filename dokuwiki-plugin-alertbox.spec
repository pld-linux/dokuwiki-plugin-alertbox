%define		plugin		alertbox
Summary:	Add Bootstrap style alert boxes to your wiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20150315
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/sjlevine/dokuwiki-alertbox/archive/master/%{plugin}-%{version}.tar.gz
# Source0-md5:	3023fb439fc1b5807f97efcfe51074cb
URL:		https://www.dokuwiki.org/plugin:alertbox
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20131208
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Add Bootstrap style alert boxes to your wiki.

%prep
%setup -qc
mv dokuwiki-%{plugin}-*/* .

%build
version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README.md

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js/css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/img
