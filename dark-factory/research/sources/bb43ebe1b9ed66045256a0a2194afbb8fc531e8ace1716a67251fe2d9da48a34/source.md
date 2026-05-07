# StrongDM — The StrongDM Software Factory: Building Software with AI

Source: https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai

---

document.addEventListener("DOMContentLoaded",function(){document.documentElement.style.setProperty("--scrollBarWidth",window.innerWidth-document.body.clientWidth+"px")});


(function(){var a=window.mutiny=window.mutiny||{};if(!window.mutiny.client){a.client={\_queue:{}};var b=["identify","trackConversion"];var c=[].concat(b,["defaultOptOut","optOut","optIn"]);var d=function factory(c){return function(){for(var d=arguments.length,e=new Array(d),f=0;f<d;f++){e[f]=arguments[f]}a.client.\_queue[c]=a.client.\_queue[c]||[];if(b.includes(c)){return new Promise(function(b,d){a.client.\_queue[c].push({args:e,resolve:b,reject:d});setTimeout(d,500)})}else{a.client.\_queue[c].push({args:e})}}};c.forEach(function(b){a.client[b]=d(b)})}})();

The StrongDM Software Factory: Building Software with AI












a.cta\_button{-moz-box-sizing:content-box !important;-webkit-box-sizing:content-box !important;box-sizing:content-box !important;vertical-align:middle}.hs-breadcrumb-menu{list-style-type:none;margin:0px 0px 0px 0px;padding:0px 0px 0px 0px}.hs-breadcrumb-menu-item{float:left;padding:10px 0px 10px 10px}.hs-breadcrumb-menu-divider:before{content:'›';padding-left:10px}.hs-featured-image-link{border:0}.hs-featured-image{float:right;margin:0 0 20px 20px;max-width:50%}@media (max-width: 568px){.hs-featured-image{float:none;margin:0;width:100%;max-width:100%}}.hs-screen-reader-text{clip:rect(1px, 1px, 1px, 1px);height:1px;overflow:hidden;position:absolute !important;width:1px}





body {
padding-top: env(safe-area-inset-top, 40px);
padding-bottom: env(safe-area-inset-bottom, 40px);
}
body {
font-family: 'Figtree', sans-serif !important;
}
a {
color: #2DADCA;
}
body.is-locked {
position: relative;
overflow: hidden;
}
.top\_header {
position: relative;
z-index: 999999999;
}
.header.header\_\_new {
z-index: 99999;
background-color: #fff;
}
.header\_\_main-bg {
position: absolute;
top: 42px;
left: 0;
width: 100%;
transition: all 350ms ease;
z-index: 9999;
background-color: #fff;
}
.header\_\_main-bg.is-hovered {
box-shadow: 0px 30px 40px rgba(0, 0, 0, 0.05);
}
.header .header\_\_nav-subnav {
position: absolute;
top: 100%;
left: 50%;
transform: translateX(-50%);
width: 100%;
list-style: none;
padding: 0 2rem 4rem 1.8rem;
margin: 0;
display: flex;
opacity: 0;
pointer-events: none;
transition: 350ms;
}
.header .header\_\_nav-item.has-subnav:hover .header\_\_nav-subnav {
opacity: 1;
pointer-events: auto;
}
.header .header\_\_nav-subnav-link {
display: flex;
justify-content: flex-start;
align-items: flex-start;
margin: 5px 0;
padding: 5px 0;
color: #000;
font-size: 15px;
font-weight: 600;
line-height: 1.2em;
}
.header .header\_\_nav-subnav-link.no-link {
pointer-events: none;
}
.header .header\_\_nav-subnav-link figure {
margin: 0.1rem .8rem 0 0;
}
.header .header\_\_nav-subnav-link figure img {
max-width: 22px !important;
}
.header .header\_\_nav-subnav-link div {
margin-top: .1rem;
}
.header .header\_\_nav-subnav-link p {
margin: 0;
line-height: 1.3em;
}
.header .header\_\_nav-subnav-link p:nth-child(1) {
color: #012F51;
font-size: 14px;
font-weight: 600;
}
.header .header\_\_nav-subnav-link p:nth-child(2) {
color: #999;
font-size: 12px;
}
.header .header\_\_nav-subnav-link:hover p:first-of-type {
color: #2DADCA;
}
.header .header\_\_nav-subnav-col {
padding-right: 3rem;
padding-top: 2rem;
}
.header .header\_\_nav-subnav-item {
margin-bottom: .5rem;
}
.header .header\_\_nav-subnav-arrow {
align-items: center;
display: flex;
justify-content: center;
color: rgba(60, 60, 61, 0.91);
font-size: 15px;
font-style: normal;
font-weight: 600;
line-height: 18px;
position: relative;
}
.header .header\_\_nav-subnav-arrow svg {
margin-right: 10px;
margin-left: 0;
height: 12px;
margin-top: 1px;
}
.header .header\_\_nav-subnav-link .font-icon {
color: #2dadca;
font-family: sdmicons,sans-serif;
font-size: 11px;
min-width: 34px;
display: block;
text-align: center;
}
.header .header\_\_nav-subnav-line-list {
position: relative;
margin-top: .5rem;
padding-left: 35px;
}
.header .header\_\_nav-subnav-line-list::after {
content: '';
position: absolute;
top: 0;
left: 10px;
height: 100%;
width: 1px;
background-color: #85C1D3;
}
.header .header\_\_nav-subnav-line-list-item,
.header .header\_\_nav-subnav-line-list-item a {
position: relative;
color: #5F7E8B;
font-size: 15px;
font-weight: 500;
line-height: 1.2em;
}
.header .header\_\_nav-subnav-line-list-item {
position: relative;
padding-bottom: 8px;
padding-top: 8px;
z-index: 3;
}
.header .header\_\_nav-subnav-line-list-item::after {
content: '';
position: absolute;
top: 17px;
left: -25px;
height: 1px;
width: 10px;
background-color: #85C1D3;
}
.header .header\_\_nav-subnav-line-list-item:last-child::before {
content: '';
position: absolute;
top: 18px;
left: -25px;
width: 2px;
height: 100%;
background-color: #fff;
}
.subnav-card {
position: relative;
}
.subnav-card figure {
position: relative;
aspect-ratio: 16/9;
padding: 0;
margin: 0;
}
.subnav-card figure img {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
object-fit: cover;
object-position: center;
}
.subnav-card div {
padding-top: 10px;
}
.subnav-card p.title {
color: #000;
font-size: 15px;
font-weight: 600;
margin-bottom: 4px;
transition: color 400ms ease-in-out;
}
.subnav-card p.title span {
transition: transform 400ms ease-in-out;
}
.subnav-card p {
color: #5F7E8B;
font-size: 12px;
font-weight: 500;
line-height: normal;
}
.subnav-card:hover p.title {
color: #2DADCA;
}
.subnav-card:hover p.title span {
transform: translateX(4px);
}
.header\_\_nav-link {
font-weight: 700;
}
.header\_\_site-bg {
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(7, 18, 27, 0.20);
z-index: 9995;
opacity: 0;
pointer-events: none;
transition: all 400ms ease-in-out;
}
.header\_\_site-bg.is-active {
opacity: 1;
}
@media(max-width:1100px){
.header\_\_logo--main {
width: 8rem;
}
.header\_\_nav-item {
padding: 1.5rem 1.3rem;
}
.header .header\_\_nav-subnav {
padding: 0 2rem 4rem 1.3rem;
}
}
@media (min-width: 1024px) {
.header .header\_\_nav-subnav {
padding-top: 2rem;
position: fixed;
top: 0;
left: 44%;
width: auto;
justify-content: center;
}
.header .header\_\_nav-subnav.full-width,
.header .header\_\_nav-subnav.narrow {
left: 50%;
width: 100%;
}
.header .header\_\_nav-subnav.relative {
left: 52%;
transform: none;
}
.header .header\_\_nav-subnav.full-width .header\_\_nav-subnav-main {
gap: 0;
max-width: 1300px;
margin: 0 auto;
width: 100%;
}
.header .header\_\_nav-subnav.full-width .header\_\_nav-subnav-main .header\_\_nav-subnav-col {
min-width: auto;
}
.header .header\_\_nav-subnav-arrow {
display: none;
}
.header .header\_\_nav-subnav-col {
flex: 1;
padding-top: 0;
padding-left: 1rem;
padding-right: 1rem;
}
.header .header\_\_nav-subnav-col.no-border {
border-left: none;
padding-left: 0;
padding-top: 44px;
}
.header .header\_\_nav-subnav-col:not(:first-child) {
border: none;
}
.header.header\_\_new {
height: 66px;
}
.header .header\_\_nav-subnav-main {
display: flex;
gap: 30px;
padding-right: 30px;
}
.header .header\_\_nav-subnav-main.no-card {
padding-right: 0;
}
.header .header\_\_nav-subnav-card {
width: 240px;
padding-top: 15px;
}
.header .header\_\_nav-subnav-list {
margin-top: .5rem;
}
.header .header\_\_nav-subnav-list:not(:last-child) {
margin-bottom: 2rem;
}
.header .header\_\_nav-subnav-link.title span {
white-space: nowrap;
}
.header .header\_\_nav-subnav-item.no-title {
margin-top: 50px;
}
}
@media (max-width: 1023px) {
.header .header\_\_nav-item {
display: flex;
align-items: flex-start;
width: 100%;
padding: 20px 0;
flex-direction: column;
justify-content: flex-start;
}
.header .header\_\_nav-list {
display: flex;
flex-wrap: wrap;
}
.header .header\_\_nav-link {
display: inline-block;
}
.header .header\_\_nav-link.append-nav {
display: block;
color: white;
font-size: 18px;
margin-bottom: 20px;
padding-bottom: 20px;
border-bottom: solid 1px rgba(255,255,255,.5);
width: 100%;
display: none;
}
.header .header\_\_nav-subnav {
align-items: flex-start;
align-content: flex-start;
flex-wrap: wrap;
position: relative;
background: #fff;
top: 0 !important;
width: 100%;
left: initial;
z-index: 2;
padding: 2rem 1.3rem 2rem 0;
height: auto;
overflow-y: scroll;
transform: none;
display: none;
}
.header .header\_\_nav-subnav.is-active {
display: block;
opacity: 1;
pointer-events: auto;
}
.header .header\_\_nav-subnav .header\_\_nav-link.append-nav {
display: none;
}
.header .header\_\_nav-subnav-link p:first-child,
.header .header\_\_nav-subnav-link p:nth-child(2){
color: #5F7E8B !important;
}
.header .header\_\_nav-subnav-line-list-item,
.header .header\_\_nav-subnav-line-list-item a,
.subnav-card h3, .subnav-card p {
color: #5F7E8B !important;
}
.header .header\_\_nav-subnav-link {
color: #000 !important;
}
.header .header\_\_nav-subnav-col {
flex: initial;
padding-right: 0;
padding-top: 0;
width: 100%;
}
.header .header\_\_main-bg {
position: fixed;
height: 100vh;
opacity: 0;
pointer-events: none;
}
.header .header\_\_nav-subnav-link {
padding: 0;
margin: 0;
}
.header .header\_\_nav-subnav-item {
margin-bottom: 1rem;
}
.header .header\_\_nav-subnav-link.title {
margin-bottom: 0;
}
.header .header\_\_nav-subnav-list .header\_\_nav-subnav-list-title,
.header .header\_\_nav-subnav-list .header\_\_nav-subnav-link {
margin-bottom: 10px;
}
.header.header\_\_new.not-home .header\_\_mobile-bar {
transition: all 350ms ease;
}
.header .header\_\_mobile-bar {
border-bottom: solid 1px rgba(160, 160, 160, 0.20);
padding-right: 40px;
}
.header\_\_mobile-row {
border-left: solid 1px rgba(160, 160, 160, 0.20);
}
.search-icon-container {
border-right: solid 1px rgba(160, 160, 160, 0.20);
}
.header\_\_nav-cta {
padding-bottom: 40px;
border-top: solid 1px rgba(160, 160, 160, 0.20);
}
.header\_\_nav-cta .flx {
flex-direction: row-reverse;
align-items: initial;
gap: 10px;
}
.header\_\_nav-cta .flx .header\_\_nav-link,
.header\_\_nav-cta .flx .btn {
flex: 1;
text-align: center;
justify-content: center;
align-items: center;
display: flex;
}
.header\_\_nav-cta .flx .header\_\_nav-link {
border-radius: 5px;
color: #000;
cursor: pointer;
display: inline-block;
font-size: .9rem;
font-weight: 600;
padding: .6rem 1.2rem;
text-align: center;
white-space: normal;
border: 1px solid #001F36;
}
.header\_\_nav-cta .btn {
margin-left: 0;
}
.header\_\_nav-subnav-link,
.header\_\_nav-subnav-line-list-item,
.header\_\_nav-subnav-line-list-item a,
.subnav-card h3,
.subnav-card p {
color: #fff;
}
.header\_\_nav-subnav-line-list-item:last-child::before {
background-color: #fff;
}
.header\_\_nav-subnav-card {
margin-top: 1rem;
display: block;
width: 100%;
}
.subnav-card {
display: flex;
width: 100%;
flex-direction: column;
}
.subnav-card figure {
width: 40%;
}
.header\_\_nav-subnav-arrow.is-active svg .y {
display: none;
}
}
.search-icon-container {
border-radius: 0 !important;
margin-right: 5px;
}
.hamburger {
right: 3px;
}
.hamburger .line {
width: 20px;
}

