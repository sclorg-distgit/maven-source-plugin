%global pkg_name maven-source-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.2.1
Release:        7.10%{?dist}
Summary:        Plugin creating source jar

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-source-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-plexus-utils
BuildRequires: %{?scl_prefix_java_common}ant
BuildRequires: maven30-maven-compiler-plugin
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-surefire-plugin
BuildRequires: maven30-maven-surefire-provider-junit
BuildRequires: maven30-maven-jar-plugin
BuildRequires: maven30-maven-javadoc-plugin
BuildRequires: maven30-mvn(org.apache.maven.surefire:surefire-junit4)


%description
The Maven 2 Source Plugin creates a JAR archive of the 
source files of the current project.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
sed -i -e "s|plexus-container-default|plexus-container|g" pom.xml
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{pkg_name}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.2.1-7.10
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.2.1-7.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.2.1-7.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-7
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 2.2.1-3
- Build with xmvn

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-2
- Install license files
- Resolves: rhbz#876837

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-6
- Use upstream source.
- Build with maven 3.x.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 9 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-4
- Do not exclude plexus-container-default from dependencies.

* Fri May 28 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-3
- Add provides/obsoletes.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-2
- Fix Url.
- More descriptive summary.
- Add missing BR.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.2-1
- Initial package.
