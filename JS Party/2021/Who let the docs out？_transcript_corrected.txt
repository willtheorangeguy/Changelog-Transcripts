[0.00 → 2.80] The more we learn about it, the better our prototypes get, maybe.
[4.36 → 8.52] And I think another thing is like MDN being in GitHub makes this stuff easier too.
[8.84 → 13.50] Because now it's just filing and I can go, and I can make big changes to it.
[14.06 → 15.98] Systemic changes across the whole thing.
[16.46 → 17.84] And it's much easier for me to make them.
[17.88 → 19.66] And it's much safer too than it used to be.
[19.66 → 24.38] It used to be terrifying making systemic changes to the wiki because there's no diff.
[24.62 → 27.38] So you have really no idea if what you're doing makes sense or not.
[27.44 → 29.58] And if you change like 500 pages, it's, you know.
[29.58 → 31.24] And I have done this, and it's terrifying.
[31.62 → 33.40] And now it's not nearly so bad.
[35.92 → 38.52] Bandwidth for Changelog is provided by Vastly.
[38.84 → 40.72] Learn more at Fastly.com.
[40.96 → 43.24] Our feature flags are powered by Launch Darkly.
[43.52 → 45.32] Check them out at LaunchDarkly.com.
[45.32 → 47.56] And we're hosted on Leno cloud servers.
[47.82 → 51.34] Get $100 in hosting credit at Leno.com slash Changelog.
[52.12 → 53.52] What's up, JS Party people?
[53.64 → 58.40] Have you ever wondered if you could be offering a faster, less buggy experience for your customers?
[58.40 → 69.62] Well, with Ray gun error and performance monitoring, you have all the information you need at your fingertips to quickly find and fix errors and performance issues across your tech stack down to the line of code.
[69.96 → 78.42] Ray gun makes it easy to monitor the impact of your performance improvements, quickly identify issues across web and mobile apps, and see how your code performs in the hands of your customers.
[78.42 → 82.50] This saves you time, this saves you money, and this saves your sanity.
[82.82 → 87.46] Head to Raygun.com to join thousands of customer-centric software teams who use Ray gun every single day.
[87.78 → 91.64] Again, Raygun.com to give them a try with a free 14-day trial.
[91.64 → 115.66] This is JS Party, your weekly celebration of JavaScript and the web.
[115.66 → 121.72] We record live on Thursdays at 1 p.m. U.S. Eastern, and you can be part of the show.
[122.32 → 124.52] Come hang with us in our community Slack.
[124.64 → 125.64] It's totally free.
[125.90 → 128.80] Head to changelog.com slash community and sign up today.
[129.22 → 130.44] Okay, let's get into it.
[130.50 → 132.12] Hey, it's party time, you all.
[132.12 → 147.22] Hello, JS Party.
[147.52 → 150.32] Welcome to another exciting week of the JS Party podcast.
[150.88 → 151.92] I'm your host this week.
[152.06 → 157.12] My name is Nick Needed, the hoi, and I am joined by the one, the only K-Ball.
[157.22 → 157.92] K-Ball, what's up?
[158.34 → 159.06] Hello, hello.
[159.22 → 159.78] Glad to be here.
[160.20 → 160.58] Excellent.
[160.58 → 164.92] Thanks so much for being here, and we have two exciting guests that I want to introduce,
[165.18 → 168.06] or I want to say their names and then let them introduce themselves.
[168.58 → 170.70] But first, we have Florian Schultz.
[170.82 → 171.76] Florian, what's up?
[172.10 → 172.76] Hey, hello.
[173.16 → 174.26] Tell us a little bit about yourself.
[174.58 → 176.00] Yeah, so I'm Florian Schultz.
[176.52 → 180.46] I'm based in Bremen, Germany, and I'm a technical writer.
[181.44 → 184.12] And recently, we've launched the Open Web Dogs project.
[184.36 → 185.56] Yes, very exciting.
[185.72 → 187.40] That's what we're here to talk about today.
[187.40 → 190.74] And with you, we also have Will Bamberg.
[190.84 → 191.44] Will, what's up?
[191.64 → 192.70] Hello, I'm Will.
[193.06 → 196.40] I'm also working on Open Web Dogs as a technical writer.
[196.68 → 202.70] I started last week in this project, and I'm based in Vancouver, BC, where it snowed this
[202.70 → 203.76] morning, unexpectedly.
[204.30 → 204.82] Very nice.
[205.00 → 206.48] I'm very much over snow right now.
[206.48 → 210.32] Yeah, how many weeks of snow are you on now, Nick?
[210.74 → 213.86] Oh, it's actually been melting quite a lot.
[214.08 → 218.46] But I built a snowman with my daughter on Sunday, and by Monday afternoon, it was totally
[218.46 → 218.74] melted.
[219.08 → 220.24] So, very good.
[220.64 → 221.20] That's progress.
[221.68 → 221.96] Yeah.
[222.22 → 224.62] It's rare enough to be exciting here, you know?
[224.78 → 225.14] But yeah.
[225.14 → 230.56] Well, as fun as the weather is, we are not here to talk about the weather.
[230.68 → 237.32] We are here to talk about docs, particularly web docs, particularly open web docs.
[237.72 → 240.38] And so, I just have to ask to kind of get us started.
[240.92 → 242.36] Who let the docs out?
[243.72 → 244.84] Yeah, open web docs.
[246.18 → 249.26] We've been just launching it in January.
[249.26 → 256.26] So, it's a pretty new initiative, and what we're trying to do is, well, support platforms
[256.96 → 264.62] like MDN with documentation, with technical writing, and, you know, help web developers
[264.62 → 267.70] out there to read all about the web and how it works.
[268.26 → 268.58] Very nice.
[268.76 → 275.60] So, when I think about web docs, there are three letters that come to mind, and it goes
[275.60 → 280.38] on the end of every DuckDuckGo search that I do, and that's MDN.
[281.00 → 286.86] And so, can you tell us a little bit about open web docs and the relationship with MDN or
[286.86 → 287.48] with Mozilla?
[288.24 → 288.54] Oh, yeah.
[288.62 → 289.02] Absolutely.
[289.58 → 295.76] Open web docs actually works a lot with MDN, because MDN is the premier source for documentation,
[296.16 → 297.62] has been for many years.
[298.36 → 302.98] I think last year, MDN celebrated its 15th anniversary.
[302.98 → 308.58] So, it's one of those old school sites out there and has been serving web developers
[308.58 → 309.64] for quite some time.
[310.52 → 314.86] And yes, we're working with them very closely, documenting web standards.
[315.92 → 318.54] And both Will and I have actually been employed there.
[318.84 → 321.14] So, we've been long-time magicians.
[322.36 → 327.50] So, yeah, we've been on this mission to document the web for quite some time now.
[327.50 → 333.48] So, I didn't know coming into this, open web docs, you all are a new organization, but not
[333.48 → 334.82] a new set of documents.
[334.90 → 335.36] Is that right?
[336.12 → 336.60] Exactly.
[337.10 → 338.82] We're a supporting initiative.
[339.64 → 343.52] And maybe I should probably talk a little bit about the history here.
[343.80 → 349.92] So, basically, I think when I got involved with MDN 2009 or 2010, something like that,
[349.92 → 357.74] MDN was actually changing from being strictly a platform for documentation around what Firefox
[357.74 → 361.00] implements and stuff like the JavaScript standard.
[361.24 → 364.78] This was actually invented by Mozilla engineers, right?
[364.88 → 366.78] So, it was kind of born there.
[367.02 → 373.10] And so, MDN used to be a very Mozilla-centric documentation platform.
[373.10 → 380.16] But over the years, and especially with the HTML5 and CSS3 hype, the documentation on MDN changed
[380.16 → 383.66] and it became more of an open web docs platform.
[384.78 → 392.58] And I think it was 2010 or 11 or so when first other organizations were interested in helping
[392.58 → 393.92] out on MDN.
[393.92 → 402.24] And so, over the years, we had different writers from, say, from Google or from other bigger
[402.24 → 407.76] browser vendor organizations who helped us out in documenting the web together on MDN.
[408.20 → 414.26] And then I think about three or four years ago, there was a thing called the MDN Product
[414.26 → 415.10] Advisory Board.
[415.10 → 422.28] So, this kind of thing that tech writers from different organizations coming together was
[422.28 → 424.06] more formalized.
[424.56 → 426.68] And so, the Product Advisory Board was formed.
[426.88 → 432.90] And so, yeah, different organizations formally came together to document the web on MDN.
[433.44 → 433.62] Yeah.
[433.68 → 440.92] And then recently, even more so, people got together and thought about having more diverse funding
[440.92 → 444.58] for MDN and for the writers working on it.
[445.20 → 449.36] And this is how Open Web Docs was born just a month ago.
[450.48 → 452.24] And so, we're an open collective.
[452.88 → 455.20] Everyone can donate to us.
[455.60 → 461.26] And, yeah, we're using the funding to help MDN and to document the web even further.
[462.36 → 466.38] So, is this related to all the like, restructuring and financial turmoil over at Mozilla?
[466.38 → 471.78] Yeah, this was kind of the event that triggered everyone getting their heads together in terms
[471.78 → 476.12] of, okay, how can we come to a more diverse funding for such an important platform?
[476.98 → 481.62] And so, we worked with our founding organizations, Open Web Docs founding organizations, to kind
[481.62 → 483.80] of figure out a way forward.
[484.56 → 484.86] And, yeah.
[485.24 → 485.46] Cool.
[485.62 → 488.14] So, you talked a little bit about those founding organizations.
[488.30 → 491.10] I guess the money before was mostly coming from Mozilla.
[491.70 → 492.76] Now, you're an open collective.
[492.76 → 497.38] I saw there are individuals fundraising, but is the expectation this is going to be something
[497.38 → 498.90] truly sponsored by the community?
[498.90 → 502.72] Or is it something that's going to be, you know, a set of large companies donating?
[503.18 → 506.14] Or how are you thinking about making this thing sustainable?
[506.86 → 509.00] Well, this is something for us to figure out this year, really.
[509.18 → 514.50] We are really happy about the generous funding that we've received from the founding organizations.
[515.10 → 520.70] And we're going to see if we're effective with this initial plan and our initial ideas around
[520.70 → 522.54] supporting web platform documentation.
[523.30 → 529.46] And, yes, ideally, we can sustain and continue with this mix of individual backers and organizations.
[530.18 → 536.80] I think everyone from the kind of larger browser vendors or larger organizations playing a big
[536.80 → 541.40] role on the web, they do have an interest in having good documentations out there so that
[541.40 → 543.42] web developers can develop for the web.
[543.42 → 548.76] So I'm actually quite positive about us getting continued funding with this.
[549.22 → 550.80] But time will tell, I guess.
[551.46 → 556.24] I think having more different sources of funding and more diverse funding,
[556.36 → 560.54] obviously, it makes us more resilient as an organization than being dependent on a few
[560.54 → 562.78] people with deep pockets first.
[562.92 → 566.94] I think also it makes it easier for us to be independent.
[567.26 → 571.22] I think everyone involved in this is very much committed to OpenWebDocs being an independent
[571.22 → 571.88] organization.
[572.52 → 577.56] But it's much easier to make that claim and for that claim to seem credible if you have
[577.56 → 580.06] a lot of different sources of funding than if you only have a few, I think.
[580.74 → 586.32] So this is one of the things in here, I think, like part of the reason why people like MDN,
[586.40 → 590.36] people use MDN, is that it's seen as a genuinely independent source of information about the web.
[591.52 → 597.38] And that's a thing that MDN has been pretty strongly protective of for a long time, really.
[597.46 → 599.70] And it's taken a long time, I think, to build up that kind of reputation.
[599.70 → 605.08] And I think everyone understands that that's one of the most important things about it,
[605.10 → 605.78] and it's worth protecting.
[606.58 → 607.34] Yeah, definitely.
[608.44 → 612.92] At this point, for me at least, MDN is synonymous with the OpenWebDocs.
[613.06 → 617.94] And if I want to find out about some esoteric web API that I didn't know about before,
[618.62 → 621.42] like I said, MDN is at the end of my search query every time.
[622.20 → 624.98] So tell us a little bit about the organization.
[624.98 → 626.10] How is it structured?
[626.42 → 627.26] What's it like?
[627.44 → 632.04] What are the different aspects that you're covering beyond contributing to MDN to start?
[632.54 → 633.90] Beyond MDN, that's a good question.
[634.08 → 636.74] So for now, we're really focusing on supporting MDN.
[637.20 → 641.78] Another project that I'm really passionate about is the Browser Combat Data Project,
[642.18 → 644.20] which is also an MDN project.
[644.86 → 647.40] But I think it goes a little bit beyond that.
[647.40 → 655.06] So to explain this a bit some more, the Browser Combat Data Project is a project that collects
[655.06 → 658.16] what each of the major browsers are supporting.
[659.08 → 664.62] And if you see the combat tables on the MDN pages, for example, then this project powers those tables.
[665.42 → 668.94] But also, Can I Use these days is powered by exactly this data.
[668.94 → 677.38] And so we're working with Alexis, who runs Can I Use, and we're discussing how to move forward with web compass,
[677.68 → 683.76] which, as we know, is one of the biggest problem, if not the biggest problem, that web developers face.
[684.66 → 689.44] So next to MDN, we're also supporting a lot the BCD, the Browser Combat Data Project.
[689.44 → 699.70] And we're looking into, yeah, how can we help web developers finally, you know, having more fun developing for more browsers
[699.70 → 701.66] and addressing some pain points there.
[702.12 → 703.80] I was going to ask about, can I use?
[704.36 → 708.12] And I didn't know that it was powered by this web Compaq data.
[708.40 → 709.14] That's really cool.
[709.32 → 709.56] Yeah.
[709.68 → 713.74] So we made this, I think, is it already two years ago or something?
[714.28 → 717.80] But basically, the Browser Combat Data Project is so rich these days.
[717.80 → 720.34] We have, like, over 12,000 features in there.
[720.58 → 726.54] Like, as you all know, probably the API surface of the web is just getting bigger and bigger and bigger every year.
[726.64 → 729.24] Like, there are tons of APIs added to it.
[729.84 → 739.50] And so there's obviously more and more Compaq data about all these new features, CSS properties, new web APIs, new JavaScript, ECMAScript core features.
[740.28 → 747.16] And so this Browser Combat Data Project is about collecting all this data and how the different browsers are supporting it.
[747.80 → 748.74] And can I use?
[748.74 → 748.80] And can I use?
[749.62 → 751.92] Did have perfect Compaq data.
[752.10 → 758.84] And obviously, it's one of the premier addresses in the net to kind of figure out compass as well.
[759.18 → 762.88] But it only covered, I think it was like 500 features or so.
[763.00 → 771.24] So we really teamed up with Alexis here and added in, like, merged in the MBN Compaq data into can I use.
[771.24 → 775.50] And, yeah, for quite some time now, you can search on can I use?
[776.12 → 781.34] And the results will also give you everything that's in the data store for Browser Combat Data.
[782.18 → 797.98] Now, in terms of what you all are planning here, at first glance, it sounds like this is essentially pull out the organization that was supporting MDN from Mozilla, create an independent organization, diverse funding sources, but essentially operate in kind of the same way.
[797.98 → 807.00] Is the intent to have primarily dedicated staff, technical writers that are employees of OWN?
[807.22 → 809.20] What's the future-facing model?
[810.04 → 816.38] Well, for this year and with the initial funding, we reckon we can finance about four full-time people.
[816.68 → 818.16] We've hired, like, me and Will.
[818.16 → 822.54] So we'll probably have money for two more full-time employees.
[823.26 → 834.00] Depending on kind of the things that we want to accomplish, we might, you know, hire some freelancers or, you know, contractors to do certain things.
[834.24 → 835.34] But we don't know yet.
[835.44 → 839.64] But we reckon with the initial funding, a staff team of four is possible.
[839.64 → 844.92] And organizationally, so Mozilla still plays a big role with MDN.
[845.04 → 847.80] Mozilla is still, you know, paying the servers.
[848.10 → 849.36] Mozilla still has a writing team.
[849.56 → 854.00] Mozilla still has engineers actually building the MDN platform.
[854.00 → 860.42] So, like, they have backend and frontend engineers actually building the site as, like, the platform MDN.
[861.42 → 865.00] And so Mozilla continues to invest in MDN heavily.
[865.40 → 866.58] So that continues.
[866.58 → 873.46] From, like, a project management standpoint, would, like, decisions about that then go through the Open Web Docs organization?
[873.98 → 875.82] Or how would that work?
[876.48 → 876.68] Yeah.
[876.76 → 879.36] So currently, I mean, Mozilla is part of our steering committee.
[879.88 → 888.16] So we are working closely with them to figure out a shared roadmap, what kinds of content projects to take on.
[888.38 → 891.22] So, yeah, we kind of work together closely with Mozilla.
[891.22 → 897.72] And I think as well, I mean, there are projects that are just content, which Open Web Docs can just do on its own.
[897.90 → 902.12] And it's, you know, just our decision about whether it's a thing we want to work on.
[902.52 → 906.38] And there are also projects that cut across the content and the development platform side as well.
[906.80 → 910.24] And those will be figured out a joint project with Mozilla.
[910.78 → 913.76] And they'll provide the kind of engineering side of it.
[913.76 → 917.44] So those are going to be more complicated, I think.
[918.26 → 920.76] And is there any plan to support other Docs platforms?
[920.98 → 923.60] Yeah, I think for this year, we're focusing on MDN.
[923.68 → 924.94] And I think that's a lot of work.
[925.04 → 929.04] I mean, documenting the web on MDN is like, wow, it's a life task.
[929.40 → 931.66] So for this year, we're focusing on that.
[931.76 → 939.92] But beyond that, I think there are opportunities for us to also contribute to, I don't know, make spec processes better.
[939.92 → 943.90] So I've been thinking a lot about how does it actually work?
[944.06 → 949.04] If someone invents something and puts it in a spec, then people implement it.
[949.10 → 954.38] Then people write tests for it in test 262 or in WPT tests.
[954.92 → 957.02] But then what they always forget is documentation.
[957.44 → 964.18] And so what I also want to work on is how can we work closely with specification for standards organizations,
[964.72 → 967.10] help them learn more about documentation.
[967.10 → 972.62] And how can we bring documentation more into the standards organizations?
[973.56 → 981.76] And yeah, make people aware that, yes, you've written the spec, but specs aren't documentation and friendly towards developers necessarily.
[982.32 → 983.78] So what can we do?
[984.28 → 987.86] This kind of questions, I think, is something I would really love to work on.
[988.26 → 994.90] As I see things anyway right now, I don't think there's any real appetite to do something like MDN that's another platform.
[994.90 → 997.66] Because, I mean, MDN does what it does, and it does what it does well.
[998.12 → 1001.64] So there might be other things that fulfill different kinds of needs that we want to work on.
[1002.10 → 1006.12] But, you know, MDN is MDN and there's not much point making another one that I can see.
[1006.88 → 1018.36] Back in 2014, there was this thing called webplatform.org, which was a project by a bunch of browser vendors to build a replacement for MDN.
[1018.36 → 1021.44] And it wasn't really successful because MDN was already there.
[1021.92 → 1026.98] So, you know, I think that doesn't seem like a direction we really want to go in.
[1027.58 → 1028.78] Yeah, I absolutely agree there.
[1029.12 → 1036.18] I've been participating a bit with web platform efforts and I thought it was pretty much a duplication of MDN.
[1036.30 → 1039.12] So I don't think this is a route that anyone should go.
[1039.12 → 1048.60] So any plans or thoughts towards changing, like removing the MDN from the docs, like that name and going with something more open?
[1049.20 → 1050.42] No, I don't think so.
[1050.54 → 1054.36] I think it's, as you say, you duck to go with the prefix.
[1054.36 → 1059.46] So I don't think, I mean, if anyone wants to, maybe.
[1059.62 → 1069.00] We changed, by the way, we changed from MDC, if you remember this, to MDN, maybe eight, seven, eight years ago or so, because it was the Mozilla Developer Centre.
[1069.72 → 1071.76] And then it was the Mozilla Developer Network.
[1072.44 → 1079.26] And then it officially became MDN Web Docs, which kind of MDN stands for itself there.
[1080.40 → 1082.72] So it's a bit like IBM or so.
[1083.34 → 1083.50] Yeah.
[1083.50 → 1083.90] Yeah.
[1084.82 → 1087.12] But I don't think this will change again.
[1087.70 → 1090.16] Plus, Mozilla is already in every user string, so.
[1090.66 → 1091.46] Yeah, right.
[1104.02 → 1106.90] This episode is brought to you by Source graph.
[1107.26 → 1109.80] Source graph is code search for every developer and team.
[1110.06 → 1113.28] Easily search across all the code that matters to you and your organization.
[1113.50 → 1114.68] Find example code.
[1114.88 → 1116.02] Explore and read code.
[1116.28 → 1117.12] Debug issues.
[1117.12 → 1118.32] And so much more.
[1118.32 → 1129.66] And I talked about Beyond Liu, CTO and co-founder of Source graph and asked him to share what code search is, what developers and teams are missing out on, and how Source graph provides code search to every developer in the world.
[1129.66 → 1137.22] If you've worked inside Google or Facebook or any one of these huge, well-respected technology companies.
[1137.22 → 1138.22] Chances are you've used something like code search for you and your team.
[1138.22 → 1142.44] Chances are you've used something like code search before, and you know the value that it provides to your team.
[1142.44 → 1147.98] You know that almost every single engineer inside these organizations uses it on a daily basis.
[1147.98 → 1152.88] If you've never had that experience, chances are you may not know what you're missing out on.
[1152.88 → 1157.90] You know, the term code search sounds a lot like, you know, grew or the search inside your editor.
[1157.90 → 1160.26] And that's what a lot of people think when they first hear it.
[1160.32 → 1162.02] But it's really about much more than that.
[1162.14 → 1179.80] It's really about connecting you as a developer to the broader universe of code and code-related data that's relevant to you, that you need at hand in order to enter that, you know, magical flow state of, you know, being in your editor, writing code quickly, making rapid progress towards that feature bug fix that you're working on.
[1179.80 → 1184.08] It's really about making all that contextual information accessible at your fingertips.
[1184.58 → 1197.20] And what that means is, think about every single repository, every single file, and every single language, every single diff, and every single open source dependency or maybe closed source dependency that's shared across your organization.
[1197.36 → 1200.00] All that is searchable through a single text box.
[1200.42 → 1206.12] And that's really powerful because it means all this friction is eliminated between you and understanding that broader world of code.
[1206.12 → 1207.86] You don't have to clone stuff down to your local machine.
[1207.98 → 1209.70] You don't have to mess around with editor config.
[1210.12 → 1218.58] You don't have to be constantly bugging people on other teams who may not even know who you are in order to teach yourself how all that code works.
[1218.58 → 1232.54] What Source graph is, is really a way for the rest of us, the people who don't work inside the Googles, the Facebook's, to get a tool that gives us access to that sort of information readily and at our fingertips.
[1232.54 → 1245.84] It's really about bringing this type of tool that a lot of the larger technology companies have developed and invested hundreds of millions of dollars into making for the productivity of their own engineers and making that accessible to every single developer in the world.
[1246.00 → 1246.50] All right.
[1246.52 → 1254.76] If Code Search powered by Source graph sounds like something you and your team can use, head to info.sourcegraph.com slash changelog and click the button that says try Source graph now.
[1255.00 → 1258.10] You can install it locally, deploy it to a server or to a cluster.
[1258.10 → 1263.56] They have a quick start guide that takes less than five minutes to install Source graph using Docker, so it's too easy to give it a try.
[1263.82 → 1267.20] Again, head to info.sourcegraph.com slash changelog.
[1267.20 → 1293.22] All right.
[1293.22 → 1303.66] So last section, we talked about what the Open Web Docs are, what the organization is, and its relationship with MDN, and a little bit about its funding.
[1303.78 → 1310.76] But let's dig a little bit deeper into the process and what goes into the organization and figuring out what to actually work on.
[1311.32 → 1315.30] So I'll just ask you, how do you decide what to work on within this?
[1315.36 → 1318.34] Do you find docs that need cleaning up on MDN?
[1318.50 → 1321.72] Do you look at new APIs coming in and kind of base it off of that?
[1321.72 → 1325.96] What's the actual process that goes into the actual work?
[1326.70 → 1327.82] Yeah, that's interesting.
[1327.98 → 1329.00] Let's dig into that.
[1329.20 → 1333.08] So MDN moved to GitHub in December 2020.
[1333.08 → 1334.00] What is it?
[1334.00 → 1334.02] What is it?
[1334.08 → 1334.44] 2020.
[1335.06 → 1348.00] And now that it's not a wiki anymore, you actually have to think of MDN as the typical GitHub project with a massive repository and people coming to it and wanting to do changes.
[1348.00 → 1351.68] And there's pull requests and all that kind of stuff.
[1351.68 → 1373.22] So if I would describe my typical day, what the hell I am doing every day for Open Web Docs is I spend a lot of time on GitHub reviewing pull requests and working with the community to get docs updated, to fix typos, to get new things, new APIs, CSS properties and things on MDN.
[1373.22 → 1383.30] So I think that's really, I don't know what percentage I should give you, but it's a lot of work is just being the cat herder on the GitHub repository.
[1384.26 → 1384.74] Absolutely.
[1385.40 → 1386.60] That's a full-time job.
[1387.36 → 1388.64] It absolutely is.
[1388.64 → 1400.88] So essentially community and project management more than doing the writing itself, which makes sense because that's always the hardest thing to get in an open source project is the organizational piece.
[1401.26 → 1412.66] Yeah, I think it's, of course, it's writing, but in this case, it's because it's open source and because we're working with a global community and everyone is really happy to contribute to MDN and that's a perfect thing.
[1412.66 → 1421.12] But it does mean that you need a bunch of cat herders to work with the community and make them feel good about their contributions.
[1421.56 → 1422.84] And I love doing that job.
[1423.54 → 1432.74] How does it work in terms of the actual content and deciding when releases get pushed to actual MDN?
[1432.82 → 1434.84] Is it just kind of ad hoc as things come in?
[1435.22 → 1439.80] Do you wait for translations, or what's the process behind that?
[1439.80 → 1439.84] Yeah.
[1440.32 → 1444.68] So I think we're going to enable a translation soon.
[1444.76 → 1449.74] And this is something that the Muscle Engineering team is working on, but we're not actually waiting on anything.
[1450.34 → 1456.90] So basically once a pull request is reviewed, it goes live, like it's merged, and then it gets deployed.
[1456.90 → 1465.00] So there's not much of any further approval thing in between there.
[1465.00 → 1473.52] I mean, it used to be a wiki and then basically everyone who had an account could just come in, make changes, and it's live, much like on Wikipedia.
[1474.42 → 1480.52] So by moving to GitHub, there's actually this new, there's a moderation level in here, which is pull requests.
[1481.28 → 1484.12] And that's how things get approved, really.
[1485.08 → 1487.34] It doesn't really need more than that, I don't think.
[1487.34 → 1492.64] Yeah, like I think Florian alluded to, it's a big change for MDN moving into GitHub.
[1492.90 → 1501.86] It really changes the dynamic a lot and the way people work and also the way staff interact with community members.
[1502.50 → 1506.92] And I think it really helps with collaboration, having a pull request modelled.
[1506.92 → 1512.12] Because in the wiki, your interactions with contributors are super limited, really.
[1512.26 → 1520.10] I mean, your options are, if you see an edit to a page, your options are you can do nothing, or you can revert the edit, or you can revert the edits and ban them.
[1520.60 → 1525.20] And they're all quite aggressive things to do apart from nothing, which is kind of passive-aggressive.
[1526.02 → 1531.34] So it's really nice, I think, having a pull request model where you can talk to people and say, you know, this is a great change.
[1531.44 → 1533.22] But, you know, maybe we should think about doing it over there.
[1533.22 → 1537.22] Or maybe we should also think about, you know, doing it on all these other pages that have this problem, too.
[1537.66 → 1542.30] And I think it's much easier to just talk to people, you know, with that kind of model.
[1542.52 → 1544.46] So as Florian says, it's kind of new.
[1544.50 → 1545.70] And I think we're kind of getting used to it.
[1545.76 → 1551.68] We're kind of learning what it's like dealing with this kind of big documentation site with a lot of contributors.
[1552.08 → 1553.52] So we're kind of finding our way there.
[1553.64 → 1557.04] But so far, it seems like it's going really well, I think.
[1557.76 → 1559.90] That's interesting to poke at a little bit more.
[1559.90 → 1563.94] Because I think most of our audience, probably their experience with MDM is like Nick's, right?
[1564.00 → 1572.70] They put it in their search bar or they, like me, forget to put it in their search bar and then scroll past the W3 schools entry to get to MDM.
[1573.62 → 1575.02] But it is open.
[1575.20 → 1578.42] It's something that we can all contribute to and help out with.
[1578.96 → 1588.26] Are there any restrictions on who can contribute or how to get started with that or recommendations that you have for if somebody wants to start helping out on the creation side?
[1588.26 → 1591.30] So there are no restrictions, really, like anyone can.
[1591.56 → 1596.24] And, you know, there are lots of newcomers that we've seen already in the first few months that we're on GitHub.
[1596.48 → 1607.36] So I can only encourage you and everyone who listens in to come to the MDM content repository and, you know, browse around and make some changes, file an issue.
[1608.04 → 1612.90] There are many issues filed, you know, as usual on large open source projects.
[1612.90 → 1616.52] Some of them, we've marked them with a good first issue.
[1617.24 → 1618.64] So you might want to look at these.
[1618.92 → 1624.36] You might want to ping some folks like me and then see if I can help to mentor a thing or two.
[1625.02 → 1626.26] I'm always happy to.
[1627.20 → 1633.68] But yeah, I mean, also, if you are passionate about an API or a thing that you're like, this is so cool.
[1633.68 → 1639.20] I love that, I don't know, someone shipped this, but where are the MDM docs for this?
[1639.42 → 1643.90] Like, do tell us, let us know, and maybe even help with documenting it.
[1644.14 → 1645.06] Yeah, this is pretty cool.
[1645.16 → 1652.50] I'm going to admit that usually I just come to MDM through search and I find the exact, you know, API that I'm looking for.
[1652.66 → 1656.64] Or it's usually like something like slice and splice or something like that where I'm trying to figure out the difference.
[1656.64 → 1661.46] And I don't do much browsing beyond that, but I am right now.
[1661.56 → 1665.42] And I noticed like under references and guides, there's like accessibility.
[1665.90 → 1669.42] There's even one on game development that kind of gives you some resources on that.
[1669.80 → 1672.58] There's a lot more here than just Web APIs, which is pretty cool.
[1672.80 → 1678.36] Or like it's kind of collating stuff together as it relates to the Web APIs, which is also pretty cool.
[1678.36 → 1687.66] I was going to ask about like how new stuff gets added in to MDN, particularly like new Web APIs.
[1688.02 → 1693.32] Or I'm thinking in terms of like one thing that I try and keep up on is like TC39 proposals.
[1693.32 → 1700.10] When things get to stage four, you know, is it at that point that things then get added to MDN?
[1700.34 → 1701.86] Or how does that work?
[1702.68 → 1703.38] Yeah, pretty much.
[1703.38 → 1709.10] I think stage four is probably a good time, sometimes even stage three proposals make it to MDN.
[1709.38 → 1718.66] I think in the past it depended on a lot, like some browser shipped it and then some technical writer of that browser vendor decided, okay, it's time to get it on MDN.
[1718.88 → 1724.18] But as I've tried to get into earlier, I want to kind of change this model also a bit.
[1724.68 → 1731.26] Stage four also means not only you have test 262 tests, but also it means you have docs on MDN, please.
[1731.26 → 1734.86] So this kind of things would be really great going forward.
[1735.44 → 1740.98] So there's definitely different signals to different people really when things should go on MDN.
[1741.12 → 1747.34] And one is, well, a browser ships this thing, and it should have, it appears in the release notes of that browser.
[1747.84 → 1750.52] And so it should be documented on MDN.
[1750.70 → 1751.64] And so, yeah.
[1752.50 → 1754.28] So Nick highlights something interesting.
[1754.42 → 1758.78] So there are things that are tied directly to a particular API or particular feature.
[1758.78 → 1764.00] There's, you know, hey, I need to know how to use this new thing that just got approved.
[1764.14 → 1768.72] And there in some ways it, you know, it sounds like there's work to be done, but it's pretty clear.
[1768.84 → 1772.28] Like, okay, once this gets past a certain stage, it should go on MDN.
[1772.40 → 1775.54] There's not a decision-making process saying, does this belong here?
[1775.58 → 1776.12] Does this not?
[1776.84 → 1781.14] What about those guides like game making or accessibility or whatever?
[1781.14 → 1794.96] Like how, what's the decision-making process around, hey, we should actually build some meta content, something that's not just describing the details of a spec or an API, but here's a guide to how to do this type of thing.
[1795.40 → 1795.58] Yeah.
[1795.66 → 1801.48] I mean, this is, I guess, in some sense, a piece of process that's a work in progress for Mo docs.
[1801.48 → 1806.28] The idea is that people can request new things they want to see on MDN.
[1806.36 → 1810.02] They can request them as issues against the MDN content repo, I think.
[1810.58 → 1819.30] And also things come through kind of it through from the steering committee of OpenWebDocs that we look at, and we say, we call these things opportunities, right?
[1819.40 → 1822.04] Because there's basically a thing, a project you want to work on.
[1822.42 → 1824.74] And we can sort of score it.
[1824.74 → 1833.92] You know, there are criteria like how timely it is, whether the time is right for this particular thing, what the impact of it is, how much work it is, that kind of thing.
[1834.38 → 1838.02] In terms of things like guides, I mean, there are areas that we know MDN is lacking.
[1838.22 → 1843.34] Like we've talked about how we could have better guide docs for performance.
[1843.50 → 1845.04] We could have better guide docs for privacy.
[1845.58 → 1850.78] These are kind of big areas where the MDN docs are kind of not that great right now, I think.
[1850.78 → 1856.74] So we kind of know where these sorts of weaknesses are, I think, you know, and they're kind of floating around in the roadmap.
[1856.88 → 1861.04] When we decide that the time's right for us to do them, we can start working on them.
[1861.54 → 1861.66] Yeah.
[1861.90 → 1871.56] But I mean, if someone files a bug and says, you know, I couldn't find anything about, you know, how to secure my website here that makes sense to me at that kind of high level, then that's a thing we'll take seriously.
[1871.68 → 1878.20] And we'll look at and say, yeah, there's obviously a gap in our docs here, you know, and it can feed into a project like that.
[1878.20 → 1890.56] So another input kind of to our work and decision-making, I think, is also, believe it or not, but we are running one of the largest surveys on MDN that kind of web developers respond to.
[1890.72 → 1895.46] So there's a Stack Overflow survey, but there's also the MDN Developer Needs Assessment.
[1895.70 → 1897.36] You might have heard about that one.
[1897.36 → 1902.80] And with this one, we were actually able to figure out what are the top pain points for web developers.
[1903.38 → 1908.10] So if they tell us it's compatibility, we should probably improve the documentation on that.
[1908.18 → 1913.52] If they tell us, I still don't get cores, CSP, like, so strange.
[1914.00 → 1916.66] Like, I need more guide material on these things.
[1916.94 → 1917.04] Right.
[1917.28 → 1917.42] Yeah.
[1917.42 → 1933.24] So, yeah, I think we're trying to, well, to do user testing and user interviews, maybe sometimes even A-B testing on some docs to figure out what is best for all the web developers using MDN.
[1933.24 → 1945.78] What about, like, what's the decision-making process behind including sort of documentation specifically about third-party stuff that's not part of the platform itself?
[1945.92 → 1947.92] Like, for example, I was just searching around.
[1948.04 → 1955.50] I was searching on JavaScript frameworks, and I saw, oh, there's an MDM article on Ember.js specifically.
[1955.90 → 1960.64] Or there are articles on accessibility in React specifically.
[1960.64 → 1969.76] So, like, what's the distinction, or what's the decision-making process around whether XYZ third-party library should get included on MDN?
[1970.28 → 1970.58] Yeah.
[1970.82 → 1974.14] So, by default, MDN really cares about a web platform.
[1974.36 → 1979.38] So, I think vanilla.js and just documenting web standards is the top priority.
[1980.12 → 1989.14] However, and as we go into guide material tutorials and that sort of thing, well, there is the reality that frameworks are used, and some are used a lot.
[1989.14 → 2005.64] And so, especially in a thing that we call the learning area on MDN, where people can go and actually follow a pathway, like, so that at the end they actually can say, okay, I've learned, I've accomplished something by going through this course or through this set of articles.
[2005.64 → 2009.30] And I've learned how to do things with Ember or React.
[2009.30 → 2025.08] And, yeah, for how to choose which kind of frameworks to use here, I think we really reached out to almost all the major frameworks to give us input and to help us contribute this documentation in the learning area specifically.
[2025.78 → 2027.18] So, I think it was kind of fair.
[2027.34 → 2030.18] Like, we weren't preferring any framework there, really.
[2030.18 → 2036.46] And if any framework doesn't see itself on MDN, but we should have it, then, yeah, talk to us.
[2036.56 → 2037.70] We're happy to add it.
[2038.46 → 2046.76] So, as Will said earlier, MDN is really trustworthy because it comes from this neutral editorial voice, and we surely want to keep that.
[2047.08 → 2049.62] Like, we're not preferring any framework or any browser vendor.
[2050.38 → 2054.56] I think that makes us so trustworthy in the Entablement community.
[2054.56 → 2066.78] Yeah, I think my perspective, my sense, anyway, is that historically we've been pretty reluctant to have a lot of documentation on MDN that's not open web docs, you know, for various reasons.
[2066.90 → 2069.04] I mean, one is that, you know, React has its own docs.
[2069.12 → 2071.58] They're great docs, you know, and they maintain perfect docs.
[2071.70 → 2076.28] What's the point in us having docs that are probably not going to be as good on MDN?
[2076.54 → 2078.86] It doesn't, you know, it doesn't seem to add any value for anybody.
[2079.50 → 2082.54] And on the other hand, people ask for these docs.
[2082.54 → 2091.94] People, quite often, and I think especially for the JS frameworks, like people, we run the most requested things on MDN, was, you know, you should have docs for JS frameworks.
[2092.12 → 2093.56] So, we do now.
[2093.80 → 2106.54] But I think they're kind of intentionally more high level than the React docs, for example, themselves, you know, because another problem with this is that they tend to change more often and more quickly.
[2106.66 → 2108.58] And so, maintenance becomes a huge problem, right?
[2108.68 → 2111.98] You don't have the same kind of insight into the roadmap for this project.
[2111.98 → 2114.82] So, you don't exactly know when changes are going to come up.
[2114.94 → 2116.54] You're going to have to update all your docs for, right?
[2116.84 → 2119.50] So, you're working at kind of disadvantage there anyway.
[2120.24 → 2130.54] So, yeah, I think there is space for some documentation that's not open web docs, but I think it kind of wants to try to be high level and the kind of stuff that won't age badly, you know?
[2130.90 → 2131.08] Yeah.
[2131.22 → 2132.32] No, that makes a ton of sense.
[2132.52 → 2137.34] I feel like there is a case to be said that there shouldn't be any of these framework-specific docs on there.
[2137.34 → 2138.42] That it should all link out.
[2138.82 → 2144.78] But, as you say, like, you also need to react to what people want and what they're looking for.
[2145.24 → 2146.04] Yeah, that's the thing.
[2146.12 → 2147.50] I mean, yeah, people do ask for them.
[2147.86 → 2148.08] And, yeah.
[2148.08 → 2159.70] Yeah, and along the same lines, like, I know that they are separate things, and it's not technically open web, but from just, like, a knee-jerk comparison between, like, as a JavaScript developer, you know, I'm writing JavaScript.
[2159.98 → 2164.52] And me, personally, I'm writing JavaScript either in a browser or on the server.
[2164.52 → 2172.84] And so I have caught myself, like, typing in, you know, read file sync MDN or something to try and find no specific APIs there.
[2173.80 → 2178.78] But you don't see that as a purview for open web docs to be looking into?
[2179.28 → 2183.60] Yeah, I don't think we're going to write server-side, like, no documentation.
[2183.60 → 2192.70] But here again, we looked at what our users want, and they actually told us that the combat tables should have Node.js as a thing in there.
[2193.12 → 2194.68] And so we did that and people love it.
[2194.88 → 2202.56] Like, whenever they browse the core JavaScript docs, and they see the Node.js support version there as well, it's, like, awesome.
[2202.72 → 2203.90] I just needed to know this.
[2203.90 → 2212.58] And apparently the Node.js docs themselves, they probably don't make it so great to browse which version supports what.
[2213.16 → 2215.78] But, yeah, there you have it directly on MDN2 now.
[2216.34 → 2220.50] Yeah, that kind of got me thinking about it because I do see Node in those combat tables.
[2221.28 → 2225.44] Yeah, so, see, sometimes we're like, okay, we've got to have Node for the combat table.
[2225.44 → 2232.84] But documenting it's on the server, the whole server-side APIs is probably stretching it a bit too far.
[2232.84 → 2240.02] And also what Will said, I mean, the good thing about the web is, I mean, it's a good and a bad thing, but we're not removing much.
[2240.26 → 2244.32] Like, we're just adding more and there are no incompatibilities really.
[2244.60 → 2246.18] I mean, there's no versioning.
[2246.32 → 2249.12] There's no web 2.0 or something really.
[2249.60 → 2251.92] It's just one version, one JS.
[2252.60 → 2256.04] But with React, you know, it's going to be, I don't know where we're at right now.
[2256.04 → 2263.32] But as Will said, those APIs, those frameworks, they just change all the time, and we have no insight into where we are with things.
[2263.46 → 2266.16] And we can never keep up an impossible job.
[2266.90 → 2269.38] They can afford to move faster, basically, than the web, right?
[2269.54 → 2272.70] So, you know, that's going to be a problem for writers.
[2272.90 → 2274.88] The backcourt story is so different, right?
[2275.16 → 2275.38] Yeah.
[2275.38 → 2283.98] The whole, you can't break the web mantra that has defined our paths forward on JavaScript and CSS and all of these things.
[2284.16 → 2288.48] Like, that's actually, I hadn't thought of it before, but that's a boon for you as documentation developers.
[2288.48 → 2290.70] Because you can be appended only, essentially.
[2291.34 → 2298.12] For prior stuff, maybe you tag it with deprecated, but it's going to keep working if it's in the platform.
[2298.12 → 2298.56] Yeah.
[2299.38 → 2310.62] I mean, as someone who works a lot with Compete stuff, thanks to the Compete, Browser Compete Data Project, I know that there's lots of stuff also that we're going to deprecate and maybe remove one day.
[2311.28 → 2315.34] And just adding to the API service, I don't know how long-term this will look like.
[2315.42 → 2321.08] Like, if we're talking again in five years, I seriously don't know where the API service will be at.
[2321.30 → 2324.20] And I don't know if we're still in this one JS world.
[2324.82 → 2326.96] It's fascinating to see what's happening there.
[2326.96 → 2330.86] But yes, we're just marking things as deprecated and don't use it anymore.
[2331.12 → 2332.60] But you know, it still exists.
[2332.88 → 2336.36] And websites from 1995, they exist, and they still work.
[2336.42 → 2337.10] And that's beautiful.
[2337.90 → 2343.22] But they probably use APIs that you shouldn't use when writing a new website today.
[2344.66 → 2345.66] Yeah, right.
[2345.82 → 2353.18] I mean, so like the APIs, you know, the APIs are technically still there, but the guidance changes still, right?
[2353.18 → 2356.48] So you still have to maintain them, but you still have to write stuff that says,
[2356.48 → 2358.74] by the way, don't use this, even though you can, you know.
[2359.12 → 2364.20] So that's quite often a thing from incidents on open web docs is updating guidance around things.
[2364.70 → 2365.28] Yeah, absolutely.
[2365.64 → 2370.66] One thing I noticed is that they are working on a new data API, and it's so, so fundamental, right?
[2370.76 → 2375.24] So data APIs are one of the most browsed docs, I think.
[2375.24 → 2378.22] I think also because the APIs are terrible.
[2378.92 → 2382.18] I was going to say, they're browsed so often because it's broken.
[2382.74 → 2383.06] Yeah.
[2383.20 → 2386.30] But imagine we have the new data API, whatever it was called.
[2386.46 → 2386.86] I forgot.
[2387.34 → 2389.48] But imagine we got this implemented everywhere.
[2389.68 → 2393.66] And now we need to advise everyone to move away from the data API to this new thing.
[2393.72 → 2395.08] That's going to be interesting, I think.
[2395.80 → 2397.48] But this is a typical task that we do.
[2397.48 → 2401.96] Like we advise, hey, this thing, App Cache or data API, we got a new one.
[2402.24 → 2406.28] Like if you are doing a new project, like don't do this anymore, do that instead.
[2406.72 → 2409.82] And this is what we're doing also a lot, I think.
[2409.96 → 2414.50] Like giving this kind of hints and best practices information.
[2415.50 → 2419.22] This is just my own ignorance speaking, but do you all do migration guides as well?
[2419.22 → 2423.54] So in that example, for example, you know, you're doing a new project.
[2423.84 → 2425.32] You shouldn't be using this.
[2425.40 → 2426.14] You should be using that.
[2426.30 → 2428.06] If you have an old project, here's how you migrate.
[2428.56 → 2430.90] Well, App Cache, I think we wrote up some material.
[2431.18 → 2432.56] Okay, App Cache is gone.
[2432.80 → 2433.80] Use Service Worker.
[2434.32 → 2436.04] But I don't think we do this regularly.
[2436.36 → 2437.68] We should probably do this more often.
[2437.94 → 2439.22] I think migration guides are great.
[2439.78 → 2440.14] All right.
[2440.28 → 2441.14] Feature request.
[2441.54 → 2441.80] Yeah.
[2441.88 → 2442.32] File it on.
[2442.32 → 2442.62] Yeah.
[2443.04 → 2443.96] Yeah, file it.
[2444.42 → 2445.34] Just file it.
[2445.58 → 2446.34] It is a good point.
[2446.98 → 2448.60] So brainstorming here.
[2448.60 → 2449.06] I love it.
[2449.22 → 2464.40] This episode is brought to you by the Dev Discuss podcast, an original show by the team behind Dev.to.
[2464.74 → 2467.98] The show is hosted by Dev co-founders Ben Harper and Jess Lee.
[2468.34 → 2474.94] Ben has been on the Change Law podcast before, talking about their decision to go open source with the Dev platform, now called Forum.
[2474.94 → 2483.50] The Dev Discuss podcast brings on notable industry guests to discuss trends and timeless software topics to help developers succeed within their teams and grow.
[2483.84 → 2484.94] Here's a clip from season two.
[2484.94 → 2498.88] When you deploy, you know, when you deploy Node.com, AWS could probably move their fleet of Lambda services to ARM and very few customers will be affected.
[2499.00 → 2503.96] And not to say nobody, but very, very few customers will be affected by that kind of migration on Lambda.
[2503.96 → 2512.50] Whereas if they were to try that migration on Margate or EC2, it's a much bigger and more complex migration for those customers.
[2513.14 → 2523.16] And, you know, here is them, you know, building something in a way that, you know, they may see as more productive or more traditional, but it is actually, you know, more locked in a way.
[2523.16 → 2529.86] All right, search for Dev Discuss, all one word in your podcast player, subscribe and skim the backlog for an episode that jumps out to you.
[2530.22 → 2532.68] Again, search Dev Discuss anywhere you listen to podcasts.
[2553.16 → 2565.44] So we talked about what the Open Web Docs is and what you've been doing and what your focus is for 2021.
[2565.70 → 2567.92] And that is MDN specifically.
[2568.30 → 2570.52] But where do you see that going beyond 2021?
[2570.96 → 2576.88] What other kinds of ideas do you maybe hope to take on or think or thinking about taking on?
[2577.22 → 2578.34] What does the future look like?
[2578.34 → 2586.84] So, as I've said in the other section, one of the things I'd like to bring in more into the standards world is how they treat documentation.
[2587.44 → 2593.00] In my eyes, hopefully at some point as a first class citizen, just like tests.
[2593.34 → 2595.78] So this is going to be something I want to work on.
[2596.60 → 2603.58] And then another thing I'm thinking about is also writing more documentation about how web platform stuff gets done.
[2603.58 → 2607.30] So how do, you know, how specs get written?
[2607.30 → 2613.32] And I think Puke was writing a web platform contribution guide at some point, which I really enjoyed.
[2613.66 → 2616.78] But I don't think it covers documentation very well.
[2617.00 → 2624.00] So we could maybe extend that and, yeah, onboard more people into writing documentation for the web.
[2624.46 → 2625.94] So I think this could be something.
[2625.94 → 2632.88] I don't think we will move away from being centred around MDN next year or in the future.
[2632.88 → 2641.44] I think MDN, open web docs is, yeah, is a thing that should support MDN long term.
[2642.14 → 2642.24] Yeah.
[2642.84 → 2646.48] And I know you mentioned, like you mentioned ECHO 262 tests.
[2646.90 → 2649.14] And I sometimes see tests as documentation.
[2649.14 → 2653.34] If they're well-written tests, you can see them as like runnable documentation.
[2653.34 → 2657.56] Do you see something like that ever becoming like the purview of open web docs?
[2658.60 → 2662.74] Another thing I'm thinking about is like I'm contractually obligated to bring up TypeScript.
[2663.40 → 2673.76] And I'm thinking like, you know, in the TypeScript core repo, there's a lot of core web API types for all the different APIs that are maintained by the TypeScript team.
[2673.76 → 2678.88] But that could be considered living documentation that is exposed to me through my editor.
[2679.52 → 2689.48] So one of the things that we started actually one or two years ago after we kind of got started with the combat data is to think more about data and documentation.
[2690.06 → 2696.86] So one of the things I could see us doing is do more research and investigate more how documentation could actually become more data.
[2696.86 → 2701.18] And, you know, TypeScript uses this a lot to kind of see what is this thing.
[2701.82 → 2722.72] And Eolian could expose a lot of its information, not only the combat data, which is structured data by now, but there's so much more information in the documentation that we could expose as data and get that integrated into IDEs or into, yeah, TypeScript or other languages that could make use of it.
[2722.72 → 2730.22] So I think this could be an area where we do more research and do interesting things.
[2731.10 → 2732.76] That raises an interesting point.
[2732.84 → 2742.46] Is there an MDM API of some sort that, for example, IDEs could pull in documentation for all of these supported APIs?
[2742.94 → 2744.64] There isn't yet.
[2746.14 → 2751.86] Maybe Will is very passionate about this whole structured documentation topic.
[2751.86 → 2753.38] So take it away.
[2754.18 → 2755.28] Well, no, there isn't.
[2755.36 → 2757.40] But it's a fascinating idea, basically.
[2757.76 → 2769.58] I'm very interested in this, the idea of whether we can structure MDM content in such a way that it's consumable by different kinds of applications, right?
[2770.00 → 2776.32] And so, you know, whether like, yeah, MDM as a website is still, you know, a focus of OpenWebDocs.
[2776.32 → 2780.08] But can the MDM content power other applications than just the website?
[2780.24 → 2783.94] Can it feed into editors, and can it feed into DevTools and stuff like that?
[2784.20 → 2794.78] You know, I'm really interested in this idea of having documentation be available in a developer's workflow, you know, in the most kind of clean way, you know, rather than maybe having to stop what you're doing.
[2794.78 → 2798.28] Go open a browser tab and do your search for MDM and find the thing.
[2798.66 → 2801.02] How can we be better integrated into people's workflows?
[2801.20 → 2804.98] And so, like, yeah, like editors is a good example of that and DevTools is too.
[2805.84 → 2810.72] And so, you know, what sorts of things would developers like to see in their workflow?
[2810.72 → 2816.26] What kinds of things can we structure and kind of make sort of semantic, you know, so that we can do that?
[2816.54 → 2824.04] And then what kind of work do we have to do in the MDM platform to rework the content so that's become as possible?
[2825.10 → 2828.46] I've done a lot of thinking about this in the last, like, year or so.
[2828.76 → 2831.64] And I think it's, I'd love to go further with this.
[2831.72 → 2837.80] And as Florian says, I mean, browser compact data is one of these things that is a kind of trailblazer for this.
[2837.80 → 2843.56] You know, like back, I guess, five years ago, compact data was just HTML in pages.
[2843.82 → 2845.76] It was like it was locked up in the HTML, right?
[2845.82 → 2851.34] The compact status of, say, you know, array. Slice was, it was like it was dead, you know?
[2851.40 → 2853.04] It was just there in the HTML.
[2853.66 → 2864.62] And what happened with browser compact data is it turns into data, and then it becomes kind of live, and you can remix it, and you can build different views of this data, and you can have a single page that lists compact story for everything in array.
[2864.90 → 2866.50] And it can just pull from the same data, right?
[2866.50 → 2869.20] And so that's a powerful thing.
[2869.36 → 2872.62] And if we can do that for more of our documentation, I think it would be super cool.
[2873.02 → 2873.82] We do this as well.
[2873.94 → 2881.82] Like there's this thing called MDN slash data, which is a kind of, again, like even before browser compact data, was like a really early attempt to try and do this.
[2881.90 → 2885.64] And it has some kind of structured content for mostly CSS properties.
[2886.52 → 2889.06] And it's actually used in MDN to power some stuff.
[2889.28 → 2891.12] It's like it was a kind of really early prototype.
[2891.12 → 2893.60] And there are things we'd do differently if we did it again.
[2893.88 → 2896.36] And there are ways we'd consume it differently if we did it again.
[2896.72 → 2899.88] It's obviously an idea that has been kind of kicking around for a long time.
[2900.66 → 2900.78] Yeah.
[2901.12 → 2904.22] The more we learn about it, the better our prototypes get, maybe.
[2904.22 → 2910.58] You know, and I think another thing is like MDN being in GitHub makes this stuff easier too.
[2910.92 → 2913.94] Because now it's just like, it's just filing.
[2914.14 → 2917.90] And I can go, and I can make kind of big changes to it.
[2918.42 → 2921.76] And kind of systemic changes across the whole thing.
[2922.20 → 2923.62] And it's much easier for me to make them.
[2923.66 → 2925.48] And it's much safer too than it used to be.
[2926.00 → 2928.94] Like it used to be terrifying making systemic changes to the wiki.
[2929.32 → 2931.54] Because there's no diff, right?
[2931.98 → 2934.84] So you have really no idea if what you're doing makes sense or not.
[2934.88 → 2937.04] And if you're changing like 500 pages, it's, you know.
[2937.40 → 2939.00] And I have done this, and it's terrifying.
[2939.38 → 2941.46] And now it's not nearly so bad, right?
[2941.46 → 2945.78] So that's another possibility, I think, that MDN being in GitHub opens up for us.
[2946.62 → 2946.98] Yeah.
[2947.44 → 2951.40] I mean, speaking in concrete terms, one thing which people have asked about is having,
[2951.62 → 2954.14] in code editors, having like short descriptions for things, right?
[2954.14 → 2957.42] So, you know, like what's the like one line description of what array. Splice does?
[2957.86 → 2958.38] That'd be helpful.
[2958.56 → 2961.22] And is that a thing we can slurp out of MDN?
[2961.62 → 2962.26] Well, okay.
[2962.32 → 2966.18] To do that, then, you know, it has to be marked up in such a way that you can actually retrieve it.
[2966.40 → 2967.80] And it has to be consistent, you know.
[2967.82 → 2970.26] It has to be short enough to fit, you know.
[2970.26 → 2973.00] And it has to actually make sense if it gets kind of contracted.
[2973.78 → 2978.48] And it has to, you know, use tags that make sense in the context where you're displaying it.
[2978.56 → 2979.66] And this kind of stuff, right?
[2980.08 → 2983.80] So your content has to be in good enough shape that this is going to work properly.
[2984.14 → 2991.60] Yeah, this really makes me think about, and I was just looking right now at what the content looks like in GitHub.
[2991.82 → 2993.30] And I don't, it doesn't look like you have it.
[2993.30 → 3000.86] But like some sort of equivalent to the type of like social markup you might put on another website or something,
[3000.86 → 3006.04] where you have a set of structured tags that include like a short description, a reference.
[3006.42 → 3006.54] Right.
[3006.54 → 3011.00] Like if, for example, if it's a browser API, like include that as a structured thing.
[3011.08 → 3017.44] And then you can write some scripts that process that and give you an index to look things up and all that other sort of fun stuff.
[3017.74 → 3020.14] But that's, if that's not already there, that's a big project.
[3020.80 → 3020.96] Yeah.
[3021.44 → 3022.40] It absolutely is.
[3022.40 → 3028.02] We've been approaching this with linting and kind of making dogs more structured.
[3028.32 → 3037.54] And first and foremost, like figuring out what kind of templates and how to structure reference documentation better so that you can, yeah, slurp information out of it.
[3038.14 → 3042.34] But one big blocker is also the source format currently is HTML.
[3042.34 → 3050.40] So, yeah, we're thinking about moving to Markdown and then maybe structuring it and giving it semantics.
[3051.00 → 3052.14] But it's a long way.
[3053.06 → 3056.62] I mean, it looks like you have some header data, essentially.
[3057.44 → 3059.00] Like the front matter, you mean?
[3059.30 → 3060.18] Yeah, the front matter.
[3060.36 → 3060.72] Yeah.
[3061.12 → 3061.40] Yeah.
[3061.40 → 3062.78] I was excited to see that too.
[3063.22 → 3063.52] Yes.
[3064.52 → 3068.14] That's something that you can stash whatever you want in there.
[3068.20 → 3071.02] It doesn't actually have to be involved with processing the HTML.
[3071.02 → 3073.40] It could actually be there for your other tools.
[3074.40 → 3074.76] Right.
[3075.36 → 3076.10] Yeah, exactly.
[3076.24 → 3081.34] It's just a matter of what we put in there and how we, yeah, I think you have to kind of design it carefully, like what you actually want to have.
[3081.40 → 3083.58] So it doesn't just become a big kind of dumping ground, you know?
[3083.96 → 3084.78] But yes, exactly.
[3084.90 → 3087.62] And at the moment, I think it has title and slug and tags.
[3087.62 → 3095.08] And the tags are just like, like back in the wiki days, this is just the same, the tag values the pages had, you know?
[3095.62 → 3095.76] Yep.
[3095.76 → 3100.84] Back in the wiki days, anybody could not just apply tags to a page, but anybody could create their own tags.
[3101.46 → 3109.48] As a result, which there were, I don't know how many, tens of thousands of tag values in the site, which I assume all still exist.
[3109.68 → 3111.08] So that would need some cleanup.
[3111.46 → 3113.74] You could have validation on those, all sorts of other stuff.
[3113.94 → 3114.08] Yeah.
[3114.08 → 3119.38] So in the combat data right now, do you have links back to relevant documentation pages?
[3120.02 → 3120.62] Yeah, we do.
[3120.84 → 3124.76] This has been good for various embedding projects.
[3125.32 → 3131.12] Like it's not only can I use embedding us and linking back to MDN, it's VS Code and other projects.
[3131.12 → 3131.52] Yeah.
[3131.84 → 3136.46] Embedding the combat data and then, yeah, using this part of structured MDN data already.
[3136.72 → 3144.82] And then this is kind of our, yeah, we want to do more of what BE did really with more like short description and more data that MDN has to offer.
[3145.70 → 3146.44] Yeah, absolutely.
[3146.70 → 3148.90] So yeah, you already have your index, right?
[3148.94 → 3155.32] So you just need to add whatever the sets of structured pieces that you want to be able to display, and you can use that index to look it up.
[3155.38 → 3155.66] True.
[3155.66 → 3161.78] And it may not right now be in a good structure, but with the index, you can write a script that's going to pull that stuff out.
[3162.10 → 3162.22] Yeah.
[3162.34 → 3162.48] Yeah.
[3162.52 → 3172.92] And I mean, the other nice thing about this, this whole idea, right, is that with BCD, because it's just data, how you represent that in the rendered pages is a matter for the tooling.
[3173.14 → 3181.02] And so if you decide you want to change how you want to represent combat across all, you know, 10,000 MDN pages, you change it in one place.
[3181.42 → 3181.68] Right.
[3181.68 → 3186.36] And back in the old days, you'd have to, you literally have to change it in 10,000 places, you know.
[3186.66 → 3188.88] And so it's good for the website too, right?
[3188.90 → 3191.02] I think having that kind of build step for the content.
[3191.78 → 3191.94] Yeah.
[3192.22 → 3195.40] So BCD is in the browser combat data repo on MDN?
[3195.90 → 3196.28] Yeah.
[3197.06 → 3197.46] Interesting.
[3197.98 → 3199.00] Yeah, this was really cool.
[3199.00 → 3208.52] As well as that, like when we moved the static HTML stuff that used to be the combat tables into data, basically into a separate repository.
[3208.52 → 3217.34] And now whenever we want to change how the browser combat tables are rendered on MDN, it's just, you know, it's just a React thing that gets the data from the data store.
[3217.70 → 3220.30] And then if you want to change the presentation, we just do so.
[3220.40 → 3223.30] And it populates to all 10,000 pages.
[3223.50 → 3231.12] It's just, I want more of that and not mass edits on the MDN pages for a thing that I want to do everywhere.
[3231.12 → 3231.26] Yeah.
[3231.74 → 3232.14] Absolutely.
[3232.48 → 3236.96] So looking at this, I'm looking at the combat data now, it's linking to the MDN URL.
[3237.44 → 3243.52] Is it straightforward to map from that to the location in GitHub, the file name?
[3244.04 → 3246.72] Or is there a processing step that makes that hard?
[3247.14 → 3250.76] Because one of the things you might want is to access that front matter, right?
[3250.78 → 3252.00] Because that's structured once again.
[3252.00 → 3254.04] Yeah, I think you have a point there.
[3254.16 → 3262.42] I think it's probably mapping because the files folder and the MDN content repository maps to the slugs.
[3262.76 → 3264.08] So to the MDN URLs.
[3264.36 → 3266.44] So I think, yeah, it should work.
[3267.06 → 3267.36] Interesting.
[3268.22 → 3271.56] So that might be a fun little project if anybody's listening and has free time.
[3272.00 → 3275.82] Write something that's going to run through the browser combat data.
[3275.82 → 3282.48] Look up the appropriate file in the content data and just pull out the structured data and make it available.
[3282.82 → 3287.68] And someday, when there's more structured data there, it will probably be more useful than it might be today.
[3288.20 → 3288.42] Yeah.
[3288.58 → 3293.88] I think it's funny that you say that because I think over the year, many people have scraped MDN in various ways.
[3293.88 → 3297.94] Like you scraped the wiki, and now they're scraping the GitHub or scraped BCD.
[3298.56 → 3303.58] And so we're going from prototype and scraping to scraping, which is great.
[3303.74 → 3305.68] Like lots of good things happen there.
[3306.14 → 3315.34] But yes, as we said earlier, ideally one day there's going to be some sort of MDN API that officially makes available this data.
[3315.86 → 3320.08] So that is definitely something in the far future to look forward to, I think.
[3320.82 → 3321.80] That is exciting.
[3321.80 → 3326.48] I'm excited about the idea of that and all that you could do with that data.
[3326.94 → 3329.60] Like being able to integrate it in all sorts of different ways.
[3329.98 → 3330.78] I don't know if it exists or not.
[3331.02 → 3334.94] One cool thing could be like, these are the browsers or the environments that I support.
[3334.94 → 3339.08] And then every time I try and use something, maybe it's like a stage three or stage four feature.
[3339.74 → 3345.44] Tell me, like show me my editor right now if it's not going to get there with or without a build.
[3345.54 → 3345.90] Yeah.
[3346.16 → 3347.46] And that'd be really cool.
[3347.46 → 3348.14] Yeah.
[3348.38 → 3353.50] Avoiding this kind of context switch from the editor, going to the documentation, going back into the editor.
[3353.74 → 3354.74] That's a good thing.
[3355.08 → 3355.70] We've done this.
[3355.82 → 3359.48] I've added a learn more link to console errors.
[3359.48 → 3373.06] So if you're in DevTools, and you're like doing something and then like syntax error, whatever it's spitting out, then in Firefox, you get a little learn more that explains what is going on and how you can debug that.
[3373.42 → 3374.56] And this has been really cool.
[3374.70 → 3383.94] So whenever you integrate into the workflow and make links or contextual information available, then people really love this.
[3383.94 → 3390.46] And I really want to see more of this and bring documentation closer to the developers and their environments.
[3390.78 → 3392.04] Yeah, I really like that.
[3392.70 → 3399.38] So we've talked about it a bit, but what is the easiest way for the community to get involved in Open Web Docs?
[3399.48 → 3405.58] Is it just go to MDN's GitHub and start looking at issues or contributing to the docs there?
[3405.58 → 3416.48] Is it go to Open Web Docs on GitHub and is there a way to get familiar or help contribute to the steering committee or things like that, like the actual organization?
[3417.80 → 3418.38] Yeah, sure.
[3418.60 → 3420.26] So both is fine.
[3420.40 → 3422.86] You can file issues on Open Web Docs and on MDN.
[3422.96 → 3429.68] I think if it's really about some MDN page that needs fixing, I think just filing it on MDN content is the better way to go about it.
[3429.68 → 3438.62] But if you're really curious and interested in specifically connecting with us, file an issue on Open Web Docs project, talk to us.
[3438.92 → 3441.64] We have all the steering committee notes available there.
[3441.72 → 3446.94] You can read about what we're up to, like radically transparent in that case.
[3447.62 → 3453.76] We have an open collective site where you can, of course, donate and kind of follow our blog there.
[3453.76 → 3463.36] Like every month I'm publishing a little work log post where I'm kind of making a roundup of what sorts of work we've got done in a month.
[3463.74 → 3467.26] So you can be updated about our progress there.
[3467.94 → 3475.26] Follow us on Twitter, you know, this kind of things where we inform about webinars or things that we're doing.
[3475.26 → 3481.26] One thing we will probably organize sometime this year is a documentation sprint.
[3482.16 → 3485.22] We used to do this a lot back in the day as well.
[3485.40 → 3492.66] So the idea is, you know, pick a thing where we need lots of people to help with and then get organized.
[3492.82 → 3494.08] Maybe hop on a Zoom call.
[3494.90 → 3498.02] Maybe once all this over, meet again also in person.
[3498.02 → 3510.96] You know, maybe, I don't know, I could imagine actually doing a little workshop or something combined with conference or so when all this is back where we could have a little session on doc sprinting on documentation.
[3511.20 → 3514.72] For this year, I guess we're going to try to do this online.
[3515.54 → 3520.68] So definitely subscribe to our channels to be updated about information on that.
[3521.36 → 3522.20] Yeah, sounds great.
[3522.20 → 3530.46] Really looking forward to seeing all the improvements coming and keep doing what you're doing because MDN is an invaluable resource.
[3531.20 → 3536.68] And I'm really excited to see how this experiment goes over the next year and into the future.
[3536.96 → 3546.04] And we definitely wish you the best of luck and hope to have you on again to talk about how it's been going and how you see it going into the future from there.
[3546.28 → 3548.70] So thank you so much, Florian and Will, for coming on.
[3548.94 → 3550.62] And we will see you next week.
[3552.20 → 3555.48] Thank you for listening to JS Party.
[3555.78 → 3557.40] Please do tell a friend about the show.
[3557.58 → 3560.70] It's the number one way people find new podcasts they love.
[3561.16 → 3564.12] This episode was hosted by Nick Needed and K-Ball.
[3564.52 → 3567.72] It was produced by Jared Santo with music by Break master Cylinder.
[3568.24 → 3570.24] We have awesome sponsors supporting the show.
[3570.54 → 3573.06] Thanks again to Vastly, Launch Darkly, and Linde.
[3573.50 → 3577.74] Next up on the pod, we are playing JS Danger with the CSS Tricks team.
[3577.74 → 3583.64] Chris Coyer, Sarah Drainer, Jeff Graham, and Madeline Suzanne put their web dev knowledge to the test.
[3583.90 → 3585.26] Who's going to finish the game on top?
[3585.46 → 3587.26] Stay tuned to find out next week.
[3587.26 → 3599.50] Game on.
