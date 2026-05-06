# InfoQ — Docker's Cagent Brings Deterministic Testing to AI Agents

Source: https://www.infoq.com/news/2026/01/cagent-testing/

---

.async-hide { opacity: 0 !important} 
.promo{background:#222528;position:fixed;z-index:1001!important;left:0;top:0;right:0;max-height:48px;min-height:48px;padding-top:0!important;padding-bottom:0!important}.promo,.promo p{-webkit-box-align:center;-ms-flex-align:center;align-items:center}.promo p{font-size:.8125rem;line-height:1rem;color:#fff;margin-bottom:0;margin-top:0;margin:0 auto;display:-webkit-box;display:-ms-flexbox;display:flex;font-weight:700}@media only screen and (max-width:650px){.promo p{font-size:.6875rem}}.promo span{overflow:hidden;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.promo a{color:#fff!important;text-decoration:underline!important}.promo a.btn{background:#d0021b;padding:7px 20px;text-decoration:none!important;font-weight:700;margin-left:10px;margin-right:10px;white-space:nowrap;border-radius:5px}@media only screen and (max-width:650px){.promo a.btn{font-size:.6875rem;padding:7px 10px}}.promo.container{padding-top:8px;padding-bottom:8px}@media only screen and (min-width:1050px){.promo.container{padding-top:0;padding-bottom:0}}.promo .actions{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.promo .actions\_\_left{-ms-flex-preferred-size:100%;flex-basis:100%;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.promo .actions\_\_right{-ms-flex-preferred-size:40px;flex-basis:40px;margin-top:0;margin-bottom:0;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.promo.hidden{display:none}.promo.show{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.promo.show .container\_\_inner{-webkit-box-flex:1;-ms-flex:1;flex:1}.promo.fixed{position:fixed}.promo.show+header.header{margin-top:48px}.header{background:#fff;-webkit-box-shadow:0 1px 0 #dde2e5;box-shadow:0 1px 0 #dde2e5}.header .actions\_\_left,.header\_\_bottom\_\_events{max-width:100%!important;margin:0}.header .header\_\_events-all{margin:0;display:-webkit-box;display:-ms-flexbox;display:flex;position:relative}.header .header\_\_events-all .header\_\_event-slot{-webkit-box-flex:1;-ms-flex:1 100%;flex:1 100%;border-right:1px solid #dde2e5;margin-top:3px;margin-bottom:3px;padding-left:15px;text-align:left;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-right:5px;min-width:300px}.header .header\_\_events-all .header\_\_event-slot:hover{text-decoration:none!important}.header .header\_\_events-all .header\_\_event-slot img{min-width:40px;height:40px}.header .header\_\_events-all .header\_\_event-slot div{margin-left:10px}.header .header\_\_events-all .header\_\_event-slot span{font-weight:700!important;font-size:.75rem;margin-bottom:0!important;margin-top:0;display:block;line-height:1.125rem;text-align:left}.header .header\_\_events-all .header\_\_event-slot p{font-weight:400;font-size:.625rem;line-height:130%!important;color:#495057!important;margin:0}@media only screen and (min-width:1050px){.header .header\_\_events-all .header\_\_event-slot p{font-size:.625rem}}.header .header\_\_events-all .header\_\_event-slot:first-child{padding-left:0}.header .header\_\_events-all .header\_\_event-slot:last-child{padding-right:0;border-right:0}@media only screen and (min-width:1050px){.header\_\_bottom,.header\_\_middle,.header\_\_top{position:relative;white-space:nowrap}}.header\_\_top{padding:10px 0}@media only screen and (min-width:800px){.header\_\_top{padding:5px 0}}.header\_\_bottom{padding:5px 0;z-index:29;max-width:100%}.header\_\_bottom a{font-size:.8125rem}.header\_\_bottom .trending{margin-left:0;margin-right:0}.header\_\_bottom .actions{-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start}.header\_\_bottom .actions\_\_left{max-width:calc(100% + 8px)}@media only screen and (min-width:800px){.header\_\_bottom .actions\_\_left{max-width:calc(100% + 24px)}}.header\_\_bottom .actions\_\_right{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;display:none}@media only screen and (min-width:1050px){.header\_\_bottom .actions\_\_right{display:-webkit-box;display:-ms-flexbox;display:flex}}.header\_\_middle{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap}@media only screen and (min-width:1050px){.header\_\_middle{-ms-flex-wrap:nowrap;flex-wrap:nowrap}}.header\_\_top .actions\_\_left{-webkit-box-align:center;-ms-flex-align:center;align-items:center;-ms-flex-line-pack:center;align-content:center}@media only screen and (min-width:1050px){.header\_\_top .actions\_\_right{max-width:430px}}.no-style.header\_\_nav li:nth-child(3){font-weight:700}.no-style.header\_\_nav li:nth-child(3) a{color:#0e5ef1!important}.header\_\_bottom\_\_events::after{background:-webkit-gradient(linear,left top,right top,color-stop(0,rgba(255,255,255,0)),to(#fff));background:linear-gradient(90deg,rgba(255,255,255,0) 0,#fff 100%);content:'';position:absolute;height:60px;right:10px;width:25px}@media only screen and (min-width:1050px){.header\_\_bottom\_\_events::after{display:none}}.contribute-link{font-weight:400;font-size:.6875rem;color:#000!important;position:relative;padding-left:10px}.contribute-link:hover{color:#00791d!important;text-decoration:none!important}.contribute-link::before{content:'';width:1px;height:12px;position:absolute;top:50%;-webkit-transform:translateY(-50%);transform:translateY(-50%);background:rgba(0,0,0,.1);left:-1px}.my-0{margin-top:0!important;margin-bottom:0!important}.header\_\_desc.my-0{margin-left:0}.header\_\_bottom\_\_events .actions\_\_left{max-width:100%!important;overflow-x:scroll;-ms-overflow-style:none;scrollbar-width:none;display:block;scroll-behavior:smooth;min-width:100%}.header\_\_bottom\_\_events .actions\_\_left::-webkit-scrollbar{display:none}.header\_\_bottom\_\_events .actions\_\_left:-webkit-scrollbar-thumb{background:#fff}.logo{line-height:1rem}.header{position:relative;z-index:41;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.header .input:focus,.header input[type=password]:focus,.header input[type=text]:focus{border:1px solid #00791d}.header a:not(.button):not(.login\_\_action):not(.active){text-decoration:none;color:#222}.header a:not(.button):not(.login\_\_action):not(.active):hover{text-decoration:underline;color:#222}.header\_\_items{display:none;-ms-flex-wrap:wrap;flex-wrap:wrap}@media only screen and (min-width:1050px){.header\_\_items{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}.header\_\_items nav{position:relative;background:0 0;padding:0;left:0;top:0;line-height:inherit;display:block;-webkit-box-shadow:none;box-shadow:none;max-width:100%;max-height:80px}}.header\_\_items>div{width:100%;margin-bottom:32px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-flow:column nowrap;flex-flow:column nowrap}@media only screen and (min-width:552px){.header\_\_items>div:not(:nth-last-child(-n+2)){margin-bottom:32px}}@media only screen and (min-width:552px) and (max-width:1050px){.header\_\_items>div{-webkit-box-flex:0;-ms-flex-positive:0;flex-grow:0;-ms-flex-negative:0;flex-shrink:0;-ms-flex-preferred-size:calc(99.7% \* 1/2 - (32px - 32px \* 1/2));flex-basis:calc(99.7% \* 1/2 - (32px - 32px \* 1/2));max-width:calc(99.7% \* 1/2 - (32px - 32px \* 1/2));width:calc(99.7% \* 1/2 - (32px - 32px \* 1/2))}.header\_\_items>div:nth-child(1n){margin-right:32px;margin-left:0}.header\_\_items>div:last-child{margin-right:0}.header\_\_items>div:nth-child(2n){margin-right:0;margin-left:auto}}@media only screen and (min-width:800px) and (max-width:1050px){.header\_\_items>div{-webkit-box-flex:0;-ms-flex-positive:0;flex-grow:0;-ms-flex-negative:0;flex-shrink:0;-ms-flex-preferred-size:calc(99.7% \* 1/4 - (32px - 32px \* 1/4));flex-basis:calc(99.7% \* 1/4 - (32px - 32px \* 1/4));max-width:calc(99.7% \* 1/4 - (32px - 32px \* 1/4));width:calc(99.7% \* 1/4 - (32px - 32px \* 1/4))}.header\_\_items>div:nth-child(1n){margin-right:32px;margin-left:0}.header\_\_items>div:last-child{margin-right:0}.header\_\_items>div:nth-child(4n){margin-right:0;margin-left:auto}}@media only screen and (min-width:1050px){.header\_\_items>div{margin-bottom:0!important;margin-right:0!important;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}}.header\_\_items .language\_\_switcher{display:none}.header\_\_items .language\_\_switcher .li-nav.active>a,.header\_\_items .language\_\_switcher>li.active>a{color:#fff!important}.header\_\_items .language\_\_switcher .li-nav.active>a:hover,.header\_\_items .language\_\_switcher>li.active>a:hover{color:#fff!important;background:#0e5ef1}.header\_\_items .language\_\_switcher .li-nav:hover>a,.header\_\_items .language\_\_switcher>li:hover>a{color:#fff}.header+main{display:block;min-height:210px;-webkit-transition:margin .15s ease;transition:margin .15s ease;margin-top:0!important}.header--hide .header+main{margin-top:50px}.header--hide .header\_\_toggle{opacity:0;top:20px;visibility:hidden}.header--hide .header\_\_logo{max-height:0}.header--hide .header\_\_middle,.header--hide .header\_\_top{max-height:0;overflow:hidden;padding-top:0;padding-bottom:0;border-color:transparent}.header--hide .header\_\_bottom .vue-portal-target{top:3px;right:0;bottom:auto;left:auto;position:absolute}.header\_\_middle,.header\_\_top{-webkit-transition:all .15s ease;transition:all .15s ease}.header\_\_middle{border-bottom:1px solid rgba(0,0,0,.1);z-index:33}.header\_\_middle .vue-portal-target{width:100%}@media only screen and (min-width:1050px){.header\_\_middle .vue-portal-target{display:none}}@media only screen and (min-width:1050px){.header\_\_middle{line-height:5.75rem;text-align:left;padding:0;z-index:30}.header\_\_middle .widget\_\_heading{display:none}}.header\_\_top>.actions\_\_left{display:none}@media only screen and (min-width:1050px){.header\_\_top>.actions\_\_left{display:-webkit-box;display:-ms-flexbox;display:flex}}.header\_\_top>.actions\_\_right{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;margin-right:0;margin-top:0;margin-bottom:0;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.header\_\_top>.actions\_\_right .dropdown\_\_holder{width:calc(100vw - 16px);max-height:80vh}@media only screen and (min-width:600px){.header\_\_top>.actions\_\_right .dropdown\_\_holder{width:auto}}.header\_\_top>.actions\_\_right>\*{margin:0}.header\_\_top>.actions\_\_right .search{display:none}@media only screen and (min-width:1050px){.header\_\_top>.actions\_\_right>\*{display:-webkit-box;display:-ms-flexbox;display:flex;white-space:nowrap}.header\_\_top>.actions\_\_right .search{display:block}}.header\_\_top .user\_\_login{display:block}.header\_\_top .user\_\_login>.button,.header\_\_top .user\_\_login>button{border-top-right-radius:0;border-bottom-right-radius:0}@media only screen and (min-width:1050px){.header\_\_top{position:relative;right:auto;width:100%}}.header\_\_logo{max-width:165px;position:absolute;top:8px;overflow:hidden;-webkit-transition:all .1s ease;transition:all .1s ease;z-index:32;line-height:2.25rem;height:36px;width:100px;margin-left:50px;-ms-flex-preferred-size:190px;flex-basis:190px}@media only screen and (min-width:800px){.header\_\_logo{top:4px}}@media only screen and (min-width:1050px){.header\_\_logo{position:relative;top:0;overflow:visible;margin-right:20px;margin-left:0;line-height:3.125rem;height:50px}.header\_\_logo>\*{width:165px}}@media only screen and (min-width:1280px){.header\_\_logo{margin-right:30px}}.header\_\_desc,.header\_\_more>button{text-transform:capitalize;color:#666;letter-spacing:0;font-size:0;font-weight:400;line-height:1.5rem;vertical-align:top;font-smoothing:antialiased;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI Variable","Segoe UI",system-ui,ui-sans-serif,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";-webkit-transition:font-size .15s ease-in-out;transition:font-size .15s ease-in-out}@media only screen and (min-width:1050px){.header\_\_desc,.header\_\_more>button{font-size:.6875rem}}.header\_\_desc{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;position:relative;width:auto}.header\_\_topics{white-space:nowrap;float:right;position:relative}.header\_\_topics \*{display:inline-block;vertical-align:top}.header\_\_topics a{font-size:.8125rem}@media only screen and (min-width:1050px){.header\_\_topics{float:none}}.header\_\_more{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;vertical-align:top}.header\_\_more:before{left:-12px}.header\_\_more:after,.header\_\_more:before{content:'';width:1px;height:12px;position:absolute;top:50%;-webkit-transform:translateY(-50%);transform:translateY(-50%);background:rgba(0,0,0,.1)}.header\_\_more:after{right:-12px}.header\_\_more:hover{cursor:pointer;color:rgba(0,0,0,.75)}.header\_\_user{display:inline-block;vertical-align:top;white-space:nowrap;margin-left:8px}@media only screen and (min-width:1050px){.header\_\_user{margin-left:0}}.header\_\_user>div{display:inline-block;vertical-align:top}.header\_\_user-nav a:not(.button){text-transform:uppercase;font-size:.75rem;font-weight:600}.header\_\_user-nav a:not(.button):not(.active){opacity:.5}.header\_\_user-nav a:not(.button):not(.active):hover{opacity:.75}.header\_\_user-nav a:not(.button):hover{text-decoration:none}.header\_\_user-nav a:not(.button).active{color:#222;cursor:default;text-decoration:none}.header\_\_user-nav a:not(.button):before{margin-right:0}.header\_\_user-nav a:not(.button):not(:last-child){margin-right:16px}@media only screen and (min-width:1050px){.header\_\_user-nav a:not(.button):not(:last-child){margin-right:32px}}@media only screen and (min-width:1050px){.header\_\_user-nav+.header\_\_topics{margin-left:56px}}.header\_\_search{display:none;vertical-align:top;margin-right:0}@media only screen and (min-width:1050px){.header\_\_search{display:inline-block}}.header\_\_search,.header\_\_user{line-height:inherit}.header\_\_nav{border-bottom:1px solid rgba(0,0,0,.1)}@media only screen and (min-width:800px){.header\_\_nav{border-bottom:0}}.header\_\_nav .button{margin-left:0}.header\_\_nav .button\_\_more{margin-right:20px}.header\_\_nav .li-nav,.header\_\_nav>li{-webkit-transition:all .15s ease;transition:all .15s ease}@media only screen and (min-width:1050px){.header\_\_nav .li-nav,.header\_\_nav>li{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle;position:static;border:none;min-height:65px}.header\_\_nav .li-nav:hover.has--subnav .nav .li-nav,.header\_\_nav .li-nav:hover.has--subnav .nav>li,.header\_\_nav>li:hover.has--subnav .nav .li-nav,.header\_\_nav>li:hover.has--subnav .nav>li{white-space:normal}.header\_\_nav .li-nav:hover.has--subnav .nav\_\_subnav,.header\_\_nav>li:hover.has--subnav .nav\_\_subnav{opacity:1;top:100%;visibility:visible;-webkit-transition-delay:.25s;transition-delay:.25s}.header\_\_nav .li-nav:hover.has--subnav .nav\_\_category,.header\_\_nav>li:hover.has--subnav .nav\_\_category{width:100%}.header\_\_nav .li-nav:hover.has--subnav .nav\_\_category:after,.header\_\_nav .li-nav:hover.has--subnav .nav\_\_category:before,.header\_\_nav>li:hover.has--subnav .nav\_\_category:after,.header\_\_nav>li:hover.has--subnav .nav\_\_category:before{-webkit-transition-delay:.25s;transition-delay:.25s;opacity:1}}@media only screen and (min-width:1080px){.header\_\_nav .li-nav:not(:last-child),.header\_\_nav>li:not(:last-child){margin-right:23px;margin-left:23px}}@media only screen and (min-width:1280px){.header\_\_nav .li-nav:not(:last-child),.header\_\_nav>li:not(:last-child){margin-right:23px;margin-left:23px}}@media only screen and (min-width:1338px){.header\_\_nav .li-nav:not(:last-child),.header\_\_nav>li:not(:last-child){margin-right:23px;margin-left:23px}}.header\_\_nav .li-nav>a,.header\_\_nav>li>a{font-size:.875rem;line-height:1.5rem;padding:12px 0;color:#000;display:inline-block;max-width:100%;position:relative;z-index:61;white-space:normal}@media only screen and (min-width:1050px){.header\_\_nav .li-nav>a,.header\_\_nav>li>a{padding:8px 0 0;font-weight:700}}.header\_\_nav .li-nav>a:after,.header\_\_nav .li-nav>a:before,.header\_\_nav>li>a:after,.header\_\_nav>li>a:before{content:'';position:absolute;bottom:-1px;left:50%;width:0;height:0;opacity:0;-webkit-transform:translateX(-50%);transform:translateX(-50%);border-style:solid;border-width:0 5px 5px 5px;-webkit-transition:opacity .15s ease-in-out;transition:opacity .15s ease-in-out;border-color:transparent transparent #fff transparent}.header\_\_nav .li-nav>a:before,.header\_\_nav>li>a:before{left:50%;bottom:0;border-width:0 6px 6px 6px;border-color:transparent transparent #f5f7f8 transparent}@media only screen and (min-width:1050px){.header\_\_nav .li-nav>a,.header\_\_nav>li>a{font-size:1rem}}@media only screen and (min-width:1800px){.header\_\_nav .li-nav>a,.header\_\_nav>li>a{font-size:1.125rem}}.header--open{overflow:hidden}@media only screen and (min-width:600px){.header--open{overflow:visible}}.header--open .content-items{max-height:215px;margin:12px 0 24px}.header--open .search{margin-top:16px;display:block}.header--open .header\_\_toggle:before{z-index:10}.header--open .header\_\_toggle>span:nth-child(1){top:50%;-webkit-transform:rotate(45deg);transform:rotate(45deg)}.header--open .header\_\_toggle>span:nth-child(2){opacity:0}.header--open .header\_\_toggle>span:nth-child(3){top:50%;-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.header--open .header\_\_items,.header--open .header\_\_items .language\_\_switcher{display:-webkit-box;display:-ms-flexbox;display:flex}.header--open .header\_\_top{z-index:100;position:absolute;left:0;right:8px;background:#fff}@media only screen and (min-width:800px){.header--open .header\_\_top{right:20px}}.header--open .header\_\_top .search{display:none}.header--open .header\_\_logo{z-index:101}.header--open .header\_\_middle{padding-top:60px}.header--open .header\_\_bottom{display:none}.header--open .header\_\_container{max-height:90vh;overflow-x:hidden;overflow-y:auto}@media only screen and (min-width:1050px){.header--open .header\_\_container{overflow:visible}}.header .subnav{position:absolute;-webkit-box-shadow:0 5px 25px 1px rgba(0,0,0,.15);box-shadow:0 5px 25px 1px rgba(0,0,0,.15);background:#fff;visibility:hidden;line-height:1.75rem;max-width:100%;width:100%;left:0;opacity:0;overflow:hidden;border:1px solid #f5f7f8;border-radius:2px;-webkit-transition:all .15s ease-in-out;transition:all .15s ease-in-out;top:105%;z-index:60;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch}.header .subnav .subnav\_\_categories{-webkit-box-flex:0;-ms-flex:0 1 280px;flex:0 1 280px;padding:24px 0;background:#f5f7f8;margin-right:0!important}.header .subnav .subnav\_\_categories>li{display:block;font-size:.9375rem;padding:2px 48px 2px 24px}.header .subnav .subnav\_\_categories>li a{display:block;font-weight:700}.header .subnav .subnav\_\_categories>li:hover{background:#e1e1e1}.header .subnav .subnav\_\_heading{margin-bottom:20px}.header .subnav .subnav\_\_content{position:relative;-ms-flex-item-align:start;align-self:flex-start;padding:24px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap}@media only screen and (min-width:1050px){.header .subnav .subnav\_\_content{padding-left:32px;padding-right:32px;margin:0 auto;-webkit-box-flex:1;-ms-flex:1 1 600px;flex:1 1 600px}}.header .subnav .subnav\_\_content .heading\_\_container{-ms-flex-preferred-size:100%;flex-basis:100%}.header .subnav .subnav\_\_content:before{content:'';position:absolute;left:0;top:0;bottom:-100%;width:1px;background:rgba(0,0,0,.1)}.languagesEdition .active{font-weight:700}.header\_\_more.dropdown:after{content:'';display:inline-block;vertical-align:middle;-ms-flex-item-align:center;-ms-grid-row-align:center;align-self:center;background-repeat:no-repeat;background-position:center;margin-bottom:2px;width:7px;height:7px;-webkit-transition:-webkit-transform .15s ease;transition:-webkit-transform .15s ease;transition:transform .15s ease;transition:transform .15s ease,-webkit-transform .15s ease;background-color:#fff!important;background-size:contain}.header\_\_more.dropdown button{color:#000!important;margin-right:-20px;padding-right:20px;z-index:1000}.header\_\_more.dropdown .dropdown\_\_holder{width:165px}.header\_\_more.dropdown .dropdown\_\_content{padding:13px;padding-top:5px;padding-bottom:5px}.header\_\_more.dropdown .languagesEdition li{border-bottom:1px solid #e6e6e6}.header\_\_more.dropdown .languagesEdition li:last-child{border:0}.logo\_\_data{display:none;color:#666;font-size:.6875rem}@media only screen and (min-width:1050px){.logo\_\_data{display:block;line-height:.8125rem}}.container{padding-left:12px;padding-right:12px;margin:0 auto;min-width:320px;-webkit-transition:padding .15s ease-in-out;transition:padding .15s ease-in-out}@media only screen and (min-width:600px){.container{padding-left:16px;padding-right:16px}}@media only screen and (min-width:800px){.container{padding-left:20px;padding-right:20px}}@media only screen and (min-width:1250px){.container{padding-left:60px;padding-right:60px}}@media only screen and (min-width:1400px){.container{padding-left:20px;padding-right:20px}}.container.white{background:#fff}.container\_\_inner{max-width:1290px;margin:0 auto;-webkit-transition:max-width .15s ease-out;transition:max-width .15s ease-out}.search{display:block;position:relative;z-index:33;width:100%;max-width:100%;margin:0}.search:before{position:absolute;top:50%;right:24px;-webkit-transform:translateY(-50%);transform:translateY(-50%);margin-right:0;z-index:34}.search\_\_bar{display:block;border-radius:2px;position:relative;z-index:33}.search\_\_bar #search{margin-bottom:0;max-width:100%;background:#fff}.search\_\_go{top:50%;right:0;bottom:0;left:auto;position:absolute;-webkit-transform:translateY(-50%);transform:translateY(-50%);z-index:32;-webkit-appearance:none;-moz-appearance:none;appearance:none;width:36px;height:36px;line-height:2.25rem;-webkit-box-shadow:none;box-shadow:none;display:block;background:0 0;border:0;font-size:0}@media only screen and (min-width:600px){.search\_\_go{z-index:35}}.header #search,.search\_\_go:hover{cursor:pointer}.header #search{height:36px;position:relative;max-width:100%;background-color:#f5f7f8!important}@media only screen and (min-width:600px){.header #search{font-size:.8125rem;min-width:165px;max-width:100%;opacity:1}}.header #search:hover{cursor:auto}@media only screen and (min-width:1050px){.header #search{margin-left:auto;border-top-right-radius:0;border-bottom-right-radius:0;border-right:0}.header #search:focus{min-width:215px}}.header #search:focus{cursor:auto}.header #search .field\_\_desc{display:none}.header #searchForm{width:100%;margin-top:8px}.header #searchForm:before{right:8px}@media only screen and (min-width:600px){.header #searchForm{margin-top:16px}}@media only screen and (min-width:1050px){.header #searchForm{margin-top:0}}
(function(a,s,y,n,c,h,i,d,e){s.className+=' '+y;h.start=1\*new Date;
h.end=i=function(){s.className=s.className.replace(RegExp(' ?'+y),'')};
(a[n]=a[n]||[]).hide=h;setTimeout(function(){i();h.end=null},c);h.timeout=c;
})(window,document.documentElement,'async-hide','dataLayer',4000,
{'GTM-W9GJ5DL':true});

var loggedIn = false;
if (loggedIn) {
var userCountryId = '';
}

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('config', 'G-VMVPD4D2JY');
//CookieControl tool recomendation
// Call the default command before gtag.js or Tag Manager runs to
// adjust how the tags operate when they run. Modify the defaults
// per your business requirements and prior consent granted/denied, e.g.:
gtag('consent', 'default', {
'ad\_storage': 'denied',
'ad\_user\_data': 'denied',
'ad\_personalization': 'denied',
'analytics\_storage': 'denied'
});
if((typeof loggedIn != "undefined") && loggedIn){
window.dataLayer.push({'logged\_in': 'true'});
} else {
window.dataLayer.push({'logged\_in': 'false'});
}
window.dataLayer.push({'show\_queryz': ''});


var gtmProfile="GTM-W9GJ5DL";
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer', gtmProfile);

Docker’s Cagent Brings Deterministic Testing to AI Agents - InfoQ




























var device='desktop';
var InfoQConstants = {};
InfoQConstants.language = 'en';
InfoQConstants.countryCode = '';
InfoQConstants.pageUrl = (typeof window.location != 'undefined' && window.location && typeof window.location.href != 'undefined' && window.location.href) ? window.location.href : "URL\_UNAVAILABLE";
InfoQConstants.cet='AHhF9WKxDpki2gpt';
InfoQConstants.userDetectedCountryCode = '';
InfoQConstants.bpadb = 'kfDqhtmpogSIA4MwuoZ7';


var JSi18n = JSi18n || {}; // define only if not already defined
JSi18n.error='Error';
JSi18n.login\_unverifiedAccount='Unverified account';
JSi18n.contentSummary\_showPresentations\_1='';
JSi18n.contentSummary\_showPresentations\_2='';
JSi18n.contentSummary\_showPresentations\_3='';
JSi18n.contentSummary\_showInterviews\_1='';
JSi18n.contentSummary\_showInterviews\_2='';
JSi18n.contentSummary\_showInterviews\_3='';
JSi18n.contentSummary\_showMinibooks\_1='';
JSi18n.contentSummary\_showMinibooks\_2='';
JSi18n.login\_sendingRequest='Sending request ...';
JSi18n.bookmark\_saved='<q>&nbsp;&nbsp;&nbsp;Saved&nbsp;&nbsp;&nbsp;&nbsp;</q>';
JSi18n.bookmark\_error='<q style=color:black;>&nbsp;&nbsp;&nbsp;Error&nbsp;&nbsp;&nbsp;&nbsp;</q>';
JSi18n.categoryManagement\_showpopup\_viewAllLink\_viewAllPrefix='View All';
JSi18n.categoryManagement\_showpopup\_viewAllLink\_viewAllSuffix='';
JSi18n.categoryManagement\_showpopup\_includeExcludeLink\_Exclude='Exclude';
JSi18n.categoryManagement\_showpopup\_includeExcludeLink\_Include='Include';
JSi18n.login\_invalid\_email='Please specify a valid email';
JSi18n.login\_email\_not\_found = 'No user found with that email';
JSi18n.content\_datetime\_format='MMM dd, yyyy';
// used by frontend
JSi18n.FE = {
labels: {
follow: "Follow",
followTopic: "Follow Topic",
unfollow: "Unfollow",
unfollowTopic: "Unfollow Topic",
following: "Following",
followers: "Followers",
like: "Like",
liked: "Liked",
authors: "Peers",
users : "Users",
topics: "Topics",
hide: "Hide Item",
hidden: "%s was hidden on your profile page.",
undo: "Undo",
showLess: "Show less",
showMore: "Show more",
moreAuthors: "And %s more",
bookmarked: "Content Bookmarked",
unbookmarked: "Content Unbookmarked",
characterLimit: "Characters Remaining"
}
}
var usersInPage = JSON.parse('[{\"id\":\"62671158\",\"ref\":\"author-Monica-Beckwith\",\"url\":\"\/profile\/Monica-Beckwith\",\"followedByCurrentUser\":false,\"minibio\":\"\",\"name\":\"Monica Beckwith\",\"bio\":\"Java Champion, Monica Beckwith is a Java performance engineer. She currently works on improving OpenJDK&#39;s HotSpot VM at Microsoft. Her past experiences include working with Arm, Oracle\/Sun and AMD; optimizing the JVM for server class systems. Monica was voted a JavaOne Rock Star speaker and was the performance lead for Garbage First Garbage Collector (G1 GC). You can follow Monica on twitter &#64;mon\_beck\",\"followers\":1807,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/QhDv7pXEUK1sdLsYArFmnLxecH4rYhAc.jpg\"},{\"id\":\"45723890\",\"ref\":\"author-Rags-Srinivas\",\"url\":\"\/profile\/Rags-Srinivas\",\"followedByCurrentUser\":false,\"minibio\":\"\",\"name\":\"Rags Srinivas\",\"bio\":\"Raghavan &#34;Rags&#34; Srinivas (&#64;ragss) works as an Architect\/Developer Evangelist goaled with helping developers build highly scalable and available systems. As an OpenStack advocate and solutions architect at Rackspace he was constantly challenged from low level infrastructure to high level application issues. His general focus area is in distributed systems, with a specialization in Cloud Computing and Big Data. He worked on Hadoop, HBase and NoSQL during its early stages. He has spoken on a variety of technical topics at conferences around the world, written for developer portals, conducted and organized Hands-on Labs and taught graduate and online classes in the evening. Rags brings with him over 25 years of hands-on software development and over 15 years of architecture and technology evangelism experience. He has evangelized and influenced the architecture of a number of emerging technology areas. He is also a repeat JavaOne rock star speaker award winner. Rags holds a Masters degree in Computer Science from the Center of Advanced Computer Studies at the University of Louisiana at Lafayette. He likes to hike, run and generally be outdoors but most of all loves to eat.\",\"followers\":340,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/t4nyfgw1THkp4wMZ9EZ59RGJx8Hf9Rk8.jpg\"},{\"id\":\"87551248\",\"ref\":\"author-Steef~Jan-Wiggers\",\"url\":\"\/profile\/Steef~Jan-Wiggers\",\"followedByCurrentUser\":false,\"minibio\":\"Cloud Queue Lead Editor | Domain Architect | Cloud Expert\",\"name\":\"Steef-Jan Wiggers\",\"bio\":\"Steef-Jan Wiggers is one of InfoQ&#39;s senior cloud editors and works as a Domain Architect at VGZ in the Netherlands. His current technical expertise focuses on implementing integration platforms, Azure DevOps, AI, and Azure Platform Solution Architectures. Steef-Jan is a regular speaker at conferences and user groups and writes for InfoQ. Furthermore, Microsoft has recognized him as a Microsoft Azure MVP for the past sixteen years.\",\"followers\":854,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/BhZx03k3Hj0pZVXmTzGqItwZxtJ06oIb.jpg\"},{\"id\":\"80977916\",\"ref\":\"author-Thomas-Betts\",\"url\":\"\/profile\/Thomas-Betts\",\"followedByCurrentUser\":false,\"minibio\":\"Senior Laureate Application Architect at Blackbaud\",\"name\":\"Thomas Betts\",\"bio\":\"Thomas Betts is the Lead Editor for Architecture and Design at InfoQ, a co-host of the InfoQ Podcast, and a Senior Laureate Software Architect at Blackbaud, working on Agents for Good.\\r\\n\\r\\nFor over two decades, his focus has always been on providing software solutions that delight his customers. He has worked in a variety of industries, including social good, retail, finance, health care, defense and travel.\\r\\n\\r\\nThomas lives in Denver with his wife and son, and they love hiking and otherwise exploring beautiful Colorado.\",\"followers\":1130,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/pSqI6HrU3k9rmmVjwS34OHG0bOMYiE6a.jpg\"},{\"id\":\"72028228\",\"ref\":\"author-Sergio-De-Simone\",\"url\":\"\/profile\/Sergio-De-Simone\",\"followedByCurrentUser\":false,\"minibio\":\"\",\"name\":\"Sergio De Simone\",\"bio\":\"<b>Sergio De Simone<\/b> is a software engineer. Sergio has been working as a software engineer for over twenty five years across a range of different projects and companies, including such different work environments as Siemens, HP, and small startups. For the last 10&#43; years, his focus has been on development for mobile platforms and related technologies. He is currently working for BigML, Inc., where he leads iOS and macOS development.\",\"followers\":750,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/NovciOoQOAYWqYqRQBFo97SuMm0xbUiC.jpg\"},{\"id\":\"126467140\",\"ref\":\"author-Renato-Losio\",\"url\":\"\/profile\/Renato-Losio\",\"followedByCurrentUser\":false,\"minibio\":\"Cloud Expert | AWS Data Hero \",\"name\":\"Renato Losio\",\"bio\":\"Renato has extensive experience as a cloud architect, tech lead, and cloud services specialist. Currently, he lives in Berlin and works remotely as a principal cloud architect. His primary areas of interest include cloud services and relational databases. He is an editor at InfoQ and a recognized AWS Data Hero. You can connect with him on LinkedIn.\",\"followers\":854,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/ptroF8HdI2vWXm0NDaKeS0JdiPxMOAra.jpg\"},{\"id\":\"126669407\",\"ref\":\"author-Matt-Foster\",\"url\":\"\/profile\/Matt-Foster\",\"followedByCurrentUser\":false,\"minibio\":\"Technical Principal at Thoughtworks\",\"name\":\"Matt Foster\",\"bio\":\"Matt is a Technical Principal with Thoughtworks. He specializes in the platforms behind modern AI such as the large\u2011scale GPU clusters that train and serve today&#39;s frontier models, and the agentic tooling used to operate them. This focus builds on years of helping customers rethink their legacy application architecture, work he has documented in articles on Domain Driven Design and Legacy Displacement Patterns in collaboration with Martin Fowler. Matt has led multi\u2011disciplinary teams across businesses both large and small in Europe and more recently North America. A firm believer in a healthy body promoting a healthy mind, when Matt is not immersed in technology he can be found swimming, biking or running towards his next triathlon.\",\"followers\":29,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/wNPrqXey9HuJh58kwmQ6a8AugAVmPVgA.jpg\"},{\"id\":\"126464202\",\"ref\":\"author-Johan-Janssen\",\"url\":\"\/profile\/Johan-Janssen\",\"followedByCurrentUser\":false,\"minibio\":\"Architect at ASML\",\"name\":\"Johan Janssen\",\"bio\":\"Architect at ASML, loves to share knowledge mainly around Java. Spoke at conferences such as Devoxx, Oracle Code One, Devnexus, and many more. Assisted conferences by participating in program committees and invented and organized JVMCON. Received the JavaOne Rock Star and Oracle Code One Star awards. Wrote various articles both for digital and printed media. Maintainer of various Java JDK\/JRE packages for Chocolatey with around 100 thousand downloads a month.\",\"followers\":506,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/Fb4eZ0mtvMf6MhsmBIhsUVueV4xAs2FD.jpg\"},{\"id\":\"39485652\",\"ref\":\"author-Daniel-Bryant\",\"url\":\"\/profile\/Daniel-Bryant\",\"followedByCurrentUser\":false,\"minibio\":\"InfoQ News Manager | Building Platforms at Syntasso\",\"name\":\"Daniel Bryant\",\"bio\":\"Daniel Bryant is the news manager at InfoQ and the emeritus chair of QCon London. He is also a platform engineer and head of product marketing at Syntasso. Daniel&#39;s technical expertise focuses on \u2018DevOps\u2019 tooling, cloud\/container platforms, and microservice implementations. He is a long-time coder and Java Champion who has contributed to several open source projects. Daniel also writes for InfoQ, O\u2019Reilly, and The New Stack and regularly presents at international conferences such as KubeCon, QCon, and JavaOne. In his copious amounts of free time, he enjoys running, reading, and travelling.\",\"followers\":2721,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/tSe5dczMaSGtRUm18VkTR2tcF4W3SogA.jpg\"},{\"id\":\"63268344\",\"ref\":\"author-Chris-Swan\",\"url\":\"\/profile\/Chris-Swan\",\"followedByCurrentUser\":false,\"minibio\":\"Engineer, Atsign\",\"name\":\"Chris Swan\",\"bio\":\"Chris Swan is an Engineer at <a href=\\\"https:\/\/atsign.com\\\" rel=\\\"nofollow\\\">Atsign<\/a>, building the atPlatform, a technology that is putting people in control of their data and removing the frictions and surveillance associated with today\u2019s Internet. He was previously a Fellow at DXC Technology where he held various CTO roles. Before that he held CTO and Director of R&amp;D roles at Cohesive Networks, UBS, Capital SCF and Credit Suisse, where he worked on app servers, compute grids, security, mobile, cloud, networking and containers. Chris co-hosts the <a href=\\\"https:\/\/techdebtburndown.com\/\\\" rel=\\\"nofollow\\\">Tech Debt Burndown Podcast<\/a> and is a Dart Google Developer Expert (<a href=\\\"https:\/\/developers.google.com\/community\/experts\\\" rel=\\\"nofollow\\\">GDE<\/a>).\",\"followers\":1850,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/8PE76nOujWAoCM8yqLn9Hfv2HqW3VlIP.jpg\"},{\"id\":\"4927376\",\"ref\":\"author-Karsten-Silz\",\"url\":\"\/profile\/Karsten-Silz\",\"followedByCurrentUser\":false,\"minibio\":\"Full-Stack Java Developer\",\"name\":\"Karsten Silz\",\"bio\":\"Karsten Silz has worked as a full-stack Java developer for 26 years in Europe and the US. In 2004, he co-founded a software product start-up in the US. Karsten led product development for 13 years and left after the company was sold successfully. Since 2003, he has also worked as a contractor. He co-founded the SaaS start-up &#34;Your Home in Good Hands&#34; as CTO in the UK in 2020.\",\"followers\":381,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/p6zmOdOcqXiRj09iiZNeDZap7f0IglQW.jpg\"},{\"id\":\"343314\",\"ref\":\"author-Jonathan-Allen\",\"url\":\"\/profile\/Jonathan-Allen\",\"followedByCurrentUser\":false,\"minibio\":\"Software Architect\",\"name\":\"Jonathan Allen\",\"bio\":\"Jonathan Allen got his start working on MIS projects for a health clinic in the late 90&#39;s, bringing them up from Access and Excel to an enterprise solution by degrees. After spending five years writing automated trading systems for the financial sector, he became a consultant on a variety of projects including the UI for a robotic warehouse, the middle tier for cancer research software, and the big data needs of a major real estate insurance company. In his free time he enjoys studying and writing about martial arts from the 16th century.\\r\\n\",\"followers\":1812,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/Wk\_C09\_mzwK23YkTkKMXResJv3LKUN5D.jpg\"},{\"id\":\"114725059\",\"ref\":\"author-Holly-Cummins\",\"url\":\"\/profile\/Holly-Cummins\",\"followedByCurrentUser\":false,\"minibio\":\"Senior Technical Staff Member, IBM\",\"name\":\"Holly Cummins\",\"bio\":\"Holly Cummins is a Senior Principal Software Engineer on the Red Hat Quarkus team. Before joining Red Hat, Holly was a long time IBMer. In her time at IBM, Holly has been a full-stack javascript developer, a WebSphere Liberty build architect, a client-facing consultant, a JVM performance engineer, and an innovation leader. During her time in the IBM Garage, Holly led projects for enormous banks, tiny startups, and everything in between. Holly has used the power of cloud to understand climate risks, count fish, help a blind athlete run ultra-marathons in the desert solo, and invent stories (although not at all the same time). Holly is also a Java Champion, author, and regular keynote speaker. You can follow her on bluesky at &#64;&#64;hollycummins.com or at hollycummins.com.\\r\\n\\r\\n\\r\\nBefore joining IBM, Holly completed a PhD in Quantum Computation.\\r\\n\",\"followers\":586,\"imgSrc\":\"https:\/\/cdn.infoq.com\/statics\_s1\_20260421232814\/images\/profiles\/cRsuGlFgKyGmGfEHvafpMO63CxbrEm22.jpg\"}]');
var topicsInPage = JSON.parse('[{\"name\":\"Architecture & Design\",\"id\":\"6816\",\"url\":\"\/architecture-design\",\"followers\":10219,\"followedByCurrentUser\":false},{\"name\":\"Culture & Methods\",\"id\":\"6817\",\"url\":\"\/culture-methods\",\"followers\":3949,\"followedByCurrentUser\":false},{\"name\":\"Continuous Integration\",\"id\":\"355\",\"url\":\"\/continuous\_integration\",\"followers\":65,\"followedByCurrentUser\":false},{\"name\":\".NET Core\",\"id\":\"15683\",\"url\":\"\/Net-Core\",\"followers\":7882,\"followedByCurrentUser\":false},{\"name\":\"Integration Testing\",\"id\":\"6213\",\"url\":\"\/integration\_testing\",\"followers\":89,\"followedByCurrentUser\":false},{\"name\":\"Agents\",\"id\":\"1317\",\"url\":\"\/Agents\",\"followers\":43,\"followedByCurrentUser\":false},{\"name\":\"Docker\",\"id\":\"18310\",\"url\":\"\/docker\",\"followers\":21,\"followedByCurrentUser\":false},{\"name\":\"Machine Learning\",\"id\":\"5449\",\"url\":\"\/MachineLearning\",\"followers\":14457,\"followedByCurrentUser\":false},{\"name\":\"Microservices\",\"id\":\"15274\",\"url\":\"\/microservices\",\"followers\":22036,\"followedByCurrentUser\":false},{\"name\":\"Testing\",\"id\":\"175\",\"url\":\"\/Testing\",\"followers\":444,\"followedByCurrentUser\":false},{\"name\":\"AI, ML & Data Engineering\",\"id\":\"16690\",\"url\":\"\/ai-ml-data-eng\",\"followers\":5892,\"followedByCurrentUser\":false},{\"name\":\"Regression Testing\",\"id\":\"7314\",\"url\":\"\/Regression\_Testing\",\"followers\":12,\"followedByCurrentUser\":false},{\"name\":\"Java9\",\"id\":\"7097\",\"url\":\"\/Java9\",\"followers\":5421,\"followedByCurrentUser\":false},{\"name\":\"DevOps\",\"id\":\"6043\",\"url\":\"\/Devops\",\"followers\":5063,\"followedByCurrentUser\":false},{\"name\":\"Reactive Programming\",\"id\":\"15453\",\"url\":\"\/reactive-programming\",\"followers\":12258,\"followedByCurrentUser\":false},{\"name\":\"Development\",\"id\":\"6815\",\"url\":\"\/development\",\"followers\":4094,\"followedByCurrentUser\":false}]');
var userContentLikesInPage = [];
var userCommentsLikesInPage = [];
var currentUserId = -855164216;

{
"@context": "http://schema.org",
"@type": "NewsArticle",
"mainEntityOfPage": {
"@type": "WebPage",
"@id": "https://www.infoq.com/news/2026/01/cagent-testing/"
},
"headline": "Docker’s Cagent Brings Deterministic Testing to AI Agents",
"image": ["https://res.infoq.com/news/2026/01/cagent-testing/en/headerimage/generatedHeaderImage-1768594554533.jpg"
],
"datePublished": "2026-01-19T07:00:00+0000",
"dateModified": "2026-01-19T07:00:00+0000",
"author": [
{
"@type": "Person",
"name": "Matt Foster",
"url": "https://www.infoq.com/profile/Matt-Foster/"
}
],
"publisher": {
"@type": "Organization",
"name": "InfoQ",
"logo": {
"@type": "ImageObject",
"url": "https://assets.infoq.com/resources/en/infoQ-logo-big.jpg"
}
},
"description": "Docker is positioning its Cagent runtime as a way to bring deterministic testing back to AI agents, addressing a growing problem for teams building production agentic systems."
}


InfoQConstants.pageType = 'NEWS\_PAGE';

















var communityIds = "4523";
var topicIds = "3653,854,2844,351,2035,172";
VCR.loadAllVcrs(communityIds, topicIds);


document.addEventListener('DOMContentLoaded', function() {
if (!window || !window.infoq) return
infoq.init()
})

window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments) }





