%define bname   fedberry
%define name    %{bname}-headless

Name:       %{name}
Version:    0.2
Release:    1%{?dist}
License:    GPLv3+
Summary:    Boot your Raspberry Pi using headless mode.
Group:      Applications/System
URL:        https://github.com/${bname}/%{name}
Source0:    https://raw.githubusercontent.com/%{bname}/%{name}/master/headless
Source1:    https://raw.githubusercontent.com/%{bname}/%{name}/master/headless-check.service
Source2:    https://raw.githubusercontent.com/%{bname}/%{name}/master/README.md
BuildArch:  noarch
BuildRequires: systemd-units
BuildRequires:  discount
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Headless mode disables the initial-setup service and obtains an ip-address through dhcp or assigns a static ip-address using information provided in the /boot/headless file.


%prep
%setup -c -T


%build
markdown -o README.html %{SOURCE2}


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_sbindir}
%{__install} -p %{SOURCE0} %{buildroot}/%{_sbindir}

%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p %{SOURCE1} %{buildroot}/%{_unitdir}


%clean
rm -rf %{buildroot}


%post
%systemd_post headless-check.service


%preun
%systemd_preun headless-check.service


%postun
%systemd_postun headless-check.service


%files
%doc README.html
%attr(0755,root,root) %{_sbindir}/headless
%attr(0644,root,root) %{_unitdir}/headless-check.service


%changelog
* Fri Feb 24 2017 Vaughan <vaughan at agrez dot net> 0.2-1
- Fix parsing of headless config options
- Create and package README.html

* Wed Aug 24 2016 Vaughan <vaughan at agrez dot net> 0.1-1
- Initial package