.form-bottom-logo {
max-width: 940px;
display: flex;
flex-wrap: wrap;
margin: 65px auto 0;
}
.form-bottom-logo .logo {
width: calc(100% / 3);
}
.form-bottom-logo .logo img {
display: block;
margin: 0px auto;
height: 162px;
}
.search-container .hs-search-field .search-close {
position: absolute;
right: -84px;
top: -73px;
cursor: pointer;
}
.mainmenu ul li:last-child {
padding: 0px;
margin: 0px;
}
.search-icon-container {
display: inline-flex;
align-items: center;
justify-content: center;
transition: background-color 0.25s;
width: 54px;
height: 54px;
padding: 10px;
border-radius: 50%;
text-align: center;
}
.search-icon-container:hover {
cursor: pointer;
background: rgb(225, 240, 245, 0.5);
}
.search-container {
display: none;
position: absolute;
left: 0px;
box-shadow: 0px 20px 30px -10px rgb(0 0 0 / 10%);
width: 100%;
background-color: #FFF;
z-index: 999;
top: 0;
padding: 20px 0;
}
.search-container .hs-search-field {
position: relative;
margin: 140px auto 20px;
max-width: 1120px;
border-bottom: 1px solid #DDD;
}
.search-container .hs-search-field\_\_bar {
position: relative;
margin-bottom: 10px;
}
.search-container .hs-search-field\_\_bar input.hs-search-field\_\_input {
background-color: transparent !important;
padding: 0 35px 0 70px !important;
font-size: 20px;
color: #333;
letter-spacing: -0.02em;
font-weight: 400;
font-family: SDMontserrat, sans-serif !important;
margin: 0 0 6px !important;
}
.search-container .hs-search-field .search-bar-icon {
position: absolute;
left: 18px;
top: 13px;
bottom: auto;
right: auto;
width: 28px;
}
.search-container .hs-search-field\_\_bar form .search-bar-img-btn {
position: absolute;
left: auto;
top: 0px;
bottom: auto;
right: 18px;
-webkit-appearance: button;
cursor: pointer;
padding: 20px 0px;
}
.hs-search-field {
position: relative;
margin-top: 10px;
}
.hs-search-field input:not([type=radio]):not([type=checkbox]):not([type=submit]):not([type=button]):not([type=image]):not([type=file]), select, textarea {
margin: 0;
padding-left: 50px;
}
@media(min-width:1024px) {
.search-container .hs-search-field {
display: block;
}
}
@media(max-width:1023px) {
.search-bar-icon-mobile {
position: absolute;
left: 18px;
top: 13px;
bottom: auto;
right: auto;
}
.search-bar-img-btn-mobile {
position: absolute;
left: auto;
top: 18px;
bottom: auto;
right: 18px;
-webkit-appearance: button;
cursor: pointer;
}
/\* #search-container,
.search-icon-container{
display: none !important;
} \*/
/\* .hs-search-field\_\_bar input.hs-search-field\_\_input {
background-color: transparent !important;
padding: 0 35px 0 55px !important;
font-size: 16px;
color: #333 !important;
letter-spacing: -0.02em;
font-weight: 400;
font-family: SDMontserrat, sans-serif !important;
margin: 0 0 6px !important;
} \*/
}
@media (min-width:992px) and (max-width:1070px) {
.search-container .hs-search-field {
max-width: 90%;
}
.search-close {
right: 0px !important;
}
}
@media (min-width:1071px) and (max-width:1215px) {
.search-container .hs-search-field .search-close {
right: 30px;
}
.search-container .hs-search-field {
max-width: 90%;
}
}
@media (min-width:1071px) and (max-width:1429px) {
.search-container .hs-search-field .search-close {
right: 0px;
}
}

.breadcrum .crum-link{
font-family: var(--buttonFontFamily);
font-size: 16px !important;
font-style: normal;
font-weight: 400 !important;
line-height: 130%; /\* 20.8px \*/
letter-spacing: 0;
}
.breadcrum span{
color: var(--colorP2);
}
.blog-post--hero h1 {
color: #000;
font-size: 44px;
}
.blog-post--hero .blog-subtitle {
padding: 24px 0;
}
.blog-post--hero-row {
column-gap: 30px;
}
.blog-post--hero-btn-row .btn.navy svg {
width: 15px;
height: 15px;
transform: translateY(3px);
}
.blog-post--hero-btn-row .btn.navy span {
display: flex;
gap: 5px;
}
.blog-post--hero-image figure {
aspect-ratio: 16/9;
margin: 0;
border-radius: 8px;
overflow: hidden;
}
.blog-post--hero-btn-row {
margin-top: 20px;
gap: 10px;
flex-direction: column;
}
.blog-post--hero-content {
flex: 1;
}
@media(max-width:767px){
.blog-post--hero {
padding: 40px 0;
}
.blog-post--hero h1 {
font-size: 32px;
}
.blog-post--hero .blog-subtitle {
padding-top: 0;
}
.blog-post--hero-content,
.blog-post--hero-image {
width: 100%;
}
.blog-post--hero-btn-row {
flex-wrap: wrap;
}
}
@media(max-width: 1024px){
.blog-post--hero-row {
row-gap: 30px;
flex-direction: column;
}
}


.blog-post--meta{
background-color: var(--colorP1);
border-color: var(--colorP2);
}
.inner-content-wrap .left .about-authortext a.download-ebook{position:relative;font-weight:bold;margin-top:20px;font-size:19px;color:#00b7ff;display:inline-block;text-transform: none;}
.share-buttons svg {width: 1em;height: 1em;fill: #fff;stroke: none;}
.share-buttons .hacker{background-color: #FF6600;}
.demo-box .social-share ul li a.reddit {background-color: #FF5700;border-color: #FF5700;}
.about-reviewer{margin: 30px 0;}
.duration{margin: 20px 0px 10px 0px;}
.post-inner-topic span, .date span{font-weight:600;}



.post-inner .img-featured{
position: static;
width: auto;
height: 150px;
max-width: none;
}
.post-inner {
align-items: center;
}
.related-post .relatedpost-wrapper .post-inner .post-content {
color: #000c14;
}
@media (max-width:767px){
.related-post .relatedpost-wrapper .post-inner .right {
padding-bottom: 20px;
background-color: #fff;
}
.post-inner .img-featured{
position: static;
width: auto;
height: 150px;
max-width: none;
}
.related-post .relatedpost-wrapper .post-inner .left .featured-image{
margin-bottom: 15px;
}
}

@font-face {
font-family: "Figtree";
font-weight: 400;
font-style: normal;
font-display: swap;
src: url("/\_hcms/googlefonts/Figtree/regular.woff2") format("woff2"), url("/\_hcms/googlefonts/Figtree/regular.woff") format("woff");
}
@font-face {
font-family: "Figtree";
font-weight: 700;
font-style: normal;
font-display: swap;
src: url("/\_hcms/googlefonts/Figtree/700.woff2") format("woff2"), url("/\_hcms/googlefonts/Figtree/700.woff") format("woff");
}


var \_hsp = window.\_hsp = window.\_hsp || [];
\_hsp.push(['addPrivacyConsentListener', function(consent) { if (consent.allowed || (consent.categories && consent.categories.analytics)) {
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create','UA-62690913-1','auto');
ga('send','pageview');
}}]);



var \_hsp = window.\_hsp = window.\_hsp || [];
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
var useGoogleConsentModeV2 = true;
var waitForUpdateMillis = 1000;
if (!window.\_hsGoogleConsentRunOnce) {
window.\_hsGoogleConsentRunOnce = true;
gtag('consent', 'default', {
'ad\_storage': 'denied',
'analytics\_storage': 'denied',
'ad\_user\_data': 'denied',
'ad\_personalization': 'denied',
'wait\_for\_update': waitForUpdateMillis
});
if (useGoogleConsentModeV2) {
\_hsp.push(['useGoogleConsentModeV2'])
} else {
\_hsp.push(['addPrivacyConsentListener', function(consent){
var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics));
var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement));
gtag('consent', 'update', {
'ad\_storage': hasAdsConsent ? 'granted' : 'denied',
'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied',
'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied',
'ad\_personalization': hasAdsConsent ? 'granted' : 'denied'
});
}]);
}
}
gtag('js', new Date());
gtag('set', 'developer\_id.dZTQ1Zm', true);
gtag('config', 'G-BZ31E5Y3QW');




var \_hsp = window.\_hsp = window.\_hsp || [];
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
var useGoogleConsentModeV2 = true;
var waitForUpdateMillis = 1000;
var hsLoadGtm = function loadGtm() {
if(window.\_hsGtmLoadOnce) {
return;
}
if (useGoogleConsentModeV2) {
gtag('set','developer\_id.dZTQ1Zm',true);
gtag('consent', 'default', {
'ad\_storage': 'denied',
'analytics\_storage': 'denied',
'ad\_user\_data': 'denied',
'ad\_personalization': 'denied',
'wait\_for\_update': waitForUpdateMillis
});
\_hsp.push(['useGoogleConsentModeV2'])
}
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WH42NPH');
window.\_hsGtmLoadOnce = true;
};
\_hsp.push(['addPrivacyConsentListener', function(consent){
if(consent.allowed || (consent.categories && consent.categories.analytics)){
hsLoadGtm();
}
}]);





