[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.30 → 18.12] This episode is brought to you by Rollbar.
[18.42 → 24.36] Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 → 28.60] And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 → 32.94] And Paul says they don't deploy a service without installing Rollbar first.
[33.32 → 34.58] It's that crucial to them.
[34.78 → 36.60] We operate at serious scale.
[37.04 → 42.46] And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 → 45.52] We need to have that visibility.
[45.94 → 50.44] And without that visibility, it would be impossible to run at the scale we do.
[50.58 → 52.54] And certainly with the number of people that we have.
[52.72 → 55.70] We're a relatively small team operating a major service.
[55.70 → 61.46] And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 → 62.00] All right.
[62.02 → 66.70] If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.36 → 70.34] Once again, Rollbar.com slash Changelog.
[70.34 → 81.76] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[81.90 → 88.38] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live.
[88.38 → 93.48] Join the community and Slack with us in real time during the show at changelog.com slash community.
[93.88 → 94.68] Follow us on Twitter.
[94.78 → 96.28] We're at JSPartyFM.
[96.48 → 97.76] And now on to the show.
[97.76 → 107.08] Hello, world, and welcome to an interesting edition of JS Party.
[107.16 → 107.94] We're trying something new.
[107.98 → 110.04] You don't like to experiment around here.
[110.04 → 118.24] And we have a brand-new segment that we're calling YupNope.js, which was an awesome library by our very own Alex Sexton back in the day.
[118.72 → 120.02] This is a debate.
[120.50 → 124.14] No, it's not inspired by the current United States political debates.
[124.14 → 132.64] It's an idea from Fears to come up with a premise and talk about it and have people take different sides and see what happens.
[132.76 → 133.90] So we're going to see what happens here.
[133.90 → 139.22] We should state up front that we aren't necessarily representing our own beliefs.
[139.62 → 141.72] We're representing the side that we were assigned.
[142.00 → 145.30] And I'm your humble moderator and the assigner of sides.
[145.74 → 147.02] We have two teams.
[147.56 → 151.70] Team Fur ball, made up of one part Fears and one part K-Ball.
[151.76 → 152.24] What's up, guys?
[152.30 → 152.84] You're teaming me up.
[153.50 → 153.96] How's it going?
[154.46 → 154.86] Yep.
[155.38 → 157.26] We're going to find out how it's going real fast.
[157.26 → 162.24] Team Short Skull, made up of Divya and Chris, representing the Nopes.
[162.42 → 163.08] What's up, Divya?
[163.14 → 163.64] What's up, Chris?
[163.78 → 164.78] I mean, nope.
[167.42 → 169.74] You have to be way more negative here, Divya.
[169.88 → 170.08] Denied.
[170.94 → 172.34] So that's the idea.
[172.50 → 173.12] It's Yup Nope.
[173.18 → 174.08] We have two teams.
[174.62 → 176.08] Furrows and K-Ball representing the Yeps.
[176.30 → 177.86] Divya and Chris representing the Nopes.
[178.08 → 183.38] The premise we hope you'll find interesting and one that, honestly, a lot of us could represent either side.
[183.38 → 190.40] I feel strongly both ways, which is quite a conundrum, is that websites should work without JavaScript.
[190.60 → 191.14] That's the premise.
[191.26 → 193.62] Websites should work without JavaScript.
[194.26 → 196.90] And on the Yup side of that is Fears and K-Ball.
[197.02 → 201.18] And on the Nope side of this debate is Divya and Chris.
[201.28 → 202.72] By the way, we would love to hear from you.
[203.14 → 206.54] If you love this segment, and you want us to do it again, let us know.
[206.62 → 213.24] If you hope it disappears and never reappears ever again in the history of humankind, let us know.
[213.76 → 216.96] You can comment on the discussion page on thechangelod.com.
[217.36 → 218.42] You can let us know on Twitter.
[218.80 → 220.30] You can send a carrier pigeon.
[220.42 → 220.92] We don't care.
[221.10 → 224.88] However you'd like to let us know, we would love for feedback because we are very much experimenting.
[225.40 → 226.44] So let's get on with it.
[226.54 → 228.36] Well, and it's super simple, right?
[228.40 → 229.78] They just have to say Yup or Nope.
[229.96 → 230.48] That's right.
[230.60 → 231.52] You can Yup this episode.
[231.62 → 232.10] You can Nope it.
[232.20 → 236.96] But we appreciate a little stronger, what do you call them, arguments than just Yup or Nope.
[236.96 → 238.12] So let's start.
[238.22 → 238.58] Segment one.
[238.74 → 241.44] This is going to be starting with Team Fur ball.
[241.54 → 242.52] Person one is Fears.
[242.52 → 246.82] Fears, you've got four minutes to introduce your side of the argument.
[247.02 → 249.36] Websites should work without JS.
[249.66 → 251.00] And you are going to say Yup.
[251.26 → 251.68] Go ahead.
[252.06 → 252.30] Great.
[252.48 → 252.64] Okay.
[252.78 → 256.52] So our premise is that websites should work without JS.
[256.52 → 261.32] And I want to start by emphasizing the word websites in the premise.
[261.32 → 265.66] So it's an important distinction to make here between websites and web apps.
[265.66 → 273.56] So because the premise is focusing on websites and not web apps, I think that it will be a lot easier for our side to argue this premise.
[273.56 → 277.90] We're talking about websites which are devoted to mainly conveying content to users.
[277.90 → 280.70] Not delivering an interactive experience.
[280.70 → 295.86] And so I want to just in advance say to our listeners that if our esteemed opponents on the other side try to switch their argument, switch the argument to focusing on web apps, that that's not the right way to be thinking about this debate.
[295.86 → 299.20] So just in advance, I want to get that out of the way.
[299.20 → 306.16] So if you're focusing on websites, then one of the things to think about is default behaviour that the browser gives us.
[306.24 → 312.50] If we use just HTML and CSS to build our websites, we get amazing default behaviours, specifically around like links.
[312.84 → 325.00] So links will just work instead of, you know, implementing a link as a DIV with an on-click handler, you know, where you have to basically then become responsible for all the various click behaviour that the browser does for you.
[325.00 → 331.50] Like command click to open a new tab or middle click to open a link in a new tab or right click not causing a navigation.
[331.70 → 338.24] You know, these are all things that are really easy to get wrong if you implement like a link as, you know, a DIV, for example, that has an on-click handler.
[338.60 → 343.80] Additionally, if your site works without JS, then it's probably quite accessible.
[344.36 → 346.88] It may not be perfect, but it's probably quite good.
[346.88 → 356.60] Building a site that works without JS and then, you know, so disabling the JS and testing the site out is a great way to sort of see how some accessibility tools will experience your site.
[356.96 → 360.54] So, you know, if your links don't work that, you know, without JS turned on, that's a problem.
[360.94 → 362.94] That's going to confuse accessibility tools.
[363.00 → 364.30] It's going to confuse search engines.
[364.78 → 371.40] And so, you know, it's not a perfect way, but it's a good way to sort of get a sense for how, you know, whether you're using the correct semantic tags whenever you can.
[371.40 → 387.20] And then the last point I want to focus on in my remaining time is that sites that work without JS probably have better performance because, at least if it's a content site, because you want to think about what the experience of a user is while the JS bundle is loading.
[387.54 → 397.16] So on a slower connection, a page will be downloading the HTML and the browser is really quite good at showing HTML to the user as that HTML is being streamed across the network.
[397.28 → 400.54] It has this thing called a speculative parser that can sort of start to show this content.
[400.54 → 403.80] And so while the JS bundle is loading, that's what the user is going to see.
[404.08 → 411.26] And so, you know, if your site works without JS, that means that something is showing up on the screen before that JS bundle has been downloaded, which is good.
[411.48 → 412.56] You know, that's just like another metric.
[412.66 → 416.56] So if you build your site so that it works without JS, you will have better performance for content sites.
[416.98 → 419.72] And lastly, just another point about the speculative parser.
[419.96 → 425.04] The browser is quite good at firing off requests for resources that it finds in the HTML as it's downloading that.
[425.04 → 429.46] And so if you have resources like images that the browser encounters while the HTML is being downloaded,
[429.46 → 436.34] it'll be able to start to do DNS lookups for those URLs, start to open TCP connections, start to do the TLS negotiation,
[436.68 → 439.82] and then eventually fire off HTTP requests for those resources.
[440.26 → 444.92] Instead of waiting for this big JS bundle to download to sort of get your app running, you're not going to be able to do that.
[445.42 → 448.26] So your site waterfall will just look completely different.
[448.70 → 450.78] So yeah, I think that those are my main arguments.
[450.90 → 451.06] Time.
[451.32 → 451.62] Time?
[451.86 → 452.42] Okay, perfect.
[452.42 → 454.30] Good job.
[454.36 → 455.48] You squeezed that last one in.
[455.56 → 457.08] I believe you're at four minutes, 11 seconds.
[457.20 → 458.48] So I gave you a little bit of a break there.
[458.74 → 459.22] All right.
[459.28 → 461.68] So there is your first argument from Team Yep.
[461.76 → 463.50] Let's hear from Team Nope.
[463.58 → 464.02] Who do we want?
[464.14 → 464.78] Chris or Divya?
[466.18 → 467.26] Not it.
[467.78 → 468.16] Not it.
[469.02 → 470.64] They're already saying nope.
[471.42 → 472.50] He's already saying no.
[472.64 → 473.58] Team Short Skull.
[473.80 → 475.10] Yeah, well, he's representing the nope side.
[475.30 → 476.84] So he's going to say nope to the response.
[476.94 → 477.58] But go ahead, Divya.
[477.80 → 478.02] Okay.
[478.02 → 478.34] You're nope.
[478.90 → 479.26] All right.
[479.26 → 481.26] So I'm not going to rebut anything was said.
[481.36 → 486.70] I'm just going to state what the premise is, which is that websites should not work without
[486.70 → 487.12] JavaScript.
[487.58 → 488.22] It's a double negative.
[488.74 → 493.56] And that's because I believe that JavaScript is an essential part of the web, and it drives
[493.56 → 494.24] interactivity.
[494.42 → 497.72] And so I know that I said I wasn't going to address the rebuttal part of it, but I want
[497.72 → 503.00] to make the distinction between websites and web apps, which I think is a ridiculous
[503.00 → 508.90] distinction and difference because a lot of the times it's really hard to define what
[508.90 → 510.58] exactly a web app is versus a website.
[510.82 → 512.08] And so I'm just going to throw that away.
[513.66 → 514.38] Throw it out.
[514.78 → 515.22] Throw it out.
[515.36 → 516.54] But the whole idea is that.
[516.70 → 521.50] So one thing that really excites me about the web is this idea, the way of building the
[521.50 → 522.54] web, which is Jam stack.
[523.10 → 524.80] It's JavaScript API and markup.
[524.98 → 528.76] And so what it does is it takes otherwise static websites, and it makes it dynamic.
[529.10 → 533.50] Static websites are really nice because like we're also saying, it makes it very fast to
[533.50 → 533.82] load.
[534.00 → 537.20] It makes it like fairly secure because you can load it from a CDN, et cetera.
[537.20 → 542.08] But the nice thing about JavaScript is that you can add additional interactivity to it,
[542.18 → 544.96] which an otherwise static page doesn't have.
[545.50 → 548.94] And so if you wanted to make an API call or if you wanted to grab content from elsewhere,
[548.94 → 552.98] you cannot do that unless you have JavaScript loaded on your thing.
[553.12 → 557.34] And JavaScript in itself in today's world is fairly, it's a first class citizen of the
[557.34 → 557.56] web.
[557.80 → 561.68] And so throwing it away and assuming that things should work without JavaScript is a ridiculous
[561.68 → 563.28] idea to begin with.
[563.28 → 569.08] And then another thing to note is also this idea of, and Frost mentioned it, I think he
[569.08 → 572.20] didn't really give a term around it, but I would call it progressive enhancement.
[572.58 → 576.96] And so this idea of progressive enhancement is this idea that if someone was loading a
[576.96 → 583.14] website on a device that was on a 3G network, maybe a Motorola-like phone that is not very
[583.14 → 583.36] good.
[583.80 → 585.74] It's not a high-powered Pixel or iPhone.
[586.16 → 587.38] You want the website to load.
[587.38 → 592.10] And so we're not saying from our side that the website shouldn't load because the idea
[592.10 → 597.56] is that ultimately you want to make sure that the user sees content and then JavaScript loads
[597.56 → 598.04] in the background.
[598.04 → 599.36] And you can easily do that.
[599.90 → 604.34] So in a sense, like making sure that your JavaScript, like having JavaScript on a page
[604.34 → 608.26] doesn't preclude you from that because you can still load content and then JavaScript can
[608.26 → 609.12] still load in the background.
[609.38 → 612.94] And there are many ways in which you can optimize for that as well.
[612.94 → 617.16] So V8 has like improvements in the way that they do script streaming.
[617.42 → 622.20] You can also have access to service workers, which are really nice because service workers
[622.20 → 627.64] give you an ability to do background app sync and do like additional app cache stuff, which
[627.64 → 629.80] is app cache was before service workers.
[630.12 → 635.16] But essentially you can cache resources that you need access to, which is really nice because
[635.16 → 641.08] it gives you the ability to optimize for offline as well, which you can't necessarily do if
[641.08 → 642.74] you did not have JavaScript loading.
[642.94 → 648.42] And so I would argue that a lot of the things that make a website terrible with JavaScript
[648.42 → 653.58] is more a lack of a developer practicing by using good practices.
[653.90 → 658.24] For example, when someone says that JavaScript isn't loading or JavaScript load is too much
[658.24 → 661.30] and it's taking really long to load, the time to interactive is very long.
[661.72 → 667.22] That's more a result of developer error than JavaScript itself because there are many ways
[667.22 → 668.32] in which you can address it.
[668.40 → 672.20] So there's code splitting, there's tree shaking, there are different ways in which you can make
[672.20 → 673.00] sure and lazy loading.
[673.00 → 676.74] There are different ways in which you can make sure your website loads faster while also
[676.74 → 680.16] having the benefits of that interactivity that JavaScript gives.
[680.48 → 681.40] You have 15 seconds.
[681.50 → 682.24] Anything else to say?
[682.72 → 685.66] I think I'll stop there before I start a new thread.
[686.18 → 688.06] You can't start a new thread in 15 seconds.
[688.36 → 688.72] Exactly.
[689.12 → 689.44] Okay.
[689.52 → 690.28] Very well done.
[690.36 → 690.82] Very well done.
[690.96 → 694.18] So there's your first round on the up and the nope.
[694.44 → 696.48] Let's turn it over for the backup.
[696.88 → 697.44] Team backup.
[697.44 → 700.12] We're going to be K-ball backing up for Ross.
[700.28 → 703.28] You have four minutes to disagree or to state your side.
[703.36 → 703.88] Whatever you want to say.
[703.92 → 704.44] You got four minutes.
[704.52 → 704.72] Go ahead.
[705.32 → 705.60] Excellent.
[705.90 → 709.64] First, I'd like to thank Divya for making our case for us by talking about progressive
[709.64 → 710.16] enhancement.
[711.48 → 717.40] Progressive enhancement is the idea that website or application should function just fine without
[717.40 → 721.40] JavaScript and JavaScript then adds something progressively on top of it.
[721.54 → 722.58] So thank you, Divya.
[722.58 → 727.68] I could stop there, but I'm going to continue going by reading statements from Hacker News
[727.68 → 729.36] comments that make our point for us.
[729.94 → 733.58] Because if we're making debates, why not make it interesting?
[734.08 → 739.26] So statement that JavaScript should be required, that sites should not work without JavaScript
[739.26 → 741.52] and that you have to enable JavaScript.
[741.82 → 744.94] Statement from Nazi on December 28th, 2015.
[745.60 → 749.30] Sorry, but your statement is ridiculous unless the website is an application.
[749.30 → 751.10] That is, it does something useful.
[751.40 → 752.90] It's just a bunch of text and images.
[753.40 → 756.88] You should not expect people to give you full Turing capacity just because you're too full
[756.88 → 758.80] of your awesomeness that you can write a program.
[759.40 → 760.72] I think that makes our statement pretty well.
[760.80 → 762.70] Coming back to progressive enhancement.
[763.30 → 764.14] Progressive enhance...
[764.14 → 764.48] Oh, sorry.
[764.58 → 769.44] This is PDKL95 on December 27th, 2015.
[769.76 → 770.92] Progressive enhancement is easy.
[771.40 → 773.86] Your framework or development tools should do most of the work for you.
[774.20 → 775.34] Maybe try different tools.
[775.78 → 777.70] Leaving out progressive enhancement is just lazy.
[777.70 → 780.92] Why would you prefer to show people a broken website as a first impression?
[781.38 → 783.52] Do you even know how many people see a broken website?
[784.14 → 789.64] Next part of our rebuttal is related to security.
[790.22 → 792.54] Comp bio, December 27th, 2015.
[793.20 → 798.40] Statement, nothing is gained from a user perspective by requiring JavaScript, but security is lost.
[798.92 → 804.42] Additionally, we can make an appeal to professional sensibilities because, gosh, web development pros,
[804.52 → 805.44] we're all so professional.
[805.44 → 812.90] Donna TJ on January 26th of 2015 states, professionally speaking, this is one of the most important tests
[812.90 → 814.02] of the quality of a site.
[814.58 → 818.96] When I see an Ajax site on a resume, this is dating them a little bit.
[819.16 → 823.96] It's the first thing I check as it is a sign of a true craftsman taking care in their work.
[824.34 → 826.96] Ajax should always degrade gracefully.
[827.30 → 830.86] Do I have any more good rebuttals?
[830.86 → 835.32] In high level, the statement here is progressive enhancement is great.
[835.80 → 836.78] We love JavaScript.
[836.98 → 839.22] All the JavaScript's, the web is unreliable.
[839.36 → 840.58] The web breaks down.
[840.74 → 841.96] JavaScript will fail to load.
[842.12 → 843.16] I'm on a mobile connection.
[843.48 → 845.38] If I travel the world, I get 2G connections.
[845.64 → 851.38] If I look at mobile internet, something upwards of 60% of access to the web is on the mobile
[851.38 → 852.22] internet.
[852.58 → 853.34] Phones are slow.
[853.82 → 855.60] Mobile network connections are unreliable.
[855.60 → 859.26] Oftentimes, JavaScript will just fail out or take forever to load.
[859.50 → 861.54] Your site should function without it.
[861.72 → 862.82] Can you make it better with JavaScript?
[863.16 → 863.40] Sure.
[863.64 → 867.34] If your site relies on JavaScript for it, you just lost a heck of a lot of people.
[868.36 → 868.72] Okay.
[869.00 → 870.78] I assume that that's your time right there.
[871.10 → 871.38] I don't know.
[871.44 → 872.02] I wasn't timing.
[872.16 → 872.74] Were you timing me?
[872.80 → 874.80] I was timing, but it sounded like a good place to stop.
[874.86 → 877.36] You had probably 45 seconds similar to Divya.
[877.50 → 880.50] I can look for more Hacker News comments, but I think my case has been made.
[880.86 → 883.66] On the one hand, I want to give you points for the research you did.
[883.66 → 887.38] On the other hand, I want to dock you points for just pulling in Hacker News trolls to
[887.38 → 888.74] state your case for you.
[888.76 → 891.24] Yeah, I would question the appeal to authority.
[892.36 → 892.76] Yes.
[893.18 → 896.42] The place of all authority is the orange website.
[896.60 → 901.08] I just figured, you know, if we were going to dive into ad hominem attacks, I would
[901.08 → 903.88] put the Hacker News people out there as the targets.
[904.30 → 904.78] There you go.
[905.10 → 905.84] Don't attack K-Ball.
[905.98 → 907.56] Attack the people he cited.
[907.82 → 908.02] Yeah.
[908.14 → 909.46] That's not in the spirit of debate, though.
[909.62 → 911.70] I would never attack any of my opponents.
[912.20 → 913.32] Well, let's see what Chris will do.
[913.32 → 914.82] Chris, would you like to attack your opponents?
[915.04 → 917.60] Would you like to retreat into a cave?
[917.90 → 919.34] You have four minutes.
[919.48 → 923.52] I know you've passed it to Divya once already.
[923.64 → 925.54] I hope you got something up your sleeve.
[925.86 → 926.24] All right.
[926.36 → 932.86] The rhetorical question that the Hacker News troll asked, which was, do you know how many
[932.86 → 934.26] people see a broken website?
[934.26 → 940.38] Well, I'm going to say the number is very few because most of those people are angry
[940.38 → 948.50] Hacker News trolls who use the No Script extension and then use it as an opportunity to shame
[948.50 → 951.96] websites that their websites don't work without JavaScript.
[952.30 → 957.92] The other people that don't see the JavaScript when they visit a website are probably using
[957.92 → 958.68] text browsers.
[958.68 → 964.76] This is also probably a subset of the angry nerd on Hacker News comments.
[965.12 → 967.94] And the other people may be somebody using a feature phone.
[968.58 → 973.86] And it just kind of depends like whether the people using feature phones are your
[973.86 → 978.80] website's intended audience and whether those people actually expect interactive
[978.80 → 980.88] browsing experience on their feature phone.
[980.88 → 987.16] The other point I'd like to make then is if your audience excludes people who don't necessarily
[987.16 → 988.46] have JavaScript running.
[988.84 → 992.40] And we can say this is not their choice.
[992.76 → 995.80] Choice, I mean, the angry nerd who turns it off.
[996.00 → 1001.30] If you're expecting your audience to have JavaScript, it may not be pragmatic to spend the
[1001.30 → 1007.14] engineering resources to make your site degrade when it's been designed from the ground up as an
[1007.14 → 1008.20] interactive experience.
[1008.20 → 1012.76] And so oftentimes it may take extra work to get that done.
[1013.60 → 1017.38] And, you know, designers may need to go in and say, OK, this is what the site's going to
[1017.38 → 1019.20] have to look like when there's no JavaScript.
[1019.94 → 1021.86] This is how things are going to have to act.
[1022.76 → 1028.92] And, you know, as a developer, there's always this push and pull between the time that you're
[1028.92 → 1031.78] allowed and the resources you're allowed and time to ship.
[1032.20 → 1033.74] And it may not be pragmatic.
[1033.88 → 1035.04] It may not make business sense.
[1035.04 → 1046.74] This episode is brought to you by DigitalOcean.
[1047.06 → 1051.98] DigitalOcean is the simplest cloud platform for developers and teams with products like
[1051.98 → 1057.80] droplets, spaces, Kubernetes, load balancers, block storage and pre-built one-click apps.
[1057.80 → 1063.72] You can deploy, manage and scale cloud applications faster and more efficiently on DigitalOcean.
[1064.08 → 1068.36] Whether you're running one virtual machine or 10,000, DigitalOcean makes managing your
[1068.36 → 1070.14] infrastructure way too easy.
[1070.50 → 1072.92] Head to do.co slash changelog.
[1073.12 → 1075.94] Again, do.co slash changelog.
[1075.94 → 1089.56] Well, it was a heated debate.
[1089.68 → 1090.62] We're going to continue this.
[1090.68 → 1091.92] A little bit shorter spurts.
[1092.42 → 1093.64] Passing it back team to team.
[1093.76 → 1099.04] I know team Short Skull took issue with the website web app distinction.
[1099.80 → 1104.32] I know team Fur balls loves that distinction, but do they really believe it?
[1104.32 → 1104.60] I don't know.
[1104.62 → 1105.18] We'll find out more.
[1105.28 → 1110.94] Let's let Short Skull speak more about that distinction or any points that you want to
[1110.94 → 1114.28] make and rebuttal to the Fur balls.
[1114.74 → 1114.92] Go ahead.
[1115.02 → 1115.90] I thought it was their turn.
[1116.50 → 1117.02] Yeah, it is.
[1117.20 → 1117.82] We're Short Skull.
[1118.20 → 1119.46] You're saying nope again.
[1119.68 → 1120.24] Come on now.
[1120.46 → 1120.66] Come on.
[1120.68 → 1122.84] I just gave you the floor, and you just batted it back to me.
[1123.08 → 1123.70] Oh, okay.
[1124.90 → 1126.04] I'm the moderator here.
[1126.06 → 1126.72] I make the rules.
[1126.88 → 1127.92] Go ahead, Short Skulls.
[1127.92 → 1133.44] Okay, so I wanted to reiterate the point that Chris was making in terms of the audience
[1133.44 → 1135.14] who we're building websites for.
[1135.64 → 1139.44] And I think the people who disable JavaScript are intentionally disabling JavaScript and
[1139.44 → 1142.48] are therefore people we do not build for in general.
[1142.82 → 1147.80] Because a lot of the times what we're focusing on in terms of this argument and what has been
[1147.80 → 1152.10] brought up so far is trying to optimize for the lowest common denominator, which is someone
[1152.10 → 1156.10] on a 3G network, on a phone, or a device that is not very high-powered.
[1156.10 → 1162.44] And so in order to do that, the argument that was made by the proposition was that you essentially
[1162.44 → 1165.74] don't want to load JavaScript because it takes a lot of time, etc., whatever.
[1166.04 → 1169.78] But the thing is, JavaScript is really nice because it gives you the capacity to check
[1169.78 → 1173.00] someone's network and then load the appropriate scripts that they need.
[1173.20 → 1178.26] Because as I said previously, I think interactivity is kind of the joy of working on the web and
[1178.26 → 1179.08] using the web today.
[1179.68 → 1184.02] And so the nice thing about JavaScript and using JavaScript today is that you have access
[1184.02 → 1187.14] to a lot of APIs that allow you to query someone's bandwidth.
[1187.72 → 1189.34] So there's like the network API.
[1189.92 → 1190.52] What is it called?
[1190.94 → 1191.08] Yeah.
[1191.20 → 1195.50] The network information API that basically allows you to check whether what connection
[1195.50 → 1199.14] someone's on, if they're on a cellular or a Wi-Fi connection.
[1199.14 → 1204.66] And then based on that connection, load the scripts that will allow them to view images or
[1204.66 → 1206.88] whatever interactivity that they would need.
[1206.88 → 1212.50] And so using that, it gives you the power of selectively loading specific things so that
[1212.50 → 1216.54] you're not giving them the bulk of JavaScript that will make it really slow and will be
[1216.54 → 1217.68] render blocking overall.
[1218.24 → 1223.42] And so this idea of kind of like selectively loading or selectively giving people scripts
[1223.42 → 1227.92] is something that I think was brought up in a BBC article a couple of years ago, which
[1227.92 → 1233.00] is this idea of cutting the mustard, which is just being able to load scripts based on whichever
[1233.00 → 1234.24] device someone is on.
[1234.24 → 1239.04] So if someone's on a low powered device, you give them less JavaScript versus someone
[1239.04 → 1241.36] who's on a high-powered device, you give them more JavaScript.
[1241.52 → 1245.86] But the idea is that JavaScript is necessary because you want to give them just some kind
[1245.86 → 1247.08] of interactivity somewhat.
[1247.70 → 1247.72] Time.
[1248.24 → 1248.44] Okay.
[1248.52 → 1248.88] Fur balls.
[1249.26 → 1252.84] That sounds like a wonderful case for progressive enhancement.
[1253.20 → 1254.32] Yeah, but progressive enhance.
[1254.54 → 1254.78] Okay.
[1254.86 → 1255.72] I'll just wait.
[1256.16 → 1257.76] I think you stopped.
[1257.84 → 1258.30] You can go ahead.
[1258.52 → 1258.94] Get into it.
[1259.32 → 1262.24] I just think that progressive enhancement doesn't mean no JavaScript.
[1262.24 → 1263.62] It doesn't mean no JavaScript.
[1263.62 → 1265.04] It means there is JavaScript.
[1265.52 → 1267.36] It's just how much JavaScript there is.
[1267.58 → 1271.10] So our premise is not that websites should never include JavaScript.
[1271.50 → 1275.04] It's rather that that website should still work without the JavaScript.
[1275.34 → 1282.66] So if I want to look at your wonderful blog with images and I try to load that page, I
[1282.66 → 1286.26] should not have to have my JavaScript working to be able to see your writing and your images.
[1286.26 → 1289.20] Now, if your JavaScript is working, wonderful.
[1289.44 → 1289.68] Okay.
[1289.74 → 1292.36] You can give me this great, beautiful, enhanced experience.
[1292.50 → 1292.98] You can check.
[1293.08 → 1293.78] Am I on a desktop?
[1293.94 → 1294.14] Great.
[1294.30 → 1294.96] Massive images.
[1295.18 → 1296.28] Am I on a phone?
[1296.40 → 1297.38] We're going to do the smaller ones.
[1297.80 → 1301.66] But I don't want to wait for that JavaScript to load.
[1301.66 → 1304.78] And I think we talk about slow time.
[1304.88 → 1308.90] And I feel that a lot every time I travel because I do, especially when I travel.
[1309.26 → 1310.98] T-Mobile is great because they give me a connection everywhere.
[1311.32 → 1313.06] But the connection they give me everywhere is 2G.
[1314.36 → 1318.44] Try loading a website from the US on a 2G connection from somewhere overseas.
[1318.82 → 1321.30] And oh my goodness, it is the definition of pain.
[1321.68 → 1323.52] But what's more painful is when you see it.
[1323.88 → 1324.84] You see it there.
[1324.94 → 1325.32] It's there.
[1325.40 → 1327.36] You can see there's just a little bit hinting.
[1327.36 → 1328.54] You read the first two paragraphs.
[1328.68 → 1329.46] You're ready to scroll.
[1329.80 → 1336.96] And your web page or application or whatever won't react to your finger because it's still
[1336.96 → 1339.96] waiting for the JavaScript, or it's trying to parse the JavaScript.
[1340.24 → 1343.32] And the JavaScript, the first bundle is loading the second bundle.
[1343.54 → 1345.72] And you're at 10 or 20 seconds to interactive.
[1346.30 → 1348.72] And measuring on 3G is one thing.
[1348.82 → 1350.20] Measuring on 2G, it's even worse.
[1350.64 → 1351.76] You should be able to function.
[1351.92 → 1352.26] And great.
[1352.32 → 1353.54] When you get the JavaScript, do more.
[1353.90 → 1354.18] Awesome.
[1354.34 → 1354.66] Love it.
[1354.66 → 1358.68] But having to wait for that JavaScript to do anything is really painful.
[1359.36 → 1359.48] Yeah.
[1359.54 → 1363.10] Can I also add something to the websites versus web apps discussion?
[1363.56 → 1368.16] So I agree that we were talking a little bit during the break about that being a difficult
[1368.16 → 1368.72] distinction.
[1368.94 → 1370.84] Like where exactly is the boundary between the two?
[1371.32 → 1376.10] So I think maybe something more useful is to ask, can this site work without
[1376.10 → 1376.52] JS?
[1376.52 → 1380.58] So ignoring the developer experience, just like, is it actually possible to make this site
[1380.58 → 1381.24] work without JS?
[1381.24 → 1384.70] And if it is, then I think that you should.
[1385.46 → 1388.50] So if it's a blog, you know, that should probably work without JS.
[1388.66 → 1394.14] But if it's like a game or something that literally requires WebGL, or if it requires the use of WebRTC,
[1394.44 → 1398.56] or the, you know, the canvas or something like that, where you need JavaScript, then obviously,
[1399.06 → 1404.04] it would be extremely burdensome to go and, you know, get the developer time to somehow
[1404.04 → 1406.26] hack together a solution maybe that would work without it.
[1406.26 → 1409.90] So it's not about making your site work without JS for the hacker news trolls.
[1410.08 → 1413.10] It's about doing it because it actually makes your site better.
[1413.50 → 1417.86] Requiring JS to show some simple text on the page makes your site more complicated and more brittle.
[1418.48 → 1422.30] And as programmers, our entire, like our entire job is to reduce complexity.
[1422.72 → 1425.78] The biggest challenge we face is this creeping complexity.
[1425.78 → 1431.16] And requiring JS to show some text is like a very clear form of complexity.
[1431.74 → 1432.64] And complexity is the enemy.
[1433.08 → 1438.32] And it makes it so that like if something slightly goes wrong with the way the page is loading,
[1438.50 → 1440.56] then the entire thing is completely broken.
[1440.56 → 1443.74] Or, you know, or the site just doesn't work until the JS arrives.
[1444.42 → 1445.20] I rest my case.
[1446.22 → 1446.82] Charles Balls.
[1447.24 → 1447.54] Chris.
[1447.54 → 1447.66] Chris.
[1448.38 → 1451.90] Uh, I had a thought.
[1452.48 → 1453.36] Come back to me.
[1454.76 → 1456.60] You're not going to quote Hacker News again, are you?
[1456.88 → 1458.30] He's always drawing Hacker News.
[1458.30 → 1460.30] I would just like to quote Hacker News one more time.
[1460.40 → 1461.36] No, no, no.
[1461.66 → 1463.48] I'm going to quote Divya's article that she posted.
[1463.78 → 1468.28] It's a wonderful article talking about the distinction between websites and web applications
[1468.28 → 1469.32] being a false distinction.
[1469.92 → 1472.22] And I just want to read this paragraph, which says,
[1472.22 → 1496.50] Coming back to progressive enhancement, it should function in some form without the JavaScript.
[1496.50 → 1501.40] I think we were all building web applications using server-side frameworks before JavaScript
[1501.40 → 1502.10] got fancy.
[1502.52 → 1503.64] And those are web apps.
[1503.90 → 1504.86] They do good stuff.
[1505.00 → 1505.56] They're important.
[1506.12 → 1507.08] You know, they're interactive.
[1507.22 → 1508.28] They do lots of different things.
[1508.92 → 1511.30] I love what we can do with client-side JavaScript today.
[1511.94 → 1517.84] But it has kind of clouded our eyes to some of the fundamentals.
[1518.74 → 1521.06] Let me hop in here real quick because I just can't stay quiet any longer.
[1521.20 → 1522.62] No, you're supposed to be neutral.
[1522.86 → 1523.42] What is this?
[1523.84 → 1525.20] Yeah, you have to be in the middle.
[1525.58 → 1526.34] I am in the middle.
[1526.42 → 1526.98] You're the moderator.
[1526.98 → 1528.24] I'm asking for this from the middle.
[1528.74 → 1531.66] K-Ball, if you were built, and this is an honest question, like let's pause the debate.
[1531.66 → 1534.64] If you were building Slack, would you progressive enhance?
[1534.88 → 1536.22] Do you think Slack should work without JavaScript?
[1537.68 → 1538.56] Great question.
[1538.56 → 1546.02] I think I should be able to read existing messages, like load a page and see what has happened.
[1546.76 → 1550.00] Creating that real-time response is, I mean, that is a JavaScript.
[1550.00 → 1551.18] You can't use, yeah, you can't.
[1551.28 → 1553.02] WebRTC does not work with JavaScript.
[1553.02 → 1557.68] Wait, so can't you HTTP post the message up and then reload the page to see the new message?
[1558.16 → 1562.14] No, you laugh, but if you look at literal Loss there.
[1562.22 → 1562.50] Yes.
[1562.82 → 1565.22] I've seen Gmail's simple HTML interface.
[1565.58 → 1568.38] Like if you're on a really slow internet connection, or you're on a really crappy phone,
[1568.74 → 1570.62] you can actually still use Gmail.
[1570.62 → 1575.60] Like you click the name of the email, and then it just loads a new page with the email in it.
[1575.82 → 1579.26] And then you can type into a box, and you can hit send, and it posts it.
[1579.58 → 1583.22] Yeah, I think essentially that's like one way of experiencing and working with the web.
[1583.30 → 1587.78] But it's this idea of you're making multiple server requests for like very simple interactions.
[1588.50 → 1592.36] And so sure, yeah, it makes it like possible for you to work without JavaScript,
[1592.36 → 1600.22] but you're still trying to lean on HTTP requests to make those interactive experiences work on a static site.
[1600.62 → 1605.92] And so the nice thing about working or when websites like Slack or I guess web apps,
[1606.02 → 1606.74] I don't know, whatever.
[1607.10 → 1607.90] Web things.
[1608.56 → 1609.66] When web things.
[1610.02 → 1610.18] Things.
[1610.44 → 1611.00] Web things.
[1611.34 → 1612.20] Yeah, web things.
[1612.44 → 1613.28] I build web things.
[1613.80 → 1619.02] For web things like Slack to work, you would need JavaScript because you want those niceties
[1619.02 → 1619.98] of that interactivity.
[1619.98 → 1623.26] You can also do a lot of preloading.
[1623.48 → 1628.98] You can make sure that resources are fetched beforehand so that you can optimize for offline experiences,
[1628.98 → 1632.32] as I mentioned earlier, which is something you cannot do without JavaScript.
[1632.90 → 1636.94] Sure, you could like, I don't know, load a static page, but you can't really.
[1637.12 → 1639.68] All hyperlinks do not work when you're offline anymore.
[1640.02 → 1645.00] Versus if something was client-side rendered, and you were using like a PWA, for instance,
[1645.00 → 1648.14] which is a progressive web application which requires JavaScript,
[1648.54 → 1650.40] which is optimized for progressive enhancement.
[1650.88 → 1656.60] You have the ability to load all of those pages so you can still access and use it as you would need
[1656.60 → 1658.84] without even noticing that you're offline.
[1658.96 → 1662.58] So if you're kicked offline, you can continue sending emails, doing whatever you need to do.
[1662.58 → 1666.20] And then when you come back online, all of those actions are then sent over the wire.
[1666.78 → 1672.64] And so that's the nice thing about JavaScript and why web apps or web things like Slack to
[1672.64 → 1673.50] need JavaScript.
[1673.92 → 1679.84] I wanted to jump in and talk about one point that's been mentioned in passing, which is accessibility.
[1679.84 → 1687.10] It's a misconception that sites with JavaScript are inaccessible, especially to like screen readers.
[1687.26 → 1687.38] Right.
[1687.50 → 1690.76] So nowadays, like a screen reader does not care about your JavaScript.
[1691.06 → 1696.02] The way a screen reader works is it cares about the markup.
[1696.46 → 1702.18] And regardless of whether your site has JavaScript, if that JavaScript is good or bad or
[1702.18 → 1709.34] whatever, if your markup is not semantic, if you're not using like the ARIA attributes and
[1709.34 → 1713.88] accessibility features built into the HTML platform, then your site will be accessible
[1713.88 → 1715.34] regardless of JavaScript.
[1716.08 → 1721.50] And so just because a site needs JavaScript doesn't necessarily mean it's going to be
[1721.50 → 1723.74] inaccessible to a screen reader.
[1723.74 → 1728.36] By the way, on that point, I just meant that if you already have something like a server-side
[1728.36 → 1732.98] rendering setup and, you know, you're getting HTML back from the server, and then you disable
[1732.98 → 1740.16] JS, that's just like an easy way to test whether you are using all of those nice properly semantic
[1740.16 → 1741.60] tags, right?
[1741.62 → 1745.38] Because now you don't have all the like on-click handlers attached to stuff that the JavaScript
[1745.38 → 1745.96] would have done.
[1746.04 → 1747.94] You just have the raw elements.
[1748.50 → 1752.40] So it's just a nice way to, it's just like a nice easy way to test whether your site is
[1752.40 → 1753.68] like minimally accessible.
[1754.20 → 1754.78] Do you agree with that?
[1755.44 → 1755.84] Yeah.
[1756.30 → 1757.26] I have no idea.
[1757.42 → 1757.60] Sure.
[1758.36 → 1760.32] Was that an argument?
[1760.52 → 1761.60] I thought you were just commenting.
[1762.06 → 1767.42] To jump on Chris's point a little bit, I think it is 100% true that the idea that JavaScript
[1767.42 → 1769.74] is not accessible is a misnomer.
[1770.18 → 1777.50] One thing that I think is overlooked is that HTML and CSS are accessible by default in the
[1777.50 → 1785.48] sense that the languages are simple enough and declarative enough that browsers, screen readers,
[1785.48 → 1789.70] et cetera, can figure out the right way to interpret them for their medium.
[1789.94 → 1795.46] Whereas with JavaScript, you've taken a lot of that control away from the browser by default.
[1795.62 → 1797.26] You've said, I'm going to control all of it.
[1797.36 → 1801.86] And now you have to put it back, and you have to re-add those accessibility features and
[1801.86 → 1803.88] functionalities to make sure that stuff continues to behave.
[1803.88 → 1805.40] I actually disagree with that.
[1805.40 → 1811.90] Just because I think that, like, sure, HTML and CSS give you attributes to make them accessible,
[1812.30 → 1817.34] but you don't get access to the accessibility model or the I think it's the accessibility
[1817.34 → 1820.34] object model because it just automatically does that for you.
[1820.34 → 1824.48] So all you have to do is use those attributes, and then it just does those parsing and it
[1824.48 → 1826.82] orders everything as it should with the screen reader.
[1827.36 → 1829.62] But there's this idea of the accessibility object model.
[1829.72 → 1831.96] I don't think it's default at the moment.
[1832.06 → 1833.94] I think it's still, like, in standards.
[1834.74 → 1839.72] But that's essentially a JavaScript API that gives you access directly into the object, the
[1839.72 → 1845.50] AOM or accessibility object model, which then allows you to move around nodes and make
[1845.50 → 1849.62] it such that you can organize how exactly you want your site to be viewed with the screen reader.
[1849.62 → 1855.82] Because if you were to use just automatic HTML, CSS, like ARIA attributes and so on, you're
[1855.82 → 1860.76] kind of ceding control to how exactly those, the standards work.
[1860.86 → 1864.24] But with the AOM, you get to actually manipulate that yourself.
[1864.24 → 1869.88] So you can create a specific user experience for screen readers if that's something that
[1869.88 → 1870.80] you would like to do.
[1871.28 → 1872.24] And it needs JavaScript.
[1872.52 → 1873.26] And it needs JavaScript.
[1873.76 → 1879.52] I don't think that we're disagreeing on that because the browser already knows how to
[1879.52 → 1881.96] create that experience for its built-in stuff, right?
[1882.00 → 1887.08] So, like, if you have a select HTML element, that element is accessible because the browser
[1887.08 → 1888.56] understands how does the select work.
[1888.78 → 1890.56] You know, screen readers understand how that works.
[1890.66 → 1895.36] You don't actually need additional ARIA attributes to explain a select element.
[1895.60 → 1896.94] It just, it functions.
[1897.08 → 1897.78] They know how it works.
[1897.78 → 1900.88] Similar to the rest of form elements, various other things.
[1900.88 → 1905.26] And until we decide that a select element is not good enough, we want a combo box.
[1905.44 → 1907.38] And we're going to implement this all in JavaScript.
[1907.90 → 1911.52] Now we have taken control back, which is true.
[1911.62 → 1912.84] We now have more control.
[1913.16 → 1914.50] But we've also taken information.
[1914.88 → 1917.68] And we need to now add that back explicitly with JavaScript.
[1917.68 → 1921.54] One nice thing you can do, by the way, is just use a select element and then enhance, like,
[1921.62 → 1926.42] the JS can sort of, the JS can see the select element there and then replace it with something,
[1926.54 → 1927.62] you know, at runtime.
[1927.84 → 1932.00] So that if, so if the JS doesn't actually load, then you still have the select element,
[1932.00 → 1937.80] which might not be as nice as your fancy little component widget thingy, a jigger, but will
[1937.80 → 1938.70] still work.
[1939.18 → 1939.42] Yes.
[1939.62 → 1943.64] The thing about JavaScript that makes it nice when you want to access that, that DOM or
[1943.64 → 1947.16] that AM tree is that events work really nicely with accessibility.
[1947.16 → 1951.46] So if you were to trigger events, like you're like this, I don't know, clicking this button
[1951.46 → 1953.62] does this other thing and opens a pop-up or whatever.
[1954.06 → 1959.60] Like you were mentioning, Ball, currently there's no way for you to manage what exactly
[1959.60 → 1961.04] happens with the accessibility tree.
[1961.54 → 1965.84] And so if you want that interactivity to work, which is often the case, then you would
[1965.84 → 1971.44] need access to that tree so that you can make sure that the event propagates properly
[1971.44 → 1976.14] and that screen readers have the ability to handle that appropriately.
[1976.14 → 1981.84] Without just like it bubbling up to, I don't know, wherever it goes, which is very jarring
[1981.84 → 1987.76] because in general, accessibility is a jarring, like viewing the web as a someone who has
[1987.76 → 1989.80] an impairment is very frustrating.
[1990.10 → 1995.10] And so the ability to handle those events as they propagate, because events are obviously
[1995.10 → 1999.14] what happened, like event delegation, all of that things is kind of standard on the
[1999.14 → 2000.06] web at this point.
[2000.28 → 2001.24] Once you add JavaScript.
[2001.64 → 2002.56] Yes, it's standard.
[2002.82 → 2003.84] It's, it's fairly standard.
[2004.32 → 2004.90] No, absolutely.
[2004.90 → 2009.22] I mean, I think part of what you're highlighting here, if I'm understanding, is just the current
[2009.22 → 2014.20] tools for making JavaScript accessible are insufficient.
[2014.56 → 2014.70] Yep.
[2015.08 → 2017.98] I'm going to appeal to authority and read some quotes at this time.
[2019.50 → 2019.98] Okay.
[2024.74 → 2026.56] I've lost complete control of this panel.
[2026.66 → 2027.52] Go ahead, Ross.
[2027.70 → 2030.38] The first quote, no code is faster than code.
[2030.68 → 2030.98] Okay.
[2030.98 → 2032.12] Second quote.
[2032.66 → 2034.24] The code you write makes you a programmer.
[2034.64 → 2036.68] The code you delete makes you a good one.
[2037.14 → 2039.52] The code you don't have to write makes you a great one.
[2040.20 → 2041.16] And next quote.
[2041.38 → 2043.48] Are you getting these off of fortune cookies or where are these coming from?
[2043.48 → 2043.66] Yeah.
[2043.76 → 2045.10] Where are these from?
[2045.74 → 2046.42] Confucius says.
[2046.62 → 2047.52] I can't disclose.
[2048.20 → 2048.50] What?
[2049.54 → 2050.66] Are they free copy?
[2050.66 → 2053.74] Is the copyright available such that we can put them on t-shirts?
[2054.02 → 2057.56] Whoever said this is going to be objectionable, and we're going to disregard them.
[2057.92 → 2058.44] Yeah, exactly.
[2059.04 → 2059.22] Yeah.
[2059.34 → 2059.48] Yeah.
[2059.54 → 2061.98] Authority doesn't work as well when the authority is anonymous.
[2062.34 → 2062.46] Yeah.
[2062.54 → 2062.74] All right.
[2062.74 → 2063.34] Last quote.
[2063.44 → 2063.74] Last quote.
[2064.38 → 2068.36] Inside every large program, there is a small program trying to get out.
[2069.96 → 2074.40] Also, I would like, I mean, since we're talking about appeal to authority, I would like to quote
[2074.40 → 2080.08] Atwood's law, which is that any application that can be written with JavaScript will be
[2080.08 → 2081.40] written with JavaScript.
[2081.94 → 2083.66] And this was a positive thing?
[2084.22 → 2084.72] Yes.
[2084.76 → 2085.28] Very positive.
[2085.62 → 2086.50] Very, very positive.
[2086.72 → 2087.54] Very positive.
[2087.76 → 2088.64] The huge statement.
[2088.96 → 2089.90] You heard it here first.
[2089.90 → 2090.90] Thank you.
[2104.40 → 2114.62] This episode is brought to you by cross-browser testing of Smart Bear, the innovator behind the
[2114.62 → 2118.08] tools that make it easier for you to create better software faster.
[2118.08 → 2123.00] If you're building a website and don't know how it's going to render across different browsers
[2123.00 → 2127.00] or even mobile devices, you'll want to give this tool a shot.
[2127.30 → 2132.90] It's the only all-in-one testing platform that lets you run automated visual and manual
[2132.90 → 2136.64] UI tests across thousands of real desktop and mobile browsers.
[2137.08 → 2140.58] Make sure every experience is perfect for everyone who uses your site.
[2140.86 → 2143.48] And it's easy and completely free to try.
[2143.64 → 2147.10] Check it out at crossbrowsertesting.com slash changelog.
[2147.22 → 2150.80] Again, crossbrowsertesting.com slash changelog.
[2160.18 → 2160.72] All right.
[2160.76 → 2162.68] We're back for the behind the scenes of the debate.
[2162.68 → 2165.46] The post-debate, you know, I like to talk about who wins, who loses.
[2165.64 → 2166.38] Well, we're not going to do that.
[2166.48 → 2168.04] We want you to do that, maybe, if you'd like.
[2168.12 → 2169.48] If you're on Team Fur ball, let us know.
[2169.98 → 2171.22] If you think the Fur balls represent.
[2171.38 → 2173.90] If you're on Team Short Skull, all are back.
[2174.28 → 2175.44] The yups versus the nopes.
[2175.70 → 2177.06] You can click on the show notes.
[2177.20 → 2178.90] There's a discuss on changelog news button.
[2179.50 → 2181.00] We'll all be in on that commentary.
[2181.30 → 2183.48] Or hit us up, jspartyfm on Twitter, if you prefer.
[2184.06 → 2185.10] Let us know what you think.
[2185.18 → 2189.92] Now, let's actually represent our real thoughts versus the pre-assigned ones that you were forced
[2189.92 → 2190.44] to represent.
[2190.44 → 2192.80] I'm curious what you all really feel about this.
[2192.92 → 2197.78] I'm firmly in camp, it depends, which is the moderator, the moderate camp.
[2198.00 → 2205.30] But I do think the distinction between web app and website is sometimes worth making, especially
[2205.30 → 2207.46] in extreme cases such as a Slack.
[2207.46 → 2214.48] I do believe it is not in Slack's best interest to simultaneously, to build in a progressive
[2214.48 → 2220.32] enhancement way or to simultaneously have an HTML only version of Slack that they're keeping
[2220.32 → 2222.60] up to date with their other code.
[2222.72 → 2223.40] That's my own opinion.
[2223.54 → 2226.10] But if you can, progressive enhance, please do.
[2226.50 → 2228.04] I do it on changelog.com all the time.
[2228.04 → 2232.92] For example, we have a JavaScript player that when you click the play button, it pops up.
[2233.02 → 2236.32] JavaScript takes over, uses all the fanciness to do the things.
[2236.50 → 2239.84] But at the end of the day, that play button is just an anchor tag which links directly to
[2239.84 → 2240.36] the MP3.
[2240.50 → 2244.02] So if you don't have JavaScript, it's just going to take you to that file and your browser
[2244.02 → 2244.54] will play it.
[2244.54 → 2248.66] So I do practice these things when they're easy or maybe just a little bit more effort.
[2249.16 → 2254.44] But if it's orders of magnitudes more effort, I tend to be a little bit more of a pragmatist.
[2254.52 → 2255.10] That's where I stand.
[2255.18 → 2256.08] That's why I say it depends.
[2256.52 → 2259.12] Curious what you all think about this in reality.
[2259.80 → 2260.66] I mean, I totally agree.
[2260.96 → 2265.24] I think obviously we have a limited amount of time to work on stuff, and we have to prioritize
[2265.24 → 2270.96] the most important features and focus on features that benefit the most users.
[2270.96 → 2275.90] Just like, you know, just like, yeah, just like the same thing as prioritizing features
[2275.90 → 2277.08] that you're going to focus on building.
[2277.40 → 2281.22] You know, you wouldn't focus on a feature that benefits like a really tiny fraction of
[2281.22 → 2286.38] your users while you have other features that you could build that would help a lot
[2286.38 → 2286.90] more of them.
[2287.44 → 2291.70] So it's, you know, it's sort of like once you've taken care of all the like easy stuff,
[2291.78 → 2295.32] then maybe if you have time, you can sort of think about making things really perfect
[2295.32 → 2298.86] and, you know, helping the sort of edge cases.
[2298.86 → 2302.02] That's how a lot of businesses operate.
[2302.36 → 2307.02] But on the other hand, accessibility is an example where you actually do take a lot of
[2307.02 → 2311.42] time and energy potentially to make a site work for a very small fraction of people.
[2311.94 → 2316.32] And so, you know, I don't know, maybe we should be thinking of the JS crowd as just another
[2316.32 → 2319.52] sort of smaller group of users that we should focus on.
[2319.70 → 2319.98] I don't know.
[2320.64 → 2321.20] I really don't know.
[2321.88 → 2323.72] Divya, you represented the Nopes.
[2323.96 → 2326.10] Do you believe in the Nopes or were you just representing the Nopes?
[2326.12 → 2327.58] I mean, I was just representing the Nopes.
[2327.58 → 2330.44] I feel like all of us, like similar to everyone here.
[2330.64 → 2334.98] And I echoed their sentiments in that we're pretty moderate in our views.
[2335.18 → 2340.34] Because I think in general, in the web world, there's this idea of JavaScript eating the
[2340.34 → 2340.74] world.
[2340.98 → 2346.72] But I think everyone feels that pain point of how complexity causes more complexity.
[2347.08 → 2349.74] Because you're like, oh, you need JavaScript for this thing to work.
[2349.74 → 2354.04] And then you need JavaScript to like to fix the issues that the JavaScript introduced.
[2354.80 → 2359.64] And then it just keeps going, which is kind of like why Babel came about and then Webpack,
[2359.74 → 2362.44] because it was issues as a result of writing more JavaScript.
[2362.44 → 2367.26] And then also trying to be super cutting edge, like using arrow functions.
[2367.68 → 2370.18] But then arrow functions are not backwards compatible.
[2370.18 → 2373.26] So you need to polyfill, which requires JavaScript.
[2373.82 → 2375.74] And like all of this extra stuff.
[2375.84 → 2378.62] And then it ends up becoming this crazy mess of JavaScript.
[2379.18 → 2381.92] And so you're loading all of this JavaScript to load more JavaScript.
[2382.24 → 2383.28] And so it just becomes, yeah.
[2383.58 → 2386.96] So in general, I think it's kind of a ridiculous conundrum that way.
[2386.96 → 2392.16] And I'm very much of the opinion of, like, I believe in progressive enhancement, as everyone
[2392.16 → 2397.26] has so far mentioned, just because I think that that's the ability to make sure that your
[2397.26 → 2398.96] site works in all scenarios.
[2399.52 → 2404.34] So because ultimately, you want the content to load, so people can at least see what's
[2404.34 → 2405.20] happening on the page.
[2405.50 → 2408.76] But of course, you also want to optimize for the time to first interactive, because it's
[2408.76 → 2412.62] really frustrating if everything loads content wise, but then it's not, it doesn't work.
[2412.86 → 2415.66] And so I believe it's kind of a balancing act.
[2415.66 → 2418.98] So you don't go like, oh, no JavaScript at all.
[2419.12 → 2421.88] But you want to make sure that it works at a minimal amount.
[2422.08 → 2426.16] And so to make time to first interactive better, there are a lot of like ways that you can make
[2426.16 → 2428.40] sure you can use like HTTP server push.
[2428.52 → 2433.64] So you're making sure that your resources load as fast as possible so that time is improved.
[2434.36 → 2436.74] And there's a lot more like techniques.
[2436.92 → 2443.08] I think Eddie Osman wrote a post called The Cost of JavaScript in maybe 2017 or 18, talking
[2443.08 → 2448.02] about just how to make that time to first interactive, which is actually perceptible to people.
[2448.02 → 2449.04] People notice that.
[2449.50 → 2453.46] And so trying to improve that using various techniques as developers and trying to be responsible
[2453.46 → 2454.00] for that.
[2454.48 → 2455.80] Cable, you're strongly on the yep.
[2455.90 → 2457.38] So are you strongly on the yep?
[2458.04 → 2459.88] Well, engineering is all about tradeoffs.
[2460.22 → 2463.66] So as everyone has said, we make tradeoffs.
[2463.78 → 2464.70] Sometimes it's the right choice.
[2464.74 → 2465.74] Sometimes it's the wrong choice.
[2465.74 → 2468.98] I do want to highlight something along this domain.
[2469.30 → 2474.10] There was a post on Brad Frost's blog recently that I will actually we should probably put
[2474.10 → 2475.20] it on page log news.
[2475.28 → 2475.76] It would be great.
[2476.00 → 2479.44] But it was reacting to a tweet somebody posted.
[2479.60 → 2483.50] Actually, somebody who was on our show at React Amersham, Sika.
[2484.02 → 2485.64] He said, you're working on a front end project.
[2485.80 → 2487.34] You can install max five dependencies.
[2487.70 → 2488.70] Which ones do you pick?
[2489.06 → 2492.62] And everybody's weighing in with their tools of choice and Ada, Ada, Ada.
[2492.62 → 2495.98] And Brad Frost raised is a fascinating point.
[2496.22 → 2501.06] Like if you were to say you're working on a home improvement project, you can choose max
[2501.06 → 2501.72] five tools.
[2501.96 → 2503.02] Which ones do you pick?
[2503.34 → 2507.34] Like your question would be, what's the project, right?
[2507.40 → 2509.80] Like, am I repairing a toilet?
[2510.20 → 2512.08] Well, I probably don't need my saw, right?
[2512.10 → 2516.48] Like there's a lot of dependency on what you're actually trying to accomplish.
[2516.68 → 2522.52] But we have a tendency to have in the web world because, you know, all languages
[2522.52 → 2524.94] are Turing complete, and we can do anything with anything.
[2525.08 → 2529.26] We have a tendency to say, okay, I have my tools, and I'm going to apply that hammer to
[2529.26 → 2531.46] every project, and it's going to look like a nail.
[2532.08 → 2534.16] And I think that that is a problem.
[2534.44 → 2539.18] And I think increasingly massive JavaScript frameworks fall into that hammer that we try
[2539.18 → 2542.80] to apply to every project and make every project into a nail.
[2542.80 → 2548.26] And that has led to an industry-wide tendency to have too much dependency on JavaScript.
[2548.86 → 2554.94] So I think, you know, the statement, your site or application should work without JavaScript
[2554.94 → 2559.50] all the time, 100% of the time is not tenable, right?
[2559.60 → 2561.66] There are Slack is actually a great example.
[2561.82 → 2564.02] You know, I tried to rebut that a little bit in the debate.
[2564.12 → 2567.58] But like, yeah, Slack, it's literally about real time conversation.
[2567.94 → 2568.04] Right.
[2568.12 → 2570.22] It makes zero sense to have a static version of that.
[2570.22 → 2575.16] I liked your response, though, because I could tell your gear started a turn and you
[2575.16 → 2577.88] started asking yourself, well, what could we provide somebody in that case?
[2577.98 → 2579.08] Maybe a read-only version.
[2579.76 → 2582.82] Maybe, Farah said, you could do an HTTP post.
[2583.50 → 2584.74] You definitely could do that.
[2584.84 → 2588.98] I wonder if the Gmail is the example there where they do have the HTML-only version.
[2589.10 → 2592.42] I wonder if that's because they built that first, and then they went, I don't remember,
[2592.54 → 2593.38] like, does that exist?
[2593.78 → 2596.98] I would love to know if they're just like continually working on that or if it's just like, well,
[2596.98 → 2599.08] this thing still works because we haven't changed our backend APIs.
[2599.08 → 2602.56] I would guess there's some segment of users that are getting some value out of it or else
[2602.56 → 2606.22] they would have deleted it like they've, like they delete so many of their products.
[2607.24 → 2607.60] Right.
[2607.90 → 2611.52] And if you have just so many million people using it, then that small percentage is still
[2611.52 → 2612.50] a large amount of people.
[2612.82 → 2613.00] Yeah.
[2613.02 → 2616.48] If I'm ever overseas and connecting through my phone through one of those super slow connections,
[2616.48 → 2618.16] I'm so grateful that that exists.
[2618.54 → 2618.70] Right.
[2618.74 → 2622.02] Like I'll be, I'll have my laptop open because it's easier to deal with things on the laptop,
[2622.02 → 2624.36] but I'll be connecting through something that's really slow.
[2624.36 → 2629.96] And Gmail will automatically say like, Hey, this, our, our JavaScript intensive experience
[2629.96 → 2631.28] is taking a long time to load.
[2631.38 → 2632.82] Do you want to go to the static version?
[2633.32 → 2639.30] And it makes it possible to use Gmail in scenarios where otherwise you really can't, like it's
[2639.30 → 2639.84] unusable.
[2640.84 → 2646.48] I am in that slice of users that once a year or so, I'm like, Oh, I'm so grateful this
[2646.48 → 2646.86] exists.
[2646.86 → 2651.22] But if you think about an email client, it really isn't a thing that should require.
[2651.52 → 2654.72] I mean, the, the fallback is you load a page, right?
[2654.76 → 2659.56] You read the stuff, you enter stuff into a form, you push submit, it posts it to the
[2659.80 → 2661.84] it's a very normal web flow.
[2661.98 → 2666.18] Whereas something like WebRTC is dramatically different web flow, right?
[2666.22 → 2669.26] Anything that's socket based stuff, dramatically different.
[2669.68 → 2673.68] And so they're really, that that's where it's like, okay, is there a progressive hand enhancement?
[2673.68 → 2678.78] If I'm building a collaborative video tool, such as appear.in, which we've, we've tried
[2678.78 → 2679.62] and it works pretty well.
[2679.70 → 2680.20] It's WebRTC.
[2680.76 → 2682.26] Is there like a fallback for that?
[2682.32 → 2685.44] And where it's like, Hey, we'll give you an ASCII version of what you guys look like
[2685.44 → 2687.10] or, you know, like what?
[2687.48 → 2689.62] So I, that's why it does depend.
[2689.74 → 2695.44] And, and I think Gmail even is a better, has a more obvious fallback than a Slack or a video
[2695.44 → 2695.72] tool.
[2695.72 → 2699.94] One interesting thing about the Gmail example is maybe a better experience for you, K-ball,
[2700.02 → 2703.66] when you're travelling would be if, if they actually got, you know, got their
[2703.66 → 2705.80] back together and added a service worker to Gmail.
[2706.10 → 2710.62] So then like all the resources that it actually takes to like load up the Gmail UI
[2710.62 → 2711.98] would have already been on your computer.
[2712.28 → 2712.96] Entirely possible.
[2713.20 → 2713.38] Yeah.
[2713.44 → 2717.14] And then it would just be one API, you know, one API requests to the server to get the new
[2717.14 → 2717.54] emails.
[2718.10 → 2719.62] I guess they do have Gmail offline now, right?
[2719.70 → 2720.26] I think so.
[2720.38 → 2723.62] Does that require like a, I forget if, it used to require a browser extension or something.
[2724.40 → 2725.38] Chrome only probably.
[2726.46 → 2727.38] Only works in Chrome.
[2727.38 → 2732.30] Actually, you can even enable, I guess you have to enable offline email for it to work and
[2732.30 → 2733.18] it has to be on Chrome.
[2733.18 → 2733.48] Okay.
[2733.66 → 2733.86] Yeah.
[2733.88 → 2734.90] It should just work out of the box.
[2735.16 → 2735.56] Let's do it.
[2735.70 → 2736.06] All right.
[2736.10 → 2737.70] Well, any other thoughts on this topic?
[2737.82 → 2738.30] Go ahead, Kimball.
[2738.56 → 2738.86] Oh yeah.
[2739.04 → 2744.64] I think, you know, just coming back to this question, there is this sort of meta question
[2744.64 → 2750.60] that gets thrown around periodically around developer ergonomics as compared to actual user
[2750.60 → 2751.04] value.
[2751.04 → 2757.04] And a lot of the overemphasis on JavaScript is around that developer ergonomics.
[2757.26 → 2758.78] And it's really focused there.
[2759.26 → 2762.06] And there are times when that's the right answer and the right tradeoff to make.
[2762.48 → 2766.32] And there are also times when, you know, as we just discussed, it enables a product experience
[2766.32 → 2768.36] that wouldn't make any sense in another world.
[2768.36 → 2773.24] However, I think we forget that it is actually a tradeoff very often.
[2773.58 → 2779.42] And we don't necessarily look at the cost that that places on users.
[2779.70 → 2780.52] We don't think about it.
[2780.52 → 2783.96] We're all using our high-end MacBooks on really fast networks.
[2784.38 → 2787.78] We develop things close to the servers that we're using.
[2787.78 → 2790.56] So we rarely have things that don't respond or time out.
[2790.60 → 2795.50] And we don't really deal with those error cases nearly to the extent that we probably
[2795.50 → 2795.82] should.
[2795.82 → 2800.38] I think we also have an overemphasis on cutting edge and latest and greatest.
[2800.86 → 2802.84] You know, I think about Craigslist, right?
[2803.02 → 2807.20] Craigslist, every developer and every designer is like, oh, I'm going to build a better Craigslist.
[2807.38 → 2808.56] Craigslist is a piece of crap.
[2808.72 → 2810.12] Craigslist is using this old, whatever.
[2810.52 → 2812.80] Millions of people still use Craigslist every day.
[2813.12 → 2816.66] And if they're over the age of 40, many of them like it better than the other options.
[2817.04 → 2822.42] Isn't that more of an argument for first to market and network effects versus like quality
[2822.42 → 2823.04] tooling?
[2823.44 → 2825.26] Like they use it because they're used to it.
[2825.26 → 2831.36] It's an argument that simplicity of use is undervalued in our industry.
[2831.72 → 2836.34] You know if we have a design, and it's two years old, and we say, oh, shit, this design is
[2836.34 → 2837.14] way out of date.
[2837.18 → 2838.24] I got to update it, right?
[2838.30 → 2839.84] Like my mom has not updated.
[2839.84 → 2842.24] I mean, now she's got Alzheimer's and whatever.
[2842.40 → 2846.24] But like even five years ago when she was still functioning, like she could not understand
[2846.24 → 2849.18] anything that changed fast, right?
[2849.22 → 2851.06] Like she was like baffled.
[2851.24 → 2852.94] She would have something she was using changed.
[2853.06 → 2854.30] And that's not uncommon, right?
[2854.30 → 2856.62] Like I still get I'm frustrated with the new Twitter interface.
[2856.74 → 2857.26] What the heck?
[2857.34 → 2858.24] The old one was fine.
[2858.68 → 2860.22] This new one adds zero value to me.
[2860.28 → 2863.18] And if it's like it's changed for change’s sake.
[2863.50 → 2864.76] She wouldn't like LinkedIn very well.
[2864.84 → 2866.64] Every time I log in, LinkedIn looks different.
[2866.64 → 2867.56] I'm like, what happened?
[2867.70 → 2869.28] Like how many people are working on this?
[2869.42 → 2871.18] It shows how rarely I log in, I guess.
[2871.18 → 2876.00] Can you imagine if physical products worked the same way that tech products do, like especially
[2876.00 → 2879.90] cloud based ones where they can change out from under you at any time?
[2880.14 → 2884.74] Like imagine if your toaster suddenly the buttons were like on the other side rearranged.
[2884.82 → 2884.92] Yeah.
[2884.92 → 2887.94] Like and you didn't even decide like you just wake up one day and like you can't find the
[2887.94 → 2890.26] buttons like the manufacturers like, oh, yeah, yeah.
[2890.26 → 2892.20] We changed them around, you know, following trends.
[2892.20 → 2895.52] I think that's the that's the argument with microwaves and ovens, right?
[2895.72 → 2898.90] Just, just like having all these extra settings that you don't need.
[2899.00 → 2901.46] It's like, oh, popcorn and for like chicken nuggets.
[2902.12 → 2902.82] Oh, my gosh.
[2902.86 → 2903.66] I totally agree.
[2903.84 → 2908.10] I've always wanted to have a microwave that just has a plus 30-second button and nothing
[2908.10 → 2908.46] else.
[2908.56 → 2909.24] Yeah, exactly.
[2909.34 → 2910.32] That's all you need.
[2910.40 → 2911.22] That's all you want to find.
[2911.22 → 2913.18] Plus, plus, plus, plus until you get to the thing you want, and you're done.
[2913.24 → 2915.84] Maybe if you wanted two buttons, you'd have plus 30 and plus one minute.
[2915.90 → 2916.44] Or a dial.
[2916.68 → 2916.92] Oh, yeah.
[2916.96 → 2917.20] A dial.
[2917.28 → 2917.42] Yeah.
[2917.48 → 2918.02] That's even better.
[2918.02 → 2918.34] Yeah.
[2918.88 → 2921.10] Simplicity is very valuable.
[2921.46 → 2924.72] And we as an industry dramatically underestimate that.
[2924.82 → 2924.98] Yeah.
[2925.08 → 2930.36] There's a perfect book on that called The Design of Everyday Things that goes into detail
[2930.36 → 2931.46] on this idea of simplicity.
[2932.28 → 2937.90] And to your point about developer economics, I believe we brought this up before, but Alex
[2937.90 → 2942.74] Russell had a post about just this idea of the developer experience beta switch, which
[2942.74 → 2947.92] talks about how developers tend to use JavaScript in a way that's better for them.
[2948.02 → 2948.98] Rather than for the users.
[2949.60 → 2952.42] And so he compares JavaScript to CO2.
[2952.86 → 2957.34] And just this idea that it's like a metaphor that as a polluter, you don't think about your
[2957.34 → 2957.72] emission.
[2957.96 → 2961.50] You just think about how is the convenience to yourself.
[2961.88 → 2965.44] So let's say you're like, I want to get from, I don't know, Boston to New York.
[2965.54 → 2969.80] I'm going to take a plane because it's faster versus like, you know, taking a train or whatever.
[2970.56 → 2975.46] But then you don't think you don't think actively about the carbon emission that comes about
[2975.46 → 2976.20] from that decision.
[2976.20 → 2979.96] And then other people have to like deal with that as a result.
[2980.62 → 2985.86] And so I think it's similar with how we build websites and web apps, whatever, web things.
[2986.44 → 2992.86] The way we build things today is just this concept of how will it make the developers happy.
[2993.36 → 2997.54] And as long as they're happy, the decision is a good one.
[2998.42 → 3001.02] Which I think is a false association.
[3001.02 → 3001.52] Yeah.
[3002.60 → 3007.40] And none of this is to say that we shouldn't have any emphasis on developer ergonomics or
[3007.40 → 3011.24] that we shouldn't have any, you know, that there's never a reason for a more complex interface
[3011.24 → 3013.22] or that, you know, we shouldn't have any change.
[3013.42 → 3017.30] It's just that all of these things, as everything in engineering, are trade-offs.
[3017.50 → 3018.66] They have consequences.
[3018.66 → 3026.60] And it is my belief that most people in the industry right now are not looking as closely
[3026.60 → 3030.24] at some of those consequences as might be valuable.
[3030.74 → 3034.32] One last thought back on simplicity before we call it a day.
[3034.42 → 3036.58] We mentioned making things simpler is better.
[3036.70 → 3040.24] I think it's Einstein quoted with everything should be made as simple as possible, but not
[3040.24 → 3040.64] simpler.
[3040.78 → 3041.90] I don't know if he actually said that.
[3041.90 → 3046.80] But remember the not simpler bit because, you know, maybe you're a chair manufacturer
[3046.80 → 3050.36] and you have the magical ability that From just mentioned of like changing products.
[3050.96 → 3054.36] And you think, you know, it's even simpler than a chair with four legs as a chair with
[3054.36 → 3056.12] three legs because that's one less leg.
[3056.26 → 3057.04] And so that's simpler.
[3057.38 → 3058.28] And so that's better, right?
[3058.56 → 3060.70] And then you pull a leg out from underneath your customer.
[3061.26 → 3062.50] So it depends.
[3062.96 → 3063.62] Don't make it.
[3063.86 → 3064.82] That smug smile.
[3065.26 → 3066.30] Full of puns.
[3066.32 → 3068.20] You're like, I made it funny.
[3068.48 → 3070.28] I'm just imagining somebody fall over.
[3070.28 → 3076.08] I'm just saying you just constructed this whole like statement in order to just say
[3076.08 → 3076.74] that one.
[3077.68 → 3080.24] Like, let me construct this type statement.
[3080.84 → 3081.88] We see what you did there.
[3082.20 → 3084.68] And at this point, I will start quoting random jokes.
[3084.94 → 3085.94] This is quite a call-out.
[3086.12 → 3088.68] As an appeal to authority, I will now start reading jokes.
[3089.50 → 3091.92] What do you call a cow with three legs?
[3092.92 → 3093.44] I don't know.
[3093.50 → 3094.28] You're going to have to tell us.
[3094.70 → 3095.18] Try tip.
[3095.60 → 3096.02] What do you say?
[3097.04 → 3097.80] Try tip.
[3098.18 → 3098.74] What do you call it?
[3098.80 → 3099.62] I can keep going.
[3099.62 → 3101.16] What do you call a cow with two legs?
[3101.30 → 3101.68] I don't know.
[3101.76 → 3102.40] Oh, gosh.
[3102.84 → 3103.62] I don't know.
[3104.38 → 3105.16] Lean beef.
[3105.48 → 3106.06] Oh, my goodness.
[3106.34 → 3106.94] Oh, gosh.
[3107.00 → 3107.66] It keeps going.
[3107.80 → 3108.72] One leg.
[3108.92 → 3110.20] This is an appeal to carnivores.
[3110.66 → 3111.38] Only carnivores.
[3111.38 → 3111.90] This is.
[3112.06 → 3113.62] You're being exclusionary.
[3114.22 → 3115.42] What do you call a cow with one leg?
[3115.52 → 3115.94] Oh, gosh.
[3115.96 → 3116.56] He keeps going.
[3116.96 → 3117.50] He keeps going.
[3117.64 → 3119.94] I can do dad jokes all day long.
[3120.18 → 3120.86] Well, tell us.
[3121.02 → 3124.50] That thing about, you know, what can you talk about for 30 minutes with no prep?
[3124.72 → 3125.36] Bad jokes.
[3125.74 → 3126.54] 100% there.
[3126.54 → 3127.10] Okay.
[3127.60 → 3129.74] Well, finish the logical conclusion.
[3129.88 → 3131.12] A one legged cow is what now?
[3131.66 → 3132.02] Steak.
[3132.36 → 3132.96] Oh, that's good.
[3133.04 → 3133.88] And then no legs.
[3134.76 → 3135.74] On the spot.
[3136.14 → 3136.92] Ground beef.
[3137.06 → 3137.50] Ground beef.
[3137.70 → 3138.64] Ground beef.
[3139.36 → 3139.92] Golf clap.
[3140.48 → 3142.78] We have to end the show, folks, before it ends itself.
[3143.58 → 3144.76] That's JS Party this week.
[3144.92 → 3146.82] Do let us know if you like our new segment.
[3146.96 → 3147.10] Yep.
[3147.16 → 3147.36] Nope.
[3147.44 → 3147.94] We had fun.
[3148.00 → 3149.72] We'll probably do it again unless you all hate it.
[3149.82 → 3151.32] So holler at us.
[3151.36 → 3152.08] We hope you enjoyed.
[3152.32 → 3153.44] We'll see you all next time.
[3153.44 → 3156.26] Also suggestions about maybe how to make the format better.
[3156.38 → 3159.56] If there were parts that you liked, parts you didn't like, that would be really helpful.
[3159.98 → 3161.16] And additional premises.
[3161.38 → 3163.46] So we have to come up with a format, and we come up with a premise.
[3163.64 → 3165.12] We have some ideas on other premises.
[3165.64 → 3171.00] But as Fears points out, if you mis word the premise a little bit, he'll use it to his advantage
[3171.00 → 3174.02] and undefined a part of it in order to win.
[3174.66 → 3177.26] And that's very tactical, but not fair.
[3177.40 → 3178.92] So help us out with premises.
[3179.30 → 3180.12] We'd love to hear from you.
[3180.12 → 3182.14] All right.
[3182.18 → 3184.02] Thank you for tuning in to JS Party this week.
[3184.16 → 3187.10] Tune in live on Thursdays at 1 p.m.
[3187.12 → 3190.18] U.S. Eastern at changelog.com slash live.
[3190.64 → 3193.20] Join the community and Slack with us in real time during the shows.
[3193.58 → 3195.00] Head to changelog.com slash community.
[3195.64 → 3196.28] And do us a favour.
[3196.42 → 3197.60] Share this show with a friend.
[3197.92 → 3198.80] Read us to have a podcast.
[3199.34 → 3200.88] Go into Overcast and favourite it.
[3201.28 → 3203.62] And thank you to Vastly, our bandwidth partner.
[3203.94 → 3205.46] Head to fastly.com to learn more.
[3205.88 → 3208.48] And we move fast to fix things right here at Changelog because of Rollbar.
[3208.48 → 3210.42] Check them out at rollbar.com.
[3210.72 → 3212.72] We're hosted on Leno cloud servers.
[3213.10 → 3214.70] Head to leno.com slash changelog.
[3214.78 → 3216.16] Check them out and support this show.
[3216.56 → 3218.60] Our music is produced by Break master Cylinder.
[3218.98 → 3222.04] And you can find more shows just like this at changelog.com.
