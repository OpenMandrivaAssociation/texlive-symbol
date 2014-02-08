# revision 21570
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2011-03-01 21:42:17 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-symbol
Version:	20110301
Release:	3
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/symbol.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/symbol/config.usy
%{_texmfdistdir}/fonts/afm/adobe/symbol/psyb.afm
%{_texmfdistdir}/fonts/afm/adobe/symbol/psyr.afm
%{_texmfdistdir}/fonts/afm/urw/symbol/usyr.afm
%{_texmfdistdir}/fonts/map/dvips/symbol/usy.map
%{_texmfdistdir}/fonts/tfm/adobe/symbol/psyr.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/symbol/rpsyr.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/symbol/rpsyro.tfm
%{_texmfdistdir}/fonts/tfm/monotype/symbol/msyr.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/symbol/usyr.tfm
%{_texmfdistdir}/fonts/type1/urw/symbol/usyr.pfb
%{_texmfdistdir}/fonts/type1/urw/symbol/usyr.pfm
%{_texmfdistdir}/tex/latex/symbol/uusy.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110301-2
+ Revision: 756418
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110301-1
+ Revision: 719624
- texlive-symbol
- texlive-symbol
- texlive-symbol
- texlive-symbol