function OptanonWrapper() {
}



fetch("https://api.vector.co/pixel/ip-info")
.then(res => res.json())
.then(data => {
const countryCode = data?.ipInfo?.countryCode;
const blockedCountries = [
"CN", "RU", "KP", "IR", "IQ", "MM", "LY",
"CC", "MS", "NR", "ST", "GF", "AX"
];
if (!countryCode || blockedCountries.includes(countryCode)) {
// Remove all existing content
document.body.innerHTML = "";
// Create message container
const message = document.createElement("div");
message.style.cssText = `
display: flex;
align-items: center;
justify-content: center;
height: 100vh;
text-align: center;
font-family: Arial, sans-serif;
background: #f5f5f5;
color: #333;
padding: 20px;
`;
message.innerHTML = `
<div>
<h1 style="font-size: 28px; margin-bottom: 10px; color:#000;">
Access Restricted
</h1>
<p style="font-size: 16px; max-width: 500px; margin: 0 auto;">
This website is currently inaccessible in your region.
</p>
</div>
`;
document.body.appendChild(message);
}
})
.catch(err => {
console.error("Geo lookup failed:", err);
});

#hs\_cos\_wrapper\_module\_1769470646767 .section-h2-text-and-logos,
#hs\_cos\_wrapper\_module\_17694699700392 .section-h2-text-and-logos {
padding: 0 !important;
}
#hs\_cos\_wrapper\_widget\_1756496981732 form input[type="submit"] {
background: #54d5f2;
color: #000;
padding: 0;
border-radius: 3px !important;
font-weight: 500;
font-size:17px;
}
#hs\_cos\_wrapper\_widget\_1656617454515 .section-h2-text-and-logos {
padding-bottom:0 !important;
}












.flx {
display: flex;
}
.flx.wrap {
flex-wrap: wrap;
}
.flx.j-sb {
justify-content: space-between;
}
.flx.j-c {
justify-content: center;
}
.flx.j-start {
justify-content: flex-start;
}
.flx.a-c {
align-items: center;
}
.flx.a-start {
align-items: flex-start;
}
.flx.center {
align-items: center;
justify-content: center;
}
.contain {
max-width: 1220px;
margin: 0 auto;
padding: 0 40px;
width: 100%;
}
@media(max-width:767px){
.contain {
padding: 0 20px;
}
.home-2023 h1 {
font-size: 28px !important;
}
}
.btn {
cursor: pointer;
display: inline-block;
text-align: center;
transition: all 0.15s linear;
white-space: normal;
padding: .6rem 1.2rem;
border-radius: 5px;
background: #63DE7E;
color: #000;
font-weight: 600;
font-size: .9rem;
}
.btn svg \* {
transition: all 0.15s linear;
}
.btn:hover {
color: #fff;
}
.btn:hover svg path {
fill: #fff;
}
.btn.green:hover {
background-color: #297D4B;
}
.btn.navy {
background-color: #001D32;
color: #fff;
}
.btn.navy:hover {
background-color: #176E8D;
}
.btn.gray {
background-color: #ECF7FF;
}
.btn.icon {
display: inline-flex;
align-items: center;
}
.btn.icon svg {
margin-right: 5px;
height: auto;
}
body {
padding-top: env(safe-area-inset-top, 40px);
padding-bottom: env(safe-area-inset-bottom, 40px);
}
body {
font-family: 'Figtree', sans-serif !important;
}
a {
color: #2DADCA;
}
body.is-locked {
position: relative;
overflow: hidden;
}
.header.header\_\_new {
z-index: 99999;
background-color: #fff;
}
.header\_\_main-bg {
position: absolute;
top: 42px;
left: 0;
width: 100%;
transition: all 350ms ease;
z-index: 9999;
background-color: #fff;
}
.header\_\_main-bg.is-hovered {
box-shadow: 0px 30px 40px rgba(0, 0, 0, 0.05);
}
.header\_\_nav-subnav {
position: absolute;
top: 100%;
left: 50%;
transform: translateX(-50%);
width: 100%;
list-style: none;
padding: 0 2rem 4rem 1.8rem;
margin: 0;
display: flex;
opacity: 0;
pointer-events: none;
transition: 350ms;
}
.header\_\_nav-item.has-subnav:hover .header\_\_nav-subnav {
opacity: 1;
pointer-events: auto;
}
.header\_\_nav-subnav-link {
display: flex;
justify-content: flex-start;
align-items: flex-start;
color: #012F51;
margin: 5px 0;
padding: 5px 0;
}
.header\_\_nav-subnav-link figure {
margin: 0.1rem .8rem 0 0;
}
.header\_\_nav-subnav-link figure img {
max-width: 22px !important;
}
.header\_\_nav-subnav-link div {
margin-top: .1rem;
}
.header\_\_nav-subnav-link p {
margin: 0;
line-height: 1.3em;
}
.header\_\_nav-subnav-link p:nth-child(1) {
color: #012F51;
font-size: 14px;
font-weight: 600;
}
.header\_\_nav-subnav-link p:nth-child(2) {
color: #999;
font-size: 12px;
}
.header\_\_nav-subnav-link:hover p:first-of-type {
color: #2DADCA;
}
.header\_\_nav-subnav-col {
padding-right: 3rem;
padding-top: 2rem;
flex: 1;
}
.header\_\_nav-subnav-item {
margin-bottom: 1rem;
}
.header\_\_nav-subnav-arrow {
align-items: center;
display: flex;
justify-content: center;
color: #012f51;
font-size: 15px;
font-style: normal;
font-weight: 600;
line-height: 18px;
position: relative;
}
.header\_\_nav-subnav-arrow svg {
margin-left: 10px;
height: 12px;
margin-top: 1px;
}
.header\_\_nav-subnav-link .font-icon {
color: #2dadca;
font-family: sdmicons,sans-serif;
font-size: 11px;
min-width: 34px;
display: block;
text-align: center;
}
@media(max-width:1100px){
.header\_\_logo--main {
width: 8rem;
}
.header\_\_nav-item {
padding: 1.5rem 1.3rem;
}
.header\_\_nav-subnav {
padding: 0 2rem 4rem 1.3rem;
}
}
@media (min-width: 1024px) {
.header\_\_nav-subnav {
width: initial;
padding-top: 2rem;
}
.header\_\_nav-subnav-arrow {
display: none;
}
.header\_\_nav-subnav-col:not(:first-child) {
border-left: solid 1px #eee;
}
.header\_\_nav-subnav-col {
min-width: 15vw;
padding-top: 0;
padding-left: 1rem;
padding-right: 1rem;
}
.header\_\_nav-subnav-col.no-border {
border-left: none;
padding-left: 0;
padding-top: 44px;
}
}
@media (max-width: 1023px) {
.header\_\_nav-item {
display: flex;
align-items: center;
width: 100%;
padding: 20px 0;
}
.header\_\_nav-list {
display: flex;
flex-wrap: wrap;
}
.header\_\_nav-link {
display: inline-block;
}
.header\_\_nav-link.append-nav {
display: block;
color: white;
font-size: 18px;
margin-bottom: 20px;
padding-bottom: 20px;
border-bottom: solid 1px rgba(255,255,255,.5);
width: 100%;
}
.header\_\_nav-subnav {
align-items: flex-start;
align-content: flex-start;
flex-wrap: wrap;
position: fixed;
background: #012F51;
top: 54px;
width: calc(100vw - 20px);
left: 100%;
z-index: 2;
padding: 2rem 1.3rem;
height: calc(100% - 54px);
overflow-y: scroll;
transform: none;
}
.header\_\_nav-subnav.is-active {
opacity: 1;
pointer-events: auto;
left: 20px;
}
.header\_\_nav-subnav-link p:first-child,
.header\_\_nav-subnav-link p:nth-child(2){
color: #fff;
}
.header\_\_nav-subnav-col {
flex: initial;
padding-right: 0;
padding-top: 0;
width: 100%;
}
.header\_\_main-bg {
position: fixed;
height: 100vh;
opacity: 0;
pointer-events: none;
}
.header\_\_nav-subnav-link {
padding: 0;
margin: 0;
}
.header\_\_nav-subnav-item {
margin-bottom: 2rem;
}
.header\_\_nav-subnav-link.title {
margin-bottom: 20px;
}
/\* .header\_\_mobile-bar.is-active {
position: fixed;
} \*/
.header.header\_\_new.not-home .header\_\_mobile-bar {
transition: all 350ms ease;
}
/\* .header.header\_\_new.not-home .header\_\_mobile-bar.is-active {
transform: translateY(-54px);
} \*/
.header\_\_nav-cta {
padding-bottom: 40px;
}
}
.hamburger {
position: absolute;
width: 44px;
height: 44px;
right: 10px;
top: 5px;
border-radius: 9999px;
transition: all 300ms ease-in-out;
z-index: 9999;
cursor: pointer;
display: flex;
align-items: center;
justify-content: center;
padding: 16px;
}
.hamburger .line {
z-index: 1;
position: relative;
width: 24px;
height: 2px;
background-color: #012f51;
display: block;
margin: 2px auto;
border-radius: 40px;
transition: all 300ms ease-in-out;
}
.hamburger.is-active {
transform: rotate(45deg);
}
.hamburger.is-active .line {
margin: 9px auto;
}
.hamburger.is-active .line:nth-child(1) {
transform: translateY(10px);
}
.hamburger.is-active .line:nth-child(2) {
opacity: 0;
}
.hamburger.is-active .line:nth-child(3) {
transform: translateY(-12px) rotate(90deg);
}
.footer.new {
background-color: #001D32;
padding-top: 60px;
}
.footer.new .top-part .inner {
padding-bottom: 40px;
border-bottom: solid 1px #013458;
}
.footer.new .bottom-part .inner {
padding-top: 20px;
}
.footer.new .bottom-part .footer-group div.widget-type-header span span {
font-size: 15px;
color: #53D5F2;
text-transform: initial;
}
.footer.new .bottom-part .footer-group a {
color: #fff;
font-size: 15px;
}
.footer.new .copy-text .inner-wrap {
color: #fff;
}
.footer.new .bottom-part .footer-group {
flex: 1;
padding-right: 20px;
}
.footer.new .copy-text .inner-wrap .copyright-link a {
color: #fff;
}
.footer.new .top-part .social-media .social-profile li a svg {
height: 16px;
width: 16px;
}
.footer.new .top-part .social-media .social-profile li a:hover {
background-color: #2DADCA;
}
.footer.new .top-part .social-media .social-profile li a:hover svg path {
fill: #001D32;
}
.footer.new .top-part .social-media .social-profile li a svg path {
fill: #2DADCA;
}
.footer.new .top-part .social-media .social-profile li a {
width: 32px;
height: 32px;
display: flex;
align-items: center;
justify-content: center;
border: solid 1px #2DADCA;
border-radius: 999px;
margin: 0 3px;
padding: 0;
}
.footer.new .top-part .social-media .social-profile li a span {
display: flex;
align-items: center;
justify-content: center;
}
@media(max-width:991px){
.footer.new .top-part .inner {
display: flex;
}
.footer.new .top-part .logo {
display: block;
}
.footer.new .top-part .social-media .social-profile li a {
width: 30px;
height: 30px;
}
.footer.new .top-part .social-media {
flex: 1;
display: flex;
justify-content: flex-end;
}
}
.top\_header.new\_2023 {
display: block;
background-color: #001D32;
font-size: 14px;
font-weight: 600;
padding: 10px 20px;
text-align: center;
color: white;
}
.top\_header.new\_2023.hidden {
display: none;
}
.top\_header.new\_2023 a {
color: #63E580;
}
.flx {
display: flex;
}
.flx.wrap {
flex-wrap: wrap;
}
.flx.j-sb {
justify-content: space-between;
}
.flx.j-c {
justify-content: center;
}
.flx.j-start {
justify-content: flex-start;
}
.flx.a-c {
align-items: center;
}
.flx.a-start {
align-items: flex-start;
}
.flx.center {
align-items: center;
justify-content: center;
}
.contain {
max-width: 1220px;
margin: 0 auto;
padding: 0 40px;
width: 100%;
}
@media(max-width:767px){
.contain {
padding: 0 20px;
}
.home-2023 h1 {
font-size: 28px !important;
}
}
.btn {
cursor: pointer;
display: inline-block;
text-align: center;
transition: all 0.15s linear;
white-space: normal;
padding: .6rem 1.2rem;
border-radius: 5px;
background: #63DE7E;
color: #000;
font-weight: 600;
font-size: .9rem;
}
.btn svg \* {
transition: all 0.15s linear;
}
.btn:hover {
color: #fff;
}
.btn:hover svg path {
fill: #fff;
}
.btn.green:hover {
background-color: #297D4B;
}
.btn.navy {
background-color: #001D32;
color: #fff;
}
.btn.navy:hover {
background-color: #176E8D;
}
.btn.gray {
background-color: #ECF7FF;
}
.btn.icon {
display: inline-flex;
align-items: center;
}
.btn.icon svg {
margin-right: 5px;
height: auto;
}
.header {
border-bottom: solid 1px #ececec;
}
.header\_\_logo {
padding-right: 1.7rem;
border-right: solid 1px #ececec;
width: 10rem;
}
.header\_\_logo img {
display: block;
}
.header\_\_nav {
position: relative;
flex: 1;
padding-left: .8rem;
}
.header\_\_nav-cta {
display: flex;
align-items: center;
}
.header\_\_nav-cta .btn {
margin-left: 1.6rem;
}
@media (max-width: 1023px) {
.header\_\_nav {
flex: initial;
padding-left: 0;
}
}
.header\_\_nav-main {
flex: 1;
}
.header\_\_nav-list {
list-style: none;
margin: 0;
padding: 0;
}
.header\_\_nav-item {
position: relative;
margin: 0;
padding: 1.5rem 1.8rem;
}
.header\_\_nav-link {
position: relative;
font-family: ;
font-style: normal;
font-size: 15px;
font-weight: 600;
line-height: 18px;
color: #012F51;
}
.header\_\_mobile-bar {
position: relative;
top: 0;
left: 0;
width: 100%;
padding: 12px 20px;
height: 54px;
}
@media(min-width:1024px){
.header\_\_mobile-bar {
display: none;
}
}
@media(max-width:1023px){
.header.header\_\_new {
border-bottom: none;
}
.header\_\_logo.header\_\_logo--main {
display: none;
}
.header\_\_container.contain {
position: fixed;
left: 100%;
top: 0;
width: 100vw;
padding: 60px 20px 30px;
transition: all 350ms ease;
background-color: white;
display: flex;
align-content: space-between;
height: 100vh;
overflow-y: scroll;
}
.header\_\_container.contain.is-active {
left: 0;
}
.header\_\_container {
flex-wrap: wrap;
}
.header\_\_nav-main {
flex-wrap: wrap;
flex: initial;
width: 100%;
}
.header\_\_nav {
width: 100%;
}
.header\_\_logo {
padding-right: 0;
border-right: none;
width: 140px;
}
.header\_\_nav-item {
padding: 20px 0;
}
.header\_\_nav-cta {
width: 100%;
}
.header\_\_nav-cta div {
width: 100%;
}
.header\_\_nav-cta .flx {
width: 100%;
justify-content: space-between;
padding-top: 1rem;
}
}





