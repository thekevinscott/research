# Stevens — Trustworthy AI Agents: Deterministic Replay

Source: https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-8/

---

Trustworthy AI Agents: Deterministic ReplayTrustworthy AI Agents: Deterministic Replay@-webkit-keyframes la-spin{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}@keyframes la-spin{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}:root{--swiper-theme-color:#007aff}:root{--swiper-navigation-size:44px}[data-aos^=fade][data-aos^=fade]{opacity:0}[data-aos=fade-up]{transform:translate3d(0,15px,0)}:root{--bs-blue:#0d6efd;--bs-indigo:#6610f2;--bs-purple:#6f42c1;--bs-pink:#d63384;--bs-red:#dc3545;--bs-orange:#fd7e14;--bs-yellow:#ffc107;--bs-green:#198754;--bs-teal:#20c997;--bs-cyan:#0dcaf0;--bs-black:#000000;--bs-white:#ffffff;--bs-gray:#6c757d;--bs-gray-dark:#343a40;--bs-gray-100:#f8f9fa;--bs-gray-200:#e9ecef;--bs-gray-300:#dee2e6;--bs-gray-400:#ced4da;--bs-gray-500:#adb5bd;--bs-gray-600:#6c757d;--bs-gray-700:#495057;--bs-gray-800:#343a40;--bs-gray-900:#212529;--bs-primary:#0d6efd;--bs-secondary:#6c757d;--bs-success:#198754;--bs-info:#0dcaf0;--bs-warning:#ffc107;--bs-danger:#dc3545;--bs-light:#FAFAFA;--bs-dark:#212529;--bs-primary-rgb:13, 110, 253;--bs-secondary-rgb:108, 117, 125;--bs-success-rgb:25, 135, 84;--bs-info-rgb:13, 202, 240;--bs-warning-rgb:255, 193, 7;--bs-danger-rgb:220, 53, 69;--bs-light-rgb:250, 250, 250;--bs-dark-rgb:33, 37, 41;--bs-primary-text-emphasis:#052c65;--bs-secondary-text-emphasis:#2b2f32;--bs-success-text-emphasis:#0a3622;--bs-info-text-emphasis:#055160;--bs-warning-text-emphasis:#664d03;--bs-danger-text-emphasis:#58151c;--bs-light-text-emphasis:#495057;--bs-dark-text-emphasis:#495057;--bs-primary-bg-subtle:#cfe2ff;--bs-secondary-bg-subtle:#e2e3e5;--bs-success-bg-subtle:#d1e7dd;--bs-info-bg-subtle:#cff4fc;--bs-warning-bg-subtle:#fff3cd;--bs-danger-bg-subtle:#f8d7da;--bs-light-bg-subtle:#fcfcfd;--bs-dark-bg-subtle:#ced4da;--bs-primary-border-subtle:#9ec5fe;--bs-secondary-border-subtle:#c4c8cb;--bs-success-border-subtle:#a3cfbb;--bs-info-border-subtle:#9eeaf9;--bs-warning-border-subtle:#ffe69c;--bs-danger-border-subtle:#f1aeb5;--bs-light-border-subtle:#e9ecef;--bs-dark-border-subtle:#adb5bd;--bs-white-rgb:255, 255, 255;--bs-black-rgb:0, 0, 0;--bs-font-sans-serif:system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";--bs-font-monospace:SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;--bs-gradient:linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));--bs-body-font-family:var(--bs-font-sans-serif);--bs-body-font-size:1rem;--bs-body-font-weight:400;--bs-body-line-height:1.5;--bs-body-color:#212529;--bs-body-color-rgb:33, 37, 41;--bs-body-bg:#ffffff;--bs-body-bg-rgb:255, 255, 255;--bs-emphasis-color:#000000;--bs-emphasis-color-rgb:0, 0, 0;--bs-secondary-color:rgba(33, 37, 41, 0.75);--bs-secondary-color-rgb:33, 37, 41;--bs-secondary-bg:#e9ecef;--bs-secondary-bg-rgb:233, 236, 239;--bs-tertiary-color:rgba(33, 37, 41, 0.5);--bs-tertiary-color-rgb:33, 37, 41;--bs-tertiary-bg:#f8f9fa;--bs-tertiary-bg-rgb:248, 249, 250;--bs-heading-color:inherit;--bs-link-color:#0d6efd;--bs-link-color-rgb:13, 110, 253;--bs-link-decoration:underline;--bs-link-hover-color:#0a58ca;--bs-link-hover-color-rgb:10, 88, 202;--bs-code-color:#d63384;--bs-highlight-color:#212529;--bs-highlight-bg:#fff3cd;--bs-border-width:1px;--bs-border-style:solid;--bs-border-color:#e4e4e4;--bs-border-color-translucent:rgba(0, 0, 0, 0.175);--bs-border-radius:0.375rem;--bs-border-radius-sm:0.25rem;--bs-border-radius-lg:0.5rem;--bs-border-radius-xl:1rem;--bs-border-radius-xxl:2rem;--bs-border-radius-2xl:var(--bs-border-radius-xxl);--bs-border-radius-pill:50rem;--bs-box-shadow:0 0.5rem 1rem rgba(0, 0, 0, 0.15);--bs-box-shadow-sm:0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);--bs-box-shadow-lg:0 1rem 3rem rgba(0, 0, 0, 0.175);--bs-box-shadow-inset:inset 0 1px 2px rgba(0, 0, 0, 0.075);--bs-focus-ring-width:0.25rem;--bs-focus-ring-opacity:0.25;--bs-focus-ring-color:rgba(13, 110, 253, 0.25);--bs-form-valid-color:#198754;--bs-form-valid-border-color:#198754;--bs-form-invalid-color:#dc3545;--bs-form-invalid-border-color:#dc3545}\*,::before,::after{box-sizing:border-box}@media(prefers-reduced-motion:no-preference){:root{scroll-behavior:smooth}}body{margin:0;font-family:var(--bs-body-font-family);font-size:var(--bs-body-font-size);font-weight:var(--bs-body-font-weight);line-height:var(--bs-body-line-height);color:var(--bs-body-color);text-align:var(--bs-body-text-align);background-color:var(--bs-body-bg);text-size-adjust:100%}h5,h2{margin-top:0;margin-bottom:.5rem;font-weight:500;line-height:1.2;color:var(--bs-heading-color)}h2{font-size:calc(1.325rem + .9vw)}@media(min-width:1200px){h2{font-size:2rem}}h5{font-size:1.25rem}p{margin-top:0;margin-bottom:1rem}ul{padding-left:2rem}ul{margin-top:0;margin-bottom:1rem}ul ul{margin-bottom:0}.small{font-size:.875em}a{color:rgba(var(--bs-link-color-rgb),var(--bs-link-opacity,1));text-decoration:underline}img,svg{vertical-align:middle}button{border-radius:0}button{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button{text-transform:none}button,[type=button]{appearance:button}::-webkit-datetime-edit-fields-wrapper,::-webkit-datetime-edit-text,::-webkit-datetime-edit-minute,::-webkit-datetime-edit-hour-field,::-webkit-datetime-edit-day-field,::-webkit-datetime-edit-month-field,::-webkit-datetime-edit-year-field{padding:0}::-webkit-inner-spin-button{height:auto}::-webkit-search-decoration{appearance:none}::-webkit-color-swatch-wrapper{padding:0}::file-selector-button{font:inherit;appearance:button}.container,.container-xxl{--bs-gutter-x:1.5rem;--bs-gutter-y:0;width:100%;padding-right:calc(var(--bs-gutter-x) \* .5);padding-left:calc(var(--bs-gutter-x) \* .5);margin-right:auto;margin-left:auto}@media(min-width:576px){.container{max-width:540px}}@media(min-width:768px){.container{max-width:720px}}@media(min-width:992px){.container{max-width:960px}}@media(min-width:1200px){.container{max-width:1140px}}:root{--bs-breakpoint-xs:0;--bs-breakpoint-sm:576px;--bs-breakpoint-md:768px;--bs-breakpoint-lg:992px;--bs-breakpoint-xl:1200px;--bs-breakpoint-xxl:1400px}.row{--bs-gutter-x:1.5rem;--bs-gutter-y:0;display:flex;flex-wrap:wrap;margin-top:calc(-1 \* var(--bs-gutter-y));margin-right:calc(-.5 \* var(--bs-gutter-x));margin-left:calc(-.5 \* var(--bs-gutter-x))}.row>\*{flex-shrink:0;width:100%;max-width:100%;padding-right:calc(var(--bs-gutter-x) \* .5);padding-left:calc(var(--bs-gutter-x) \* .5);margin-top:var(--bs-gutter-y)}.col-12{flex:none;width:100%}.gx-4{--bs-gutter-x:1.5rem}.gy-5{--bs-gutter-y:3rem}@media(min-width:768px){.col-md-6{flex:none;width:50%}}@media(min-width:992px){.col-lg-3{flex:none;width:25%}.col-lg-12{flex:none;width:100%}}.btn{--bs-btn-padding-x:0.75rem;--bs-btn-padding-y:0.375rem;--bs-btn-font-family: ;--bs-btn-font-size:1rem;--bs-btn-font-weight:400;--bs-btn-line-height:1.5;--bs-btn-color:var(--bs-body-color);--bs-btn-bg:transparent;--bs-btn-border-width:var(--bs-border-width);--bs-btn-border-color:transparent;--bs-btn-border-radius:var(--bs-border-radius);--bs-btn-hover-border-color:transparent;--bs-btn-box-shadow:inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 1px rgba(0, 0, 0, 0.075);--bs-btn-disabled-opacity:0.65;--bs-btn-focus-box-shadow:0 0 0 0.25rem rgba(var(--bs-btn-focus-shadow-rgb), .5);display:inline-block;padding:var(--bs-btn-padding-y)var(--bs-btn-padding-x);font-family:var(--bs-btn-font-family);font-size:var(--bs-btn-font-size);font-weight:var(--bs-btn-font-weight);line-height:var(--bs-btn-line-height);color:var(--bs-btn-color);text-align:center;text-decoration:none;vertical-align:middle;border:var(--bs-btn-border-width)solid var(--bs-btn-border-color);border-radius:var(--bs-btn-border-radius);background-color:var(--bs-btn-bg)}.btn-primary{--bs-btn-color:#ffffff;--bs-btn-bg:#0d6efd;--bs-btn-border-color:#0d6efd;--bs-btn-hover-color:#ffffff;--bs-btn-hover-bg:#0b5ed7;--bs-btn-hover-border-color:#0a58ca;--bs-btn-focus-shadow-rgb:49, 132, 253;--bs-btn-active-color:#ffffff;--bs-btn-active-bg:#0a58ca;--bs-btn-active-border-color:#0a53be;--bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);--bs-btn-disabled-color:#ffffff;--bs-btn-disabled-bg:#0d6efd;--bs-btn-disabled-border-color:#0d6efd}.collapse:not(.show){display:none}.dropdown{position:relative}.dropdown-toggle{white-space:nowrap}.dropdown-toggle::after{display:inline-block;margin-left:.255em;vertical-align:.255em;content:"";border-width:.3em .3em 0;border-top-style:solid;border-top-color:initial;border-right-style:solid;border-right-color:transparent;border-bottom-style:initial;border-bottom-color:initial;border-left-style:solid;border-left-color:transparent}.dropdown-menu{--bs-dropdown-zindex:1000;--bs-dropdown-min-width:10rem;--bs-dropdown-padding-x:0;--bs-dropdown-padding-y:0.5rem;--bs-dropdown-spacer:0.125rem;--bs-dropdown-font-size:1rem;--bs-dropdown-color:var(--bs-body-color);--bs-dropdown-bg:var(--bs-body-bg);--bs-dropdown-border-color:var(--bs-border-color-translucent);--bs-dropdown-border-radius:var(--bs-border-radius);--bs-dropdown-border-width:var(--bs-border-width);--bs-dropdown-inner-border-radius:calc(var(--bs-border-radius) - var(--bs-border-width));--bs-dropdown-divider-bg:var(--bs-border-color-translucent);--bs-dropdown-divider-margin-y:0.5rem;--bs-dropdown-box-shadow:var(--bs-box-shadow);--bs-dropdown-link-color:var(--bs-body-color);--bs-dropdown-link-hover-color:var(--bs-body-color);--bs-dropdown-link-hover-bg:var(--bs-tertiary-bg);--bs-dropdown-link-active-color:#ffffff;--bs-dropdown-link-active-bg:#0d6efd;--bs-dropdown-link-disabled-color:var(--bs-tertiary-color);--bs-dropdown-item-padding-x:1rem;--bs-dropdown-item-padding-y:0.25rem;--bs-dropdown-header-color:#6c757d;--bs-dropdown-header-padding-x:1rem;--bs-dropdown-header-padding-y:0.5rem;position:absolute;z-index:var(--bs-dropdown-zindex);display:none;min-width:var(--bs-dropdown-min-width);padding:var(--bs-dropdown-padding-y)var(--bs-dropdown-padding-x);margin:0;font-size:var(--bs-dropdown-font-size);color:var(--bs-dropdown-color);text-align:left;list-style:none;background-color:var(--bs-dropdown-bg);background-clip:padding-box;border:var(--bs-dropdown-border-width)solid var(--bs-dropdown-border-color);border-radius:var(--bs-dropdown-border-radius)}.dropdown-item{display:block;width:100%;padding:var(--bs-dropdown-item-padding-y)var(--bs-dropdown-item-padding-x);clear:both;font-weight:400;color:var(--bs-dropdown-link-color);text-align:inherit;text-decoration:none;white-space:nowrap;background-color:initial;border:0;border-radius:var(--bs-dropdown-item-border-radius,0)}.dropdown-item.active{color:var(--bs-dropdown-link-active-color);text-decoration:none;background-color:var(--bs-dropdown-link-active-bg)}.nav-link{display:block;padding:var(--bs-nav-link-padding-y)var(--bs-nav-link-padding-x);font-size:var(--bs-nav-link-font-size);font-weight:var(--bs-nav-link-font-weight);color:var(--bs-nav-link-color);text-decoration:none;background:0 0;border:0}.navbar{--bs-navbar-padding-x:0;--bs-navbar-padding-y:0.5rem;--bs-navbar-color:rgba(var(--bs-emphasis-color-rgb), 0.65);--bs-navbar-hover-color:rgba(var(--bs-emphasis-color-rgb), 0.8);--bs-navbar-disabled-color:rgba(var(--bs-emphasis-color-rgb), 0.3);--bs-navbar-active-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-brand-padding-y:0.3125rem;--bs-navbar-brand-margin-end:1rem;--bs-navbar-brand-font-size:1.25rem;--bs-navbar-brand-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-brand-hover-color:rgba(var(--bs-emphasis-color-rgb), 1);--bs-navbar-nav-link-padding-x:0.5rem;--bs-navbar-toggler-padding-y:0.25rem;--bs-navbar-toggler-padding-x:0.75rem;--bs-navbar-toggler-font-size:1.25rem;--bs-navbar-toggler-icon-bg:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%2833, 37, 41, 0.75%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");--bs-navbar-toggler-border-color:rgba(var(--bs-emphasis-color-rgb), 0.15);--bs-navbar-toggler-border-radius:var(--bs-border-radius);--bs-navbar-toggler-focus-width:0.25rem;position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:var(--bs-navbar-padding-y)var(--bs-navbar-padding-x)}.navbar-brand{padding-top:var(--bs-navbar-brand-padding-y);padding-bottom:var(--bs-navbar-brand-padding-y);margin-right:var(--bs-navbar-brand-margin-end);font-size:var(--bs-navbar-brand-font-size);color:var(--bs-navbar-brand-color);text-decoration:none;white-space:nowrap}.navbar-nav{--bs-nav-link-padding-x:0;--bs-nav-link-padding-y:0.5rem;--bs-nav-link-font-weight: ;--bs-nav-link-color:var(--bs-navbar-color);--bs-nav-link-hover-color:var(--bs-navbar-hover-color);--bs-nav-link-disabled-color:var(--bs-navbar-disabled-color);display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .dropdown-menu{position:static}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:var(--bs-navbar-toggler-padding-y)var(--bs-navbar-toggler-padding-x);font-size:var(--bs-navbar-toggler-font-size);line-height:1;color:var(--bs-navbar-color);background-color:initial;border:var(--bs-border-width)solid var(--bs-navbar-toggler-border-color);border-radius:var(--bs-navbar-toggler-border-radius)}@media(min-width:992px){.navbar-expand-lg{flex-wrap:nowrap;justify-content:flex-start}.navbar-expand-lg .navbar-nav{flex-direction:row}.navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-lg .navbar-nav .nav-link{padding-right:var(--bs-navbar-nav-link-padding-x);padding-left:var(--bs-navbar-nav-link-padding-x)}.navbar-expand-lg .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-lg .navbar-toggler{display:none}}.card{--bs-card-spacer-y:1rem;--bs-card-spacer-x:1rem;--bs-card-title-spacer-y:0.5rem;--bs-card-title-color: ;--bs-card-subtitle-color: ;--bs-card-border-width:var(--bs-border-width);--bs-card-border-color:var(--bs-border-color-translucent);--bs-card-border-radius:var(--bs-border-radius);--bs-card-box-shadow: ;--bs-card-inner-border-radius:calc(var(--bs-border-radius) - (var(--bs-border-width)));--bs-card-cap-padding-y:0.5rem;--bs-card-cap-padding-x:1rem;--bs-card-cap-bg:rgba(var(--bs-body-color-rgb), 0.03);--bs-card-cap-color: ;--bs-card-height: ;--bs-card-color: ;--bs-card-bg:var(--bs-body-bg);--bs-card-img-overlay-padding:1rem;--bs-card-group-margin:0.75rem;position:relative;display:flex;flex-direction:column;min-width:0;height:var(--bs-card-height);color:var(--bs-body-color);overflow-wrap:break-word;background-color:var(--bs-card-bg);background-clip:border-box;border:var(--bs-card-border-width)solid var(--bs-card-border-color);border-radius:var(--bs-card-border-radius)}.card-body{flex:auto;padding:var(--bs-card-spacer-y)var(--bs-card-spacer-x);color:var(--bs-card-color)}.card-title{margin-bottom:var(--bs-card-title-spacer-y);color:var(--bs-card-title-color)}.card-text:last-child{margin-bottom:0}.d-flex{display:flex!important}.position-relative{position:relative!important}.h-100{height:100%!important}.flex-fill{flex:auto!important}.flex-column{flex-direction:column!important}.justify-content-center{justify-content:center!important}.justify-content-between{justify-content:space-between!important}.align-items-center{align-items:center!important}.mx-auto{margin-right:auto!important;margin-left:auto!important}.mb-0{margin-bottom:0!important}.mb-2{margin-bottom:.5rem!important}.mb-3{margin-bottom:1rem!important}.p-0{padding:0!important}.p-3{padding:1rem!important}.pb-0{padding-bottom:0!important}.pb-5{padding-bottom:3rem!important}.text-start{text-align:left!important}.text-center{text-align:center!important}.text-uppercase{text-transform:uppercase!important}.text-break{overflow-wrap:break-word!important;word-break:break-word!important}.preloader{position:fixed;inset:0;background-color:#fff;z-index:9999;display:flex;align-items:center;justify-content:center}.img{max-width:100%;height:auto}h2,h5{color:#222;font-weight:600;line-height:1.4}a{color:#888;text-decoration:none}ul,li{padding:0;margin:0;list-style-position:inside}h5{line-height:calc(2ex + 4px);margin-bottom:.65em}h2{line-height:calc(2ex + 4px);margin-bottom:.65em}@media(max-width:991px){h2:not(h4,.h4,h5,.h5,h6,.h6){margin-bottom:.55em}}.btn{padding:.875rem 1.5rem;font-size:.875rem;font-weight:500;border-radius:.375rem;position:relative;z-index:1;overflow:hidden;border:0}.btn::after{position:absolute;content:"";height:0;width:100%;left:0;top:0;background-color:rgba(0,0,0,.1);z-index:-1;border-radius:.375rem}.btn.btn-primary{border:0;background-color:#000!important}body{color:#888;background-color:#fff;font-family:Robot,sans-serif;font-weight:400;font-size:.9rem;line-height:1.7}:focus{outline:0}.preloader img{animation:.5s linear 0s infinite normal none running la-spin}img{max-width:100%;height:auto;display:inline-block}@media(min-width:992px){.container{max-width:1060px}}@media(min-width:1200px){.container{max-width:1260px}}.container-xxl{max-width:1440px;width:100%;padding-right:.9rem;padding-left:.9rem;margin-right:auto;margin-left:auto}@media(max-width:1466px){.container-xxl{max-width:1260px}}.section{padding:6.25rem 0}.section-title{margin-bottom:3.12rem}.section-title .title{text-transform:capitalize;margin-bottom:2.5rem;position:relative;line-height:1.3}.section-title .title::after{position:absolute;content:"";height:5px;width:4.3rem;border-radius:1.8rem;left:0;bottom:-1.25rem;background-color:#000}@media(max-width:767px){.section-title .title{font-size:2rem}}.section-title.text-center .title::after{left:50%;transform:translateX(-50%)}.header-height-fix{height:7.3rem}@media(max-width:991px){.header-height-fix{height:6.625rem}}@media(max-width:767px){.header-height-fix{height:5.25rem}}header{position:fixed;width:100%;top:0;left:0;z-index:99999;background-color:#fff;padding:1.8rem 0}@media(max-width:767px){header{padding:1.25rem 0}}@media(max-width:767px){header .navbar-brand img{height:1.8rem;width:auto}}@media(max-width:400px){header .navbar-brand img{height:1.5rem}}header .navbar-light .navbar-toggler{padding:0;color:#222;border:0;box-shadow:none}header .navbar-light .navbar-toggler .show{display:none}header .navbar-light .navbar-toggler .hide{display:block}@media(max-width:767px){header .navbar-light .navbar-toggler{font-size:2rem}}header .nav-item .nav-link{font-weight:500;font-size:1rem;color:#222!important;padding:.9rem 1.06rem!important}@media(max-width:1200px){header .nav-item .nav-link{font-size:.9rem;padding:.9rem .625rem!important}}header .nav-item.active .nav-link{color:#000!important}header .nav-item.dropdown .nav-link::after{display:inline-block;vertical-align:.255em;content:"";height:.56rem;width:.56rem;border-width:0 2px 2px 0;border-right-style:solid;border-bottom-style:solid;border-image:initial;border-left-style:initial;border-top-style:initial;border-color:inherit;border-radius:2px;transform:rotate(45deg)}header .dropdown-menu{padding:0 .625rem;border-radius:.375rem;background-color:rgba(0,0,0,5%);border:1px solid rgba(0,0,0,5%)}header .dropdown-menu li:first-child{margin-top:.75rem}header .dropdown-menu li:last-child{margin-bottom:.75rem}header .dropdown-menu .dropdown-item{padding:.5rem .9rem;font-size:.875rem;font-weight:500;color:#222;border-radius:.375rem}header .dropdown-menu .dropdown-item.active{color:#000;background-color:initial}@media(min-width:991px){header .dropdown-menu{display:block;visibility:hidden;width:13.75rem;transform:translate(-50%,-6px);z-index:1;border:0;background-color:initial;left:50%!important;margin-top:0!important}header .dropdown-menu::after{position:absolute;content:"";height:0;width:100%;top:0;left:0;background-color:#fff;z-index:-1;border-radius:.375rem;border:1px solid rgba(0,0,0,.3);box-shadow:rgba(0,0,0,.1)0 .9rem 1.56rem}header .dropdown-menu li{transform:translateY(1.25rem);opacity:0}}@media(max-width:991px){header .navbar-nav{max-width:18.75rem;max-height:25rem;overflow-y:auto;text-align:center;padding-top:1.8rem}header .navbar-right{text-align:center;margin-top:5px;padding-bottom:.625rem}header .dropdown-menu{padding:1px .9rem;text-align:center;height:initial!important}header .nav-item .nav-link{padding:.31rem 1.25rem!important}}.page-header{position:relative}.card .card-img-top{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;object-position:center;display:block}.badge{background-color:var(--primary-color);color:var(--white);padding:.4em .65em;font-weight:600;font-size:.8rem}.badge:hover{background-color:var(--text-color);color:var(--white)}.badge-tag{background-color:#f0f0f0;color:var(--text-color-light);padding:.4em .65em;font-weight:500;font-size:.8rem;border-radius:.25rem}.badge-tag:hover{background-color:var(--primary-color);color:var(--white)}window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(e){plausible.o=e||{}},plausible.init()(function(){"use strict";window.addEventListener("load",function(){document.querySelector(".preloader").style.display="none"})})()

* [Home](/ "/")
* [Capability](# "#")
  + [Cloud](/cloud "/cloud")
  + [Data & AI](/data "/data")
  + [Security](/security "/security")
* [Solutions](# "#")
  + [Accelerate](/accelerate/ "/accelerate/")
  + [Catalyst](/catalyst/ "/catalyst/")
  + [Enclave](/enclave/ "/enclave/")
  + [Sentinel](/sentinel/ "/sentinel/")
* [Services](# "#")
  + [Professional Services](/professional-services/ "/professional-services/")
  + [Managed Services](/managed-services/ "/managed-services/")
* [Insights](# "#")
  + [Blog](/blog/ "/blog/")
  + [White Papers](/white-papers/ "/white-papers/")
  + [Podcasts](/podcasts/ "/podcasts/")
* [About Us](# "#")
  + [Our History](/about/ "/about/")
  + [Our Customers](/our-customers/ "/our-customers/")
  + [Case Studies](/case-studies/ "/case-studies/")

[Contact Us](/contact/ "/contact/")

[Opinion](/categories/opinion/ "/categories/opinion/")

Trustworthy AI Agents: Deterministic Replay
===========================================

[Andrew Stevens](/author/andrew-stevens/ "/author/andrew-stevens/")

Nov 20, 2025 - 26
Min read

[Opinion](/categories/opinion/ "/categories/opinion/")
 [Ai](/tags/ai/ "/tags/ai/")
 [Security](/tags/security/ "/tags/security/")
 [Governance](/tags/governance/ "/tags/governance/")

.series-pull-quote{float:right;clear:both;width:340px;margin-left:2rem;margin-bottom:1.5rem;border:1px solid #e9ecef;border-radius:6px;overflow:hidden;background-color:#fff;position:relative;z-index:20}@media(max-width:768px){.series-pull-quote{float:none;clear:both;width:100%;margin-left:0}}.series-header{background-color:#f8f9fa;color:#6c757d;font-size:.65rem;font-weight:700;letter-spacing:.05em;padding:.8rem 1.25rem;border-bottom:1px solid #e9ecef}.part-label{display:block;font-size:.6rem;color:#adb5bd;margin-bottom:.15rem;text-transform:uppercase}.nav-link-text{font-size:.85rem;line-height:1.4;color:#495057;text-decoration:none;position:relative;z-index:21}.active-part{border-left:4px solid #000!important;background-color:#fff!important}.active-part .nav-link-text{font-size:.9rem;font-weight:700;color:#212529;text-decoration:underline;text-underline-offset:3px}.locked-part .nav-link-text{color:#ced4da}.list-group-item{border-bottom:1px solid #f8f9fa;padding:1rem 1.25rem!important}

READ MORE IN THIS SERIES

[Part 0 - Introduction](/blog/missing-primitives-for-trustworthy-ai/ "/blog/missing-primitives-for-trustworthy-ai/")

[Part 1 - End-to-End Encryption](/blog/missing-primitives-for-trustworthy-ai-part-1/ "/blog/missing-primitives-for-trustworthy-ai-part-1/")

[Part 2 - Prompt Injection Protection](/blog/missing-primitives-for-trustworthy-ai-part-2/ "/blog/missing-primitives-for-trustworthy-ai-part-2/")

[Part 3 - Agent Identity and Attestation](/blog/missing-primitives-for-trustworthy-ai-part-3/ "/blog/missing-primitives-for-trustworthy-ai-part-3/")

[Part 4 - Policy-as-Code Enforcement](/blog/missing-primitives-for-trustworthy-ai-part-4/ "/blog/missing-primitives-for-trustworthy-ai-part-4/")

[Part 5 - Verifiable Audit Logs](/blog/missing-primitives-for-trustworthy-ai-part-5/ "/blog/missing-primitives-for-trustworthy-ai-part-5/")

[Part 6 - Kill Switches and Circuit Breakers](/blog/missing-primitives-for-trustworthy-ai-part-6/ "/blog/missing-primitives-for-trustworthy-ai-part-6/")

[Part 7 - Adversarial Robustness](/blog/missing-primitives-for-trustworthy-ai-part-7/ "/blog/missing-primitives-for-trustworthy-ai-part-7/")

[Part 8 - Deterministic Replay](/blog/missing-primitives-for-trustworthy-ai-part-8/ "/blog/missing-primitives-for-trustworthy-ai-part-8/")

[Part 9 - Formal Verification of Constraints](/blog/missing-primitives-for-trustworthy-ai-part-9/ "/blog/missing-primitives-for-trustworthy-ai-part-9/")

[Part 10 - Secure Multi-Agent Protocols](/blog/missing-primitives-for-trustworthy-ai-part-10/ "/blog/missing-primitives-for-trustworthy-ai-part-10/")

[Part 11 - Agent Lifecycle Management](/blog/missing-primitives-for-trustworthy-ai-part-11/ "/blog/missing-primitives-for-trustworthy-ai-part-11/")

[Part 12 - Resource Governance](/blog/missing-primitives-for-trustworthy-ai-part-12/ "/blog/missing-primitives-for-trustworthy-ai-part-12/")

[Part 13 - Distributed Agent Orchestration](/blog/missing-primitives-for-trustworthy-ai-part-13/ "/blog/missing-primitives-for-trustworthy-ai-part-13/")

[Part 14 - Secure Memory Governance](/blog/missing-primitives-for-trustworthy-ai-part-14/ "/blog/missing-primitives-for-trustworthy-ai-part-14/")

[Part 15 - Agent-Native Observability](/blog/missing-primitives-for-trustworthy-ai-part-15/ "/blog/missing-primitives-for-trustworthy-ai-part-15/")

[Part 16 - Human-in-the-Loop Governance](/blog/missing-primitives-for-trustworthy-ai-part-16/ "/blog/missing-primitives-for-trustworthy-ai-part-16/")

[Part 17 - Conclusion (Operational Risk Modeling)](/blog/missing-primitives-for-trustworthy-ai-part-17/ "/blog/missing-primitives-for-trustworthy-ai-part-17/")

Deterministic Replay (Part 8)
-----------------------------

Debugging agent systems is fundamentally harder than debugging traditional software. Logs, metrics, and traces show you what happened, but they cannot reconstruct why it happened or the exact sequence of decisions that led to an unexpected outcome. Once an LLM produces a faulty or surprising plan in production, reproducing the exact path to that decision is functionally impossible without specialized tooling.

Deterministic replay gives teams the ability to reconstruct an agent run step by step, using recorded events to override nondeterminism and rebuild the exact execution path.

This section defines the primitives required for deterministic replay and shows how to build a practical replay harness for real systems.

Why Agent Debugging Is Non Deterministic
----------------------------------------

Agent behavior depends on multiple non deterministic inputs:

1. LLM sampling: Temperature and sampling introduce inherent variability, and model versions shift over time.
2. Tool nondeterminism : APIs and external tools may return different results on each invocation.
3. System clock access : Calls to `time.time()` or `datetime.now()` depend on real time. To ensure fidelity during replay, these calls must be intercepted and replaced with recorded timestamps. This technique is known as time warping or clock virtualization and is required to guarantee that time dependent logic executes identically during replay.
4. Data drift: Datasets and structured data sources change, introducing nondeterminism when replayed.
5. Concurrency and task ordering: In multi agent environments, the order of operations cannot be assumed to be stable.
6. Prompt and configuration drift: Small changes to templates, hidden prompts, or config values can alter execution.

Deterministic replay collects these variables during the original run and substitutes them back in during replay.

Primitive 1: Structured Execution Trace
---------------------------------------

A deterministic replay system starts with one requirement: every meaningful step an agent performs must be captured as a structured, append only event. This is the only way to later reconstruct the exact execution path. Traditional logging is insufficient because logs are unstructured, lossy, and mix human oriented descriptions with machine oriented state. Deterministic replay requires something closer to event sourcing for agents.

To support reliable reconstruction, the trace must include the following information:

* LLM calls: Every interaction with the model must be recorded, including the prompt, sampling parameters, and the exact response returned. This is essential because LLMs are inherently nondeterministic. During replay, we must substitute the recorded responses verbatim.
* Tool calls: Any API call, file write, database query, or subprocess execution must be traced with both the request and response. Tools are a major source of nondeterminism because their outputs depend on external state. By recording tool inputs and outputs, we eliminate the need to query the real system during replay.
* Decisions: Agents make intermediate decisions: selecting a plan, choosing which tool to invoke, or determining the next action. These high level decisions often shape control flow, and must be recorded independently of LLM or tool events so that replay reproduces the control graph correctly.
* Model parameters: `Temperature`, `max_tokens`, `top_p`, and other decode parameters influence the distribution of outputs. Recording these ensures we understand why a particular generation occurred and can validate that replay clients use matching configurations.
* Tool versions: If the agent calls a versioned tool (for example, an internal API or library), the version must be recorded. During replay we must verify that the expected version is used. If not, the system can warn that replay may deviate from real execution.
* Timestamps: Event ordering and time dependent logic require stable timestamps. The trace must record the time of each event, and during replay calls to the system clock must be replaced with these recorded values (via time warping / clock virtualization).
* Structured inputs and outputs: To ensure deterministic interpretation, the trace should store inputs and outputs in consistent machine readable structures such as dictionaries. Free form text, while sometimes unavoidable, should be wrapped in structured envelopes.

Together these fields form the ground truth of the agent run: the canonical representation from which replay derives.

### Why structured tracing is necessary

Without a structured, append only trace, the system cannot:

* reproduce LLM outputs
* simulate external tools
* enforce event ordering
* inspect intermediate agent decisions
* diagnose adversarial interference
* test new policies or model versions against real incidents

This makes deterministic replay impossible. The trace writer is therefore the conceptual and architectural center of the replay system.

### Example: trace writer

The following code shows a minimal trace writer that captures each event in an execution trace. It serializes events as JSON Lines (JSONL), which is easy to append, stream, diff, and load incrementally. Senior engineers will recognize that this functions like a lightweight event log or write ahead log for agent execution.

The writer is intentionally simple: deterministic replay depends on the fidelity of recorded events, not the complexity of the system that records them.

```
import json
import time
import uuid
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

@dataclass
class TraceEvent:
    """
    A single structured event in an agent's execution trace.

    Attributes:
        run_id: Unique identifier for the agent run.
        step_id: Sequential step number ensuring stable ordering.
        timestamp: Logical or wall clock time captured at record time.
        kind: Event type such as "llm_call", "tool_call", or "decision".
        input: Structured input to the operation.
        output: Structured output returned by the operation.
        metadata: Additional context such as model_id or tool version.
    """
    run_id: str
    step_id: int
    timestamp: float
    kind: str
    input: Dict[str, Any]
    output: Dict[str, Any]
    metadata: Dict[str, Any]


class TraceWriter:
    """
    Append-only JSONL writer for deterministic replay.
    Each call to record() generates a complete, immutable TraceEvent.
    """

    def __init__(self, file_path: str, run_id: Optional[str] = None):
        self.file_path = file_path
        self.run_id = run_id or str(uuid.uuid4())
        self.step_counter = 0

    def record(self, kind: str, input: Dict[str, Any],
               output: Dict[str, Any],
               metadata: Optional[Dict[str, Any]] = None) -> TraceEvent:
        """
        Create and append a new trace event.

        The step_id increments monotonically, ensuring deterministic ordering.
        Timestamps capture real or logical time and may later be replayed
        via clock virtualization.
        """
        self.step_counter += 1

        event = TraceEvent(
            run_id=self.run_id,
            step_id=self.step_counter,
            timestamp=time.time(),
            kind=kind,
            input=input,
            output=output,
            metadata=metadata or {},
        )

        # Append to JSONL
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(event)) + "\n")

        return event
```

Primitive 2: Stable Model and Tool Metadata
-------------------------------------------

Deterministic replay is only possible when you can re-establish the exact execution context that produced the original agent behavior. For LLM-driven systems, this context includes far more than the prompt and output. A model invocation is defined by an entire configuration surface area: model identifier, decoding parameters, safety settings, and the version of the underlying model weights. If any of these differ between record time and replay time, the agent’s decision path may diverge.

Similarly, tool calls introduce nondeterminism unless their identity and configuration are captured. APIs evolve, backend services deploy new versions, and data sources change. During replay, using the wrong tool version would produce results that differ from the original run and invalidate the debugging session.

A robust deterministic replay system therefore must record every detail needed to reconstruct the model and tool environment for each step. This includes:

* Model identifier: LLM vendors update model weights, safety settings, and reasoning behavior frequently. Recording the model id (for example, gpt-4.1, internal-model-2025-01, or a fine tuned checkpoint hash) ensures replay validates that responses came from the expected version.
* Decode parameters: Temperature, top\_p, top\_k, max\_tokens, presence penalties, and frequency penalties affect the token distribution. Even small deviations lead to different control flow. These must be recorded and replayed exactly.
* Safety configurations: Modern LLMs have safety settings, guardrails, or policy constraints that influence behavior. If these settings are not recorded, replay will not emulate the same inference path.
* Tool identifiers: If an agent interacts with a tool such as a REST API, SQL database, internal service, or Python function, the tool id must be recorded. This tells the replay harness which deterministic stub should handle the event.
* Tool versions: Backend tools change more frequently than LLMs. A schema migration, model update, or service deployment can change behavior in subtle ways. Capturing the tool version ensures replay validations and mismatches can be correctly surfaced.
* Tool configuration and arguments: Tool calls often depend on configuration (API keys, parameters) or nondeterministic arguments generated by the LLM. Recording the exact input sent to the tool makes the tool call reproducible even if the tool normally queries live state.

Together, these metadata fields form the execution signature of each step in the agent run. The replay engine uses this signature to decide whether replay conditions match the original environment and whether to issue warnings or abort the replay entirely.

### Why metadata fidelity matters

Model and tool metadata are the glue that binds deterministic replay to real production constraints. Without precise metadata:

* replay output may diverge from the original run
* debugging conclusions may be misleading
* regression tests may inadvertently test against a different model
* policy changes cannot be validated against historical behavior
* forensics cannot reliably reproduce the incident

In short, recording this metadata converts the execution trace from an audit log into a replayable execution state machine.

### Example: traced LLM wrapper

The following wrapper demonstrates how to capture a complete LLM call, including model id, decoding parameters, prompt, and response. The trace becomes a source of truth for replay clients.

```
class TracedLLMClient:
    """
    Wraps an LLM backend and records all requests and responses.
    """

    def __init__(self, backend, trace_writer: TraceWriter,
                 model_id: str, temperature: float = 0.0, max_tokens: int = 512):
        self.backend = backend
        self.trace = trace_writer
        self.model_id = model_id
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        result = self.backend.generate(
            model=self.model_id,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        # Capture model configuration alongside inputs and outputs.
        self.trace.record(
            kind="llm_call",
            input={"prompt": prompt},
            output={"text": result},
            metadata={
                "model_id": self.model_id,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            },
        )

        return result
```

Primitive 3: Replay Engine
--------------------------

Recording a structured trace gives you a chronological log of what happened. The replay engine is the component that transforms that log into a deterministic simulation environment. Its job is to take the recorded execution trace and inject those events back into the agent at replay time, replacing all nondeterministic operations.

Conceptually, the replay engine functions like the runtime of an event sourced system. Instead of calling the live LLM or live tools, the agent calls deterministic stubs which query the replay engine for the next recorded event. The replay engine then provides the exact input, output, and metadata that were captured during the original run.

This allows the agent to run entirely within a closed, deterministic world. All live dependencies are replaced by trace backed sources of truth.

For senior engineers, the replay engine must satisfy several correctness properties:

* Deterministic event ordering: The engine must return events in exactly the same order in which they were recorded. If a trace contains interleaved LLM calls, tool calls, and decisions, the replay engine must replay them in the correct sequence for each category of operation.
* Event type isolation: LLM calls, tool calls, decision events, and timestamps must be separated so that the replay stubs can request events of the correct type without ambiguity. For example, a ReplayLLMClient should only consume “llm\_call” events, while a ReplayToolClient should only consume “tool\_call” events.
* Cursor state: Replay must be stateful. Each class of event needs an independent cursor, tracking progress through its segment of the trace. This prevents events from being consumed out of order.
* Exhaustion detection: If the agent attempts to perform more operations than appear in the trace, the replay engine must fail loudly. Silent fallbacks to live systems would break determinism and invalidate the debugging session.
* Integrity and version checks: Each event includes metadata describing model\_id, tool\_id, version numbers, and configuration. The replay engine must enforce metadata consistency so that engineers know if the replay environment diverges from the original run.

These guarantees ensure the replay engine is not just a convenience layer but a true deterministic substrate under the agent runtime.

Example: trace loader and index
-------------------------------

The following code shows two core components of the replay engine:

1. load\_trace: Reads all trace events for a given run\_id into memory and sorts them deterministically.
2. TraceIndex: Groups events by kind and provides a cursor so replay clients can fetch events sequentially.

This pair of components forms the backbone of deterministic behavior. All replay stubs rely on them to retrieve the correct recorded state.

```
def load_trace(file_path: str, run_id: str):
    """
    Load and return all TraceEvent objects for the given run_id.
    The result is sorted by step_id to ensure deterministic ordering.
    """
    events = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if data["run_id"] == run_id:
                events.append(TraceEvent(**data))

    events.sort(key=lambda e: e.step_id)
    return events


class TraceIndex:
    """
    Provides deterministic, cursor-based access to trace events.
    Events are grouped by kind (e.g., llm_call, tool_call, decision).
    Each event kind has its own cursor so replay clients can request
    the next appropriate event without interfering with others.
    """

    def __init__(self, events):
        self.by_kind = {}
        for event in events:
            self.by_kind.setdefault(event.kind, []).append(event)

        # Independent cursor per kind guarantees isolation
        self.cursors = {kind: 0 for kind in self.by_kind}

    def next_event(self, kind: str) -> TraceEvent:
        """
        Return the next event of the specified kind.
        Raises an error if events are exhausted or unavailable.
        """
        if kind not in self.by_kind:
            raise RuntimeError(f"No events of kind '{kind}' in trace")

        idx = self.cursors[kind]
        events = self.by_kind[kind]

        if idx >= len(events):
            raise RuntimeError(f"Exhausted events of kind '{kind}'")

        event = events[idx]
        self.cursors[kind] += 1
        return event
```

This minimal structure is intentionally simple because deterministic replay depends more on fidelity than sophistication. Engineers must be able to trust:

* that the events provided by replay are exact
* that ordering is stable
* that metadata is faithfully preserved
* that replay will fail loudly if the agent attempts an operation that was not captured
* that no hidden nondeterminism leaks into the replay environment

Together, `load_trace` and `TraceIndex` serve as the deterministic foundation for all higher abstractions: ReplayLLMClient, ReplayToolClient, the agent harness, and eventually regression testing.

Primitive 4: Deterministic Stubs for LLMs and Tools
---------------------------------------------------

Once an execution trace has been captured and indexed, the next requirement is to replace every nondeterministic dependency with deterministic, trace-backed components. These replacements are known as replay stubs. Their job is simple but foundational: instead of calling real models or live tools, they query the replay engine and return the exact outputs recorded during the original run.

To an engineer, this mirrors how tests isolate external systems in distributed environments. Just as microservices are tested with mock clients or in-memory fakes, agent systems require deterministic substitutes for LLMs and tools to guarantee that replay does not leak nondeterminism back into the execution path.

Replay stubs must satisfy several engineering constraints:

* Strict determinism: Replay stubs must never call the live model, hit a real API, read from a database, or depend on the system clock. All outputs must come directly from the trace.
* Event-type isolation: Each stub must request specific event kinds (for example “llm\_call” or “tool\_call”) from the replay engine. This prevents accidental consumption of unrelated events, which would break re-execution consistency.
* Input consistency validation: Optional but recommended. Replay stubs can validate that inputs during replay match the recorded inputs. This helps engineers detect cases where control flow diverged from the recorded run.
* Metadata verification: Stubs should verify model ids, tool ids, version numbers, and configuration metadata. If the environment has drifted since the original run, the stub should surface this mismatch immediately.
* Failure on exhaustion: If the agent attempts to perform additional calls that were not captured in the original trace, the replay engine must throw an error. Continuing silently would produce a partial or misleading reproduction.

Replay stubs turn the trace into a deterministic “execution oracle,” ensuring the agent sees exactly what it saw at record time.

### Replay Stubs in Practice

A replay system must provide deterministic versions of:

* LLM client: Returns the recorded model output token-for-token.
* Tool client: Returns the recorded tool output (API response, file result, SQL query output, etc).

This transforms the entire agent runtime into a closed deterministic environment that behaves identically on each replay.

### ReplayLLMClient

The R`eplayLLMClient` replaces the real LLM with a stub that reads from the trace.

If the agent asks for an LLM generation, it does not call the model. It asks the `TraceIndex` for the next “llm\_call” event and returns its recorded output.

This guarantees deterministic reproduction of model behavior without the variability of temperature sampling, distribution drift, or model updates.

```
class ReplayLLMClient:
    """
    Deterministic stub that replays recorded LLM responses.
    """

    def __init__(self, trace_index: TraceIndex, model_id: str):
        self.index = trace_index
        self.model_id = model_id

    def generate(self, prompt: str) -> str:
        event = self.index.next_event("llm_call")

        # Validate that this replay is aligned with the recorded model.
        if event.metadata.get("model_id") != self.model_id:
            raise RuntimeError("Model id mismatch during replay")

        # Optional: validate prompt similarity if strict replay is desired.

        return event.output["text"]
```

Engineer’s note: This approach does not require prompting the model or re-running any token generation. It emulates the exact decision chain by reusing recorded outputs. This eliminates nondeterminism and ensures debugging sessions produce identical reasoning paths.

### ReplayToolClient

Tools introduce even more nondeterminism than LLMs: external APIs, databases, file operations, and long-running services all have state that drifts over time. Replay must avoid touching these real systems.

`ReplayToolClient` fills this gap by replaying only the recorded tool outputs. During replay, tool invocations become pure functions backed entirely by the trace.

```
class ReplayToolClient:
    """
    Deterministic stub that replays recorded tool responses.
    """

    def __init__(self, trace_index: TraceIndex, tool_id: str):
        self.index = trace_index
        self.tool_id = tool_id

    def execute(self, plan: str) -> str:
        event = self.index.next_event("tool_call")

        # Ensure the recorded tool identity matches expectations.
        if event.metadata.get("tool_id") != self.tool_id:
            raise RuntimeError("Tool id mismatch during replay")

        # Optional: validate the plan or arguments for strict replay.

        return event.output["result"]
```

Engineer’s note: Tool calls often introduce hidden time, randomness, or version drift. ReplayToolClient eliminates all of these factors, turning the agent’s tool interactions into deterministic, replayable steps.

### Why Deterministic Stubs Are Essential

Replay stubs allow you to:

* debug complex agent failures without touching external systems
* re-evaluate agent performance under new policies or model versions
* investigate adversarial incidents (see Part 7)
* test control flow without risk to production infrastructure
* isolate whether a failure came from the LLM, the tool, or agent logic

Without deterministic stubs, replay is incomplete, and engineers are left attempting to reconstruct behavior through logs alone.

Replay stubs turn recorded traces into a fully controlled sandbox for debugging, testing, and governance.

Primitive 5: Deterministic Agent Harness
----------------------------------------

With structured traces (Primitive 1), deterministic metadata capture (Primitive 2), and replay stubs for all nondeterministic components (Primitive 4), we can build a deterministic agent harness: an execution environment where the agent can run in either:

1. Record mode — interacting with real LLMs, real tools, real data, while capturing everything into a trace.
2. Replay mode — interacting exclusively with deterministic stubs that feed back recorded results from the trace.

A well-designed harness ensures the agent itself remains unchanged. The agent logic, state machine, or task orchestration operates as-is. Only the dependencies around it change. This provides two major advantages:

1. Zero-intrusion debugging: You do not need to rewrite the agent to debug it. You simply swap the LLM and tool clients, and the agent proceeds through its workflow, consuming recorded outputs deterministically.
2. Binary equivalence between record and replay: If the agent code is unchanged, any divergence during replay signals a real correctness issue: a control-flow fork, prompt drift, misalignment between planning logic and execution logic, or an untraced dependency. Engineers get an immediate signal that something in the system is unstable or implicitly nondeterministic.
3. Full coverage of agent behavior: Replaying an agent deterministically allows engineers to inspect intermediate decisions, verify model-to-tool interactions, run adversarial forensics, and apply policy changes to past runs.

### The importance of structured LLM outputs

A replay harness is only useful if the agent behaves the same way under record and replay. One of the most common sources of hidden nondeterminism is the LLM “plan” output used to construct the next tool call.

If the model returns free-form text and the agent parses it heuristically (regex, keyword matching, pattern extraction), then minor differences between runs can cause:

* different tool arguments
* different tool selection
* branching into different actions
* inconsistent parsing
* diverging control flow during replay

To avoid this, the plan must be emitted in a fully structured and deterministic format.

In production, the LLM output that determines the tool call (the plan) should be emitted in strict structured form such as JSON or a Pydantic model.
This guarantees that tool invocation is fully deterministic, parseable, and replayable. It also ensures the replay trace captures semantically meaningful structures rather than brittle free-text instructions.

### Example: agent class

The following simplified agent example demonstrates a typical three-step workflow:

1. Use an LLM to generate a structured plan.
2. Execute a tool based on the plan.
3. Use the LLM to summarize or synthesize results.

Because the agent’s LLM and tool clients are injected, the same code path supports both record mode and replay mode transparently.

```
class Agent:
    """
    Example agent workflow:
      1. LLM plan
      2. Tool execute
      3. LLM summarize

    This class is intentionally minimal. Its determinism relies entirely on
    the behavior of the injected clients and the structure of the recorded trace.
    """

    def __init__(self, llm_client, tool_client, trace_writer: TraceWriter):
        self.llm = llm_client
        self.tool = tool_client
        self.trace = trace_writer

    def run(self, user_query: str) -> str:
        # Step 1: Ask the LLM to create a structured plan.
        plan = self.llm.generate(f"Plan a response for: {user_query}")

        # Record the decision explicitly.
        self.trace.record(
            kind="decision",
            input={"user_query": user_query},
            output={"plan": plan},
            metadata={},
        )

        # Step 2: Execute the plan using a tool.
        tool_result = self.tool.execute(plan)

        # Step 3: Ask the LLM to summarize the tool result.
        summary = self.llm.generate(
            f"Summarize the tool result: {tool_result}"
        )

        return summary
```

### Why this harness design matters

This form of dependency injection accomplishes several important engineering goals:

* Determinism: During replay, LLM and tool calls are fetched exclusively from the trace. No external nondeterminism can leak in.
* Consistency: The agent’s actual logic remains unchanged between record and replay. This ensures that debugging is accurate and that regressions detected via replay reflect real-world control-flow differences rather than artifacts of a modified code path.
* Runtime symmetry: Record mode and replay mode share the same agent implementation. Engineers can trust the replay results because the agent is executing the same logic in both cases.
* Testability: The harness behaves like a pure function of trace input. Given the same trace, the agent must produce the same deterministic output every time.
* Safety and governance integration: Because the harness integrates with the trace writer, it creates a unified timeline of decisions, tool usage, and final results that can be tied back to audit logs, policy decisions, or adversarial detection layers.

Primitive 6: Governance Integration
-----------------------------------

Deterministic replay is not just a debugging primitive. It is a foundational capability for AI governance, operational assurance, and post-incident forensics. In a mature agent platform, replay does not sit aside from the safety stack. It is woven directly into it.

A well-governed agent ecosystem relies on trace-level visibility to validate compliance, diagnose failures, and reconstruct complex multi-step interactions across agents, tools, and policy layers. When combined with the primitives introduced in earlier parts of this series, deterministic replay becomes a unifying mechanism that ties together identity, policy, audit logging, and observability into a coherent whole.

A senior engineer should view replay not as an isolated debugging feature but as the glue layer connecting operational reliability with trust and compliance requirements.

Replay integrates with other primitives in the following ways:

##### 1. Audit logs (Part 5)

The execution trace and audit log should share the same run\_id. This creates a single source of truth where:

* trace events provide step-level execution detail
* audit events provide compliance and lineage detail

Together, these form a two-dimensional record: what the agent did and why it was allowed to do it.

Replay leverages this linkage to correlate decisions with authorization checks, which is essential for post-incident analysis.

##### 2. Kill switches and circuit breakers (Part 6)

Kill switch or breaker activations should also be recorded as trace events.
This allows the replay engine to surface moments when a safety layer intervened.

During analysis, engineers can:

* verify whether breakers fired at the correct threshold
* simulate different breaker configurations by replaying historical runs
* validate that kill-switch logic interacts correctly with updated policies

Replay makes it possible to test these changes safely using historical real-world bursts, spikes, or anomalies.

##### 3. Identity and attestation metadata (Part 3)

Every LLM call, tool call, or decision should include the identity of the calling agent.
Replay must preserve:

* the SPIFFE or SVID identity
* the agent’s attestation
* any identity-scoped configuration

This matters for governance because identity dictates:

* which policies apply
* which resources the agent is allowed to access
* how suspicious actions should be interpreted

During replay, identity metadata allows teams to reproduce the exact trust boundary in place during the original incident.

##### 4. Policy evaluations (Part 4)

Policy checks should be surfaced as explicit events in the trace.
For example, an agent action that required OPA evaluation should result in:

```
kind: "policy_check"
input: { action, agent_id, payload }
output: { decision, reason }
```

This allows replay workflows to:

* validate policy behavior over time
* detect regressions in policy logic
* replay historical policy decisions under new rules for impact analysis
* identify when a misconfiguration caused an agent to be allowed or denied incorrectly

Replay becomes a governance tool that explains policy decisions, not just code behavior.

##### 5. Adversarial detection signals (Part 7)

Adversarial flags, filtered inputs, classifier scores, and probe detection events should also be part of the trace.

These signals allow replay to reconstruct:

* how an adversarial input propagated
* how safety filters handled it
* whether a misclassification or bypass occurred
* where in the pipeline the failure originated

Replay becomes a forensic tool capable of reconstructing adversarial events end-to-end.

##### 6. Complete behavioral lineage

When all the above are combined, deterministic replay provides a complete behavioral lineage for every agent run:

1. Who the agent was (identity, attestation)
2. What decisions it made (LLM and plan outputs)
3. What policies applied (OPA or equivalent checks)
4. What tools it invoked (versioned, replayable calls)
5. Which safety layers triggered (breakers, kill switches, adversarial detectors)
6. What the final result was

This makes deterministic replay the unifying primitive for trustworthy AI.
It bridges operations, forensics, governance, safety, and debugging without requiring divergent tooling.

### Why this integration matters

For senior engineers responsible for reliability and risk:

* Replay enables post-incident reproducibility
* Governance teams gain transparent, verifiable behavioral records
* Security teams gain a mechanism for adversarial incident reconstruction
* Platform teams gain historical regression datasets
* Architects gain a tool for policy effect simulation across historical workloads

Replay is not an observability add-on. It is a structural requirement for future agent systems that operate with autonomy and high-stakes decision making.

Primitive 7: Deterministic Regression Testing
---------------------------------------------

Deterministic replay does more than enable one-off debugging. It opens the door to a new category of automated testing for agentic systems: replay-driven regression testing, often referred to in traditional software development as golden file testing or snapshot testing. In agent environments, however, the stakes and complexity are far higher.

Agents behave as distributed reasoning engines, combining LLM planning, policy checks, tool use, and intermediate decision steps. Their output is not a single function of the input. It is a temporal chain of reasoning and external effects, any part of which may shift subtly when models, configuration, or policies drift.

Deterministic regression testing allows engineering teams to use historical traces as frozen behavioral baselines, ensuring that:

* changes to prompts
* upgrades to model versions
* policy adjustments
* tool migrations
* or safety-layer modifications

do not unintentionally change how agents behave on real-world workloads.

This solves a fundamental problem in modern ML systems: we cannot rely on unit tests alone because the outputs of LLM-driven agents are emergent, contextual, and highly sensitive to upstream configuration. Instead, we use deterministic replay to treat historical agent behavior as a stable contract and verify that future behavior does not violate it.

What deterministic regression testing provides

##### 1. Behavior as a stable artifact

Instead of asserting that “the agent should respond like X,” regression tests assert, “When replaying a specific historical run, the agent must behave exactly as it did before.”

This aligns testing with reality rather than an expectation codified by humans.

##### 2. Policy and model upgrade safety

If a new model release or policy configuration alters behavior during replay, engineers can compare the new output with the old one and determine whether the change is intentional or a regression.

##### 3. Adversarial reproduction

Historical adversarial interactions (as captured in Part 7) can be replayed to confirm defenses are effective under new model versions.

##### 4. Safety net against subtle drift

Even small changes in prompts or model defaults can materially alter behavior. Replay-based regression testing highlights these changes without requiring manual inspection.

##### 5. Auditable, reproducible evidence

Replay produces deterministic outputs that can be archived, versioned, or compared over time, enabling auditability and long-term behavioral stability guarantees.

### Example: simplified regression harness

The following harness demonstrates how to perform deterministic regression testing using the previously defined replay components.

The workflow is:

1. Load the trace from disk.
2. Create a TraceIndex for deterministic cursor-based access.
3. Plug deterministic replay stubs into the agent harness.
4. Choose the historical user input from the trace.
5. Run the agent deterministically.
6. Assert properties of the final output, simulating golden file testing.

```
def run_regression(trace_path: str, run_id: str):
    """
    Deterministically replay a historical run and verify expected behavior.
    This is a form of golden file or snapshot testing, where the replayed
    output is compared against known good historical behavior.
    """

    # Load and index historical trace
    events = load_trace(trace_path, run_id)
    index = TraceIndex(events)

    # Create deterministic replay stubs for LLM and tools
    replay_llm = ReplayLLMClient(index, model_id="internal-model-2025-01")
    replay_tool = ReplayToolClient(index, tool_id="example-tool")

    # Replay mode does not write new trace events
    trace_writer = TraceWriter("/dev/null", run_id=run_id)

    # Agent instance wired entirely to deterministic components
    agent = Agent(replay_llm, replay_tool, trace_writer)

    # Extract the original user query from the first decision event
    decision_events = [e for e in events if e.kind == "decision"]
    if not decision_events:
        raise RuntimeError("No decision event found in trace")

    user_query = decision_events[0].input["user_query"]

    # Perform a full deterministic re-execution
    result = agent.run(user_query)

    # Golden file style assertion
    # If this property fails, it indicates behavioral drift.
    assert "ERROR" not in result

    return result
```

### Why deterministic regression testing is essential

For senior engineers responsible for reliability, governance, and ML platform stability, deterministic regression testing provides unique assurances:

* Behavioral invariance: If behavior changes, you know it changed, when, and under what configuration.
* Impact analysis: You can replay thousands of historical runs against a new model or new prompts to evaluate impact before production rollout.
* Safety and policy correctness: You can verify that changes in OPA rules, prompt guardrails, or kill-switch thresholds do not produce unexpected agent behavior.
* Production-grade adversarial hardening: Captured adversarial traces become a permanent test suite, protecting the system against regression vulnerabilities.
* Confidence in controlled deploys: Before rolling out new model versions, you can deterministically replay a representative corpus of past traffic to ensure the new model behaves as expected.

Why This Matters
----------------

Deterministic replay closes the final observability gap in agent systems. It gives engineering teams the ability to:

* reliably reproduce errors
* inspect internal decision chains
* analyze adversarial inputs with precision
* validate policy changes across historical workflows
* run snapshot tests using real world traffic

Combined with the previous primitives, deterministic replay completes the foundation for trustworthy AI agents.

Practical Next Steps
--------------------

* Wrap all LLM and tool calls with trace recording wrappers.
* Apply time warping or clock virtualization during replay.
* Require structured outputs from LLM planning steps.
* Treat execution traces as golden files for regression testing.
* Integrate replay into your on call and forensic workflows.

Part 9 will explore dynamic conformance checking and test time safety guarantees.

Related Articles
----------------

### [Trustworthy AI Agents: Adversarial Robustness](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-7/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-7/")

[November 19, 2025
  
8 minutes](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-7/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-7/")

[Opinion](/categories/opinion/ "/categories/opinion/")
 [AI](/tags/ai/ "/tags/ai/")
 [Security](/tags/security/ "/tags/security/")
 [Governance](/tags/governance/ "/tags/governance/")

### [Trustworthy AI Agents: Kill Switches and Circuit Breakers](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-6/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-6/")

[November 18, 2025
  
10 minutes](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-6/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-6/")

[Opinion](/categories/opinion/ "/categories/opinion/")
 [AI](/tags/ai/ "/tags/ai/")
 [Security](/tags/security/ "/tags/security/")
 [Governance](/tags/governance/ "/tags/governance/")

### [Trustworthy AI Agents: Verifiable Audit Logs](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-5/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-5/")

[November 17, 2025
  
9 minutes](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-5/ "https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-5/")

[Opinion](/categories/opinion/ "/categories/opinion/")
 [AI](/tags/ai/ "/tags/ai/")
 [Security](/tags/security/ "/tags/security/")
 [Governance](/tags/governance/ "/tags/governance/")
 [AWS](/tags/aws/ "/tags/aws/")

window.addEventListener("load",function(){if(!window.WebFont||!window.WebFont.load)return;WebFont.load({google:{api:"https://fonts.googleapis.com/css2",families:["Roboto:wght@400;500;600","Roboto:wght@400;500;600&display=swap"],version:2},active:()=>{sessionStorage.fontsLoaded=!0}})})"serviceWorker"in navigator&&navigator.serviceWorker.register("/service-worker.js")

Intelligence, Engineered.
-------------------------

Accelerate your operations with proven expertise built to scale and adapt.  
Enable, automate, and govern the intelligent systems that keep your business moving.

[Unlock Your Potential](/contact/ "/contact/")

* [+1 (415) 323-3621](tel:+1%20%28415%29%20323-3621 "tel:+1%20%28415%29%20323-3621")
* [hello@sakurasky.com](mailto:hello@sakurasky.com "mailto:hello@sakurasky.com")

#### Capability

* [Cloud](/cloud/ "/cloud/")
* [Data & AI](/data/ "/data/")
* [Security](/security/ "/security/")

#### Solutions

* [Accelerate](/accelerate/ "/accelerate/")
* [Catalyst](/catalyst/ "/catalyst/")
* [Enclave](/enclave/ "/enclave/")
* [Sentinel](/sentinel/ "/sentinel/")

#### Services

* [Professional Services](/professional-services/ "/professional-services/")
* [Managed Services](/managed-services/ "/managed-services/")

© Since 2011 Sakura Sky | All Rights Reserved | Some content has been AI generated. | [Privacy Policy](/privacy-policy/ "/privacy-policy/")
