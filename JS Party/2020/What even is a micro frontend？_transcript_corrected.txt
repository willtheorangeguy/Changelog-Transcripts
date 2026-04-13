[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.40 → 18.16] This episode is brought to you by Rollbar.
[18.48 → 20.24] Move fast and fix things.
[20.52 → 22.62] Resolve errors and minutes and deploy with confidence.
[23.18 → 25.46] Head to Rollbar.com slash Changelog.
[25.54 → 26.34] Request a demo.
[26.50 → 27.38] Get started today.
[27.38 → 33.04] It's loved by developers, trusted by enterprises, and most of all, we use it here at Changelog.
[33.38 → 36.04] Move fast and fix things with Rollbar.
[36.44 → 39.34] Once again, Rollbar.com slash Changelog.
[50.42 → 54.72] Welcome to JS Party, your weekly celebration of JavaScript and the web.
[54.72 → 60.98] On next week's episode, Divya and I are talking Next, JS, and of course, more Jam stack
[60.98 → 63.38] with special guest Guillermo Rank from Site.
[63.62 → 68.24] Be sure to subscribe at Changelog.com slash JS Party or in your podcast app of choice.
[68.84 → 72.52] One last thing, make sure you listen to the end of today's show because we're giving away
[72.52 → 73.20] some free stuff.
[73.20 → 74.16] Okay.
[74.58 → 75.56] Party time, you all.
[86.86 → 87.62] All right.
[87.72 → 89.32] We are here for a party.
[89.60 → 90.32] I am Jared.
[90.48 → 92.70] I am joined by K-Ball and a special guest.
[92.76 → 93.36] What's up, K-Ball?
[94.46 → 95.16] I'm here.
[95.26 → 95.84] I'm ready.
[96.30 → 98.18] I've got my coffee this week, so we're set.
[98.84 → 100.28] Micro front ends.
[100.28 → 102.20] Is this a term, K-Ball, that you've come across before?
[102.70 → 105.00] Oh, I even wrote a post about it at some point.
[105.00 → 106.06] The good, bad, and the ugly.
[106.22 → 111.34] I'm in a micro front end Slack channel that I don't participate in, but because of that
[111.34 → 111.76] post.
[112.24 → 113.56] I think, Michael, you're in there too.
[114.16 → 114.76] Oh, really?
[115.52 → 115.76] Yeah.
[115.80 → 116.96] So, I let them know we're doing this.
[117.02 → 121.90] So, if there's any micro front Enders in the live audience, say hey in the, well, you
[121.90 → 125.60] can say hey in the micro front end Slack if you want, but we also have the changelog Slack.
[125.82 → 126.28] That's right.
[126.28 → 131.38] So, we're joined today by the person, the man who's writing the book or has written the
[131.38 → 131.52] book.
[131.58 → 132.72] It's not quite completely out.
[132.82 → 138.28] It's in Manning Early Access, but we'll be out very soon on micro front ends, Michael
[138.28 → 138.76] Gears.
[138.88 → 139.88] Michael, thanks for joining us.
[140.18 → 140.28] Hi.
[140.46 → 141.30] Thanks for the invitation.
[141.74 → 143.02] We are happy to have you.
[143.06 → 148.66] We're happy to discuss new trends, new techniques, new terms, and try to dive into them, explore
[148.66 → 151.42] them from our perspective, and hopefully help the audience as well.
[152.08 → 154.98] Figure out what is up with micro front ends.
[154.98 → 156.90] So, Ball has some exposure.
[157.56 → 161.86] I have enough exposure so far as I've been perusing through your book, Micro Front Ends
[161.86 → 162.60] in Action.
[163.42 → 167.00] But from your perspective, let's, well, before we get into the concept, let's get into you,
[167.06 → 169.56] Michael, a little bit and what brought you to this place to write the book.
[170.18 → 174.86] So, just share real quickly your career experience and when you were exposed to micro front ends
[174.86 → 176.24] or when you invented the term.
[176.30 → 177.14] I'm not sure of the background.
[177.36 → 180.02] So, help us out and help us all get on the same foundation.
[180.36 → 181.34] I didn't invent the term.
[181.54 → 181.76] Okay.
[181.76 → 182.66] Hi, Michael.
[182.92 → 185.40] I'm a software engineer from Germany.
[185.72 → 189.30] I work for a company called Newland Burn fur Information.
[189.46 → 192.84] And we specialize on building e-commerce systems.
[193.08 → 198.62] And this is where I came across this architecture for the first time, I guess.
[198.62 → 207.92] I think the first project we did was in 2014, where we were faced with an e-commerce project
[207.92 → 210.80] with more than 30, 40 people.
[211.56 → 217.96] And we needed a way to scale this development in a good way that was able to let us grow.
[217.96 → 223.02] And there we implemented a technique, which we called verticalization.
[223.24 → 224.50] So, having multiple teams.
[224.80 → 226.64] So, we had five teams at this time.
[227.00 → 232.02] And each team built one piece of the e-commerce system from top to bottom.
[232.24 → 232.66] So, everything.
[233.42 → 236.66] And then we integrated in the front end layer.
[237.06 → 237.66] So, yeah.
[237.72 → 239.02] This was our first project.
[239.02 → 244.50] And then, at this time, the term micro front ends wasn't around yet.
[244.50 → 252.58] I think it came up two or three years later in one of ThoughtWorks technology radar episodes.
[253.62 → 257.94] So, you were doing micro front ends, but there was no term for micro front ends.
[258.34 → 258.48] Yeah.
[258.56 → 263.96] People were calling it self-contained systems or front end integration for verticalized systems.
[263.96 → 268.12] So, many companies were doing it.
[268.34 → 273.50] So, companies like Spotify talked about this kind of organizational structures for a long time,
[273.60 → 278.52] but they didn't use the term micro front ends for it because it didn't exist.
[278.76 → 279.34] Didn't exist.
[279.44 → 282.00] So, what year was that when you started playing around with this architecture?
[282.54 → 285.60] In 2014, we did our first project.
[285.80 → 288.78] And then, we did a couple of them the years after.
[289.44 → 289.78] Okay.
[290.44 → 291.88] So, it was successful for you.
[291.88 → 294.80] And so, you decided we're going to keep going down this path.
[295.00 → 299.62] And then, I think 2017, I read, was an important year surrounding that?
[300.34 → 300.44] Yeah.
[300.48 → 303.90] In 2017, I had a little bit of time off.
[304.26 → 308.94] And so, one project was I had a little bit more breathing room in one project.
[309.12 → 315.66] And then, I sat down and had the feeling that I should write up the things we've learned to do this kind of projects.
[315.84 → 320.04] And the term micro front ends just was used by the ThoughtWorks folks.
[320.04 → 333.06] And so, I created a website called microfront ends.org where I described how we are doing it and how I think this concept can play together with modern web technology like JavaScript frameworks, for example.
[333.76 → 333.90] Gotcha.
[335.16 → 335.74] All right.
[335.80 → 336.66] So, enough background.
[336.84 → 339.50] Let's get into the concept and unpack it for folks.
[339.80 → 341.96] What's your executive summary?
[342.12 → 344.04] Like, when someone says, what's a micro front end?
[344.26 → 345.42] What do you say to that?
[345.42 → 347.02] What's a micro front end?
[347.08 → 349.06] Yeah, it's not really one specific thing.
[349.20 → 352.74] So, I'd like to talk about micro front end style architecture.
[352.98 → 354.62] So, this is the thing I just explained.
[354.72 → 358.66] So, having multiple teams which are working end to end.
[358.72 → 364.50] So, having front end developers and backend developers and data science guys, whatever, all in one team and multiple of these teams.
[364.76 → 368.80] And all of these teams deliver their piece of the front end.
[368.92 → 370.28] So, let's pick a real example.
[370.28 → 374.28] So, we are doing e-commerce, and we have one team who is dedicated to search.
[375.04 → 378.04] So, giving the customer the best search experience.
[378.42 → 383.62] Or we have another team called Team Inspire, for example, which job it is to inspire the customer.
[383.84 → 394.08] So, they do promotional stuff, or they do banners, teasers, email newsletters, but they also do recommendation strips other teams can embed into their pages.
[394.08 → 405.32] And so, we have different teams working on different aspects, and we need a strategy to assemble all of this together in a way that feels good for the customer in the end.
[405.88 → 405.98] Huh.
[406.52 → 409.64] So, it's more about team structure than it is about code structure?
[409.80 → 412.28] Or is it like the code structure follows the team structure?
[412.72 → 415.44] I would say both have to align to make it successful.
[415.62 → 418.44] But for us, it's very much about the team structure.
[418.44 → 428.34] You could implement micro-frontends in a team with you and five of your friends, but I wouldn't recommend this architecture just from a technical motivation.
[428.66 → 434.04] So, we always do it to scale projects and to be able to develop features faster.
[434.22 → 441.58] So, having cross-functional teams being more effective than one front-end team and microservices teams below this front-end team, for example.
[441.58 → 449.36] That actually, that is very similar to the lessons I think have been learned in the microservices' community, right?
[449.40 → 454.72] It's very similar in that microservices are not usually solving a product or technical problem.
[454.84 → 459.56] They're solving an organizational problem where it's how do we coordinate between all of these different pieces.
[459.80 → 465.72] I mean, to be honest, that's a world where I have much more direct hands-on experience, the microservices world, as compared to micro-frontends.
[465.72 → 473.00] But there are some interesting things that have been learned there that I'm curious if we can apply or figure out what the equivalent is in micro-frontends.
[473.26 → 483.56] So, one example there is that in microservices, the trade-off that you're making is you're trading off developer simplicity and organizational alignment.
[484.10 → 487.50] The downside of what you get instead is you get a lot more operational complexity.
[487.90 → 494.32] You've got to deal with all of these different coordinated services and deal with often like coordination problems and various other things.
[494.32 → 498.12] So, what's the equivalent trade-off in the micro-frontends world?
[498.34 → 506.52] Like, what do you get, and what is it that you're giving up or that you're having to take on when you adopt a micro-frontend approach?
[507.14 → 508.92] Yeah, I think it's quite comparable.
[509.40 → 512.60] So, micro-frontends as microservices is also a distributed system.
[512.60 → 522.80] So, developing a monolith is always easier than running a distributed system with multiple groups of teams that have to coordinate with each other.
[522.80 → 536.80] The trade-offs are different in the aspect that we now have to think about assembling a frontend out of pieces, which we wouldn't have to do if we just implemented a monolithic frontend.
[536.80 → 545.86] And with this assembly of multiple pieces, you also introduce redundancy, which you do with microservices as well.
[546.02 → 549.90] But with microservices, this redundancy is only server-side.
[550.00 → 560.20] So, you can offset the redundancy by increasing your server capacity, for example, which you can't do if you're putting more load on your customer's browser, for example.
[560.20 → 569.96] If you have five teams and all five teams use different JavaScript frameworks, the browser or your customer has to download them and has to cope with all of this code.
[570.06 → 575.38] So, you have to do a lot more planning in the frontend than you have to do in the backend.
[575.38 → 583.56] Yeah, so, because everything's coming together in the browser, the level of decoupling you can get is potentially lower.
[583.70 → 590.62] You have to do more sort of upfront planning to figure out what are your integration points so that you don't overload the browser.
[591.00 → 591.32] Interesting.
[591.32 → 600.82] So, kind of following on that, one of the things that microservices did is it changed sort of where the fault lines of where problems are.
[601.00 → 608.32] So, like, you had to be much, much more clear about your kind of integration points and contracts of integration.
[608.58 → 610.44] And in that world, it was the APIs.
[610.58 → 614.58] Like, you had to be very clear about your API structure, consistency, backwards compatibility.
[614.86 → 615.64] How are you doing that?
[616.18 → 618.16] What's the equivalent in the micro frontend world?
[618.16 → 621.52] Where are the new fault lines between these different micro frontends?
[621.64 → 623.46] Where are they having to connect?
[623.60 → 626.92] Or what are the things that you have to suddenly get crystal clear on?
[628.28 → 628.44] Yeah.
[628.94 → 636.94] I think APIs, like with microservices, you also have APIs or contracts between the teams in the frontend.
[637.06 → 644.74] So, if you are agreeing to integrate a recommendation frontend or a recommendation micro frontend from another team,
[644.74 → 651.84] you have to know how to speak to this, how to initialize this fragment, for example, which has to be documented.
[652.16 → 656.96] And you also have to deal with what happens if this fragment breaks.
[657.10 → 658.50] So, do you provide a fallback?
[658.62 → 661.74] Do you have strategy for providing fallbacks in general?
[662.18 → 669.92] So, you mentioned that if you are building a web app with five of your friends, you probably don't need this architecture.
[669.92 → 685.16] Where is the sweet spot of an organizational side or team size or maybe teams count where all of a sudden the payoffs become bigger than the drawbacks, and it becomes worthwhile to adopt this style architecture?
[685.16 → 688.38] I don't think there's a perfect size for it.
[688.44 → 695.48] But I think when you're running a monolith or having one team, and you're thinking about splitting this team,
[695.70 → 699.08] so we have multiple options like doing a frontend-backend split, for example,
[699.54 → 705.14] this is a good point to at least look at the microservices' architecture, micro frontends,
[705.46 → 708.78] look at the micro frontends architecture as an alternative.
[708.78 → 714.76] So, having two teams that are both cross-functional and have full stack in each team.
[714.94 → 721.10] The smallest project we did was with 10 people, and we are running an e-commerce shop with two teams.
[721.22 → 729.56] So, one team handled everything before the checkout and the other team did the checkout and the self-service area of the e-commerce system.
[729.80 → 732.20] So, this worked also really well.
[732.20 → 743.10] So, with a frontend-backend split, you tend to split more on technology or skill set.
[744.12 → 750.18] Whereas with a cross-functional split, you're splitting on the function.
[751.10 → 755.44] Give me some examples of a cross-functional team split because I've never done that.
[755.44 → 758.52] What is e-commerce?
[758.92 → 763.72] One's working on the cart and the other person is working on auth or not person, but team.
[763.82 → 766.32] What's a cross-functional split look like in teams?
[766.86 → 767.08] Yes.
[767.54 → 775.58] As we focus on e-commerce, we have a pattern or pattern that is applicable for many of our e-commerce customers.
[775.88 → 783.30] And the thing that works really well for us is looking at the customer and the way the customer takes throughout the e-commerce system.
[783.30 → 798.10] So, he starts at the homepage and then looks around, doesn't know what he's wanting to buy, then comes in the decision phase, having picked three products, for example, deciding which one to buy or which one would fit best.
[798.34 → 802.56] And then when he decided, he goes into the checkout flow and moves on.
[802.68 → 806.80] And we do our boundaries or our team cuts along these lines.
[806.90 → 812.24] So, we have one team that handles everything after the customer made his decision.
[812.24 → 816.92] So, we try to do the cuts from the customer need point of view.
[817.04 → 823.24] So, the jobs the customer needs to have done in order to finish the thing he's looking for.
[823.56 → 832.44] So, another example, if you're building a banking site, for example, you have an area where you can check your balances, do your money transfer.
[832.94 → 839.78] But you might also have an area where you can do your financing or look at housing loans, for example.
[839.78 → 842.10] And these areas are two different areas.
[842.42 → 848.42] And in these companies, most of the time, there are also different departments in a classical way of speaking.
[849.82 → 850.14] But, yeah.
[850.32 → 856.50] So, doing the cut from the user's perspective and the mode the user is in when he enters your site works well for us.
[857.30 → 857.74] Interesting.
[857.74 → 865.46] So, there we're talking about lines that are split more or less along route or along segment of the site where it's like, okay.
[865.84 → 870.14] You would almost look at your top level nav and say, like, here's this part of our team and here's that part.
[870.22 → 871.84] Based on your navigation almost, right?
[872.58 → 872.78] Yes.
[872.78 → 880.50] So, classical pages are a perfect indicator for here's something, a specific task the user wants to know.
[880.60 → 883.98] So, getting informed about one specific product, for example.
[884.66 → 893.86] And these are typically good boundaries, which they're not perfect because on one page there are things that are going on across teams.
[893.86 → 902.28] So, on the product page, you might also see recommendations or see shipping information, which is not the primary goal of the team who does the product page, for example.
[902.74 → 909.38] So, you have to do some assembly in some cases, but in general, pages are a good indicator.
[909.38 → 939.36] Thank you.
[939.38 → 969.36] So, Michael, you were talking a little bit, and just before the break, we were talking about the way,
[969.36 → 970.54] is that we can divide these out.
[970.62 → 972.58] We can divide them out by route or by specialty.
[973.24 → 974.64] Sometimes you might have a nav team.
[975.14 → 980.22] Those different division points have different implications for how you might do integration.
[980.50 → 985.28] So, can you talk us through some of the different types of integration that folks have come up with?
[985.34 → 988.16] I know there are some server-side solutions, there are client-side solutions.
[988.70 → 994.86] What is the spectrum of options that people are using here, and how does that end up, or what are the trade-offs involved with them?
[994.86 → 995.42] Yeah.
[995.42 → 995.60] Yeah.
[996.04 → 1006.94] As you mentioned, so the decision, if you want to integrate server-side or client-side, is essential because all the tools following this decision will be different.
[1006.94 → 1011.62] And I think we have two things we need to think about.
[1011.78 → 1020.36] So, first thing is, if we divide on page level, so we have two pages owned by one team and two other pages owned by the other team, this is pretty straightforward.
[1020.36 → 1029.68] So, you create a link between the teams, the teams need to know the link to the other team, and then they can link to there, send the user over, and the user can go back.
[1029.88 → 1031.70] For server-side, this is really easy.
[1031.96 → 1035.46] And for client-side, there are tools to create.
[1035.88 → 1042.50] So, there are tools that implement essentially in a meta-routing framework.
[1042.50 → 1049.82] So, you have run one application shell, and inside this application shell, you have two single-page apps.
[1049.96 → 1053.76] So, single-page app from team one and single-page app from team two.
[1054.04 → 1058.64] And if you're navigating inside these single-page apps, everything is as normal.
[1058.90 → 1070.82] And if you want to cross boundaries, the meta-framework kicks in and moves, clears one of the single-page app frameworks and introduces the framework from the other team.
[1070.82 → 1074.30] So, this is page transition moving from one page to the other.
[1075.20 → 1083.98] And the second concept is what we often call fragments or includable micro-frontends or whatever if we are talking about composition.
[1084.38 → 1089.78] So, having one page with UI fragments from different team on the same page.
[1089.98 → 1092.50] You need to assemble markup in essence.
[1093.04 → 1098.84] So, you have one team that, for example, delivers the product page, and they want to implement the recommendation strip.
[1098.84 → 1102.42] And there are different techniques for doing this.
[1102.66 → 1110.78] So, we are using server-side includes, which is a ancient concept available in all the web servers.
[1111.00 → 1116.64] So, we are using Nginx for it, which essentially is an HTML marker you put into your markup.
[1116.64 → 1130.76] And the Nginx, the web server, will fetch the markup from the URL from the other team who provides the recommendation strip, load the markup, puts it into the page, and then assembles the page and sends it over to the customer.
[1130.88 → 1135.96] So, in the browser of the customer, you don't notice anything from the assembly.
[1135.96 → 1140.96] And this is the server-side aspect.
[1141.22 → 1147.30] And if you're going client-side for composition, the technique we are using is web components.
[1147.78 → 1156.94] So, essentially, each fragment is a web component, which the API of the web component is available or known to the team that includes it.
[1156.94 → 1162.44] And the other team, which owns the fragment, provides the implementation.
[1162.74 → 1167.30] So, they can implement the recommendation strip in any way they want, load libraries, whatever.
[1167.84 → 1173.48] But the other team doesn't have to know about the internals of the web component, of the custom element, in essence.
[1173.86 → 1175.32] So, these are the techniques we are using.
[1175.32 → 1186.26] And there are also more sophisticated libraries or platforms out there, which will handle the stuff I talked about in a more easy-to-use way.
[1186.46 → 1199.22] So, a prominent player is the framework called Single SPA, which is the meta-router framework, but also companies like Zalando, which is in Europe, it's a big e-commerce player.
[1199.22 → 1203.34] They published a tool called Taylor, which does server-side integration.
[1203.94 → 1207.88] There's also a library called Podium, which is in a similar spirit.
[1208.24 → 1215.16] So, when you do these different types of integrations, like, for example, in your web components-based integration, how does that impact deployment?
[1215.44 → 1223.84] Like, when you do, for example, one of the micro front-ends changes, can you do an isolated deploy, or you've got to package everything together and deploy everything?
[1224.00 → 1225.36] Or, like, how does that work?
[1225.36 → 1225.84] Yeah.
[1226.38 → 1235.44] So, autonomy and being able to test and deploy your piece of the user interface of the system yourself as a team is one of the key factors.
[1235.44 → 1246.98] So, it's very important for us, at least, that the teams are able to deploy, to update, to move on with their UI without having to coordinate with the other teams.
[1246.98 → 1256.32] So, the recommendation fragment, for example, if the team owning it decides to, wants to add new functionality, they can do it.
[1256.40 → 1263.46] They just have to publish the new JavaScript or the new markup generation piece, whatever, and integration happens at runtime.
[1263.64 → 1269.04] So, the other teams shouldn't notice any change from the integration perspective.
[1269.04 → 1270.04] Nice.
[1270.04 → 1270.36] Nice.
[1270.60 → 1276.98] And then, for some of the server-side coordination pieces, that's similarly, like, they can independently deploy?
[1278.20 → 1278.46] Yes.
[1278.46 → 1291.58] So, the SSI technique, or there is, when you talk about CDNs, ESI, so edge-side includes, is a comparable technique, is something that runs just before the page is delivered to the customer.
[1291.74 → 1296.70] So, the pieces are assembled before, just before they go out.
[1296.70 → 1300.96] So, you have the possibility to dynamically assemble, if you want.
[1301.20 → 1306.26] You can also implement caching when you say, okay, the navigation only changes every five minutes, for example.
[1306.46 → 1310.36] It's easy to do HTTP caching beneath this integration layer.
[1311.02 → 1311.50] Interesting.
[1311.70 → 1317.18] So, at this point, we're back into kind of the operational complexity.
[1317.38 → 1324.42] So, if I'm understanding correctly, you have a set of independent web servers that are serving these independent micro frontends.
[1324.42 → 1330.32] And they might just be static files, or they might be PHP, or Ruby, or whatever servers that are doing this.
[1330.32 → 1338.06] And then, you have a server that's running Nginx, or something else, that's doing this edge-side include, that's stitching everything together.
[1338.24 → 1341.24] And then, that's what's talking out to the final client?
[1342.40 → 1342.58] Yes.
[1342.96 → 1352.20] The ESI, or SSI, is the step that gets done just before the complete markup gets sent to the customer to render it in the browser.
[1353.46 → 1354.02] Interesting.
[1354.42 → 1354.66] Okay.
[1354.92 → 1356.20] That's kind of a runtime stitching.
[1356.72 → 1356.94] Yes.
[1357.00 → 1358.62] Are there build-time stitching?
[1358.76 → 1362.80] So, if you were doing, like, Jam stack-style pre-compilation, things like that.
[1362.92 → 1365.02] I know Chris brought up Jam stack in the chat.
[1365.02 → 1373.32] But, like, if you're doing a Gatsby-style pre-compile, or Svelte-style pre-compile, are there solutions to do that at a micro frontend level that does essentially,
[1373.82 → 1381.02] server-side includes, but it then pre-builds everything and publishes out the final frontend to, like, a CDN or something?
[1381.02 → 1386.90] After you stitch together the user interface paths, you can do it.
[1386.90 → 1396.28] But I think, at least from the values we associate with this architecture, we wouldn't be able to do the independent deployment, I guess.
[1396.28 → 1400.58] So, for us, we don't do integration at build time.
[1400.72 → 1408.22] We're only doing it at runtime to give every team the opportunity to update and release their user interface as they feel.
[1408.22 → 1414.66] Without having to push a button to please assemble everything together in a new form.
[1415.10 → 1424.48] Which could be an internal feature for an assembly service, for example, to an optimization you could do in there, but we are not doing this.
[1424.48 → 1434.34] Yeah, I could see where it would make some sense to still be able to deploy autonomously, but basically request, at a certain point in time,
[1434.46 → 1440.54] everybody else's micro frontends that you need in order to deploy the entire application and just go.
[1441.28 → 1445.34] Or whichever ones have changed, or, you know, you could probably get as fancy as you wanted with that,
[1445.38 → 1448.16] but maybe it's solving a problem that is a premature optimization.
[1448.16 → 1454.04] If you guys have been doing this for years in this style and haven't run into that as a need,
[1454.80 → 1460.18] do you think that's something that other teams might desire, or is it just kind of non-issue in practice?
[1460.72 → 1467.24] We are running quite large platforms with this technique, but we are not at Amazon scale or whatever.
[1467.54 → 1474.44] So, it's definitely possible that the things we are using are not built for doing a much larger integration.
[1474.44 → 1478.84] You need more optimization in the integration points than we are currently practicing.
[1479.36 → 1482.36] One thing that happened with microservices was a bit of a brush fire of adoption
[1482.36 → 1489.42] when people started to use them and talk about them and advocate that style architecture
[1489.42 → 1498.36] because it seemed to solve a need that so many organizations had or thought they had.
[1498.68 → 1502.50] Turns out you can make a big ball of mess with microservices just like you can with a monolith.
[1502.50 → 1508.88] That being said, I'm curious if there are other teams, organizations, maybe bigger or smaller
[1508.88 → 1516.00] than the teams you've been working with that are adopting micro frontends or at least testing the waters.
[1516.52 → 1516.66] Yeah.
[1516.76 → 1523.78] In the last years, I could see a lot of adoption of companies coming out and saying,
[1523.94 → 1529.58] okay, we also did this for a long time, and we also didn't call it micro frontends,
[1529.58 → 1531.16] but this is how we do it.
[1531.16 → 1537.96] So, companies like IKEA or I mentioned Zalando before, which is a big German e-commerce player.
[1538.16 → 1543.32] They also did it way before the micro frontends term was a thing, Spotify.
[1544.10 → 1549.20] The sports streaming service DAZN also uses this technique and promotes it strongly.
[1549.20 → 1557.64] But also large players like SAP, so the enterprise company they published in October, I guess,
[1558.24 → 1565.94] published a tool to do micro frontends' integration, more platform-y style, not in the way we do it,
[1566.00 → 1572.94] but they also are playing around with this concept and integrating different applications into one view with similar techniques.
[1572.94 → 1581.64] So, when that kind of zeitgeist happened, people then suddenly were all encountering whole new failure modes with microservices
[1581.64 → 1583.52] that weren't really there for monoliths.
[1583.58 → 1589.30] So, like one of the big failure modes is this sort of coordination problems and if you get an error on one,
[1589.48 → 1594.96] like how that cascades through the system or especially like if you have poorly planned timeout regimes,
[1595.10 → 1597.82] you can have one timeout that triggers another timeout that triggers another
[1597.82 → 1601.76] and just kind of bring down all these systems with cascading problems.
[1602.32 → 1608.28] And that then sparked new systems like Kubernetes, and it sparked different approaches.
[1608.80 → 1611.52] What are some of the equivalent things going on in micro frontends?
[1611.58 → 1613.70] What are the new failure modes that we're seeing?
[1613.88 → 1618.36] And then what are the new approaches or systems that are addressing those failure modes?
[1618.84 → 1619.70] Interesting question.
[1619.70 → 1627.58] So, the most obvious one is one system is down, and it's not able to produce its frontend, for example,
[1627.58 → 1635.72] and that you need the concept of providing a fallback or at least thinking about cases where different parts of your page might not be present
[1635.72 → 1637.44] or might be slow or whatever.
[1637.64 → 1644.82] So, having to wait for the slowest fragment when you're doing server-side integration is definitely something you didn't have to do before
[1644.82 → 1649.82] because everything was, the data was fetched in one piece, rendered and then put out.
[1649.90 → 1653.00] And now you have multiple teams doing all of this at the same time.
[1653.00 → 1655.92] When one team is slow to plan at least.
[1656.14 → 1663.06] So, how long do you wait until you do the final delivery when you decide to leave this one out?
[1663.06 → 1666.76] So, this is one failure mode.
[1667.02 → 1672.88] And one thing we, when we do this kind of projects, we use a concept which is called self-contained systems.
[1673.08 → 1681.00] So, the idea of having the system that a team owns be as self-contained as possible, holding its own data,
[1681.16 → 1684.94] don't use a central data store together with the other team.
[1685.06 → 1687.78] So, we do replication in the background, for example.
[1687.78 → 1691.68] So, we have one team who owns the master product database, for example.
[1691.84 → 1696.20] They also do the UI where the people from the company can enter new products.
[1696.76 → 1698.90] And all other teams also need product data.
[1699.04 → 1703.10] Not the full database, but at least a name and an image, maybe a price.
[1703.10 → 1709.26] And we do replication between the systems to cope for the case of one team failing.
[1709.50 → 1716.24] So, that we don't have this cascade of one thing goes down, and the other teams have to deal with it.
[1716.24 → 1720.52] Other than losing the UI parts, that will definitely be gone when one team goes out.
[1720.70 → 1726.02] So, in this case, adopting microfinance forced you into a microservices' architecture as well.
[1726.44 → 1726.84] Definitely.
[1727.42 → 1729.86] Yeah, definitely a huge amount of power.
[1729.86 → 1734.82] So, there are also people who are coming from the microservices world, which say,
[1734.94 → 1740.40] okay, the thing you are now calling microfinance are just microservices with UIs,
[1740.52 → 1744.70] which we were promoting for a long time, but nobody implemented them.
[1745.16 → 1745.86] Ah, interesting.
[1746.68 → 1746.96] Uh-huh.
[1747.52 → 1753.34] So, are there situations in which you have microfinance that aren't tied into microservices?
[1753.34 → 1759.12] I've also talked to people who are, as we are using microservices and the microfrontends,
[1759.28 → 1765.50] as we are using the term microfrontends, and we are practicing it, we also associate the system with the team.
[1765.50 → 1770.68] And we try to do the team as cross-functional as possible.
[1771.22 → 1777.88] But you could also use this, the composition techniques or this single spa approach, for example,
[1777.96 → 1782.50] the application shell just in the frontend, just doing a classical backend, for example,
[1782.60 → 1786.94] but having multiple frontend teams sitting on the same backend or GraphQL layer or whatever,
[1786.94 → 1793.72] and just using the microfrontends techniques to assemble pages and distribute frontend work to multiple teams.
[1793.80 → 1797.98] This is also something that's quite possible, but it's not the thing we are doing.
[1798.50 → 1800.04] Yeah, that's fascinating.
[1800.32 → 1805.30] One thing that it makes me wonder too now, so one of the techniques that I've seen coming out,
[1805.54 → 1807.50] I think Facebook is doing this and some other folks,
[1807.68 → 1812.92] is around trying to prevent data cascades in the frontend by essentially bundling up,
[1813.26 → 1814.96] having components own their own data queries,
[1814.96 → 1819.26] but then having a preprocessing layer that bundles up those queries and puts them at the top level.
[1819.96 → 1821.84] So like Relay coming out of Facebook did this,
[1821.86 → 1826.58] and I've seen a couple folks addressing alternative stuff that is not tied into Facebook's ownership.
[1826.96 → 1832.18] Is there anything like that in the microfrontend world where you could essentially have each microfrontend,
[1832.58 → 1834.48] if, for example, you were doing what you just described,
[1834.56 → 1836.18] where they're all talking to a GraphQL database,
[1836.36 → 1839.78] so there's a unified backend layer that they could all talk to.
[1839.90 → 1841.20] Even if underneath that GraphQL,
[1841.20 → 1844.58] you might have the data being sourced from different microservices or whatever.
[1844.96 → 1849.66] Is there any way these microfrontends can, for example, publish their data needs,
[1849.92 → 1852.88] such that the stitching layer, the aggregation layer,
[1853.00 → 1858.40] whether it's single spa or whether it's server-side integration or something like that,
[1858.58 → 1864.80] can pull up those data needs and fetch them in a single query or a set of single queries?
[1864.80 → 1868.70] So reduce the overhead, eliminate the number of requests.
[1868.70 → 1868.78] Exactly.
[1869.12 → 1871.62] Or reduce redundancy, for example.
[1872.12 → 1877.02] So I think you could build it, but I haven't read from someone who did it.
[1877.20 → 1880.02] So you're opting for other priorities.
[1880.28 → 1883.24] So you are accepting a single backend,
[1883.62 → 1886.28] and I think you are in a tighter coupling mode.
[1886.28 → 1891.00] So your language, what is a product, has to be the same across all teams.
[1891.00 → 1897.68] And the thing we are advocating comes more from the domain-driven design world,
[1897.76 → 1900.94] where you accept that the term product means something completely different
[1900.94 → 1902.40] when you talk to warehouse people,
[1902.78 → 1904.56] whereas when you talk to marketing people,
[1904.66 → 1907.28] they think about a product in a completely different way.
[1907.60 → 1910.76] And yeah, so dividing the data model into multiple parts
[1910.76 → 1914.32] is the thing that might get into your way
[1914.32 → 1916.56] if you're trying to build a large application
[1916.56 → 1919.36] where people don't talk to each other at this point.
[1926.96 → 1927.94] What up, nerds?
[1927.94 → 1929.64] I've got some pretty awesome news to share with you.
[1929.96 → 1933.78] Pluralsight is totally free for the entire month of April.
[1934.18 → 1934.66] I'm not kidding.
[1934.92 → 1937.16] Seriously, head to pluralsight.com slash changelog
[1937.16 → 1938.66] and skill up while you stay at home.
[1938.96 → 1942.68] For the entire month of April, you'll get access to over 7,000 courses
[1942.68 → 1946.34] from experts in software development, security, cloud, and data,
[1946.56 → 1948.24] there's never been a better time to skill up.
[1948.48 → 1950.18] Head to pluralsight.com slash changelog.
[1950.28 → 1952.96] Again, pluralsight.com slash changelog.
[1965.84 → 1968.22] One thing you mentioned in that last bit, Michael,
[1968.38 → 1974.10] was around wanting to really allow teams to go their own way
[1974.10 → 1976.98] and make their own decisions and all of that sort of thing.
[1977.04 → 1981.88] But that can also potentially lead to catastrophic performance implications.
[1982.42 → 1985.56] One of the early criticisms I saw of micro frontends
[1985.56 → 1990.42] is it now becomes really easy to have a frontend application
[1990.42 → 1992.48] that's loading all of React and all of Vue
[1992.48 → 1993.86] and maybe even all of Angular
[1993.86 → 1996.64] because each team is making their own decisions
[1996.64 → 1999.02] and suddenly you've got megabytes of JavaScript
[1999.02 → 2000.62] going out to your browser.
[2000.62 → 2006.54] So one, how do you mitigate that?
[2006.96 → 2010.18] And two, what are the practices you've started seeing?
[2010.34 → 2012.52] Are people actually doing that
[2012.52 → 2015.84] or are people doing sort of a partway along the spectrum
[2015.84 → 2017.86] where they at least agree on a shared framework?
[2017.98 → 2020.20] Maybe we're all going to use React, or we're all going to use Vue.
[2020.46 → 2023.58] What are you seeing in that sort of space?
[2023.58 → 2030.16] Yes. So the feature of being able to use everything together,
[2030.26 → 2034.48] which is the thing we pull out to demonstrate the number,
[2034.76 → 2039.46] the amount of autonomy that this architecture should provide
[2039.46 → 2043.82] is the first thing that jumps to mind for many people
[2043.82 → 2045.38] to react to this in this,
[2045.60 → 2047.14] oh my God, the site will be a slow way.
[2047.38 → 2049.58] And in practice, I haven't seen projects
[2049.58 → 2052.02] projects where you open one page
[2052.02 → 2054.04] and five frameworks are loading
[2054.04 → 2057.78] just to do one simple microphone, for example.
[2058.50 → 2059.52] So in the teams we did,
[2059.90 → 2063.76] creating a notion or an awareness for performance
[2063.76 → 2066.06] was always a critical first step.
[2066.38 → 2069.26] So getting your performance monitoring,
[2069.40 → 2071.14] talking about performance budgets,
[2071.38 → 2074.40] how large should a product page be, for example,
[2074.76 → 2077.52] are all discussions we shouldn't have too late in the process
[2077.52 → 2079.38] to get everyone on the same page.
[2079.56 → 2082.10] So measuring your performance is,
[2082.32 → 2083.62] I think, it's key number one.
[2083.70 → 2086.96] And then you can talk about reducing the framework load
[2086.96 → 2089.76] or implementing restrictions, for example.
[2090.48 → 2092.16] And we had different setups.
[2092.28 → 2093.76] So we had one project where we said,
[2093.82 → 2095.06] okay, everyone is on React.
[2095.14 → 2096.36] React is our default framework.
[2096.36 → 2100.06] And we will allow for teams to upgrade independently,
[2100.40 → 2104.68] but also upgrading should be done within three weeks, for example.
[2104.68 → 2107.92] So you might have periods where an older version
[2107.92 → 2110.72] and a newer version of React are used in tandem,
[2110.94 → 2113.82] but in the most time, everyone uses the same library
[2113.82 → 2116.88] and it only has to be downloaded once, for example.
[2117.10 → 2119.80] Another interesting trend we are starting to see
[2119.80 → 2122.80] is the appearance of smaller libraries.
[2122.98 → 2125.72] So in the current project, we are using Preach and HyperApp.
[2125.84 → 2127.10] So two different frameworks.
[2127.36 → 2130.28] And we have five teams and some teams use Preach,
[2130.38 → 2131.42] some teams use HyperApp.
[2131.42 → 2135.58] And these frameworks are so small that the effort
[2135.58 → 2137.22] on centralizing this framework,
[2137.36 → 2139.56] so HyperApp is one or two kilobytes in size
[2139.56 → 2142.74] and everything else you build will be larger than HyperApp.
[2142.96 → 2144.58] So this becomes a non-issue.
[2144.70 → 2146.68] You don't have to talk about the load
[2146.68 → 2149.36] because you're not using something that introduces load.
[2149.52 → 2154.40] And I think trends for stuff like Svelte or Stencil,
[2154.64 → 2157.64] which reduce the framework overhead completely,
[2157.82 → 2160.76] so the code grows linear to the amount of feature you build,
[2160.76 → 2163.56] will play in this direction even further.
[2163.76 → 2165.54] So you minimize the overhead.
[2166.50 → 2169.50] Yeah, it does seem like runtime-less frameworks like Svelte
[2169.50 → 2171.62] are a perfect match for this
[2171.62 → 2173.66] because you can bundle down your components,
[2174.12 → 2176.04] make them into web components or what have you.
[2176.12 → 2177.48] You don't have to ship a big runtime.
[2178.14 → 2181.60] And it really does grow with your feature size.
[2181.82 → 2183.92] You don't have that fixed overhead of the runtime.
[2184.64 → 2186.70] And you have, via the UI component structure,
[2186.82 → 2189.36] you have code splitting built in, I guess.
[2189.36 → 2190.64] So you have different teams
[2190.64 → 2193.12] and each team only delivers the stuff
[2193.12 → 2196.02] that's necessary for their page.
[2196.16 → 2197.44] So you don't have one team
[2197.44 → 2200.58] that builds a complete JavaScript bundle for all the pages,
[2201.10 → 2204.40] which you manually have to implement code splitting as well.
[2204.40 → 2209.68] How do you deal with things like inter-micro front-end communication,
[2209.84 → 2210.48] if that's a thing?
[2210.66 → 2212.12] I know you're supposed to be decoupled as possible,
[2212.36 → 2214.80] but in the real world, things happen,
[2215.28 → 2217.84] and certain data or events or things.
[2218.06 → 2219.58] Is Pub Sub the best practice?
[2219.70 → 2220.84] Or how do you guys actually deal with
[2220.84 → 2224.38] when you do need to communicate between multiple micro front-ends?
[2225.06 → 2226.62] Yeah, Public subscribe.
[2226.78 → 2229.86] So having an event system is definitely a way to go.
[2229.86 → 2233.76] What we like to do is piggyback on the native features of the browser.
[2233.98 → 2235.42] So using custom events, for example,
[2235.52 → 2238.38] if you're including the recommendation strip, for example,
[2238.60 → 2241.64] and an event occurs inside this recommendation strip,
[2241.72 → 2243.92] maybe a customer marked a product as whatever,
[2244.30 → 2245.92] and the outer page wants to know about it,
[2246.32 → 2248.06] the fragment or the included microphone
[2248.06 → 2249.66] can just bubble up an event,
[2249.92 → 2253.02] which is published in the documentation of the microphone,
[2253.22 → 2255.70] and the team that uses it can react to it.
[2255.70 → 2258.80] So if you're having a parent-child situation
[2258.80 → 2262.04] or doing just plain events on the window document,
[2262.24 → 2263.38] so publishing events there
[2263.38 → 2265.60] and allowing everyone to read from there,
[2266.02 → 2267.64] so that's a good way to doing it.
[2267.72 → 2270.26] So essentially an event bus style approach?
[2270.46 → 2270.86] Yes.
[2271.70 → 2272.18] Interesting.
[2272.46 → 2273.34] What about code sharing?
[2273.48 → 2275.84] So we talked about small framework.
[2275.90 → 2277.00] We talked a little bit about code sharing,
[2277.20 → 2280.46] but when it comes to not necessarily libraries
[2280.46 → 2282.80] that are third-party dependencies or frameworks,
[2283.12 → 2284.28] component frameworks and whatnot,
[2284.28 → 2286.18] code sharing between teams,
[2286.82 → 2288.54] business logic shared between teams,
[2288.68 → 2290.48] database, GraphQL things.
[2291.18 → 2294.06] Is there a known best practice
[2294.06 → 2297.56] for how you go about not re-implementing 16 wheels
[2297.56 → 2299.12] if you have 16 micro frontends
[2299.12 → 2300.38] that build into an application?
[2301.74 → 2301.90] Yeah.
[2302.22 → 2304.30] So the way we do it is
[2304.30 → 2307.00] so distributing business logic
[2307.00 → 2309.28] is so logic specific for our use case.
[2309.70 → 2311.96] Other components that multiple teams can use
[2311.96 → 2313.48] is something we try to avoid.
[2313.48 → 2315.80] We have some areas where we think,
[2316.16 → 2317.60] okay, I've built a complex thing
[2317.60 → 2320.80] and I couldn't use a standard NPM library for it.
[2320.86 → 2322.30] I had to build it on my own
[2322.30 → 2323.96] and I don't want other teams to build it.
[2324.16 → 2327.56] Then we allow publishing this library to other teams,
[2327.72 → 2330.16] but we encourage the people who are publishing it
[2330.16 → 2332.16] to run it as an internal open source project.
[2332.16 → 2335.48] So do proper versioning to do proper documentation
[2335.48 → 2337.50] and everything that comes with it
[2337.50 → 2339.44] to enable other people to,
[2340.06 → 2341.92] in the worst case, fork it and run with it
[2341.92 → 2345.08] so that we don't introduce coupling
[2345.08 → 2348.60] by shipping a poorly documented library
[2348.60 → 2350.74] that suddenly everyone relies on.
[2350.74 → 2353.52] Yeah, I think it forces you,
[2354.06 → 2356.12] I mean, in the same way that microservices
[2356.12 → 2359.42] forces you to be very strict
[2359.42 → 2360.76] about your API versioning
[2360.76 → 2362.66] and the contracts that you make there,
[2363.18 → 2365.62] this forces you into those same levels
[2365.62 → 2367.64] of kind of awareness and concern
[2367.64 → 2369.00] for publishing UI components.
[2369.00 → 2372.08] Yeah, it's kind of a slow-down to go faster thing
[2372.08 → 2373.86] because there's a certain rigidity
[2373.86 → 2376.54] and thoroughness, for lack of a better term,
[2376.62 → 2380.28] required in order to do this correctly and well
[2380.28 → 2383.88] that will slow you down in the small,
[2384.12 → 2387.52] but if it all works out to allow for these advantages
[2387.52 → 2389.48] of team autonomy
[2389.48 → 2391.40] and the other things you spoke about, Michael,
[2391.50 → 2394.28] ends up on a large being a win,
[2394.42 → 2396.20] even though in these small little ways
[2396.20 → 2397.50] you're actually slowing down.
[2397.50 → 2400.82] For instance, to really document the API of this thing.
[2401.38 → 2403.34] I think that's why it comes back to this
[2403.34 → 2405.22] being really an org structure thing
[2405.22 → 2406.84] rather than a product thing, right?
[2406.92 → 2409.28] Like you implement these approaches
[2409.28 → 2411.78] when the communication challenges
[2411.78 → 2413.48] of your org structure get large enough
[2413.48 → 2414.96] that you reap a lot of benefits
[2414.96 → 2417.02] by shrinking things down into isolated teams.
[2417.84 → 2420.30] And then you have to formalize
[2420.30 → 2422.18] the communication structures across those teams,
[2422.24 → 2423.30] which include code
[2423.30 → 2425.40] and places where you're sharing things.
[2425.40 → 2430.20] But because communication overheads rise exponentially
[2430.20 → 2431.42] with the number of people,
[2431.42 → 2433.82] that can be really valuable beyond some point.
[2434.08 → 2434.86] And it sounds like, Michael,
[2434.94 → 2437.68] you've seen that value even be 10 people
[2437.68 → 2439.16] where you can split across two teams
[2439.16 → 2441.14] and suddenly you see a pretty big increase.
[2441.34 → 2441.94] Yes, definitely.
[2442.10 → 2443.74] Coming to a decision with five people
[2443.74 → 2446.22] is much easier than coming to the same decision
[2446.22 → 2446.98] with 10 people.
[2446.98 → 2449.42] Any other words of wisdom or experience
[2449.42 → 2450.88] that you've gained,
[2451.14 → 2452.52] maybe things that you're putting in the book
[2452.52 → 2453.88] that we haven't talked about today
[2453.88 → 2455.40] that you would love to talk about?
[2455.98 → 2457.86] We talked about shared libraries
[2457.86 → 2459.94] and the biggest shared library
[2459.94 → 2461.96] we have in all of our project is,
[2462.12 → 2463.48] you mentioned UI components.
[2463.62 → 2465.30] So we have a design system
[2465.30 → 2468.66] from the start for all teams to use.
[2469.22 → 2471.46] So, and we're distributing it as a library,
[2471.62 → 2473.56] as an NPM package, for example,
[2473.56 → 2475.54] that other teams can use,
[2475.70 → 2477.84] pick the UI elements they need
[2477.84 → 2480.58] and use it inside their MicroFrontence UI
[2480.58 → 2483.12] to at least have the same building blocks
[2483.12 → 2484.82] for everyone to create a UI,
[2485.04 → 2487.94] which does not say that every UI feels the same.
[2488.08 → 2490.12] There are also UX stuff
[2490.12 → 2492.72] and talking and distributing knowledge
[2492.72 → 2495.16] or creating a shared vision between teams
[2495.16 → 2497.90] that have to be done on an interpersonal way.
[2498.56 → 2499.70] But having a design system,
[2499.76 → 2501.16] I think is crucial
[2501.16 → 2503.50] if you want to build something larger
[2503.50 → 2505.98] which should go out to your end customer.
[2506.78 → 2507.52] Yeah, that's huge
[2507.52 → 2508.96] because one of my biggest concerns
[2508.96 → 2511.38] when folks started talking about MicroFrontends
[2511.38 → 2512.82] and is actually a concern
[2512.82 → 2515.84] also related to this whole global CSS
[2515.84 → 2518.12] versus CSS and JS and things like that
[2518.12 → 2519.28] is if you're not careful,
[2519.64 → 2521.92] you create a set of disjointed experiences
[2521.92 → 2525.38] and people interpret user experiences,
[2525.52 → 2526.34] they interpret your product,
[2526.42 → 2527.72] they interpret your company holistically.
[2527.96 → 2529.22] They don't think about it isolated
[2529.22 → 2530.50] in the same way developers do.
[2530.50 → 2533.18] And so having something like a design system
[2533.18 → 2534.88] that can weave it all together
[2534.88 → 2538.84] and make sure that at least from a visual
[2538.84 → 2542.62] and hopefully at least from parts of your experience level,
[2542.70 → 2544.78] it feels consistent is huge.
[2545.42 → 2545.94] Yeah.
[2545.94 → 2549.86] Well, the book is called Micro Frontends in Action.
[2549.86 → 2551.32] As I mentioned at the top,
[2551.40 → 2553.38] it is part of Manning's early access program.
[2553.54 → 2555.60] Michael is putting the final touches on the book
[2555.60 → 2557.70] so it'll be complete soon.
[2558.14 → 2559.32] If you are interested,
[2559.62 → 2560.96] thanks to our friends at Manning,
[2561.02 → 2563.56] we do have three free copies of the e-book
[2563.56 → 2564.60] that we will be giving away.
[2564.60 → 2566.48] So just pop open your show notes,
[2566.56 → 2568.74] leave a comment on the episode page in the discussion.
[2569.12 → 2570.26] I will receive that comment.
[2570.38 → 2571.04] K-Ball will get it.
[2571.08 → 2571.54] Michael will get it.
[2571.56 → 2573.52] We can start a discussion in the comments
[2573.52 → 2574.94] about Micro Frontends.
[2575.32 → 2576.00] Share your thoughts.
[2576.18 → 2577.82] Do you think this is a good practice?
[2577.94 → 2578.68] What are your concerns,
[2578.80 → 2579.68] questions you may have
[2579.68 → 2580.96] that we didn't answer on the show?
[2581.02 → 2582.08] You can ask Michael directly.
[2582.74 → 2584.20] Each person who comments will be entered
[2584.20 → 2586.04] to win a free copy of the e-book.
[2586.46 → 2589.48] We also have a discount code
[2589.48 → 2591.62] off of Manning's entire catalogue.
[2591.74 → 2593.04] This is incredibly generous of them.
[2593.04 → 2596.24] If you use the code PODJSPARTY20,
[2596.72 → 2599.44] you will receive 40% off your purchase.
[2599.54 → 2600.56] That's not 20% off.
[2601.12 → 2603.02] That 20 in the code means 2020.
[2603.92 → 2605.24] You'll save 40% off.
[2605.30 → 2606.22] So if you want the print book,
[2606.52 → 2608.64] if you're trying to get something else from Manning,
[2608.70 → 2609.62] you can use that
[2609.62 → 2613.38] and save a bundle on their awesome books.
[2613.50 → 2615.06] Michael, thanks so much for joining us today.
[2615.56 → 2616.52] This was a great conversation.
[2616.64 → 2617.90] I think a great intro for me
[2617.90 → 2619.92] to Frontend or Micro Frontends
[2619.92 → 2620.84] and Frontends in general.
[2620.84 → 2621.52] What's a Frontend?
[2621.52 → 2624.20] And K-Ball, thanks for playing Wing.
[2624.26 → 2625.30] You had a lot of great questions.
[2625.56 → 2626.24] That's our show
[2626.24 → 2627.78] and we will talk to you next time.
[2631.14 → 2633.22] Thank you for listening to JS Party.
[2633.60 → 2635.88] We appreciate your time and your attention.
[2636.26 → 2637.48] And thanks again to Manning
[2637.48 → 2639.28] for being so generous with their authors
[2639.28 → 2641.12] and awesome catalogue of books.
[2641.58 → 2642.26] One more time,
[2642.36 → 2645.42] that 40% discount code is PODJSPARTY20
[2645.42 → 2647.20] and it works on their entire library.
[2647.56 → 2648.74] What's better than 40% off?
[2648.94 → 2649.86] 100% off.
[2649.86 → 2651.80] Enter to win a free e-book copy
[2651.80 → 2653.32] of Micro Frontends in action
[2653.32 → 2655.38] simply by commenting on this episode
[2655.38 → 2656.66] on changelog.com
[2656.66 → 2657.92] slash JS Party
[2657.92 → 2659.10] slash 121.
[2659.36 → 2661.80] That discussion link is also in your show notes.
[2662.20 → 2663.62] Thanks to Michael Gears for joining us
[2663.62 → 2665.30] and K-Ball for co-hosting with me.
[2665.88 → 2667.44] Our music is produced by the Beat Freak,
[2667.56 → 2668.44] Break master Cylinder,
[2668.84 → 2670.66] and we're brought to you by awesome sponsors.
[2670.96 → 2673.00] Thank you Vastly, Linde, and Rollbar.
[2673.36 → 2674.34] That's all for now.
[2674.66 → 2675.82] We'll talk to you next time.
[2675.82 → 2675.86] We'll talk to you next time.
[2675.86 → 2679.84] We'll talk to you next time.
[2679.84 → 2682.78] Music All powered by
[2682.78 → 2683.80] allctarresponsries