(function () {
var zi = document.createElement('script');
zi.type = 'text/javascript';
zi.async = true;
zi.referrerPolicy = 'unsafe-url';
zi.src = 'https://ws.zoominfo.com/pixel/6169bf9791429100154fc0a2';
var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(zi, s);
})();

<img src="https://ws.zoominfo.com/pixel/6169bf9791429100154fc0a2" width="1" height="1" style="display: none;">

var punch\_globals = punch\_globals || {};
punch\_globals.jsAssets = punch\_globals.jsAssets || {};
punch\_globals.cssAssets = punch\_globals.cssAssets || {};
punch\_globals.jsAssets.mej = '//21126185.fs1.hubspotusercontent-na1.net/hubfs/21126185/hub\_generated/template\_assets/1/197732594840/1777918344855/template\_mej.js';
punch\_globals.jsAssets.videoCombo = '//21126185.fs1.hubspotusercontent-na1.net/hubfs/21126185/hub\_generated/template\_assets/1/197732580529/1777918344840/template\_video-combo.min.js';
punch\_globals.jsAssets.slideshow = '//21126185.fs1.hubspotusercontent-na1.net/hubfs/21126185/hub\_generated/template\_assets/1/197732594836/1777918339516/template\_slideshow.min.js';
punch\_globals.cssAssets.slideshow = '//21126185.fs1.hubspotusercontent-na1.net/hubfs/21126185/hub\_generated/template\_assets/1/197732594817/1777918339825/template\_slideshow.min.css';

function punchClassApplier(el, classes){
el.classList.add( ...classes );
}
function punchAttachOverlay(thisEl, thisOverlayEl) {
thisEl.insertBefore(thisOverlayEl, thisEl.firstChild);
}