[BT](/int/bt/ "bt")

var allCountries = [{"id":3,"name":"Afghanistan"},{"id":244,"name":"Åland"},{"id":6,"name":"Albania"},{"id":61,"name":"Algeria"},{"id":13,"name":"American Samoa"},{"id":1,"name":"Andorra"},{"id":9,"name":"Angola"},{"id":5,"name":"Anguilla"},{"id":11,"name":"Antarctica"},{"id":4,"name":"Antigua and Barbuda"},{"id":12,"name":"Argentina"},{"id":7,"name":"Armenia"},{"id":16,"name":"Aruba"},{"id":15,"name":"Australia"},{"id":14,"name":"Austria"},{"id":17,"name":"Azerbaijan"},{"id":31,"name":"Bahamas"},{"id":24,"name":"Bahrain"},{"id":20,"name":"Bangladesh"},{"id":19,"name":"Barbados"},{"id":35,"name":"Belarus"},{"id":21,"name":"Belgium"},{"id":36,"name":"Belize"},{"id":26,"name":"Benin"},{"id":27,"name":"Bermuda"},{"id":32,"name":"Bhutan"},{"id":29,"name":"Bolivia"},{"id":254,"name":"Bonaire, Sint Eustatius, and Saba"},{"id":18,"name":"Bosnia and Herzegovina"},{"id":34,"name":"Botswana"},{"id":33,"name":"Bouvet Island"},{"id":30,"name":"Brazil"},{"id":104,"name":"British Indian Ocean Territory"},{"id":28,"name":"Brunei Darussalam"},{"id":23,"name":"Bulgaria"},{"id":22,"name":"Burkina Faso"},{"id":25,"name":"Burundi"},{"id":114,"name":"Cambodia"},{"id":46,"name":"Cameroon"},{"id":37,"name":"Canada"},{"id":52,"name":"Cape Verde"},{"id":121,"name":"Cayman Islands"},{"id":40,"name":"Central African Republic"},{"id":207,"name":"Chad"},{"id":45,"name":"Chile"},{"id":47,"name":"China"},{"id":53,"name":"Christmas Island"},{"id":38,"name":"Cocos (Keeling) Islands"},{"id":48,"name":"Colombia"},{"id":116,"name":"Comoros"},{"id":39,"name":"Congo (Democratic Republic)"},{"id":41,"name":"Congo (People\u0027s Republic)"},{"id":44,"name":"Cook Islands"},{"id":49,"name":"Costa Rica"},{"id":43,"name":"Cote D\u0027Ivoire"},{"id":97,"name":"Croatia"},{"id":51,"name":"Cuba"},{"id":253,"name":"Curaçao"},{"id":54,"name":"Cyprus"},{"id":55,"name":"Czech Republic"},{"id":58,"name":"Denmark"},{"id":57,"name":"Djibouti"},{"id":59,"name":"Dominica"},{"id":60,"name":"Dominican Republic"},{"id":213,"name":"East Timor"},{"id":62,"name":"Ecuador"},{"id":64,"name":"Egypt"},{"id":203,"name":"El Salvador"},{"id":87,"name":"Equatorial Guinea"},{"id":66,"name":"Eritrea"},{"id":63,"name":"Estonia"},{"id":68,"name":"Ethiopia"},{"id":72,"name":"Falkland Islands (Malvinas)"},{"id":74,"name":"Faroe Islands"},{"id":71,"name":"Fiji"},{"id":70,"name":"Finland"},{"id":75,"name":"France"},{"id":80,"name":"French Guiana"},{"id":170,"name":"French Polynesia"},{"id":208,"name":"French Southern Territories"},{"id":76,"name":"Gabon"},{"id":84,"name":"Gambia"},{"id":79,"name":"Georgia"},{"id":56,"name":"Germany"},{"id":81,"name":"Ghana"},{"id":82,"name":"Gibraltar"},{"id":88,"name":"Greece"},{"id":83,"name":"Greenland"},{"id":78,"name":"Grenada"},{"id":86,"name":"Guadeloupe"},{"id":91,"name":"Guam"},{"id":90,"name":"Guatemala"},{"id":249,"name":"Guernsey"},{"id":85,"name":"Guinea"},{"id":92,"name":"Guinea-Bissau"},{"id":93,"name":"Guyana"},{"id":98,"name":"Haiti"},{"id":95,"name":"Heard Island and McDonald Islands"},{"id":96,"name":"Honduras"},{"id":94,"name":"Hong Kong"},{"id":99,"name":"Hungary"},{"id":107,"name":"Iceland"},{"id":103,"name":"India"},{"id":100,"name":"Indonesia"},{"id":106,"name":"Iran"},{"id":105,"name":"Iraq"},{"id":101,"name":"Ireland"},{"id":245,"name":"Isle of Man"},{"id":102,"name":"Israel"},{"id":108,"name":"Italy"},{"id":109,"name":"Jamaica"},{"id":111,"name":"Japan"},{"id":250,"name":"Jersey"},{"id":110,"name":"Jordan"},{"id":122,"name":"Kazakhstan"},{"id":112,"name":"Kenya"},{"id":115,"name":"Kiribati"},{"id":243,"name":"Kosovo"},{"id":120,"name":"Kuwait"},{"id":113,"name":"Kyrgyzstan"},{"id":123,"name":"Laos"},{"id":132,"name":"Latvia"},{"id":124,"name":"Lebanon"},{"id":129,"name":"Lesotho"},{"id":128,"name":"Liberia"},{"id":133,"name":"Libya"},{"id":126,"name":"Liechtenstein"},{"id":130,"name":"Lithuania"},{"id":131,"name":"Luxembourg"},{"id":143,"name":"Macau"},{"id":139,"name":"Macedonia"},{"id":137,"name":"Madagascar"},{"id":151,"name":"Malawi"},{"id":153,"name":"Malaysia"},{"id":150,"name":"Maldives"},{"id":140,"name":"Mali"},{"id":148,"name":"Malta"},{"id":138,"name":"Marshall Islands"},{"id":145,"name":"Martinique"},{"id":146,"name":"Mauritania"},{"id":149,"name":"Mauritius"},{"id":238,"name":"Mayotte"},{"id":152,"name":"Mexico"},{"id":73,"name":"Micronesia"},{"id":136,"name":"Moldova"},{"id":135,"name":"Monaco"},{"id":142,"name":"Mongolia"},{"id":246,"name":"Montenegro"},{"id":147,"name":"Montserrat"},{"id":134,"name":"Morocco"},{"id":154,"name":"Mozambique"},{"id":141,"name":"Myanmar"},{"id":155,"name":"Namibia"},{"id":164,"name":"Nauru"},{"id":163,"name":"Nepal"},{"id":161,"name":"Netherlands"},{"id":8,"name":"Netherlands Antilles"},{"id":156,"name":"New Caledonia"},{"id":166,"name":"New Zealand"},{"id":160,"name":"Nicaragua"},{"id":157,"name":"Niger"},{"id":159,"name":"Nigeria"},{"id":165,"name":"Niue"},{"id":158,"name":"Norfolk Island"},{"id":118,"name":"North Korea"},{"id":144,"name":"Northern Mariana Islands"},{"id":162,"name":"Norway"},{"id":167,"name":"Oman"},{"id":173,"name":"Pakistan"},{"id":180,"name":"Palau"},{"id":178,"name":"Palestinian Territory"},{"id":168,"name":"Panama"},{"id":171,"name":"Papua New Guinea"},{"id":181,"name":"Paraguay"},{"id":169,"name":"Peru"},{"id":172,"name":"Philippines"},{"id":176,"name":"Pitcairn"},{"id":174,"name":"Poland"},{"id":179,"name":"Portugal"},{"id":177,"name":"Puerto Rico"},{"id":182,"name":"Qatar"},{"id":183,"name":"Reunion"},{"id":184,"name":"Romania"},{"id":185,"name":"Russian Federation"},{"id":186,"name":"Rwanda"},{"id":193,"name":"Saint Helena"},{"id":117,"name":"Saint Kitts and Nevis"},{"id":125,"name":"Saint Lucia"},{"id":251,"name":"Saint Martin"},{"id":175,"name":"Saint Pierre and Miquelon"},{"id":229,"name":"Saint Vincent and the Grenadines"},{"id":247,"name":"Saint-Barthélemy"},{"id":236,"name":"Samoa"},{"id":198,"name":"San Marino"},{"id":202,"name":"Sao Tome and Principe"},{"id":187,"name":"Saudi Arabia"},{"id":199,"name":"Senegal"},{"id":248,"name":"Serbia"},{"id":189,"name":"Seychelles"},{"id":197,"name":"Sierra Leone"},{"id":192,"name":"Singapore"},{"id":252,"name":"Sint Maarten"},{"id":196,"name":"Slovakia"},{"id":194,"name":"Slovenia"},{"id":188,"name":"Solomon Islands"},{"id":200,"name":"Somalia"},{"id":239,"name":"South Africa"},{"id":89,"name":"South Georgia and the South Sandwich Islands"},{"id":119,"name":"South Korea"},{"id":255,"name":"South Sudan"},{"id":67,"name":"Spain"},{"id":127,"name":"Sri Lanka"},{"id":190,"name":"Sudan"},{"id":201,"name":"Suriname"},{"id":195,"name":"Svalbard and Jan Mayen"},{"id":205,"name":"Swaziland"},{"id":191,"name":"Sweden"},{"id":42,"name":"Switzerland"},{"id":204,"name":"Syria"},{"id":220,"name":"Taiwan"},{"id":211,"name":"Tajikistan"},{"id":221,"name":"Tanzania"},{"id":210,"name":"Thailand"},{"id":209,"name":"Togo"},{"id":212,"name":"Tokelau"},{"id":216,"name":"Tonga"},{"id":218,"name":"Trinidad and Tobago"},{"id":215,"name":"Tunisia"},{"id":217,"name":"Turkey"},{"id":214,"name":"Turkmenistan"},{"id":206,"name":"Turks and Caicos Islands"},{"id":219,"name":"Tuvalu"},{"id":223,"name":"Uganda"},{"id":222,"name":"Ukraine"},{"id":2,"name":"United Arab Emirates"},{"id":77,"name":"United Kingdom"},{"id":224,"name":"United States Minor Outlying Islands"},{"id":226,"name":"Uruguay"},{"id":225,"name":"USA"},{"id":227,"name":"Uzbekistan"},{"id":234,"name":"Vanuatu"},{"id":228,"name":"Vatican City (Holy See)"},{"id":230,"name":"Venezuela"},{"id":233,"name":"Vietnam"},{"id":231,"name":"Virgin Islands (British)"},{"id":232,"name":"Virgin Islands (U.S.)"},{"id":235,"name":"Wallis and Futuna"},{"id":65,"name":"Western Sahara"},{"id":237,"name":"Yemen"},{"id":241,"name":"Zaire"},{"id":240,"name":"Zambia"},{"id":242,"name":"Zimbabwe"}];
var gdprCountriesIds = [196,194,191,184,179,174,161,148,132,131,130,108,101,99,97,88,77,75,70,67,63,58,56,55,54,37,23,21,14];

