%define with_version %{?_with_version:1}%{!?_with_version:0}

Summary: Module rewrites connection's Remote IP to value of X-Real-IP header.
Name: mod_realip2
Version: 1.1
Release: 1%{?dist}
License: Apache Software License
Group: System Environment/Daemons
#URL: 
Source: mod_realip2.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: httpd httpd-mmn = %([ -a %{_includedir}/httpd/.mmn ] && cat %{_includedir}/httpd/.mmn || echo missing)
BuildRequires: httpd-devel

%description
mod_realip2 is an Apache 2 module for rewriting connection's Remote IP
to value of a X-Real-IP header. The module is IPv6 compatible.
It is free software, licensed under the Apache license.

Building option:
        --with version : add the module info to server version string.

%prep
%setup -T -c
%{__cp} %{SOURCE0} .

%build
/usr/sbin/apxs %{?_with_version:-DREALIP2_VERSION_SHOW} -c mod_realip2.c

%install
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -Dp .libs/mod_realip2.so %{buildroot}%{_libdir}/httpd/modules/mod_realip2.so

cat << EOF > %{buildroot}%{_sysconfdir}/httpd/conf.d/realip2.conf
#
# This module rewrites connection's Remote IP to value of X-Real-IP.
#

LoadModule realip2_module modules/mod_realip2.so
EOF

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
#%doc
%{_libdir}/httpd/modules/mod_realip2.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_realip2.conf

%changelog
* Thu Feb 14 2008 Olexander Shtepa <isk@idegroup.com> 1.1-1
- Move the `realip2_post_read_request' handler from being APR_HOOK_MIDDLE to
  APR_HOOK_FIRST to make the module run before modules like mod_geoip (from mod_rpaf).

* Mon Dec 10 2007 Olexander Shtepa <isk@idegroup.com> 1.0-1
- Initial build