:root{
--containerWidth: 1410px;
}
.container {
max-width: 1410px;
}
#top .header{
position: absolute;
}
/\* 2025 Blog Post Detail \*/
.blog-post--nav-title{
border-bottom: 1px solid var(--colorP1) !important;
}
.blog-post--nav-title p{
font-style: normal;
font-weight: 400;
line-height: 130%; /\* 27.3px \*/
}
.inner-content-wrap .inner .left {
width: 25%;
max-width: initial;
padding-bottom: 35px;
bottom: initial;
top: 35px;
align-self: flex-start;
}
.inner-content-wrap .inner .left {
-ms-overflow-style: none;
scrollbar-width: none;
}
.inner-content-wrap .inner .left::-webkit-scrollbar {
display: none;
}
.inner-content-wrap .inner .right {
width: 75%;
flex: 1;
padding-left: 50px;
padding-top: 40px;
}
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--content li {
margin-bottom: 0;
}
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--content table {
table-layout: initial !important;
width: 100% !important;
}
.blog-post .inner-content-wrap {
padding-top: 20px;
}
.blog-post .inner-content-wrap {
margin: 0;
padding-bottom: 0;
}
.blog-post--meet {
color: var(--colorWhite, #FFF);
padding: 60px 0;
}
.blog-post--meet-author {
width: 66%;
padding-top: 20px;
padding-right: 20px;
margin-right: 40px;
}
.blog-post--meet-subscribe {
flex: 1;
}
.blog-subscription .sub-right .subsribe-form form .hs-submit .actions input[type="submit"] {
background-color: #2DADCA !important;
}
.blog-post--meet-author small {
display: block;
margin-bottom: 10px;
color: var(--Cyan, #2DADCA);
font-size: 16px;
font-weight: 700;
line-height: 120%;
}
.blog-post--meet-author a {
font-weight: 600;
letter-spacing: -0.39px;
}
.blog-post--meet-author h2 {
color: var(--colorWhite, #FFF);
font-size: 29px;
font-weight: 600;
line-height: 120%;
letter-spacing: -0.39px;
font-family: 'SDMontserrat' , sans-serif;
}
.blog-post--meet-author p {
color: var(--colorWhite, #FFF);
font-size: 19px;
font-weight: 500;
line-height: 135%;
}
.blog-post--meet-author .portrait {
background-color: white;
border-radius: 100%;
width: 200px;
height: 200px;
overflow: hidden;
}
.blog-post--meet-author .meta {
flex: 1;
padding-left: 30px;
}
.blog-post--meet-subscribe .blog-subscription .sub-right .text-line {
font-size: 18px;
}
.blog-post--meet .blog-subscription {
border-top: none;
border-radius: 10px;
box-shadow: 0px 30px 30px 0px rgba(0, 0, 0, 0.10);
margin: 0;
padding: 30px;
}
.blog-post--meet .blog-subscription .sub-right {
border-left: none;
width: 100%;
padding: 0;
}
.blog-post--meet-subscribe .blog-subscription .sub-right .subsribe-form form .hs\_email .input .hs-input {
margin: 0;
}
.blog-post--nav-title {
padding-bottom: 10px;
border-bottom: solid 2px #D9E1E5;
}
.blog-post--nav-title p {
font-weight: 600;
font-size: 19px;
line-height: 30px;
}
.blog-post--nav-list {
list-style: none;
padding: 0;
}
.blog-post--nav-list li,
.blog-post--nav-list li a {
color: var(--colorWhite, #FFF);
/\* Post/H6 \*/
font-size: 15px;
font-style: normal;
font-weight: 400;
line-height: 130%; /\* 20.8px \*/
}
.blog-post--nav-list li {
margin-bottom: 2px;
}
.blog-post--nav-list li a {
padding: 7px 10px;
display: block;
border: 1px solid transparent;
}
.blog-post--nav-list li.is-active a,
.blog-post--nav-list li a:hover {
border-radius: 4px;
border: 1px solid var(--Gradient-Stroke, #2C7B8C);
background: rgba(1, 52, 88, 0.50);
}
/\* \*/
.inner-content-wrap .left .demo-box .demo-title {
padding-bottom: 12px !important;
}
.inner-content-wrap .left .demo-box .demo-btn {
padding-bottom: 8px !important;
}
.inner-content-wrap .left .demo-box .list ul li {
padding-left: 16px;
position: relative;
}
.inner-content-wrap .left .demo-box .list p {
font-family: system-ui;
font-size: 15px;
line-height: 23px;
position: relative;
font-weight: 500;
}
.blog-post--nav-cta {
margin-top: 20px;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box {
background: transparent;
margin-top: 20px;
padding: 24px;
border-radius: 8px;
border: 1px solid #2C7B8C;
background: rgba(1, 52, 88, 0.25);
position: relative;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box:before{
content: "";
position: absolute;
top: 50%;
left: 50%;
width: calc(100% - 20px);
height: calc(100% - 20px);
z-index: 0;
background: rgba(1, 52, 88, 0.25);
border-radius: 8px;
border: 0.75px solid #53D5F2;
transform: translate(-50%, -50%);
pointer-events: none;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box li {
color: var(--colorWhite);
font-size: 14px;
font-weight: 500;
line-height: 135%;
margin-bottom: 5px;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box .demo-btn a.cta {
border-radius: 4px;
background: #2dacda;
font-size: 18px;
font-weight: 600;
line-height: 100%;
padding: 16px 10px;
text-align: center;
flex: 1;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box .demo-btn a.cta:hover {
background: #176e8d;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box .demo-btn a.image-link {
padding: 0;
background-color: transparent;
border-radius: 0;
line-height: 0;
}
.inner-content-wrap .left .demo-box .demo-btn {
gap: 15px;
}
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next{
border-radius: 8px;
border: 1px solid var(--Gradient-Stroke, #2C7B8C);
background: rgba(1, 52, 88, 0.50);
}
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next-text p {
color: white !important;
}
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next h3,
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next h3 span,
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next h3 strong,
.inner-content-wrap .inner .right .blog-post\_\_body .blog-post--endcap-next h3 strong span {
margin-top: 0;
}
.inner-content-wrap .inner .right .blog-post\_\_body h3 {
font-size: 20px !important;
}
.inner-content-wrap .inner .right .blog-post\_\_body h3.new-h6 {
font-family: var(--buttonFontFamily);
font-size: 18px;
font-style: normal;
font-weight: 400;
line-height: 130%; /\* 23.4px \*/
}
.inner-content-wrap .inner .right .blog-post\_\_body blockquote {
margin-right: 0;
background-color: #013458 !important;
}
.inner-content-wrap .inner .right .blog-post\_\_body blockquote \*{
color: white !important
}
.inner-content-wrap .inner .right .blog-post\_\_body blockquote p {
font-size: 19px !important;
line-height: 30px !important;
}
.inner-content-wrap .inner .right .blog-post\_\_body blockquote p:only-child {
margin-bottom: 0 !important;
}
.blog-subscription .sub-right .subsribe-form form .hs\_email {
width: 100% !important;
}
.blog-subscription .sub-right .subsribe-form form .hs-submit .actions {
position: relative !important;
right: initial !important;
top: initial !important;
margin-top: 10px !important;
margin-left: 0 !important;
}
.blog-subscription .sub-right .subsribe-form form .hs-submit .actions input[type="submit"] {
margin-right: auto;
margin-left: 0;
width: 100%;
}
.blog-post--hero-row {
padding-right: 110px;
}
.blog-post--meet-row {
display: flex;
padding: 40px 50px;
flex-direction: row;
justify-content: flex-end;
align-items: center;
gap: 12.845px;
align-self: stretch;
border-radius: 20px;
border: 1px solid #53D5F2;
background: #001D32;
position: relative;
}
.blog-post--meet-row:before{
content: "";
position: absolute;
top: 50%;
left: 50%;
width: calc(100% - 20px);
height: calc(100% - 20px);
z-index: 0;
background: rgba(1, 52, 88, 0.25);
border-radius: 12px;
border: 0.75px solid #53D5F2;
transform: translate(-50%, -50%);
display: block;
pointer-events: none;
}
.blog-post--meet-row \* {
position: relative;
}
@media(max-width:1440px){
.inner-content-wrap .inner .right {
padding-left: 30px;
}
.inner-content-wrap .left .demo-box .demo-btn {
flex-direction: column;
align-content: flex-start;
justify-content: flex-start;
}
}
@media(max-width:992px){
.blog-post--hero-row {
padding-right: 0;
}
.blog-post .inner-content-wrap .main-inner {
flex-direction: column;
}
.inner-content-wrap .inner .right {
width: 100%;
padding-left: 0;
padding-right: 0;
}
.inner-content-wrap .inner .left {
width: 100%;
max-width: 100%;
}
.blog-post--nav {
display: none;
}
.inner-content-wrap .left .demo-box .demo-btn {
gap: 10px;
}
.inner-content-wrap .left .demo-box .demo-btn a {
flex: 1;
}
.blog-post--meet-row {
flex-direction: column;
gap: 40px;
display: flex;
}
.blog-post--meet-author {
width: 100%;
}
.inner-content-wrap .left .blog-post--nav-cta .demo-box .demo-btn a.image-link img {
width: initial;
max-width: initial;
}
}
.related-post{
background-color: var(--colorP1);
color: var(--colorWhite);
}
@media(max-width:767px){
.inner-content-wrap .inner .left {
padding-bottom: 40px;
}
.inner-content-wrap .inner .left-inner {
padding-top: 0;
}
.blog-post--meet-author {
flex-direction: column;
text-align: center;
border-right: none;
padding-right: 0;
}
.blog-post--meet-author .portrait {
width: 100px;
height: 100px;
margin: 0 auto;
}
.blog-post--meet-author .meta {
padding-left: 0;
margin-top: 20px;
}
}
@media (max-width: 500px) {
.inner-content-wrap .inner .right .blog-post\_\_body p:first-child {
font-size: 19px;
line-height: 30px;
}
}
.blog-post--endcap-category,
.inner-content-wrap .inner .left{
border-color: #30709F;
}
@media (max-width: 767px) {
.blog-post--endcap-social{
padding-bottom: 40px;
}
.related-post .relatedpost-wrapper .post-inner {
flex-direction: column;
gap: 20px;
}
.related-post .relatedpost-wrapper .post-inner .left {
width: 100%;
}
.blog-post--meet-author {
margin-right: 0;
}
.related-post .relatedpost-wrapper .post-inner .right{
background-color: transparent !important;
}
}
.blog-subscription {
border-radius: 8px !important;
border: 1px solid #2C7B8C !important;
background: rgba(1, 52, 88, 0.25);
position: relative;
}
.blog-post--endcap-social-buttons a{
border: 0 !important;
background-color: var(--colorP2);
}
.blog-content-wrapper .filter-topic ul li a{
background-color: var(--colorP2);
font-family: var(--buttonFontFamily);
font-size: 16px;
font-style: normal;
font-weight: 700;
line-height: 22px; /\* 137.5% \*/
text-transform: uppercase;
padding: 7px 15px 7px !important;
}
.blog-post--meet-subscribe .blog-subscription .sub-right .subsribe-form form .hs\_email .input .hs-input{
background-color: white !important;
}
.inner-content-wrap .left .demo-box .list ul li:after{
background-color: white;
}
@media (max-width: 767px) {
.hs-form .hs-form-field:not(:last-of-type) div.input{
margin: 0 !important
}
}
.blog-subscription .sub-right .subsribe-form form .hs-submit .actions input[type="submit"],
.inner-content-wrap .left .demo-box .demo-btn a.punch-btn-inner{
display: flex;
padding: 10px 18px;
align-items: center;
gap: 6px;
border-radius: 8px;
background: #D152F2 !important;
color: #001D32;
font-family: var(--buttonFontFamily);
font-size: 14.4px;
font-style: normal;
font-weight: 700;
line-height: 22px;
text-transform: uppercase;
}
.inner-content-wrap .left .demo-box .demo-btn .punch-btn-inner:after,
.inner-content-wrap .left .demo-box .demo-btn .punch-btn-inner:before{
display: none;
}
@media (max-width: 767px) {
.blog-post--author{
margin-top: 15px;
}
.blog-post--author-text{
padding-left: 0;
padding-top: 12px;
}
.blog-post--meta-item{
border: 0 !important;
}
.blog-post--endcap-social-buttons{
display: flex;
}
}
.related-post .relatedpost-wrapper .post-inner .right{
padding-top: 0;
}
.





(function() {
if (typeof window === 'undefined') return;
if (typeof window.signals !== 'undefined') return;
var script = document.createElement('script');
script.src = 'https://cdn.cr-relay.com/v1/site/1cc37ee0-f2fe-44be-89ad-641115799d83/signals.js';
script.async = true;
window.signals = Object.assign(
[],
['page', 'identify', 'form'].reduce(function (acc, method){
acc[method] = function () {
signals.push([method, arguments]);
return signals;
};
return acc;
}, {})
);
document.head.appendChild(script);
})();

[Curious about how StrongDM works? 🤔 Learn more here!](https://www.strongdm.com/blog/year-of-access "https://www.strongdm.com/blog/year-of-access")

* Product

  Product

  The StrongDM Platform

  + - [Access](https://www.strongdm.com/platform/access-management "https://www.strongdm.com/platform/access-management")
    - [Analyze](https://www.strongdm.com/platform/access-analytics "https://www.strongdm.com/platform/access-analytics")
    - [Govern](https://www.strongdm.com/platform/access-governance "https://www.strongdm.com/platform/access-governance")

  [How It Works](https://www.strongdm.com/how-it-works "https://www.strongdm.com/how-it-works")

  + [Bring Your Own Stack](https://www.strongdm.com/connect "https://www.strongdm.com/connect")
    [Case Studies](https://www.strongdm.com/customer-stories "https://www.strongdm.com/customer-stories")
    [Pricing](https://www.strongdm.com/pricing "https://www.strongdm.com/pricing")
    [Reviews](https://www.strongdm.com/reviews "https://www.strongdm.com/reviews")

  [StrongDM Architecture Overview

  Discover how StrongDM enables seamless, secure access across your entire stack while protecting your enterprise with modern, future-proof security controls.](https://www.strongdm.com/whitepaper/technical-overview "https://www.strongdm.com/whitepaper/technical-overview")
* [Solutions](https://www.strongdm.com/solutions "https://www.strongdm.com/solutions")

  Solutions

  Access Management

  + - [Lifecycle Management](https://www.strongdm.com/solution/user-lifecycle-management "https://www.strongdm.com/solution/user-lifecycle-management")
    - [Just-in-Time Access](https://www.strongdm.com/solution/just-in-time-access "https://www.strongdm.com/solution/just-in-time-access")
    - [Privileged Credential Management](https://www.strongdm.com/solution/privileged-credential-management "https://www.strongdm.com/solution/privileged-credential-management")
    - [Permissions Management](https://www.strongdm.com/solution/permissions-management "https://www.strongdm.com/solution/permissions-management")
    - [Database Access Management](https://www.strongdm.com/solution/database-access-management "https://www.strongdm.com/solution/database-access-management")


  Session & Activity Control

  + - [Audit & Compliance](https://www.strongdm.com/solution/security-compliance "https://www.strongdm.com/solution/security-compliance")
    - [Privileged Session Management](https://www.strongdm.com/solution/privileged-session-management "https://www.strongdm.com/solution/privileged-session-management")

  Infrastructure

  + - [Zero Trust PAM](https://www.strongdm.com/solution/zero-trust-pam "https://www.strongdm.com/solution/zero-trust-pam")
    - [PAM for Kubernetes](https://www.strongdm.com/solution/pam-kubernetes "https://www.strongdm.com/solution/pam-kubernetes")
    - [PAM for Databases](https://www.strongdm.com/solution/pam-databases "https://www.strongdm.com/solution/pam-databases")
    - [PAM for Network Devices](https://www.strongdm.com/solution/pam-network-devices "https://www.strongdm.com/solution/pam-network-devices")
    - [PAM for Cloud](https://www.strongdm.com/solution/cloud-pam "https://www.strongdm.com/solution/cloud-pam")
    - [PAM for Servers](https://www.strongdm.com/solution/pam-servers "https://www.strongdm.com/solution/pam-servers")
    - [Vendor PAM](https://www.strongdm.com/solution/vendor-privileged-access-management "https://www.strongdm.com/solution/vendor-privileged-access-management")

  Policy-Based Action Control

  + - [Adaptive Policy-Based Access Management](https://www.strongdm.com/solution/adaptive-policy-based-access-management "https://www.strongdm.com/solution/adaptive-policy-based-access-management")
    - [Granular Access Controls](https://www.strongdm.com/solution/granular-access-controls "https://www.strongdm.com/solution/granular-access-controls")
    - [Context-Aware Access Policies](https://www.strongdm.com/solution/context-aware-access-policies "https://www.strongdm.com/solution/context-aware-access-policies")
    - [Policy-Based Action Control](https://www.strongdm.com/solution/policy-based-action-control "https://www.strongdm.com/solution/policy-based-action-control")
    - [Policy Enforcement Solution](https://www.strongdm.com/solution/policy-enforcement "https://www.strongdm.com/solution/policy-enforcement")

  By Role

  + - [IAM](https://www.strongdm.com/team/iam "https://www.strongdm.com/team/iam")
    - [Security](https://www.strongdm.com/team/security "https://www.strongdm.com/team/security")
    - [Developers](https://www.strongdm.com/team/developers "https://www.strongdm.com/team/developers")

  [How Zero Trust PAM Defines Modern Enterprise Security

  Legacy PAM solutions that focus on controlling access at the "front door" are no longer sufficient. The future of security lies in applying fine-grained permissions to control user actions on critical resources and continuously assessing the risk profile of those users.](https://www.strongdm.com/ebooks/ztpam-manifesto "https://www.strongdm.com/ebooks/ztpam-manifesto")
* [Docs](https://www.strongdm.com/docs "https://www.strongdm.com/docs")

  Docs

  [Product Documentation](https://www.strongdm.com/docs "https://www.strongdm.com/docs")

  + [User Guide](https://docs.strongdm.com/users/client "https://docs.strongdm.com/users/client")
    [Admin Guide](https://docs.strongdm.com/admin/ "https://docs.strongdm.com/admin/")
    [API](https://docs.strongdm.com/references/api "https://docs.strongdm.com/references/api")
* [Resources](https://www.strongdm.com/resources "https://www.strongdm.com/resources")

  Resources

  Explore

  + - [Blog](https://www.strongdm.com/blog "https://www.strongdm.com/blog")
    - [Policies](https://www.strongdm.com/policies "https://www.strongdm.com/policies")
    - [Glossary](https://www.strongdm.com/glossary "https://www.strongdm.com/glossary")
    - [Videos](https://www.strongdm.com/resources?type=video "https://www.strongdm.com/resources?type=video")
    - [Secure Access Maturity  
      Model Journey](https://www.strongdm.com/samm-journey "https://www.strongdm.com/samm-journey")

  Join Us

  + - [Events](https://www.strongdm.com/events "https://www.strongdm.com/events")
    - [Webinars](https://www.strongdm.com/webinars "https://www.strongdm.com/webinars")

  Solution Guides

  + - [AWS Well-Architected Framework](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-aws-well-architected-framework.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-aws-well-architected-framework.pdf")
    - [CISA Zero Trust Maturity Model](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-the-cisa-zero-trust-maturity-model.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-the-cisa-zero-trust-maturity-model.pdf")
    - [FedRAMP](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-fedramp.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-fedramp.pdf")
    - [Cyber Insurance](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-cyber-insurance.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-cyber-insurance.pdf")
    - [MITRE ATT&CK](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-mitre-att%26ck-for-containers.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-mitre-att%26ck-for-containers.pdf")
    - [Cloud Control Matrix (CCM) 4.0](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-ccm-4-0.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-ccm-4-0.pdf")
    - [NIST 800-53 Access Controls](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nist-800-53.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nist-800-53.pdf")

  + - [HIPAA Compliance](https://discover.strongdm.com/hubfs/ebooks/hipaa-compliance-solution-guide-by-strongdm.pdf "https://discover.strongdm.com/hubfs/ebooks/hipaa-compliance-solution-guide-by-strongdm.pdf")
    - [SOC 2 Compliance](https://discover.strongdm.com/hubfs/soc-2/how-strongdm-helps-with-soc2-compliance.pdf "https://discover.strongdm.com/hubfs/soc-2/how-strongdm-helps-with-soc2-compliance.pdf")
    - [NYDFS Compliance](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nydfs-cybersecurity-regulation.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nydfs-cybersecurity-regulation.pdf")
    - [NIS2 Compliance](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nis2-compliance.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-nis2-compliance.pdf")
    - [PSD2 & PSD3 Compliance](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-psd2-and-psd3-compliance.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-psd2-and-psd3-compliance.pdf")
    - [PCI DSS 4.0 Compliance](https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-pci-dss-4-0-compliance.pdf "https://discover.strongdm.com/hubfs/ebooks/how-strongdm-helps-with-pci-dss-4-0-compliance.pdf")
    - [ISO 27001 Compliance](https://discover.strongdm.com/hubfs/lp-assets/iso-27001-compliance-guide.pdf "https://discover.strongdm.com/hubfs/lp-assets/iso-27001-compliance-guide.pdf")

  Knowledge Guides

  + - [Zero Trust](https://www.strongdm.com/zero-trust "https://www.strongdm.com/zero-trust")
    - [PAM](https://www.strongdm.com/privileged-access-management "https://www.strongdm.com/privileged-access-management")
    - [RBAC](https://www.strongdm.com/rbac "https://www.strongdm.com/rbac")
    - [IAM](https://www.strongdm.com/iam "https://www.strongdm.com/iam")
    - [SASE](https://www.strongdm.com/sase "https://www.strongdm.com/sase")
    - [SAML](https://www.strongdm.com/saml "https://www.strongdm.com/saml")
    - [Authentication](https://www.strongdm.com/authentication "https://www.strongdm.com/authentication")

  + - [DAM](https://www.strongdm.com/dynamic-access-management-dam "https://www.strongdm.com/dynamic-access-management-dam")
    - [SAMM](https://www.strongdm.com/secure-access-maturity-model "https://www.strongdm.com/secure-access-maturity-model")
    - [SOC 2](https://www.strongdm.com/soc2/compliance "https://www.strongdm.com/soc2/compliance")
    - [ISO 27001](https://www.strongdm.com/iso-27001 "https://www.strongdm.com/iso-27001")
    - [HIPAA](https://www.strongdm.com/hipaa-compliance "https://www.strongdm.com/hipaa-compliance")
    - [PCI](https://www.strongdm.com/pci-compliance "https://www.strongdm.com/pci-compliance")
    - [Observability](https://www.strongdm.com/observability "https://www.strongdm.com/observability")
* Company

  Company

  [About Us](https://www.strongdm.com/about "https://www.strongdm.com/about")

  + [Contact Us](https://www.strongdm.com/contact "https://www.strongdm.com/contact")

[Login](https://app.strongdm.com/app/login "https://app.strongdm.com/app/login")

[Try it free](/signup "/signup")

{
"@context": "http://schema.org",
"@type": "BlogPosting",
"mainEntityOfPage":{
"@type":"WebPage",
"@id":"https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai"
},
"headline": "The StrongDM Software Factory: Building Software with AI",
"image": {
"@type": "ImageObject",
"url": "https://discover.strongdm.com/hubfs/Software%20Factory\_1560x877-1.png"
},
"datePublished": "February 19, 2026",
"dateModified": "February 19, 2026",
"author": {
"@type": "Person",
"name": "StrongDM Team",
"url": "https://www.strongdm.com/blog/author/strongdm-team",
"jobTitle": "Universal Privileged Access Authorization (UPAA)"
},
"publisher": {
"@type": "Organization",
"name": "StrongDM, Inc.",
"logo": {
"@type": "ImageObject",
"url": "https://www.strongdm.com/hubfs/brand/strongdm\_logo\_320x320.png"
},
"address": "228 Hamilton Avenue, 3rd Floor ",
"location": "Palo Alto, CA"
},
"description": "Inside the StrongDM Software Factory: a new approach to building software with AI using agent-driven execution, scenario-based validation, and digital twin systems\u2014where validation replaces code review."
}

{
"@context": "https://schema.org",
"@type": "BreadcrumbList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"name": "Blog",
"item": "https://www.strongdm.com/blog"
},
{
"@type": "ListItem",
"position": 2,
"name": "Security",
"item": "https://www.strongdm.com/blog/tag/security"
}
]
}

[Blog](/blog "/blog")
/
[Security](https://www.strongdm.com/blog/tag/security "https://www.strongdm.com/blog/tag/security")

The StrongDM Software Factory: Building Software with AI
========================================================

[See StrongDM in action →](https://www.strongdm.com/get-a-demo "https://www.strongdm.com/get-a-demo")

Written by

[StrongDM Team](https://www.strongdm.com/blog/author/strongdm-team "https://www.strongdm.com/blog/author/strongdm-team")

Universal Privileged Access Authorization (UPAA)

[StrongDM](https://www.strongdm.com "https://www.strongdm.com")

Last updated on:

February 19, 2026

Reading time:

1 minutes

Contents

Secure Access Made Simple

Built for Security. Loved by Devs.

* Free Trial — No Credit Card Needed
* Full Access to All Features
* Trusted by the Fortune 100, early startups, and everyone in between

[Free Trial](https://www.strongdm.com/signup "https://www.strongdm.com/signup")

Last summer, we launched the StrongDM AI Lab with a simple premise: how best to maximize building software with AI. This led us to some interesting discoveries on how to operate in this new world and the creation of what we call the Software Factory.

Humans define intent: what the system should do, the scenarios it needs to handle, the constraints that matter. After that, the agents take it from there. They generate code, validate it against real-world behavior, and iterate until it converges, without hand-tuning or human review.

The factory is powered by scenario-based validation, a Digital Twin Universe of systems like Okta and Slack, and agents that run end-to-end once the work is fully specified. It’s what happens when validation replaces code review.

The result is a system that gets better by iterating against reality. This system runs real scenarios, validates real behavior, and corrects itself without humans in the loop.

See it to believe it: [https://factory.strongdm.ai/](https://factory.strongdm.ai/ "https://factory.strongdm.ai/")

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Conversations**
-----------------

* [Post](https://www.linkedin.com/posts/emollick_a-genuinely-radical-approach-to-software-activity-7425896189767622656-EMLP?utm_source=share&utm_medium=member_desktop&rcm=ACoAABJUpYQB-VhCXxTE4DozgXS77zPR9Bgzl-I "https://www.linkedin.com/posts/emollick_a-genuinely-radical-approach-to-software-activity-7425896189767622656-EMLP?utm_source=share&utm_medium=member_desktop&rcm=ACoAABJUpYQB-VhCXxTE4DozgXS77zPR9Bgzl-I") by Co-Director of the Generative AI Lab at Wharton, [Professor Ethan Mollick](https://www.linkedin.com/in/emollick/ "https://www.linkedin.com/in/emollick/")
* [Post](https://x.com/garrytan/status/2020387162009797017?s=20 "https://x.com/garrytan/status/2020387162009797017?s=20") by President and CEO of Y Combinator, [Garry Tan](https://x.com/garrytan "https://x.com/garrytan")
* [Blog](https://simonwillison.net/2026/Feb/7/software-factory/ "https://simonwillison.net/2026/Feb/7/software-factory/") by AI Thought Leader [Simon Willison](https://www.linkedin.com/in/simonwillison/ "https://www.linkedin.com/in/simonwillison/")
* [Blog](https://ai-business-automation-digest.beehiiv.com/p/ai-automation-digest-002 "https://ai-business-automation-digest.beehiiv.com/p/ai-automation-digest-002") by AI Automation Digest

Next Steps
----------

StrongDM unifies access management across databases, servers, clusters, and more—for IT, security, and DevOps teams.

* Learn [how StrongDM works](https://www.strongdm.com/whitepaper/technical-overview "https://www.strongdm.com/whitepaper/technical-overview")
* Book a [personalized demo](https://www.strongdm.com/get-a-demo "https://www.strongdm.com/get-a-demo")
* Start your [free StrongDM trial](https://www.strongdm.com/signup "https://www.strongdm.com/signup")

### Share this:

* [Share The StrongDM Software Factory: Building Software with AI on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai&title=The+StrongDM+Software+Factory%3A+Building+Software+with+AI&summary=Inside+the+StrongDM+Software+Factory%3A+a+new+approach+to+building+software+with+AI+using+agent-driven+execution%2C+scenario-based+validation%2C+and+digital+twin+systems%E2%80%94where+validation+replaces+code+review. "Share The StrongDM Software Factory: Building Software with AI on LinkedIn")
* [Share The StrongDM Software Factory: Building Software with AI on Reddit](https://www.reddit.com/submit/?url=https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai&title=The%20StrongDM%20Software%20Factory:%20Building%20Software%20with%20AI&resubmit=true "Share on Reddit")
* [Share The StrongDM Software Factory: Building Software with AI on Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai&title=The+StrongDM+Software+Factory%3A+Building+Software+with+AI&picture=https://discover.strongdm.com/hubfs/Software%20Factory_1560x877-1.png&description=Inside%20the%20StrongDM%20Software%20Factory:%20a%20new%20approach%20to%20building%20software%20with%20AI%20using%20agent-driven%20execution,%20scenario-based%20validation,%20and%20digital%20twin%20systems—where%20validation%20replaces%20code%20review. "Share The StrongDM Software Factory: Building Software with AI on Facebook")
* [Share The StrongDM Software Factory: Building Software with AI on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai "Share The StrongDM Software Factory: Building Software with AI on HackerNews")

### Categories:

* [Security](https://www.strongdm.com/blog/tag/security "https://www.strongdm.com/blog/tag/security")
* [Access](https://www.strongdm.com/blog/tag/access "https://www.strongdm.com/blog/tag/access")
* [Privileged Access Management](https://www.strongdm.com/blog/tag/privileged-access-management "https://www.strongdm.com/blog/tag/privileged-access-management")

About the Author
----------------

[StrongDM Team](https://www.strongdm.com/blog/author/strongdm-team "https://www.strongdm.com/blog/author/strongdm-team"), **Universal Privileged Access Authorization (UPAA)**, the StrongDM team is building and delivering a Zero Trust Privileged Access Management (PAM), which delivers unparalleled precision in dynamic privileged action control for any type of infrastructure. The frustration-free access stops unsanctioned actions while ensuring continuous compliance.

💙 this post?

Then get all that StrongDM goodness, right in your inbox.

You May Also Like
-----------------

[When AI Tools Get Standing Access: Lessons from the Vercel Breach](/blog/when-ai-tools-get-standing-access-lessons-from-the-vercel-breach "/blog/when-ai-tools-get-standing-access-lessons-from-the-vercel-breach")

As AI agents take on actions once performed only by humans, traditional identity systems can’t provide clear delegation or accountability. StrongDM ID gives every agent a unique, verifiable identity linked to a human sponsor, ensuring organizations always know who authorized every action. In the next era of identity, authentication matters—but delegation defines trust.

[Identity Was Built for Humans. AI Agents Change the Rules.](/blog/identity-was-built-for-humans.-ai-agents-change-the-rules "/blog/identity-was-built-for-humans.-ai-agents-change-the-rules")

As AI agents take on actions once performed only by humans, traditional identity systems can’t provide clear delegation or accountability. StrongDM ID gives every agent a unique, verifiable identity linked to a human sponsor, ensuring organizations always know who authorized every action. In the next era of identity, authentication matters—but delegation defines trust.

[The End of “Verify Once, Trust Forever”](/blog/the-end-of-verify-once-trust-forever "/blog/the-end-of-verify-once-trust-forever")

The modern cloud is fast, dynamic, and complex. But legacy security tools can’t keep up. As containers and ephemeral resources constantly change, and access requests surge, security teams are left scrambling. Entitlements pile up, visibility fades, and audits become a nightmare.

[From Authentication to Authorization: The KPI Set Every Board Needs](/blog/from-authentication-to-authorization-the-kpi-set-every-board-needs "/blog/from-authentication-to-authorization-the-kpi-set-every-board-needs")

StrongDM debuts in Gartner’s Magic Quadrant for PAM, redefining privileged access with real-time, policy-based authorization for modern cloud environments.

[StrongDM Debuts in Gartner’s Magic Quadrant for Privileged Access Management](/blog/gartner-magic-quadrant-privileged-access-management "/blog/gartner-magic-quadrant-privileged-access-management")

StrongDM debuts in Gartner’s Magic Quadrant for PAM, redefining privileged access with real-time, policy-based authorization for modern cloud environments.

PRODUCT

* [Infrastructure Access Platform](https://www.strongdm.com/infrastructure-access-platform "https://www.strongdm.com/infrastructure-access-platform")
* [Solutions](https://www.strongdm.com/solutions "https://www.strongdm.com/solutions")
* [How It Works](https://www.strongdm.com/how-it-works "https://www.strongdm.com/how-it-works")
* [Bring Your Own Stack](https://www.strongdm.com/connect "https://www.strongdm.com/connect")
* [Pricing](https://www.strongdm.com/pricing "https://www.strongdm.com/pricing")
* [Customers](https://www.strongdm.com/customer-stories "https://www.strongdm.com/customer-stories")
* [Compare](https://www.strongdm.com/compare "https://www.strongdm.com/compare")

Docs

* [Docs Home](https://www.strongdm.com/docs/ "https://www.strongdm.com/docs/")
* [User Guide](https://docs.strongdm.com/users/client "https://docs.strongdm.com/users/client")
* [Admin Guide](https://www.strongdm.com/docs/admin-ui-guide/index "https://www.strongdm.com/docs/admin-ui-guide/index")
* [API](https://www.strongdm.com/docs/api "https://www.strongdm.com/docs/api")

Resources

* [Blog](https://www.strongdm.com/blog "https://www.strongdm.com/blog")
* [Articles](https://www.strongdm.com/resources?type=article "https://www.strongdm.com/resources?type=article")
* [Videos](https://www.strongdm.com/resources?type=video "https://www.strongdm.com/resources?type=video")
* [Webinars](https://www.strongdm.com/resources?type=webinar "https://www.strongdm.com/resources?type=webinar")
* [Customer Stories](https://www.strongdm.com/customer-stories "https://www.strongdm.com/customer-stories")

Company

* [About Us](https://www.strongdm.com/about "https://www.strongdm.com/about")
* [Careers](https://www.strongdm.com/careers "https://www.strongdm.com/careers")
* [Security](https://www.strongdm.com/security "https://www.strongdm.com/security")
* [Legal](https://www.strongdm.com/legal "https://www.strongdm.com/legal")
* [Press](https://www.strongdm.com/press-staging "https://www.strongdm.com/press-staging")

Get Started

* [Try It Free](/signup "/signup")
* [Contact Us](/contact "/contact")
* [Schedule a Demo](/get-a-demo "/get-a-demo")

© 2026 StrongDM

[Privacy Policy](https://www.strongdm.com/privacy "https://www.strongdm.com/privacy")[Terms of Use](https://www.strongdm.com/terms-of-use "https://www.strongdm.com/terms-of-use")





$(".blog-post\_\_body img").each(function() {
$(this).attr("loading", "lazy");
});
$(function(){
$('#cta-ebook-copy').clone().appendTo('#cta-ebook-copied');
});
$(function(){
const $navList = $('.blog-post--nav-list');
const $headings = $('.blog-post\_\_body h2');
$headings.each(function(index) {
const $heading = $(this);
const text = $heading.text().trim();
const id = text.toLowerCase().replace(/[^\w\s-]/g, '').replace(/\s+/g, '-');
$heading.attr('id', id);
const $li = $('<li></li>');
const $link = $('<a></a>').attr('href', '#' + id).text(text);
$li.append($link);
$navList.append($li);
});
$navList.find('li:first-child').addClass('is-active');
$('.blog-post--nav-list a').on('click', function(e) {
e.preventDefault();
const targetId = $(this).attr('href');
const $target = $(targetId);
if ($target.length) {
$('html, body').animate({
scrollTop: $target.offset().top - 50
}, 600);
}
});
$(window).on('scroll', function() {
const scrollMiddle = $(window).scrollTop() + $(window).height() / 2;
let currentId = '';
$headings.each(function() {
const $heading = $(this);
const top = $heading.offset().top;
if (scrollMiddle >= top) {
currentId = $heading.attr('id');
}
});
if (currentId) {
$navList.find('li').removeClass('is-active');
$navList.find(`a[href="#${currentId}"]`).parent().addClass('is-active');
}
});
});

var hsVars = hsVars || {}; hsVars['language'] = 'en';



$('.search-icon-container').click(function() {
$('.search-container').slideToggle(200);
$('.search-icon-container').dimToggle();
$('#main-content').dimToggle(0.3);
$('footer.footer').dimToggle(0.3);
});
$('.search-close').click(function() {
$('.search-container').slideToggle(200);
$('.search-icon-container').dimToggle();
$('#main-content').dimToggle();
$('footer.footer').dimToggle();
});
$.fn.dimToggle = function(n) {
if (this.css('opacity') < 1) {
this.css('opacity', 1);
} else if (n) {
this.css('opacity', n);
} else {
this.css('opacity', 0.5);
}
}
$(document).click(function(event) {
var $target = $(event.target);
if (!$target.closest('#search-container').length && !$target.hasClass('search-icon') && !$target.hasClass('search-icon-container') && $('.search-container').is(":visible")) {
$('.search-container').slideToggle(200);
$('.search-icon-container').dimToggle();
$('#main-content').dimToggle();
$('footer.footer').dimToggle();
}
});

window.mainTagSlug = "";

document.addEventListener("DOMContentLoaded", function() {
const mainTag = window.mainTagSlug;
document.querySelectorAll('li[data-slug]').forEach(el => {
if (el.dataset.slug === mainTag) {
el.classList.add('current');
}
});
});



var options = {
portalId: '21126185',
formId: '00151378-e8c7-43a3-8c02-bed2528a95bf',
formInstanceId: '8623',
pageId: '207196427028',
region: 'na1',
pageName: "The StrongDM Software Factory: Building Software with AI",
redirectUrl: "https:\/\/discover.strongdm.com\/blog-subscribe-thank-you",
css: '',
target: '#hs\_form\_target\_form\_141296240',
contentType: "blog-post",
formsBaseUrl: '/\_hcms/forms/',
formData: {
cssClass: 'hs-form stacked hs-custom-form'
}
};
options.getExtraMetaDataBeforeSubmit = function() {
var metadata = {};
if (hbspt.targetedContentMetadata) {
var count = hbspt.targetedContentMetadata.length;
var targetedContentData = [];
for (var i = 0; i < count; i++) {
var tc = hbspt.targetedContentMetadata[i];
if ( tc.length !== 3) {
continue;
}
targetedContentData.push({
definitionId: tc[0],
criterionId: tc[1],
smartTypeId: tc[2]
});
}
metadata["targetedContentMetadata"] = JSON.stringify(targetedContentData);
}
return metadata;
};
hbspt.forms.create(options);


var \_hsq = \_hsq || [];
\_hsq.push(["setContentType", "blog-post"]);
\_hsq.push(["setCanonicalUrl", "https:\/\/discover.strongdm.com\/blog\/the-strongdm-software-factory-building-software-with-ai"]);
\_hsq.push(["setPageId", "207196427028"]);
\_hsq.push(["setContentMetadata", {
"contentPageId": 207196427028,
"legacyPageId": "207196427028",
"contentFolderId": null,
"contentGroupId": 68271253872,
"abTestId": null,
"languageVariantId": 207196427028,
"languageCode": "en",
}]);



var hsVars = {
render\_id: "3934d148-d826-4365-aee5-e98a1d5758da",
ticks: 1777998367443,
page\_id: 207196427028,
content\_group\_id: 68271253872,
portal\_id: 21126185,
app\_hs\_base\_url: "https://app.hubspot.com",
cp\_hs\_base\_url: "https://cp.hubspot.com",
language: "en",
analytics\_page\_type: "blog-post",
scp\_content\_type: "",
analytics\_page\_id: "207196427028",
category\_id: 3,
folder\_id: 0,
is\_hubspot\_user: false
}


let ogUrl = document.querySelector('meta[property~=og\\:url]');
if(ogUrl !== null){
ogUrl.setAttribute("content", "https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai");
}
let ogImg = document.querySelector('meta[property~=og\\:image]');
if(ogImg !== null && ogImg.hasAttribute('content')){
ogImg.setAttribute("content", ogImg.content.replace('discover','www'));
let twitterImg = document.querySelector('meta[name~=twitter\\:image]');
if(twitterImg !== null && twitterImg.hasAttribute('content')){
twitterImg.setAttribute("content", ogImg.content);
}
}

;(function(p,l,o,w,i,n,g){if(!p[i]){p.GlobalSnowplowNamespace=p.GlobalSnowplowNamespace||[];
p.GlobalSnowplowNamespace.push(i);p[i]=function(){(p[i].q=p[i].q||[]).push(arguments)
};p[i].q=p[i].q||[];n=l.createElement(o);g=l.getElementsByTagName(o)[0];n.async=1;
n.src=w;g.parentNode.insertBefore(n,g)}}(window,document,"script","/js/sdmt.js","sdmt"));

function getDomain(fromUrl) {
var url = fromUrl
url = url.replace(/(https?:\/\/)?(www.)?/i, '');
url = url.split('.');
url = url.slice(url.length - 2).join('.');
if (url.indexOf('/') !== -1) {
return url.split('/')[0];
}
return url;
}
function getCollectorUrl(domain) {
var collectorPath = "/sdmt"
if(domain.toLowerCase().startsWith('localhost')) {
return domain + collectorPath
}
return "app." + domain + "/sdmt"
}
currentDomain = getDomain(window.location.origin)
collectorUrl = getCollectorUrl(currentDomain)
window.sdmt('newTracker', 'sdmt1', collectorUrl, {
appId: 'sdm\_web\_www\_browser',
platform: "web",
postPath: "/\_s/t",
discoverRootDomain: true,
cookieName: "sdmt",
forceSecureTracker: true,
cookieSecure: true,
contexts: {
webPage: true,
gaCookies: true
}
});
window.sdmt('enableActivityTracking', 15, 10);
window.sdmt('enableLinkClickTracking');
window.sdmt('enableFormTracking');
window.sdmt('trackPageView');


\_linkedin\_partner\_id = "116193";
window.\_linkedin\_data\_partner\_ids = window.\_linkedin\_data\_partner\_ids || [];
window.\_linkedin\_data\_partner\_ids.push(\_linkedin\_partner\_id);
(function(l) {
if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
window.lintrk.q=[]}
var s = document.getElementsByTagName("script")[0];
var b = document.createElement("script");
b.type = "text/javascript";b.async = true;
b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
s.parentNode.insertBefore(b, s);})(window.lintrk);




let wl = [
'www.linkedin.com',
'csrc.nist.gov',
'krebsonsecurity.com',
'techrobot.com',
'www.aicpa.org',
'youtu.be',
'www.upwork.com',
'www.gartner.com',
'www.forrester.com',
'www.whitehouse.gov',
'www.cybersecurity-insiders.com',
'www.datacenterknowledge.com',
'www.cisa.gov',
'www.nvlpubs.nist.gov',
'www.phoenixnap.com',
'www.mackeeper.com',
'www.thinkremote.com',
'www.scnsoft.com',
'www.securew2.com',
'www.veriff.com',
'www.bitsight.com',
'www.speedster-it.com',
'www.dataedo.com',
'www.lepide.com',
'www.lifars.com',
'www.inwebo.com',
'www.spanning.com',
'www.authomize.com',
'www.sangfor.com',
'bazaarexpert.com',
'recruitcrm.io',
'thesmsworks.co.uk',
'preply.com',
'zefr.com',
'www.g2.com',
'wordable.io',
'instasize.com',
'mobidev.biz',
'measuremindsgroup.com',
'thrivemyway.com',
'writersperhour.com',
'writesonic.com',
'technologyadvice.com',
'shift4shop.com',
'pollthepeople.app',
'spdload.com',
'betternurse.org',
'getvoip.com',
'easydmarc.com',
'project-management.com',
'datamation.com',
'snacknation.com',
'easydmarc.com',
'mobilunity.com',
'blog.internxt.com',
'whatismyipaddress.com',
'www.designrush.com',
'phdkingdom.com',
'academicbrits.com',
'blog.empuls.io',
'www.zavvy.io',
'www.ninjaone.com',
'www.cloudtalk.io',
'xobin.com',
'www.goodelearning.com',
'www.adaface.com',
'recruiterflow.com/blog/',
'acowebs.com',
'www.hostinger.com',
'middleware.io',
'asperbrothers.com',
'www.studocu.com',
'bankinggeek.com',
'www.airwallex.com',
'www.dialpad.com',
'www.pandadoc.com',
'blog.scalefusion.com',
'www.ridge.co',
'www.pelco.com',
'scalefusion.com',
'trueconf.com',
'mediaonemarketing.com.sg',
'themoneymaniac.com',
'www.vz.ae',
'contractbook.com',
'www.openpath.com',
'www.avigilon.com',
'www.valimates.com',
'myhours.com',
'www.edapp.com',
'www.chamberofcommerce.org',
'www.aura.com',
'macpaw.com',
'www.bigcommerce.com',
'powerdmarc.com',
'cybernews.com',
'www.nakivo.com',
'youngandtheinvested.com',
'www.cloudeagle.ai',
'airbyte.com',
'www.accelo.com',
'www.superannotate.com',
'www.nextiva.com',
'jooble.org',
'www.currentware.com',
'birdeye.com',
'www.zonkafeedback.com',
'earthweb.com',
'www.hostingadvice.com',
'spp.co',
'www.atera.com',
'devrev.ai',
'droppe.com',
'www.uniqode.com',
'www.getastra.com',
'www.identityguard.com',
'www.centime.com',
'www.tealhq.com',
'visme.co',
'www.wiz.io',
'www.springboard.com',
'aloa.co',
'spacelift.io',
'dealhub.io',
'www.neo.space',
'www.stationx.net',
'whatfix.com',
'www.namehero.com',
'www.printful.com',
'www.atlantic.net',
'www.teramind.co',
'www.myrasecurity.com',
'cleanmymac.com',
'www.ringcentral.com',
'www.wiz.io',
'www.surveysensum.com',
'thectoclub.com',
'pentest-tools.com',
'www.adobe.com',
'www.auslogics.com',
'appliger.com',
'www.geteppo.com',
'diceus.com',
'blog.coupler.io',
'www.breachlock.com',
'www.pelco.com',
'www.superside.com',
'www.nextiva.com',
'arc.dev',
'clockwise.software',
'www.inmotionhosting.com',
'www.thepaystubs.com',
'www.swarmia.com',
'learn.g2.com',
'remote.com',
'www.sage.com',
'360learning.com',
'remotepeople.com',
'www.getastra.com',
'www.artisan.co',
'www.designrush.com',
'www.cloudways.com',
'donorbox.org',
'alcor-bpo.com',
];
$(document).ready(function() {
$('.blog-post\_\_body a').each(function() {
var href = $(this).attr('href');
if(href.startsWith("https://discover.strongdm.com/")){
$(this).attr('href', href.replace('//discover', '//www'));
$(this).removeAttr('rel');
}else if(href.startsWith("https://www.strongdm.com/") || href.startsWith("/")){
$(this).removeAttr('rel');
}else if (href.startsWith("https://calendly.com/")) {
$(this).attr('href', '/get-a-demo');
}else if (!(href.startsWith("/") || href.startsWith("https://www.strongdm.com/"))) {
$(this).attr('target','\_blank');
let linkDomain = (new URL(href));
if(jQuery.inArray(linkDomain.hostname, wl) > -1){
$(this).attr('rel', 'noreferrer noopener');
}else{
$(this).attr('rel', 'noreferrer noopener nofollow');
}
}
});
});

function loadChat(){
let chatEl = document.createElement("script");
chatEl.src = "https://chat-application.com/embed/index.php?tracker\_id=64797305";
chatEl.defer = true;
chatEl.type = "text/javascript";
document.getElementsByTagName("head")[0].appendChild(chatEl);
}
function delay(milliseconds){
return new Promise(resolve => {
setTimeout(resolve, milliseconds);
});
}
async function init(){
await delay(5000);
loadChat();
}
if (screen.width > 480) {
init();
}
(function(w, d, c) {w['techtargetic'] = w['techtargetic'] || {};w['techtargetic'].client = c;var s = d.createElement("script");s.type = "text/javascript";s.defer = true;s.crossorigin = "anonymous";var rd = new Date();rd=rd.getFullYear()+''+rd.getMonth()+rd.getDate();s.src = "https://trk.techtarget.com/tracking.js";var n = d.getElementsByTagName("script")[0];n.parentNode.insertBefore(s, n);})(window, document, '17831169');

(function(c,l,a,r,i,t,y){
c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "4gogyl4ufo");

window.addEventListener("message", function(event) {
if(event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormSubmit') {
let thisFormData = {
'hs\_form\_id': event.data.id,
'page\_title': document.title
}
if (event.data.id === '00151378-e8c7-43a3-8c02-bed2528a95bf') {
thisFormData.marketing\_asset = "Newsletter"
}
gtag('event', 'form\_submitted', thisFormData);
}
});















function loadChat(){
let chatEl = document.createElement("script");
chatEl.src = "https://chat-application.com/embed/index.php?tracker\_id=64797305";
chatEl.defer = true;
chatEl.type = "text/javascript";
document.getElementsByTagName("head")[0].appendChild(chatEl);
}
function delay(milliseconds){
return new Promise(resolve => {
setTimeout(resolve, milliseconds);
});
}
async function init(){
await delay(5000);
loadChat();
}
if (screen.width > 480) {
init();
}
(function(w, d, c) {w['techtargetic'] = w['techtargetic'] || {};w['techtargetic'].client = c;var s = d.createElement("script");s.type = "text/javascript";s.defer = true;s.crossorigin = "anonymous";var rd = new Date();rd=rd.getFullYear()+''+rd.getMonth()+rd.getDate();s.src = "https://trk.techtarget.com/tracking.js";var n = d.getElementsByTagName("script")[0];n.parentNode.insertBefore(s, n);})(window, document, '17831169');

(function(c,l,a,r,i,t,y){
c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "4gogyl4ufo");

window.addEventListener("message", function(event) {
if(event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormSubmitted') {
window.dataLayer.push({
'event': 'hubspot-form-success',
'hs-form-guid': event.data.id
});
}
});