InfoQ Software Architects' Newsletter
-------------------------------------

A monthly overview of things you need to know as an architect or aspiring architect.

[View an example](https://www.infoq.com/software-architects-newsletter#placeholderPastIssues "https://www.infoq.com/software-architects-newsletter#placeholderPastIssues")

Enter your e-mail address

Select your country

Select a country


I consent to InfoQ.com handling my data as explained in this [Privacy Notice](https://www.infoq.com/privacy-notice "https://www.infoq.com/privacy-notice").

[We protect your privacy.](/privacy-notice/ "/privacy-notice/")

Close

var dataCollectNewsletter = new Newsletter('Enter your e-mail address',
'email-dataCollectnewsletter-infoq', 'dataCollectNewsletterType','dataCollectNewsletterMessage', 'fnt\_d', 'input\_email\_h\_d', 'input-dataCollect-newsletter-country', 'cmpi\_d','popup\_all\_pages');

Toggle Navigation 

Facilitating the Spread of Knowledge and Innovation in Professional Software Development

English edition 

* [English edition](# "#")
* [Chinese edition](https://www.infoq.cn "https://www.infoq.cn")
* [Japanese edition](/jp/ "/jp/")
* [French edition](/fr/ "/fr/")

[Write for InfoQ](/write-for-infoq/ "Write for InfoQ")

Search

[Register](/reginit.action? "/reginit.action?")
[Sign in](/social/keycloakLogin.action?fl=login "/social/keycloakLogin.action?fl=login")

Unlock the full InfoQ experience
--------------------------------

Unlock the full InfoQ experience by logging in! Stay updated with your favorite authors and topics, engage with content, and download exclusive resources.

[Log In](/social/keycloakLogin.action?fl=login "/social/keycloakLogin.action?fl=login")

or

### Don't have an InfoQ account?

[Register](/reginit.action? "/reginit.action?")

* **Stay updated on topics and peers that matter to you**Receive instant alerts on the latest insights and trends.
* **Quickly access free resources for continuous learning**Minibooks, videos with transcripts, and training materials.
* **Save articles and read at anytime**Bookmark articles to read whenever youre ready.

[Logo - Back to homepage](/ "/")

[News](/news/ "/news/")
[Articles](/articles/ "/articles/")
[Presentations](/presentations/ "/presentations/")
[Podcasts](/podcasts/ "/podcasts/")
[Guides](/minibooks/ "/minibooks/")

### Topics

[Development](/development/ "Development")

* [Java](/java/ "Java")
* [Kotlin](/kotlin/ "Kotlin")
* [.Net](/dotnet/ ".Net")
* [C#](/c_sharp/ "C#")
* [Swift](/swift/ "Swift")
* [Go](/golang/ "Go")
* [Rust](/rust/ "Rust")
* [JavaScript](/javascript/ "JavaScript")

### Featured in Development

* #### [From VR to Flat Screens: Bridging the Input and Immersion Gap](/presentations/game-vr-flat-screens "/presentations/game-vr-flat-screens")

  Dany Lepage discusses the architectural journey of porting a hit VR title to seven non-VR platforms. He explains how his team solved the challenges of cross-progression, diverse input paradigms, and maintaining release velocity across Steam, iOS, and PlayStation. Beyond the tech, he shares candid lessons on the "product fit" gap when translating immersive social presence to 2D screens.

[All in development](/development/ "/development/")

[Architecture & Design](/architecture-design/ "Architecture & Design")

* [Architecture](/architecture/ "Architecture")
* [Enterprise Architecture](/enterprise-architecture/ "Enterprise Architecture")
* [Scalability/Performance](/performance-scalability/ "Scalability/Performance")
* [Design](/design/ "Design")
* [Case Studies](/Case_Study/ "Case Studies")
* [Microservices](/microservices/ "Microservices")
* [Service Mesh](/servicemesh/ "Service Mesh")
* [Patterns](/DesignPattern/ "Patterns")
* [Security](/Security/ "Security")

### Featured in Architecture & Design

* #### [Stripe’s Docdb: How Zero-Downtime Data Movement Powers Trillion-Dollar Payment Processing](/presentations/docdb-online-database "/presentations/docdb-online-database")

  Jimmy Morzaria discusses the evolution of Stripe’s database tier to support 5 million QPS with 5.5 nines of reliability. He explains the architecture of DocDB and shares how Stripe leverages a custom zero-downtime data movement platform to perform horizontal sharding, version upgrades, and multi-tenant migrations - all while maintaining the strict consistency required for global commerce.

[All in architecture-design](/architecture-design/ "/architecture-design/")

[AI Infrastructure](/ai-ml-data-eng/ "AI Infrastructure")

* [Big Data](/bigdata/ "Big Data")
* [Machine Learning](/machinelearning/ "Machine Learning")
* [NoSQL](/nosql/ "NoSQL")
* [Database](/database/ "Database")
* [Data Analytics](/data-analytics/ "Data Analytics")
* [Streaming](/streaming/ "Streaming")

### Featured in AI, ML & Data Engineering

* #### [AI-First Software Delivery: Balancing Innovation with Proven Practices](/presentations/ai-first-practices "/presentations/ai-first-practices")

  Wes Reisz discusses the shift toward AI-first software delivery, emphasizing that agentic workflows are not one-size-fits-all. He explains a strategic two-by-two model based on code longevity and automated verification to decide between supervised and unsupervised agents. He shares the RIPER-5 framework - Research, Innovate, Plan, Execute, Review - to amplify engineering discipline.

[All in ai-ml-data-eng](/ai-ml-data-eng/ "/ai-ml-data-eng/")

[Culture & Methods](/culture-methods/ "Culture & Methods")

* [Agile](/agile/ "Agile")
* [Diversity](/diversity/ "Diversity")
* [Leadership](/leadership/ "Leadership")
* [Lean/Kanban](/lean/ "Lean/Kanban")
* [Personal Growth](/personal-growth/ "Personal Growth")
* [Scrum](/scrum/ "Scrum")
* [Sociocracy](/sociocracy/ "Sociocracy")
* [Software Craftmanship](/software_craftsmanship/ "Software Craftmanship")
* [Team Collaboration](/team-collaboration/ "Team Collaboration")
* [Testing](/testing/ "Testing")
* [UX](/ux/ "UX")

### Featured in Culture & Methods

* #### [The Human Scalability Problem: Why Your Teams Don’t Scale Like Your Code](/presentations/human-scalability "/presentations/human-scalability")

  Charlotte de Jong Schouwenburg discusses the "human bottlenecks" of hyper-growth. While systems scale, human cooperation often breaks down due to communication overload and lost context. She shares proven tools for behavioral scalability - including communication architecture and "engineering trust" - to help leaders maintain high-performing, autonomous teams without sacrificing speed or culture.

[All in culture-methods](/culture-methods/ "/culture-methods/")

[DevOps](/devops/ "/devops/")

* [Infrastructure](/infrastructure/ "Infrastructure")
* [Continuous Delivery](/continuous_delivery/ "Continuous Delivery")
* [Automation](/automation/ "Automation")
* [Containers](/containers/ "Containers")
* [Cloud](/cloud-computing/ "Cloud")
* [Observability](/observability/ "Observability")

### Featured in DevOps

* #### [How Netflix Shapes our Fleet for Efficiency and Reliability](/presentations/strategy-workload-hardware "/presentations/strategy-workload-hardware")

  The speakers explain the inherent tension between service efficiency and reliability at Netflix's global scale. They share a mental model for "risk-adjusted net value," moving beyond simple CPU utilization to focus on capacity buffers. They discuss hardware shaping, proactive traffic steering, and reactive levers like "hammers" and prioritized load shedding to protect critical playback.

[All in devops](/devops/ "/devops/")

[Events](https://events.infoq.com/ "Events")

### Helpful links

* [About InfoQ](/about-infoq "About InfoQ")
* [InfoQ Editors](/infoq-editors "InfoQ Editors")
* [Write for InfoQ](/write-for-infoq "Write for InfoQ")
* [About C4Media](https://c4media.com/ "About C4Media")
* [Diversity](https://c4media.com/diversity "Diversity")

### Choose your language

* [En](# "InfoQ English")
* [中文](https://www.infoq.cn "https://www.infoq.cn")
* [日本](/jp/ "/jp/")
* [Fr](/fr/ "/fr/")

[Online InfoQ Architect Certification

Join Luca Mezzalira for this 5-week online cohort. Master socio-technical architecture leadership.

**Register Now.**](https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_onlinecohortaprmayjun26 "https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_onlinecohortaprmayjun26")
[QCon AI Boston

Learn how leading engineering teams run AI in production—reliably, securely, and at scale.

**Early Bird ends April 14.**](https://boston.qcon.ai/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_qaiboston26 "https://boston.qcon.ai/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_qaiboston26")
[QCon San Francisco

Learn what's next in AI and software, from teams already doing it.

**Early Bird ends April 14.**](https://qconsf.com/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_qsf26 "https://qconsf.com/?utm_source=infoq&utm_medium=referral&utm_campaign=homepageheader_qsf26")




[InfoQ Homepage](/ "InfoQ Homepage")
[News](/news "News")
Docker’s Cagent Brings Deterministic Testing to AI Agents

[AI, ML & Data Engineering](/ai-ml-data-eng/ "AI, ML & Data Engineering")

Docker’s Cagent Brings Deterministic Testing to AI Agents
=========================================================

$("#translated\_"+InfoQConstants.userDetectedCountryCode.toLowerCase()).show();

Jan 19, 2026
2
min read

by

* [Matt Foster](/profile/Matt-Foster/ "/profile/Matt-Foster/")

#### Write for InfoQ

**Feed your curiosity.**
Help 550k+ global   
senior developers   
each month stay ahead.[Get in touch](https://www.infoq.com/write-for-infoq/ "https://www.infoq.com/write-for-infoq/")

var playing = false;
function ttsPlaying(content\_url) {
if (loggedIn && !playing) {
gtag('event', 'GA4\_EVENT', {
'category': 'tts',
'action': 'play',
'label': content\_url
});
playing = true;
}
}

Listen to this article -  0:00

Audio ready to play

Your browser does not support the audio element.

0:000:00

Normal1.25x1.5x

Like

* [Reading list](/showbookmarks.action "/showbookmarks.action")

if(loggedIn){
$('#showBookmarks').css('display', 'flex');
}
function performBookmark() {
Bookmarks.toggleBookmark('news', '2026/01/cagent-testing');
}
infoq.event.on('bookmarkRequested', function(e) {
Bookmarks.toggleBookmark('news', '2026/01/cagent-testing');
});
infoq.event.on("loaded", function(){
if(loggedIn){
var href = window.location.href;
if(href.indexOf("#bookmarkPage") != -1){
$('#bookmarkBtn').click();
}
}
});
$(document).ready(function() {
if(Bookmarks.isContentBookmarked == 'true'){
$('#bookmarkBtn').addClass('button\_\_green');
$('#bookmarkBtn').removeClass('button\_\_gray');
}else{
$('#bookmarkBtn').removeClass('button\_\_green');
$('#bookmarkBtn').addClass('button\_\_gray');
}
});

Docker is [positioning its Cagent runtime](https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/ "https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/") as a way to bring deterministic testing to AI agents, addressing a growing problem for teams building production agentic systems.

As agentic systems become more commonplace, engineering teams are discovering the [difficulty arising](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents "https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents") from testing probabilistic outputs. Traditional enterprise systems are built on a simple assumption: the same input produces the same output. Agentic systems break that assumption, and much of today’s ecosystem has adapted by evaluating variability rather than eliminating it.

Over the past two years, a growing class of evaluation frameworks has emerged to make agent behavior observable and measurable. Tools such as [LangSmith](https://www.langchain.com/langsmith "https://www.langchain.com/langsmith"), [Arize Phoenix](https://github.com/Arize-ai/phoenix "https://github.com/Arize-ai/phoenix"), [Promptfoo](https://www.promptfoo.dev "https://www.promptfoo.dev"), [Ragas](https://github.com/explodinggradients/ragas "https://github.com/explodinggradients/ragas"), and [OpenAI Evals](https://github.com/openai/evals "https://github.com/openai/evals") capture execution traces and apply qualitative or LLM-based scoring to judge outcomes.

These tools are essential for monitoring safety and performance, but they introduce a different testing model. Results are rarely binary. Teams increasingly rely on thresholds, retries, and soft failures to cope with evaluator variance. For example, [industry coverage](https://www.domo.com/blog/ai-evaluations-101-testing-llms-agents-and-everything-in-between "https://www.domo.com/blog/ai-evaluations-101-testing-llms-agents-and-everything-in-between") of AI agent testing notes that traditional QA assumptions break down for agents because outputs are probabilistic and evaluation often requires more flexible, probabilistic frameworks rather than strict pass/fail assertions.

In parallel, some teams have rediscovered a more traditional approach, targeting repeatability and determinism in testing using the record and replay pattern. Borrowed from integration testing tools like [vcr.py](https://vcrpy.readthedocs.io/ "https://vcrpy.readthedocs.io/"), the pattern captures real API interactions once and replays them deterministically in future test runs. LangChain [now recommends](https://docs.langchain.com/oss/python/langchain/test "https://docs.langchain.com/oss/python/langchain/test") this technique explicitly for LLM testing, noting that recording HTTP requests and responses can make CI runs fast, cheap, and predictable. In practice, however, this has often remained an external testing concern rather than a first-class part of how agents execute.

[Docker’s Cagent](https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/ "https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/") follows this example. Architecturally, Cagent uses a proxy-and-cassette model. In recording mode, it forwards requests to real providers such as OpenAI or Anthropic, captures the full request and response, normalizes volatile fields like IDs, and stores the interaction in a YAML cassette. In replay mode, Cagent blocks external calls entirely, matches incoming requests against the cassette, and returns the recorded response. If the agent’s execution diverges, for example, a different prompt, tool call, or sequence — the run fails deterministically.

Cagent is still at an [early stage](https://docs.docker.com/ai/cagent/ "https://docs.docker.com/ai/cagent/") of maturity. Docker’s own GitHub repository describes the project as under active development, with breaking changes expected, and most public examples of its use so far come from Docker’s documentation rather than large-scale production deployments.

Cagent does not replace existing evaluation frameworks, but it highlights a different direction in how agent testing is evolving. While much of today’s tooling focuses on assessing outcomes after execution, Cagent shifts attention to making agent behavior reproducible in the first place. As teams experiment with increasingly complex agent workflows, this distinction is becoming more visible. Deterministic replay does not determine whether an agent’s output is correct, but it does make changes in behavior explicit, offering a foundation for testing that looks closer to traditional software engineering.

About the Author
----------------

#### **Matt Foster**

Show moreShow less

ContentRating.readMessages();
ContentRating.readContentItem();


### Rate this Article

Adoption

Style

Author Contacted

if (!InfoQConstants.editorUser || InfoQConstants.editorUser == 'false') {
$('.contentRatingWidget').remove();
} else {
if (InfoQConstants.chiefEditor !== 'undefined' && InfoQConstants.chiefEditor == 'false') {
$('#chiefEditorReview').remove();
}
}

#### This content is in the [AI, ML & Data Engineering](/ai-ml-data-eng/ "/ai-ml-data-eng/") topic

##### Related Topics:

* [AI, ML & Data Engineering](/ai-ml-data-eng/ "/ai-ml-data-eng/")
* [Docker](/docker/ "/docker/")
* [Agents](/Agents/ "/Agents/")
* [Regression Testing](/Regression_Testing/ "/Regression_Testing/")
* [Continuous Integration](/continuous_integration/ "/continuous_integration/")
* [Integration Testing](/integration_testing/ "/integration_testing/")
* [Testing](/Testing/ "/Testing/")

var uriMapping = "news";
var showVcr = "true";
var fillWithVcr = "false";
var sponsorshipsJson = "{&quot;links&quot;:null}";
var sponsoredLinks = $.parseJSON($("<div/>").html(sponsorshipsJson).text()).links;
var numberOfSponsoredVcrIds = sponsoredLinks != null ? sponsoredLinks.length : 0;
var maxItems = 5 - numberOfSponsoredVcrIds;
var displayWidget = false;
var intervalVcrSponsorEditorial = setInterval(function() {
if (window.vcrsLoaded) {
clearInterval(intervalVcrSponsorEditorial);
if(showVcr || fillWithVcr) {
if(fillWithVcr) {
for(var index in window.vcrList) {
if(VCR.isVcrSponsored(sponsoredLinks, window.vcrList[index])) {
VCR.addToExcludedList(window.vcrList[index]);
}
}
}
var vcrs = VCR.getByTopicsAndCommunities(window.vcrList, topicIds, communityIds, maxItems, false, null);
if (vcrs != null && vcrs.length > 0 || (sponsoredLinks != null && sponsoredLinks.length > 0)) {
VCR.addToExcludedList(vcrs);
getCommonElements(vcrs, uriMapping, "BOTTOM");
$('.related\_\_group').find(".rvc\_\_list").css("display", "block");
displayWidget = true;
} else {
$('.related\_\_group').find(".rvc\_\_list").parent("li").remove();
}
}
window.contentVcrFinished = true;
// search for infoq.event.on("contentVcrFinished",... to see how/where it is used
infoq.event.trigger("contentVcrFinished");
}
}, 200);


$(document).ready(function() {
$.ajax({
url: "/api/recommendationlinks.action",
contentType: "application/x-www-form-urlencoded; charset=utf-8",
type: 'POST',
data: {
"primaryTopicAlias": "ai-ml-data-eng",
"topicIds": "3653,854,2844,351,2035,172",
"title": "Docker’s Cagent Brings Deterministic Testing to AI Agents",
"contentPath": "/news/2026/01/cagent-testing",
"language": "en"
},
success: displayRelatedEditorial,
async: false
});
});
function displayRelatedEditorial(data) {
$('.related\_\_editorial h4').text("Related Editorial");
if (data && data.length > 0) {
if(data[0].fromEs) {
//change title and tracking params
var box\_title="AI, ML &amp; Data Engineering";
//replace html entity since it conflicts with style
box\_title=box\_title.replace("&amp;","&");
$('.related\_\_editorial h4').text("Popular in " + box\_title);
}
for (var i = 0; i < data.length; i++) {
if (i === 5) {
break;
}
if (data[i].url.indexOf("/news/2026/01/cagent-testing") !== -1) {
console.log("Removing the current item from list...");
continue;
}
var theLinkURL = data[i].url;
if(!theLinkURL.endsWith("/")) {
theLinkURL = theLinkURL + "/";
}
var link = $('<li><h5 class="rvc\_\_title"><a title="" href="' + theLinkURL + '">' + data[i].title + '</a></h5></li>');
$('.related\_\_editorial ul').append(link);
}
$('.related\_\_editorial').show();
displayWidget = true;
}else{
$('.related\_\_editorial').parent("li").remove();
}
if(displayWidget==true){
$('.related\_\_group').attr("data-cols", $('.related\_\_group').find(">li").length);
$('.related\_\_group').css("display", "flex");
}
}

* #### Related Editorial
* #### Related Sponsors
* #### Popular across InfoQ

  + ##### [Cloudflare Announces Agent Memory, a Managed Persistent Memory Service for AI Agents](/news/2026/04/cloudflare-agent-memory-beta/ "/news/2026/04/cloudflare-agent-memory-beta/")
  + ##### [Vercel Releases Open Agents to Support Background AI Coding Workflows](/news/2026/04/vercel-open-agents/ "/news/2026/04/vercel-open-agents/")
  + ##### [Inside Claude Code Auto Mode: Anthropic’s Autonomous Coding System with Human Approval Gates](/news/2026/05/anthropic-claude-code-auto-mode/ "/news/2026/05/anthropic-claude-code-auto-mode/")
  + ##### [DBmaestro MCP Server Puts Natural Language in Control of Database Pipelines](/news/2026/04/dbmaestro-mcp-server/ "/news/2026/04/dbmaestro-mcp-server/")
  + ##### [Roq: Leveraging Quarkus to Build Static Sites at the Speed of Go](/podcasts/leveraging-quarkus-build-static-sites/ "/podcasts/leveraging-quarkus-build-static-sites/")
  + ##### [Cloudflare Builds High-Performance Infrastructure for Running LLMs](/news/2026/05/cloudflare-llm-infrastructure/ "/news/2026/05/cloudflare-llm-infrastructure/")

window.finishedRightbarVcr = false;
var \_gaq = \_gaq || [];
var recomJson ="[{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1778061600000,&quot;url&quot;:&quot;/news/2026/05/google-8th-tpu-generation&quot;,&quot;title&quot;:&quot;Google New TPU Generation is Specifically Designed for Agents and SOTA Model Training&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/05/google-8th-tpu-generation&quot;,&quot;score&quot;:100002,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777975680000,&quot;url&quot;:&quot;/news/2026/05/mistral-agents-lechat&quot;,&quot;title&quot;:&quot;Mistral Adds Remote Agents and Work Mode to Le Chat&quot;,&quot;authorsList&quot;:[&quot;Daniel Dominguez&quot;],&quot;itemPath&quot;:&quot;/news/2026/05/mistral-agents-lechat&quot;,&quot;score&quot;:98863,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777636800000,&quot;url&quot;:&quot;/news/2026/05/meta-ai-agents-hyperscale&quot;,&quot;title&quot;:&quot;Meta Deploys Unified AI Agents to Automate Performance Optimization at Hyperscale&quot;,&quot;authorsList&quot;:[&quot;Craig Risi&quot;],&quot;itemPath&quot;:&quot;/news/2026/05/meta-ai-agents-hyperscale&quot;,&quot;score&quot;:94564,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777543800000,&quot;url&quot;:&quot;/news/2026/04/cloudflare-agent-memory-beta&quot;,&quot;title&quot;:&quot;Cloudflare Announces Agent Memory, a Managed Persistent Memory Service for AI Agents&quot;,&quot;authorsList&quot;:[&quot;Steef-Jan Wiggers&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/cloudflare-agent-memory-beta&quot;,&quot;score&quot;:93550,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777540800000,&quot;url&quot;:&quot;/news/2026/04/vercel-open-agents&quot;,&quot;title&quot;:&quot;Vercel Releases Open Agents to Support Background AI Coding Workflows&quot;,&quot;authorsList&quot;:[&quot;Robert Krzaczyński&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/vercel-open-agents&quot;,&quot;score&quot;:93550,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777398900000,&quot;url&quot;:&quot;/news/2026/04/agents-cli-google-cloud&quot;,&quot;title&quot;:&quot;Google Cloud Introduces Agents CLI to Streamline AI Agent Development Lifecycle&quot;,&quot;authorsList&quot;:[&quot;Robert Krzaczyński&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/agents-cli-google-cloud&quot;,&quot;score&quot;:92558,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776852000000,&quot;url&quot;:&quot;/news/2026/04/cloudflare-sandboxes-ga&quot;,&quot;title&quot;:&quot;Cloudflare Sandboxes Reach General Availability, Giving AI Agents Persistent Isolated Environments&quot;,&quot;authorsList&quot;:[&quot;Steef-Jan Wiggers&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/cloudflare-sandboxes-ga&quot;,&quot;score&quot;:86223,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776782160000,&quot;url&quot;:&quot;/news/2026/04/anthropic-managed-agents&quot;,&quot;title&quot;:&quot;Anthropic Introduces Managed Agents to Simplify AI Agent Deployment&quot;,&quot;authorsList&quot;:[&quot;Leela Kumili&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/anthropic-managed-agents&quot;,&quot;score&quot;:85398,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776738840000,&quot;url&quot;:&quot;/news/2026/04/cloudflare-project-think&quot;,&quot;title&quot;:&quot;Cloudflare Introduces Project Think: a Durable Runtime for AI Agents&quot;,&quot;authorsList&quot;:[&quot;Patrick Farry&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/cloudflare-project-think&quot;,&quot;score&quot;:85398,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776697140000,&quot;url&quot;:&quot;/news/2026/04/linkedin-cognitive-memory-agent&quot;,&quot;title&quot;:&quot;Designing Memory for AI Agents: inside Linkedin’s Cognitive Memory Agent&quot;,&quot;authorsList&quot;:[&quot;Leela Kumili&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/linkedin-cognitive-memory-agent&quot;,&quot;score&quot;:84593,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776687960000,&quot;url&quot;:&quot;/news/2026/04/subagents-gemini-cli&quot;,&quot;title&quot;:&quot;Subagents in Gemini CLI Enable Task Delegation and Parallel Agent Workflows&quot;,&quot;authorsList&quot;:[&quot;Robert Krzaczyński&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/subagents-gemini-cli&quot;,&quot;score&quot;:84593,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776437340000,&quot;url&quot;:&quot;/news/2026/04/meta-jit-testing-ai-detection&quot;,&quot;title&quot;:&quot;Meta Reports 4x Higher Bug Detection with Just-in-Time Testing&quot;,&quot;authorsList&quot;:[&quot;Leela Kumili&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/meta-jit-testing-ai-detection&quot;,&quot;score&quot;:82286,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776349020000,&quot;url&quot;:&quot;/news/2026/04/cloudflare-code-mode-mcp-server&quot;,&quot;title&quot;:&quot;Cloudflare Launches Code Mode MCP Server to Optimize Token Usage for AI Agents&quot;,&quot;authorsList&quot;:[&quot;Leela Kumili&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/cloudflare-code-mode-mcp-server&quot;,&quot;score&quot;:81549,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/securing-autonomous-ai-agents-kubernetes/en/smallimage/securing-autonomous-ai-agents-kubernetes-thumbnail-1777378848477.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1777626000000,&quot;url&quot;:&quot;/articles/securing-autonomous-ai-agents-kubernetes&quot;,&quot;title&quot;:&quot;Securing Autonomous AI Agents on Kubernetes: Trust Boundaries, Secrets, and Observability for a New Category of Cloud Workload&quot;,&quot;authorsList&quot;:[&quot;Nik Kale&quot;],&quot;itemPath&quot;:&quot;/articles/securing-autonomous-ai-agents-kubernetes&quot;,&quot;score&quot;:78501,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1775723400000,&quot;url&quot;:&quot;/news/2026/04/colab-mcp-server&quot;,&quot;title&quot;:&quot;Google Brings MCP Support to Colab, Enabling Cloud Execution for AI Agents&quot;,&quot;authorsList&quot;:[&quot;Robert Krzaczyński&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/colab-mcp-server&quot;,&quot;score&quot;:76853,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/enterprise-grade-observability-extension-docker/en/smallimage/enterprise-grade-observability-extension-docker-thumbnail-1775560652994.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1776157200000,&quot;url&quot;:&quot;/articles/enterprise-grade-observability-extension-docker&quot;,&quot;title&quot;:&quot;Beyond One-Click: Designing an Enterprise-Grade Observability Extension for Docker&quot;,&quot;authorsList&quot;:[&quot;Pragya Keshap&quot;],&quot;itemPath&quot;:&quot;/articles/enterprise-grade-observability-extension-docker&quot;,&quot;score&quot;:73546,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/coding-agents/en/smallimage/Adrian-Cockcroft-thumbnail-1774443559104.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1775121540000,&quot;url&quot;:&quot;/presentations/coding-agents&quot;,&quot;title&quot;:&quot;Directing a Swarm of Agents for Fun and Profit&quot;,&quot;authorsList&quot;:[&quot;Adrian Cockcroft&quot;],&quot;itemPath&quot;:&quot;/presentations/coding-agents&quot;,&quot;score&quot;:69801,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/evaluating-ai-agents-lessons-learned/en/smallimage/evaluating-ai-agents-lessons-learned-thumbnail-1773307288872.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1773658800000,&quot;url&quot;:&quot;/articles/evaluating-ai-agents-lessons-learned&quot;,&quot;title&quot;:&quot;Evaluating AI Agents in Practice: Benchmarks, Frameworks, and Lessons Learned&quot;,&quot;authorsList&quot;:[&quot;Amit Kumar Padhy&quot;],&quot;itemPath&quot;:&quot;/articles/evaluating-ai-agents-lessons-learned&quot;,&quot;score&quot;:64701,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/devops-modernization-ai-agents/en/smallimage/infoq-live-thumbnail-1771422477828.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1771506480000,&quot;url&quot;:&quot;/presentations/devops-modernization-ai-agents&quot;,&quot;title&quot;:&quot;DevOps Modernization: AI Agents, Intelligent Observability and Automation&quot;,&quot;authorsList&quot;:[&quot;Olalekan Elesin&quot;,&quot;Patrick Debois&quot;,&quot;Mallika Rao&quot;,&quot;Martin Reynolds&quot;,&quot;Renato Losio&quot;],&quot;itemPath&quot;:&quot;/presentations/devops-modernization-ai-agents&quot;,&quot;score&quot;:57201,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/one-testing-environment/en/smallimage/po-linn-chia-thumbnail-1768379281165.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1768828860000,&quot;url&quot;:&quot;/presentations/one-testing-environment&quot;,&quot;title&quot;:&quot;No QA Environment? No Problem: How Classpass Enables Testing on a Single Environment in ECS&quot;,&quot;authorsList&quot;:[&quot;Po Linn Chia&quot;],&quot;itemPath&quot;:&quot;/presentations/one-testing-environment&quot;,&quot;score&quot;:50001,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777888800000,&quot;url&quot;:&quot;/news/2026/05/doordash-copilot-swift-testing&quot;,&quot;title&quot;:&quot;DoorDash Used Copilot to Convert Its XCTest-Based iOS Test Suite to Swift Testing&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/05/doordash-copilot-swift-testing&quot;,&quot;score&quot;:195,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777449600000,&quot;url&quot;:&quot;/news/2026/04/github-stacked-prs&quot;,&quot;title&quot;:&quot;GitHub Targets Large Merge Problem with Stacked PRs&quot;,&quot;authorsList&quot;:[&quot;Matt Saunders&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/github-stacked-prs&quot;,&quot;score&quot;:185,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777276800000,&quot;url&quot;:&quot;/news/2026/04/gitlab-flatrate-view-ai-access&quot;,&quot;title&quot;:&quot;GitLab Adds Flat-Rate Code Reviews, Free-Tier AI Access, and Spending Caps&quot;,&quot;authorsList&quot;:[&quot;Matt Saunders&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/gitlab-flatrate-view-ai-access&quot;,&quot;score&quot;:181,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776867240000,&quot;url&quot;:&quot;/news/2026/04/dropbox-reduces-git-optimization&quot;,&quot;title&quot;:&quot;Dropbox Collaborates with GitHub to Reduce Monorepo Size from 87GB to 20GB&quot;,&quot;authorsList&quot;:[&quot;Leela Kumili&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/dropbox-reduces-git-optimization&quot;,&quot;score&quot;:172,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/alternative-reduce-test-suite-size/en/smallimage/alternative-reduce-test-suite-size-thumbnail-1774943323622.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1775473200000,&quot;url&quot;:&quot;/articles/alternative-reduce-test-suite-size&quot;,&quot;title&quot;:&quot;A Better Alternative to Reducing CI Regression Test Suite Sizes&quot;,&quot;authorsList&quot;:[&quot;James Bornefelt Westfall&quot;],&quot;itemPath&quot;:&quot;/articles/alternative-reduce-test-suite-size&quot;,&quot;score&quot;:15,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777626180000,&quot;url&quot;:&quot;/news/2026/05/vitest-4-1-ai-agents&quot;,&quot;title&quot;:&quot;Vitest 4.1: Test Tags, Native Node.js Execution and AI Agent Reporter&quot;,&quot;authorsList&quot;:[&quot;Daniel Curtis&quot;],&quot;itemPath&quot;:&quot;/news/2026/05/vitest-4-1-ai-agents&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777464000000,&quot;url&quot;:&quot;/news/2026/04/sauce-labs-ai-test-creation&quot;,&quot;title&quot;:&quot;Sauce Labs Launches AI Agent to Automate Test Creation and Close the DevOps “Velocity Gap”&quot;,&quot;authorsList&quot;:[&quot;Craig Risi&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/sauce-labs-ai-test-creation&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777410000000,&quot;url&quot;:&quot;/news/2026/04/slack-agent-context-management&quot;,&quot;title&quot;:&quot;How Slack Manages Context in Long-Running Multi-agent Systems&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/slack-agent-context-management&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1777281420000,&quot;url&quot;:&quot;/news/2026/04/junior-developer-pipeline-crisis&quot;,&quot;title&quot;:&quot;Microsoft's Russinovich and Hanselman Warn AI Is Hollowing out the Junior Developer Pipeline&quot;,&quot;authorsList&quot;:[&quot;Steef-Jan Wiggers&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/junior-developer-pipeline-crisis&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776679200000,&quot;url&quot;:&quot;/news/2026/04/google-adk-1-0-new-architecture&quot;,&quot;title&quot;:&quot;Google ADK for Java 1.0 Introduces New App and Plugin Architecture, External Tools Support, and More&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/google-adk-1-0-new-architecture&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776511860000,&quot;url&quot;:&quot;/news/2026/04/aws-devops-agent-ga&quot;,&quot;title&quot;:&quot;AWS Announces General Availability of DevOps Agent for Automated Incident Investigation&quot;,&quot;authorsList&quot;:[&quot;Renato Losio&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/aws-devops-agent-ga&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776408840000,&quot;url&quot;:&quot;/news/2026/04/aws-agent-registry-preview&quot;,&quot;title&quot;:&quot;AWS Launches Agent Registry in Preview to Govern AI Agent Sprawl across Enterprises&quot;,&quot;authorsList&quot;:[&quot;Steef-Jan Wiggers&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/aws-agent-registry-preview&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1776114000000,&quot;url&quot;:&quot;/news/2026/04/gemma-4-android-ai-inference&quot;,&quot;title&quot;:&quot;Google Released Gemma 4 with a Focus on Local-First, On-Device AI Inference&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/gemma-4-android-ai-inference&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/ai-coding-agents-copilot/en/smallimage/thumbnail-1775046920020.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1775736000000,&quot;url&quot;:&quot;/presentations/ai-coding-agents-copilot&quot;,&quot;title&quot;:&quot;Choosing Your AI Copilot: Maximizing Developer Productivity&quot;,&quot;authorsList&quot;:[&quot;Sepehr Khosravi&quot;],&quot;itemPath&quot;:&quot;/presentations/ai-coding-agents-copilot&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/ai-coding-assistants/en/smallimage/birgitta-bockeler-thumbnail-1775631877853.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1775637240000,&quot;url&quot;:&quot;/presentations/ai-coding-assistants&quot;,&quot;title&quot;:&quot;State of Play: AI Coding Assistants&quot;,&quot;authorsList&quot;:[&quot;Birgitta B&#xF6;ckeler&quot;],&quot;itemPath&quot;:&quot;/presentations/ai-coding-assistants&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:null,&quot;topicsIds&quot;:null,&quot;date&quot;:1775548800000,&quot;url&quot;:&quot;/news/2026/04/google-agent-testbed-scion&quot;,&quot;title&quot;:&quot;Google Open Sources Experimental Multi-Agent Orchestration Testbed Scion&quot;,&quot;authorsList&quot;:[&quot;Sergio De Simone&quot;],&quot;itemPath&quot;:&quot;/news/2026/04/google-agent-testbed-scion&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;news&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/presentations/image-processing-automated-tests/en/smallimage/stefan-dirnstorfer-thumbnail-1773150417759.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1773669720000,&quot;url&quot;:&quot;/presentations/image-processing-automated-tests&quot;,&quot;title&quot;:&quot;Image Processing for Automated Tests&quot;,&quot;authorsList&quot;:[&quot;Stefan Dirnstorfer&quot;],&quot;itemPath&quot;:&quot;/presentations/image-processing-automated-tests&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;presentations&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/building-ai-agent-gateway-mcp/en/smallimage/building-ai-agent-gateway-mcp-thumbnail-1771417896950.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1771844400000,&quot;url&quot;:&quot;/articles/building-ai-agent-gateway-mcp&quot;,&quot;title&quot;:&quot;Building a Least-Privilege AI Agent Gateway for Infrastructure Automation with MCP, OPA, and Ephemeral Runners&quot;,&quot;authorsList&quot;:[&quot;Nabin Debnath&quot;],&quot;itemPath&quot;:&quot;/articles/building-ai-agent-gateway-mcp&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/architecting-agentic-mlops-a2a-mcp/en/smallimage/architecting-agentic-mlops-a2a-mcp-1770303550343.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1771232400000,&quot;url&quot;:&quot;/articles/architecting-agentic-mlops-a2a-mcp&quot;,&quot;title&quot;:&quot;Architecting Agentic MLOps: a Layered Protocol Strategy with A2A and MCP&quot;,&quot;authorsList&quot;:[&quot;Shashank Kapoor&quot;,&quot;Sanjay Surendranath Girija&quot;,&quot;Lakshit Arora&quot;],&quot;itemPath&quot;:&quot;/articles/architecting-agentic-mlops-a2a-mcp&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;articles&quot;},{&quot;imageStoragePath&quot;:&quot;https://imgopt.infoq.com/fit-in/50x50/filters:quality(80)/articles/prompts-to-production-playbook-for-agentic-development/en/smallimage/prompts-to-production-playbook-thumbnail-1770374539263.jpg&quot;,&quot;topicsIds&quot;:null,&quot;date&quot;:1770800400000,&quot;url&quot;:&quot;/articles/prompts-to-production-playbook-for-agentic-development&quot;,&quot;title&quot;:&quot;From Prompts to Production: a Playbook for Agentic Development&quot;,&quot;authorsList&quot;:[&quot;Abhishek Goswami&quot;],&quot;itemPath&quot;:&quot;/articles/prompts-to-production-playbook-for-agentic-development&quot;,&quot;score&quot;:1,&quot;contentType&quot;:&quot;articles&quot;}]";
var whitepaperVcrsJson = null;
var topicSponsorshipJson = "";
var vcrOptionalListJson = null;
/\* do not delete these two, as they are used further in the code \*/
var contentDatetimeFormat='MMM dd, yyyy';
var contentUriMapping="news";
JSi18n.relatedRightbar\_relatedContent='Related Content';
JSi18n.relatedRightbar\_sponsoredContent='Related Sponsors';
JSi18n.relatedRightbar\_sponsoredBy='Sponsored by';
var topicIds = "3653,854,2844,351,2035,172";
var communityIds = "4523";
var company = "";
// this event is fired by frontend once all the necessary things have been done(mobile display, moving vcr boxes around when needed...)
var canStartTrackingCustomRightbar = false;
infoq.event.on('loaded', function(e) {
canStartTrackingCustomRightbar = true;
});
var intervalRightbar = setInterval(function() {
if (window.vcrsLoaded) {
clearInterval(intervalRightbar);
if(company != null && company != "") {
whitepaperVcrsJson = VCR.filterByCompany(company, window.vcrList);
} else {
whitepaperVcrsJson = VCR.getByTopicsAndCommunities(window.vcrList, topicIds, communityIds, 5, false, null);
}
vcrOptionalListJson = VCR.getByTopicsAndCommunities(window.vcrList, topicIds, communityIds, 10, true, null);
VCR.displayCustomRightbar(recomJson, whitepaperVcrsJson, topicSponsorshipJson);
VCR.displayCustomRightbarOptionalVcrWidget(vcrOptionalListJson);
window.finishedRightbarVcr = true;
}
}, 200);
// these two events can happen one before another async(no precedence any can be first or second). Make sure tracking starts when both happened
var intervalTrackingRightbar = setInterval(function() {
if(canStartTrackingCustomRightbar && window.finishedRightbarVcr){
clearInterval(intervalTrackingRightbar);
VCR.doTrackingCustomRightbar();
}
}, 200);


### Related Content

### **The InfoQ** Newsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.
[View an example](https://assets.infoq.com/newsletter/regular/en/newsletter_sample/newsletter_sample.html "https://assets.infoq.com/newsletter/regular/en/newsletter_sample/newsletter_sample.html")

Enter your e-mail address

Select your country

Select a country


I consent to InfoQ.com handling my data as explained in this [Privacy Notice](https://www.infoq.com/privacy-notice "https://www.infoq.com/privacy-notice").

[We protect your privacy.](/privacy-notice/ "/privacy-notice/")

var floatingNewsletterForm = new Newsletter('Enter your e-mail address',
'email-newsletter-infoq-guide', 'floatingNewsletterType','floatingNewsletterEmailMessage', 'floating\_fnt', 'input\_floating\_email\_h', 'input-floating-newsletter-country','cmpi\_f','floating\_box');

// global vars that can be used for this page, us ethis section to add more.
var contentTitle = "Docker’s Cagent Brings Deterministic Testing to AI Agents",
contentPath = "/news/2026/01/cagent-testing",
contentUUID = "a2799ffb-9ccb-4cfd-b358-f5f51a3722dd",
authorUserCSVIds = "126669407";



* [Development](/development/ "/development/")

  + ##### [Attacker Bought 30 WordPress Plugins on Flippa and Backdoored All of Them](/news/2026/05/wordpress-plugins-supply-chain/ "Attacker Bought 30 WordPress Plugins on Flippa and Backdoored All of Them")
  + ##### [Cloudflare Introduces Flagship: an Edge-Native Feature Flag Service Built on OpenFeature](/news/2026/05/cloudflare-flagship-openfeature/ "Cloudflare Introduces Flagship: an Edge-Native Feature Flag Service Built on OpenFeature")
  + ##### [QCon San Francisco 2026: 12 Tracks Announced](/news/2026/04/qconsf-2026-tracks-announced/ "QCon San Francisco 2026: 12 Tracks Announced")
* [Architecture & Design](/architecture-design/ "/architecture-design/")

  + ##### [LinkedIn Consolidates Hiring Data Pipelines to Power AI Driven Talent Systems](/news/2026/05/linkedin-unified-hiring-platform/ "LinkedIn Consolidates Hiring Data Pipelines to Power AI Driven Talent Systems")
  + ##### [Inside Claude Code Auto Mode: Anthropic’s Autonomous Coding System with Human Approval Gates](/news/2026/05/anthropic-claude-code-auto-mode/ "Inside Claude Code Auto Mode: Anthropic&rsquo;s Autonomous Coding System with Human Approval Gates")
  + ##### [Cloudflare Processes 10M+ Daily Insights with New Security Overview Dashboard](/news/2026/05/cloudflare-security-dashboard/ "Cloudflare Processes 10M+ Daily Insights with New Security Overview Dashboard")
* [Culture & Methods](/culture-methods/ "/culture-methods/")

  + ##### [The Human Scalability Problem: Why Your Teams Don’t Scale Like Your Code](/presentations/human-scalability/ "The Human Scalability Problem: Why Your Teams Don&rsquo;t Scale Like Your Code")
  + ##### [Driving and Measuring the Impact of Platform Engineering](/news/2026/04/measure-platform-engineering/ "Driving and Measuring the Impact of Platform Engineering")
  + ##### [How Observability and Telemetry Can Enhance the Practice of Software Engineering](/news/2026/04/observability-telemetry/ "How Observability and Telemetry Can Enhance the Practice of Software Engineering")
* [AI, ML & Data Engineering](/ai-ml-data-eng/ "/ai-ml-data-eng/")

  + ##### [AI-First Software Delivery: Balancing Innovation with Proven Practices](/presentations/ai-first-practices/ "AI-First Software Delivery: Balancing Innovation with Proven Practices")
  + ##### [Google New TPU Generation is Specifically Designed for Agents and SOTA Model Training](/news/2026/05/google-8th-tpu-generation/ "Google New TPU Generation is Specifically Designed for Agents and SOTA Model Training")
  + ##### [Mistral Adds Remote Agents and Work Mode to Le Chat](/news/2026/05/mistral-agents-lechat/ "Mistral Adds Remote Agents and Work Mode to Le Chat")
* [DevOps](/devops/ "/devops/")

  + ##### [Grafana's Kubernetes Monitoring Helm Chart v4 Brings Multiple Fixes](/news/2026/05/kubernetes-monitoring-helm/ "Grafana's Kubernetes Monitoring Helm Chart v4 Brings Multiple Fixes")
  + ##### [How Netflix Shapes our Fleet for Efficiency and Reliability](/presentations/strategy-workload-hardware/ "How Netflix Shapes our Fleet for Efficiency and Reliability")
  + ##### [GitHub Enhances CodeQL with Declarative Security Modeling for Faster, More Flexible Analysis](/news/2026/05/github-codeql-security-modeling/ "GitHub Enhances CodeQL with Declarative Security Modeling for Faster, More Flexible Analysis")

**The InfoQ** Newsletter
------------------------

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.
[View an example](https://assets.infoq.com/newsletter/regular/en/newsletter_sample/newsletter_sample.html "https://assets.infoq.com/newsletter/regular/en/newsletter_sample/newsletter_sample.html")

* Get a quick overview of content published on a variety of innovator and early adopter technologies
* Learn what you don’t know that you don’t know
* Stay up to date with the latest information from the topics you are interested in

Enter your e-mail address

Select your country

Select a country


I consent to InfoQ.com handling my data as explained in this [Privacy Notice](https://www.infoq.com/privacy-notice "https://www.infoq.com/privacy-notice").

[We protect your privacy.](/privacy-notice/ "/privacy-notice/")

var footerNewsletter = new Newsletter('Enter your e-mail address',
'email-newsletter-infoq', 'footerNewsletterType','footerNewsletterMessage', 'fnt', 'input\_email\_h', 'input-simple-newsletter-country', 'cmpi','footer\_except\_homepage');

[**May 7 | June 10, 2026 | Online**  
  
Architecture decisions are hard to validate while shipping.
  
Join a **5-week online cohort** for **senior engineers, architects, and team leads** to pressure-test real decisions, apply practical frameworks, and work through challenges with a confidential peer group.
  
  
Facilitated by Luca Mezzalira, Principal Architect at AWS, this cohort helps you:

* Pressure-test real decisions.
* Apply frameworks to real problems.
* Publish on InfoQ.com and earn your certification.

 **RESERVE YOUR PLACE**](https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=largefooterad_onlinecohortaprmayjun26 "https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=largefooterad_onlinecohortaprmayjun26")

[Home](/ "Home")
[Create account](/reginit.action "Create account")
Log In
[QCon Conferences](http://qconferences.com/ "QCon Conferences")
[Events](https://events.infoq.com/ "https://events.infoq.com/")
[Write for InfoQ](/write-for-infoq/ "Write for InfoQ")
[InfoQ Editors](/infoq-editors/ "InfoQ Editors")
[About InfoQ](/about-infoq/ "About InfoQ")
[About C4Media](https://c4media.com/ "About C4Media")
[Media Kit](https://get.infoq.com/infoq-mediakit/ "Media Kit")
[InfoQ Developer Marketing Blog](https://devmarketing.c4media.com/?utm_source=infoq "InfoQ Developer Marketing Blog")
[Diversity](https://c4media.com/diversity "Diversity")

#### Events

* ##### [Online InfoQ Architect Certification](https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_onlinecohortaprmayjun26 "https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_onlinecohortaprmayjun26")

  May 7, 2026
* ##### [QCon AI Boston](https://boston.qcon.ai/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_qaiboston26 "https://boston.qcon.ai/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_qaiboston26")

  June 1-2, 2026
* ##### [Online InfoQ Architect Certification](https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_onlinecohortaprmayjun26 "https://certification.qconferences.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_onlinecohortaprmayjun26")

  June 10, 2026
* ##### [QCon San Francisco](https://qconsf.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_qsf26 "https://qconsf.com/?utm_source=infoq&utm_medium=referral&utm_campaign=footer_qsf26")

  November 16-20, 2026

#### Follow us on

[Youtube232K Followers](https://www.youtube.com/infoq "https://www.youtube.com/infoq")
[Linkedin26K Followers](http://www.linkedin.com/company/infoq "http://www.linkedin.com/company/infoq")
[InstagramNew](https://www.instagram.com/infoqdotcom/ "https://www.instagram.com/infoqdotcom/")
[RSS19K Readers](# "#")
[X57.1k Followers](http://twitter.com/infoq "http://twitter.com/infoq")
[Facebook21K Likes](https://www.facebook.com/InfoQ-75911537320 "https://www.facebook.com/InfoQ-75911537320")
[BlueskyNew](https://bsky.app/profile/infoq.com "https://bsky.app/profile/infoq.com")

#### Stay in the know

[The InfoQ Podcast](/podcasts/ "/podcasts/")
[Engineering Culture Podcast](/podcasts/#engineering_culture "/podcasts/#engineering_culture")
[The Software Architects' Newsletter](/software-architects-newsletter/ "/software-architects-newsletter/")

General Feedback
[feedback@infoq.com](mailto:feedback@infoq.com "mailto:feedback@infoq.com")

Advertising
[sales@infoq.com](mailto:sales@infoq.com "mailto:sales@infoq.com")

Editorial
[editors@infoq.com](mailto:editors@infoq.com "mailto:editors@infoq.com")

Marketing
[marketing@infoq.com](mailto:marketing@infoq.com "mailto:marketing@infoq.com")

InfoQ.com and all content copyright © 2006-2026 C4Media Inc.

[BT](/int/bt/ "bt")

$.when(humanDetectionAsync()).then(
function(status) {
$.getScript("/scripts/\_\_hd.ifq?hdt=AHhF9WKxDpki2gpt&ha=" + status);
}
);

var pageFullyLoaded = false;
// this event is fired by frontend once all the necessary things have been done(mobile display, moving vcr boxes around when needed...)
infoq.event.on('loaded', function(e) {
pageFullyLoaded = true;
});
infoq.event.on('pageWidthChanged', function(e) {
// re-execute tracking vcr impressions when this event happens (it only happens when elements are added/removed from page)
// doTrackVcrImpressions takes into account the data-trk-impr="true" if =false the element was already tracked.
// this is needed when switching from mobile to desktop or when layout on mobile changes and desktop version is displayed. New elements become visible.
Tracker.safeExec(Tracker.doTrackVcrImpressions);
// these 2 need to be called also because we might be on a content page. In case we are not nothing happens
VCR.doTrackingCustomRightbar();
VCR.doTrackingCustomRightbarForPresentations()
});
//check to see if error page
if(window.device !== undefined) {
var intervalImpressions = setInterval(function() {
var shouldTrack = false;
// no vcr widgets on index pages
if(window.isIndexPage) {
if(window.sponsoredPodcastDone === undefined || window.sponsoredPodcastDone) {
shouldTrack = true;
}
} else
//on homepage, bottom widget + 2 native widgets
if(InfoQConstants.pageType == "HOMEPAGE" && window.finishedVcrOptional1 && window.finishedRelatedVcr && (window.finishedVcrOptional2 === undefined || window.finishedVcrOptional2)) {
shouldTrack = true;
} else
// rightbar widgets + native widgets + content vcr widgets
if((InfoQConstants.pageType == "NEWS\_PAGE" || InfoQConstants.pageType == "ARTICLE\_PAGE")
&& ((window.finishedRightbarVcr || window.finishedRightbarVcr === undefined) && window.contentVcrFinished)) {
shouldTrack = true;
} else if ((InfoQConstants.pageType == "PRESENTATION\_PAGE")
&& (window.contentVcrFinished || window.contentVcrFinished === undefined)
&& (window.finishedRightbarVcr || window.finishedRightbarVcr === undefined)
) {
shouldTrack = true;
} else
// native widgets + content widgets
if(window.contentVcrFinished && (window.finishedVcrOptional1 || window.finishedVcrOptional1 === undefined)
&& (window.finishedVcrOptional2 || window.finishedVcrOptional2 === undefined)) {
shouldTrack = true;
}
// we start tracking only after the page is fully loaded, frontend signals that they finished everything related to page display.
if(shouldTrack && pageFullyLoaded) {
clearInterval(intervalImpressions);
Tracker.safeExec(Tracker.doTrackVcrImpressions);
// start tracking viewable impressions also only after everything is ready
function callbackRouter(entries, observer) {
var targets = new Array();
entries.forEach(function (entry) {
var target = entry.target;
if (target.dataset.trkView === 'false') return;
if (entry.intersectionRatio > 0) {
target.dataset.trkView = false;
targets.push(target);
}
});
Tracker.doTrackViewableImpressions(targets);
}
var elementsForTrackingViewableImpressions = document.querySelectorAll('[data-trk-view="true"]')
var observer = new IntersectionObserver(callbackRouter, { threshold: 0.3 });
elementsForTrackingViewableImpressions.forEach(observer.observe.bind(observer));
}
}, 500);
}
$(document).ready(function () {
// desktop notifications widget
Tracker.encodeNotificationLinks($(".f\_notificationWidget"));
// mobile notifications widget
Tracker.encodeNotificationLinks($(".h\_notifications"));
// desktop notifications page
Tracker.encodeNotificationLinks($(".notification-page"));
// mobile notifications page
Tracker.encodeNotificationLinks($(".notifications\_page"));
});

if(window.location.hash){
var hash = window.location.hash.substring(1);
if(hash == 'subscribe'){
$('html,body').animate({scrollTop: $('.ftxt3 > .newsletter').offset().top}, 'slow');
}
}

var newsletterSubscriptionURL ='/newsletter/subscribe.action';
DynamicLinks.updateRssLinks('3405691582');
ContentSummary.setSelectedTab('en');
//when user enters the main content area show default topics in the topics bar
$("#content-wrapper").mouseenter(function() {
showDefaultTopics();
});
Bookmarks.contentTitle = "Docker’s Cagent Brings Deterministic Testing to AI Agents";
Bookmarks.apiUrl = '/widgets/bookmark.action';
Bookmarks.isContentBookmarked = "false";

var $buoop = {vs:{i:6,f:1,o:10.1,s:1}}
$buoop.ol = window.onload;
$(document).ready(function() {
try {if ($buoop.ol) $buoop.ol();}catch (e) {}
var e = document.createElement("script");
e.setAttribute("type", "text/javascript");
e.setAttribute("src", "https://cdn.infoq.com/statics\_s1\_20260421232814/scripts/lib/browser-update-org/update.js");
document.body.appendChild(e);
});

!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f.\_fbq)f.\_fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window,document,'script',
'https://connect.facebook.net/en\_US/fbevents.js');
fbq('init', '842388869148196');
fbq('track', 'PageView');




try {
mixpanel.track('page viewed', {
'page name' : document.title,
'url' : window.location.pathname
});
}
catch(err) {
}



const config = {
apiKey: '8910ea974a96ffb6f927952b4ae9b9b0cc3e5973',
product: 'PRO\_MULTISITE',
// general settings
consentCookieExpiry: 90,
encodeCookie: true,
sameSiteCookie: true, // if false, cookie set as SameSite=None;secure;
sameSiteValue: ';secure', // either 'Strict', 'Lax', or 'None'
subDomains: true,
initialState: 'notify', // 'notify','top','box' require pro licence
notifyOnce: false,
setInnerHTML: true,
//layout settings
layout: 'slideout',
position: 'left',
theme: 'light',
acceptButton: true,
rejectButton: true,
closeOnGlobalChange: true,
closeStyle: 'icon',
toggleType: 'slider',
notifyDismissButton: true,
settingsStyle: 'link',
excludedCountries: ['US'],
/\*accessibility: {
disableSiteScrolling: true,
},\*/
statement: {
description: 'For more detailed information about the cookies we use, see our',
name: 'Cookie Policy',
url: 'https://www.infoq.com/cookie-policy',
updated: '01/01/2024',
},
// cookies starting from 'cookie\_expire' are from live.infoq.com but since we use the same tool on the same domain we need to specify those too so
// that infoq.com cookieControl does not delete live.infoq.com cookies(also infoq.com cookies have been specified in live.infoq.com cookieControl configs)
necessaryCookies: ['RegUserCookie', 'UserCookie', 'IdpCookie', 'ConversionTrackingV2\_','PSAdialog','\*P13NWN\*','topbarSurvey','\_\_bkm','JSESSIONID','mp\_','\_mixpanel','CloudFront-Key-Pair-Id','CloudFront-Policy','CloudFront-Signature','cookie\_expire','discount\_promo\_closed','discount\_promo\_code','discount\_promo\_submitted','exit\_survey\_popup','referrer\_popup','voting\_popup\_\*','AWSALB','AWSALBCORS','aws-waf-token'],
optionalCookies: [
{
name: 'analytics',
label: 'Analytics',
description: 'Analytical cookies help us to improve our website by collecting and reporting information on its usage.',
cookies: ['\_ga', '\_ga\*', '\_gid', '\_gat', '\_\_utma', '\_\_utmt', '\_\_utmb', '\_\_utmc', '\_\_utmz', '\_\_utmv'],
onAccept: function(){
gtag('consent', 'update', {'analytics\_storage': 'granted'});
},
onRevoke: function(){
gtag('consent', 'update', {'analytics\_storage': 'denied'});
}
},
{
name: 'marketing',
label: 'Advertising',
description: 'We use advertising cookies to display advertisements to you for our products.',
onAccept: function(){
gtag('consent', 'update', {'ad\_storage': 'granted', 'ad\_personalization': 'granted', 'ad\_user\_data': 'granted'});
},
onRevoke: function(){
gtag('consent', 'update', {'ad\_storage': 'denied', 'ad\_personalization': 'denied', 'ad\_user\_data': 'denied'});
}
}
],
text : {
// main preference panels
title: '<h3>Our use of cookies</h3>',
intro: 'We use necessary cookies to make our site work. Functional cookies help enhance the performance and functionality of the site. '+
'We\'d also like to set analytics cookies to help us improve your experience by measuring how you use the site. '+
'These will be set only if you accept. ',
acceptSettings: 'I Accept',
rejectSettings: 'I Do Not Accept',
necessaryTitle : '<h3>Necessary Cookies</h3>',
necessaryDescription : 'Necessary cookies enable core functionality ' +
'such as page navigation and access to secure areas. '+
'The website cannot function properly without '+
'these cookies, and can only be disabled by changing '+
'your browser preferences.',
closeLabel: 'Close Cookie Control',
cornerButton: 'Set cookie preferences',
// main preference panel controls
on: 'On',
off : 'Off',
thirdPartyTitle : 'Some cookies require your attention',
thirdPartyDescription : 'Consent for the following cookies could not be '+
'automatically revoked. Please follow the link(s) '+
'below to opt out manually.',
// notification panels (only accessible for pro licences)
notifyTitle : 'Your choice regarding cookies on this site',
notifyDescription : 'We use cookies to optimise site functionality and '+
'give you the best possible experience.',
accept : 'I Accept',
reject: 'I Do Not Accept',
settings : 'Settings',
},
branding : {
removeAbout: true,
},
};
// do not load this for local envs only. for testing on local envs remove/modify this condition
if(InfoQConstants.pageUrl.indexOf('local')===-1){
CookieControl.load( config );
}
