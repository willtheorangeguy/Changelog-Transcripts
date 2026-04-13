[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.14]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to Linode.com slash Changelog.
[15.30 --> 18.12]  This episode is brought to you by Rollbar.
[18.42 --> 24.36]  Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 --> 28.60]  And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 --> 32.94]  And Paul says they don't deploy a service without installing Rollbar first.
[33.10 --> 34.58]  It's that crucial to them.
[34.86 --> 36.60]  We operate at serious scale.
[37.04 --> 42.46]  And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 --> 45.52]  We need to have that visibility.
[45.92 --> 50.44]  And without that visibility, it would be impossible to run at the scale we do.
[50.58 --> 52.54]  And certainly with the number of people that we have.
[52.72 --> 55.70]  We're a relatively small team operating a major service.
[55.70 --> 61.46]  And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 --> 62.00]  All right.
[62.02 --> 66.70]  If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.36 --> 70.34]  Once again, Rollbar.com slash Changelog.
[70.34 --> 81.76]  Welcome to JS Party, a weekly celebration of JavaScript and the web.
[81.90 --> 88.38]  Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live.
[88.38 --> 93.48]  Join the community and Slack with us in real time during the show at changelog.com slash community.
[93.88 --> 94.68]  Follow us on Twitter.
[94.78 --> 96.28]  We're at JSPartyFM.
[96.48 --> 97.76]  And now on to the show.
[97.76 --> 105.50]  Hello, JS Party people out there.
[105.56 --> 111.96]  Whether you're live or listening to this delayed on podcast, we are excited to have you back with us today.
[112.08 --> 113.02]  I will be your host today.
[113.08 --> 113.82]  This is K-Ball.
[114.08 --> 118.20]  I'm joined by two of our amazing panelists, Divya and Chris.
[118.28 --> 118.96]  Divya, how's it going?
[119.28 --> 119.72]  Pretty good.
[119.84 --> 120.20]  How are you?
[120.56 --> 121.30]  Life is good.
[121.36 --> 124.66]  I'm getting over jet lag and starting to feel normal during the day again.
[125.28 --> 126.02]  Chris, how are you doing?
[126.02 --> 127.32]  Super duper.
[127.42 --> 128.12]  How are you doing?
[128.84 --> 130.80]  I know you just answered that question.
[131.92 --> 134.08]  But that's how we do it here in the States.
[134.34 --> 134.78]  It is.
[134.84 --> 135.80]  We have all these automatics.
[135.88 --> 136.40]  How are you doing?
[136.50 --> 140.40]  Well, I can't say bad because then you actually have to have a conversation, right?
[140.44 --> 142.36]  You got to say, oh, life's good.
[142.60 --> 142.96]  Fine.
[143.10 --> 143.74]  How are you?
[144.40 --> 144.80]  All right.
[144.80 --> 151.70]  So our episode today, we are going to do three of our recurring segments, except one
[151.70 --> 152.44]  of them is brand new.
[152.54 --> 153.94]  We're going to experiment with a new segment.
[154.50 --> 157.90]  So if you're listening to this, let us know what you think of our new segment.
[158.42 --> 163.66]  So we will start off with a segment called the framework wars.
[163.66 --> 165.84]  We're not going to make it into an actual war.
[165.96 --> 172.08]  But one of the big, rapidly changing, hard to keep track of things in the JavaScript world
[172.08 --> 174.12]  is all these crazy front end frameworks.
[174.38 --> 178.54]  So we're going to do some quick hits on what's going on in at least some of the big ones.
[178.64 --> 179.92]  Some new stuff we've checked out.
[180.74 --> 183.52]  I think Divya is excited to talk about Vue.
[183.68 --> 184.34]  I don't blame her.
[184.46 --> 185.18]  Vue is pretty awesome.
[185.38 --> 188.62]  But then there's interesting things happening in React Land, Angular.
[188.62 --> 193.64]  I think we might touch on Svelte a little bit, that type of thing.
[193.70 --> 198.06]  Then we will kick into another segment on pro tips and close out with some shout outs to
[198.06 --> 199.32]  awesome stuff in the community.
[200.44 --> 203.02]  But let's start on framework wars.
[203.18 --> 204.18]  The framework wars.
[205.06 --> 208.42]  If we were going to go in order of use and popularity, we should start with React.
[208.54 --> 211.38]  But instead, let's go with order of enthusiasm of panelists.
[211.74 --> 213.38]  Divya, you want to tell us what's going on with Vue?
[214.06 --> 214.38]  Yeah.
[214.58 --> 216.86]  So Vue 3 is in the works.
[216.86 --> 219.38]  I do not know what the release date is.
[219.48 --> 222.86]  I think it's slated for end of this year, potentially.
[223.18 --> 225.96]  I don't know if they've actually confirmed a specific date.
[226.40 --> 227.78]  It's been said end of this year.
[228.28 --> 236.56]  But there's a lot of talk happening in the Vue 3 RFC repository on GitHub, where people
[236.56 --> 237.66]  are just talking about APIs.
[238.66 --> 242.58]  And for those of you who are not familiar, I mean, I'm sure everyone at this point is
[242.58 --> 249.08]  because it was a huge conversation that happened from one of the Vue RFC recently.
[249.60 --> 252.00]  Well, semi-recently, a couple months it's been.
[252.60 --> 255.32]  So that was with the functions-based API.
[256.78 --> 260.48]  Cable, you were like aware of that as it was happening, right?
[261.04 --> 261.36]  Yeah.
[261.36 --> 265.66]  I thought it was awesome, but there was definitely some blowback going on there.
[266.46 --> 266.78]  Yeah.
[267.16 --> 269.66]  So it's a huge change to the...
[269.66 --> 274.20]  It's a sort of a pattern that was being introduced into how you would write Vue.
[274.86 --> 281.54]  Essentially, they took a page from React and were moving towards a functions-based API.
[281.78 --> 286.94]  So writing more function-based things rather than your component ties.
[287.18 --> 289.94]  It's still component ties, but the way you write it is slightly different.
[289.94 --> 296.06]  So instead of having your JavaScript, your script, your HTML markup, and your CSS, you
[296.06 --> 299.02]  have just one single function that returns some markup.
[299.66 --> 306.54]  And so that whole thing caused a lot of controversy, mainly because people felt like that was a huge
[306.54 --> 308.08]  shift in the way you would write Vue.
[308.24 --> 315.00]  So the functions-based API was written in a way that seemed to indicate that Vue 3 would
[315.00 --> 321.06]  move away from Vue 2's current syntax, which I think sent a lot of people up in arms because
[321.06 --> 328.30]  the reason a lot of people love Vue and use Vue is because of the current syntax and the
[328.30 --> 335.32]  functions-based API in implying that there was going to be a change basically pulled an Angular
[335.32 --> 336.32]  in a sense.
[336.32 --> 341.18]  Or the community assumed it was pulling an Angular and moving and shifting completely
[341.18 --> 344.40]  away from what the community had been used to.
[345.30 --> 350.82]  What I think sparked that is, and the functions API has been in the works for a while.
[350.94 --> 352.46]  I believe Evan has been talking about it.
[352.94 --> 355.24]  It's been labeled differently.
[355.38 --> 357.50]  It was called the Reactivity API.
[357.50 --> 360.30]  And then there was various other things.
[360.82 --> 364.06]  And then Function API was kind of a consolidation of all of that.
[364.56 --> 368.94]  But what caused that whole debate was this idea of different builds.
[369.64 --> 377.38]  So within the Vue 3 RFC, there was mention of there being a standard build and a compatibility
[377.38 --> 377.98]  build.
[378.24 --> 384.50]  And the idea was that Vue was recommending people to move away from...
[384.50 --> 390.58]  So the standard build would not include a lot of Vue 2 syntax, whereas the compatibility
[390.58 --> 391.52]  build would.
[392.18 --> 396.78]  And so in doing so, there was already, like what we mentioned earlier, there was an indication
[396.78 --> 399.82]  that they were not going to support Vue 2 anymore.
[400.64 --> 405.42]  And so Vue 3, potentially Vue 4, would look completely different than what you were used
[405.42 --> 406.34]  to in Vue 2.
[406.72 --> 410.50]  And so that was the reason why I blew up on Hacker News and Reddit.
[410.72 --> 412.70]  And there was a lot of conversations that happened there.
[412.70 --> 416.10]  Um, there's been some...
[416.10 --> 422.34]  Granted, it was a bit of a miscommunication of like, the Vue core team could have talked
[422.34 --> 423.36]  about things a little better.
[423.58 --> 427.96]  And the community could have kind of tried to ask questions in a way to understand what
[427.96 --> 430.80]  the meaning of things were, instead of jumping to conclusion.
[431.14 --> 434.06]  There was a lot of missteps that happened along the way.
[434.18 --> 439.46]  But essentially, the conclusion is that Vue 3 will not move away from Vue 2 and neither
[439.46 --> 440.18]  Vue 4.
[440.32 --> 444.98]  I think they made that promise as well, that both Vue 3 and Vue 4 will include a lot of
[444.98 --> 445.84]  Vue 2 syntax.
[446.02 --> 452.60]  And so the community can rest assured that they will be able to continue to use Vue how
[452.60 --> 453.48]  they would now.
[453.72 --> 459.66]  But Vue 3 obviously will still include newer patterns like functions and so on.
[460.14 --> 461.68]  Thank you for that summary.
[461.68 --> 464.86]  Yeah, I thought it was an interesting thing to observe in real time.
[465.24 --> 473.00]  Vue has relatively recently adopted a process where they're asking for feedback and they're
[473.00 --> 475.72]  proposing things before they implement things.
[476.56 --> 478.84]  And this was kind of a...
[478.84 --> 483.00]  I mean, on the one hand, they got exposed to a lot of fire from that.
[483.06 --> 487.80]  On the other hand, they probably kept themselves from making some missteps by doing this because
[487.80 --> 491.66]  they heard about it early enough in the process that it was easy to adjust.
[492.48 --> 492.62]  Yeah.
[493.16 --> 498.12]  I've heard people say, you know, pulling an Angular or making the mistake.
[498.28 --> 505.44]  I think that we should just like have a word and say something like, if a library or a project
[505.44 --> 518.80]  completely breaks all of its API in this terrible way that alienates all its users, it's an angularization
[518.80 --> 519.84]  of the project.
[521.52 --> 522.08]  Yes.
[522.40 --> 523.94]  Just turn it into a verb.
[524.22 --> 526.36]  Yeah, it needs to be a verb.
[527.70 --> 528.18]  Angularize.
[529.50 --> 529.68]  Yeah.
[529.88 --> 531.00]  Change management is hard.
[531.92 --> 535.26]  Actually, I really like what Ember does on this.
[535.44 --> 542.28]  Even if it's a little unintuitive for folks coming from other places, Ember will, in their
[542.28 --> 545.98]  major releases, they are never adding new features.
[546.44 --> 549.30]  Major releases are for removing deprecated features.
[549.58 --> 552.82]  So they'll move over the course of a set of minor releases, they'll add new features,
[552.94 --> 554.08]  they'll deprecate old features.
[554.48 --> 556.36]  So they give you lots of time to migrate.
[556.68 --> 561.32]  And then a major update or upgrade is not about adding new functionality.
[561.60 --> 564.78]  It's about removing that deprecated stuff that's been around long enough.
[564.78 --> 566.08]  You've probably moved off it anyway.
[567.78 --> 570.56]  Yeah, that's a really good method of doing things.
[571.10 --> 576.36]  So instead of forcing the community to move and alienating them completely, it's not like
[576.36 --> 577.18]  a cutoff.
[577.32 --> 582.66]  It's you give that tail, the long tail of allowing people to slowly transition.
[583.30 --> 583.46]  Yeah.
[583.56 --> 587.02]  And you introduce the new features early on.
[587.02 --> 589.86]  So they'll never remove functionality in a minor release.
[589.94 --> 591.30]  They'll always add or deprecate.
[591.60 --> 595.14]  So you introduce stuff and people can start experimenting and trying things.
[595.78 --> 599.34]  But you never have a backwards incompatible break except in a major.
[599.70 --> 602.72]  And there you've always had a long run up leading into it.
[602.72 --> 607.46]  So other stuff going on in some of the other frameworks.
[609.08 --> 612.12]  React obviously had their big hooks release a while back.
[612.20 --> 615.58]  That's almost old news, except that it's inspiring view.
[615.94 --> 622.32]  But they're working hard on some new things related to concurrent mode and suspense, which
[622.32 --> 624.14]  I think are pretty interesting.
[624.14 --> 632.92]  They're allowing much cleaner component related abstractions around asynchronous stuff.
[633.20 --> 639.44]  How do we represent a state while we're off fetching data and coming back?
[639.80 --> 647.42]  There was a really fun in-depth blog post that Dan Abramoff did because he loves to tie
[647.42 --> 651.08]  up all of developers' productivity as they try to wrap their heads around his blog posts.
[651.08 --> 656.64]  But he wrote this post on this concept of algebraic effects, which is one of the things they're
[656.64 --> 658.96]  using inside suspense, I think.
[659.76 --> 666.36]  But basically, being able to more or less do go-to statements going around or doing try-catch
[666.36 --> 671.74]  stuff, but where you can kind of move back and forth between different layers of the stack
[671.74 --> 674.62]  in pretty powerful ways.
[674.78 --> 677.20]  So I'm excited to see what they're doing there.
[677.20 --> 682.32]  We've seen before that frameworks can push languages forward.
[682.58 --> 689.44]  A lot of functionality that is in JavaScript now is in it because of things like jQuery
[689.44 --> 696.72]  and Dojo that early on were working around the limitations of the language and of DOM APIs.
[697.00 --> 701.18]  And now they've been embedded in web APIs and embedded in the language.
[701.18 --> 707.72]  So some of the stuff that React is doing now, I think, is really pushing the entire ecosystem
[707.72 --> 710.42]  forward in pretty interesting ways.
[710.98 --> 711.48]  Yeah.
[711.52 --> 717.74]  There was also a conversation that was happening online on Twitter yesterday.
[718.20 --> 720.02]  So actually, the day before yesterday.
[720.14 --> 727.60]  So the 13th of August about I think Sebastian Mark Badge tweeted that render should be pure.
[727.60 --> 732.84]  And it was just about this whole concept of algebraic side effects and how exactly people
[732.84 --> 738.48]  deal with render and how the patterns are generally anti-patterns and how React is trying to move
[738.48 --> 742.92]  people away from doing those things, which sparked a really interesting discussion online.
[742.98 --> 749.40]  Because I think even like Yehuda Katz, who's in the Ember core team and wrote Ember, weighed in
[749.40 --> 757.20]  on that in terms of React, because I think that the concept of and the conversation around
[757.20 --> 763.34]  algebraic effects a lot of the time was framed in terms of purity and writing it purely.
[764.34 --> 769.72]  And I think the argument there was that whenever you talk about something being pure, it's no
[769.72 --> 771.98]  longer it becomes like very abstract.
[771.98 --> 778.18]  And it takes away from beginners learning it because you're starting to make it like super
[778.18 --> 782.98]  high level and you're introducing patterns that kind of are hard to grok if you're learning
[782.98 --> 787.82]  a framework or you're new to a framework, which I think there's a lot to be said there
[787.82 --> 790.40]  and like unpacked within that.
[790.58 --> 795.06]  But I think React has done a lot of this, like, as you said, pushing the bar of thinking
[795.06 --> 802.24]  and introducing ideas and concepts that I think sometimes the community has to, like,
[802.30 --> 804.42]  take time to catch up with, in a sense.
[805.16 --> 811.20]  Because again, it's similar to a conversation we had before, which is that what makes a lot
[811.20 --> 816.72]  of the, and I feel like I'm going ahead a little here, is that every framework is very
[816.72 --> 822.24]  unique because specifically with React, it has a huge company behind it.
[822.24 --> 825.12]  Facebook is what drives a lot of React development.
[825.34 --> 831.14]  And so the problems and the solutions that React, basically a lot of the features that
[831.14 --> 834.88]  React implements is solving problems that Facebook has.
[836.00 --> 843.14]  And so it might be a little high level for, like, us as a community or as a single person
[843.14 --> 848.46]  who's working on a project, a side project or whatever, a company that's really small to
[848.46 --> 853.82]  work on stuff and try to understand why exactly you would need those pieces of the feature.
[854.42 --> 858.84]  And that's compared to, you know, something that's more open source.
[859.10 --> 861.52]  So Svelte, we'll talk about that in a bit, Vue is the same.
[861.80 --> 863.26]  It's not backed by an organization.
[863.48 --> 867.82]  It's pretty much one developer with maybe a couple of people in the core team working
[867.82 --> 868.78]  on specific things.
[868.86 --> 869.50]  They're all developers.
[869.64 --> 873.62]  They have problems that are unique in things that they worked on.
[873.62 --> 875.14]  And that drives the development.
[875.36 --> 880.78]  So it's a lot more, you could argue, community driven than others.
[881.50 --> 886.58]  Even a framework like Ember that is driven by quite a team that's distributed, but it's
[886.58 --> 887.96]  not owned by a single company.
[888.24 --> 890.14]  It's more community driven.
[890.36 --> 891.90]  They have much more of a community process.
[892.52 --> 897.00]  That said, they have very large numbers of core team members who are inside of big companies.
[897.00 --> 904.86]  I think their core team is quite large compared to, for example, Vue, which was for so long
[904.86 --> 906.60]  the one person driven thing.
[906.80 --> 911.82]  And even though it is expanded, it's still a pretty small core team relative to the popularity
[911.82 --> 912.48]  of the project.
[913.96 --> 913.98]  Yeah.
[914.26 --> 914.48]  Yeah.
[914.54 --> 917.60]  This type of cross proliferation is super cool.
[917.74 --> 921.50]  And I love, one of the things I love about the Vue functions API that we were talking about
[921.50 --> 927.82]  is how it takes concepts that were introduced with hooks, which were really quite innovative
[927.82 --> 934.48]  and adapts them to the somewhat different mental model that Vue has and the way that
[934.48 --> 935.74]  Vue approaches reactivity.
[935.94 --> 940.66]  And it almost, I mean, part of this is my bias enjoying Vue quite a lot, but it feels almost
[940.66 --> 942.40]  more natural in the second iteration.
[942.40 --> 946.22]  It works really cleanly with Vue's reactivity model.
[947.06 --> 947.22]  Yeah.
[947.28 --> 949.82]  I think that's the whole point of the functions API.
[949.82 --> 954.84]  It's because a lot of the times with Vue, the reactivity is tied into the component.
[955.24 --> 958.74]  So you need Vue logic in order to have the reactivity work.
[959.82 --> 964.54]  But with the functions API, you get the niceties of reactivity without you having to actually
[964.54 --> 965.86]  write much Vue logic.
[966.46 --> 971.94]  So if you were to, I think this, it's a very common example of like the use mouse where you
[971.94 --> 977.78]  have a mouse and then you want to follow the, and change the XY coordinates as you're moving
[977.78 --> 978.32]  your mouse.
[978.90 --> 984.78]  You can extrapolate the logic of calculating that XY into a separate, so a functions API,
[985.14 --> 990.68]  and then the logic of the front end and manipulating that event can be separate as well.
[990.80 --> 998.02]  So it's kind of like you encapsulate the business logic in a function, and then you can create
[998.02 --> 1000.02]  your Vue or whatever else elsewhere.
[1000.02 --> 1002.58]  And then you can plug and play, which is really nice.
[1003.54 --> 1003.66]  Yeah.
[1003.88 --> 1004.10]  Yeah.
[1004.16 --> 1005.74]  And I found it more intuitive too.
[1005.90 --> 1013.66]  Like, I think when hook, this is also, again, biased opinion and partially a result of being
[1013.66 --> 1015.68]  outside of the react world for a while.
[1016.20 --> 1020.84]  But when hooks came about, I was like, I don't fully understand.
[1020.84 --> 1025.72]  I think there was a lot of magic that happened with like set state and use state and all of
[1025.72 --> 1026.26]  these things.
[1026.56 --> 1030.94]  And so when you're using a hook, you'd use those specific things and then manipulate things
[1030.94 --> 1031.90]  in a specific way.
[1032.86 --> 1037.18]  Versus in the functions API, all you're doing is you're literally writing functions.
[1038.04 --> 1040.90]  And there's actually zero magic there.
[1041.30 --> 1045.72]  I think the reactivity is the one piece where it's like, it's using proxies under the hood.
[1045.72 --> 1049.68]  So if you change the data similar to set state, it updates and so on.
[1049.94 --> 1051.06]  But that sounds magic.
[1051.80 --> 1053.32]  Yeah, it's a little magic.
[1053.70 --> 1054.62]  It is magic.
[1055.68 --> 1059.28]  But I think, yeah, again, it's like a very biased opinion.
[1060.00 --> 1065.92]  But for what it's worth, and I didn't actually, I've barely used react.
[1066.06 --> 1070.64]  But when I first touched it, it was after hooks had come out.
[1070.64 --> 1077.82]  And it made a lot of sense, like not having all this baggage of what react used to do in
[1077.82 --> 1078.30]  my head.
[1078.40 --> 1080.72]  And it was like, oh, well, you can just use this thing.
[1080.80 --> 1081.44]  And there you go.
[1081.86 --> 1086.16]  Of course, I haven't looked at some of the other functions that people talk about, like
[1086.16 --> 1087.30]  use effect or whatever.
[1087.66 --> 1098.36]  But hooks seem to make a lot of sense to me, just coming in as a new, a new, a noob with
[1098.36 --> 1098.96]  react.
[1098.96 --> 1107.94]  Yeah, they're pretty, I like that the hooks approach, and it's a very approachable concept.
[1108.18 --> 1111.56]  It's just different enough that people who were deeply invested in there absolutely had
[1111.56 --> 1112.60]  a little bit of an adjustment.
[1113.44 --> 1120.22]  And that seemed to be like a big part of the uproar with Vue was people who didn't want
[1120.22 --> 1121.90]  to have to change their stuff.
[1122.78 --> 1128.60]  I don't know if they were, you probably have a better idea if they were actually against
[1128.60 --> 1135.18]  the idea itself or just that they didn't want to have to change, you know, how they were
[1135.18 --> 1135.84]  writing code.
[1135.84 --> 1140.14]  I think there was definitely some of each there.
[1140.14 --> 1144.40]  But yeah, there's a lot of just resistance.
[1144.64 --> 1145.72]  I don't I like what it is.
[1145.78 --> 1146.66]  I don't want to change it.
[1146.86 --> 1152.74]  And it's something that is important for framework and library maintainers to remember is that
[1152.74 --> 1155.02]  we like continuity.
[1155.02 --> 1160.16]  There's enough stuff changing in the world that things that we can hold on to are rare
[1160.16 --> 1161.38]  and valuable.
[1161.38 --> 1166.48]  Wasn't some of the motivation there to better support TypeScript, essentially?
[1167.62 --> 1168.14]  Yes.
[1168.78 --> 1169.82]  What do you know?
[1169.96 --> 1172.46]  Like, can you explain in a nutshell what the problem is?
[1172.96 --> 1174.74]  I can explain a little bit.
[1176.32 --> 1180.10]  Though, maybe Divya, you may know a little bit more.
[1180.10 --> 1189.54]  But I think the one of the big challenges with supporting TypeScript within Vue is that it uses
[1189.54 --> 1198.34]  a lot of essentially metaprogramming and introspection, which is somewhat magical and can be somewhat hard
[1198.34 --> 1200.82]  to represent with types.
[1201.38 --> 1208.44]  People who have used Ruby and Rails a lot may know that there they used a lot of metaprogramming.
[1208.44 --> 1213.88]  And if you tried to come in and insert hard types, or at least early days, I always ran into
[1213.88 --> 1218.00]  typing problems because the introspection and metaprogramming meant you had to do a lot of
[1218.00 --> 1219.28]  extra stuff to deal with types.
[1219.40 --> 1222.16]  And I think the Ruby is a very flexible type system.
[1222.92 --> 1225.54]  TypeScript, I don't know.
[1225.88 --> 1226.74]  It's challenging.
[1227.12 --> 1229.86]  And it's trying not to be duct typed in the way that Ruby is.
[1231.44 --> 1237.64]  Going to a functions based API, it removes, you know, Divya, you said there's no magic.
[1237.64 --> 1238.60]  There's still magic.
[1239.18 --> 1241.88]  Reactivity still feels like magic, but it removes some of the magic.
[1242.02 --> 1242.86]  It's just functions.
[1243.06 --> 1247.22]  It's, you know, functions with defined types for their arguments.
[1247.66 --> 1254.84]  It's easy to model and represent in a system in a way that a type checker can validate, as
[1254.84 --> 1259.50]  opposed to something that's assuming properties on an object that may or may not be there that
[1259.50 --> 1261.86]  can be set dynamically in various ways.
[1262.38 --> 1263.64]  Is that a fair assessment?
[1263.64 --> 1270.82]  Yeah, I think the whole reasoning for the rewrite is to support TypeScript and type inference,
[1271.50 --> 1275.22]  because that was an issue, especially with how components were being wrapped.
[1275.48 --> 1277.44]  And checking for types was an issue.
[1277.70 --> 1283.36]  And I think there was also discrepancies in types and specific components or props and
[1283.36 --> 1283.76]  so on.
[1283.84 --> 1286.48]  And so the rewrite kind of made it a first class citizen.
[1286.48 --> 1291.14]  So if you were to write view in TypeScript, it would work very well.
[1291.34 --> 1297.82]  And also whenever, so you have the option in view, whenever you create a component, you
[1297.82 --> 1299.92]  can choose to give the props types.
[1300.54 --> 1303.86]  I think that makes it a little better with the new rewrite.
[1303.98 --> 1305.46]  It makes it a bit better as well.
[1305.96 --> 1309.38]  I'm not 100% sure in terms of the internals of how exactly that is.
[1309.38 --> 1317.58]  But there's more information in the RFC for the function API, I believe, on TypeScript support.
[1318.10 --> 1322.96]  One thing I want to make sure we touch on before we leave a segment on frameworks is Angular.
[1323.42 --> 1328.50]  They are often neglected by me personally, I know, and I think by other folks on this show.
[1328.60 --> 1334.52]  But they do still have huge numbers of people using them, especially, I think, in the enterprise
[1334.52 --> 1335.04]  world.
[1335.80 --> 1338.24]  So I did a little looking to see what's new in Angular.
[1338.24 --> 1345.94]  It sounds like much of the buzz right now is around Angular Ivy, which is a new compiler
[1345.94 --> 1348.10]  slash engine slash renderer.
[1348.18 --> 1349.88]  I'm not being an Angular expert.
[1350.00 --> 1353.14]  I don't know exactly how it fits into the ecosystem.
[1353.96 --> 1359.86]  Some of the touted benefits include reducing bundle size, though coming from view, I was
[1359.86 --> 1362.60]  looking at the bundle sizes they were quoting and being like, really?
[1363.28 --> 1368.18]  Because there was an example on a blog post that I'll put here where it's like, oh,
[1368.18 --> 1368.38]  yeah.
[1368.80 --> 1374.16]  With Angular Ivy, we dropped the bundle size from 509 kilobytes to 432.
[1375.12 --> 1380.54]  And I was kind of groaning a little bit about size.
[1380.62 --> 1382.38]  Is Ivy the current version of Ember?
[1382.80 --> 1383.66]  This is Angular.
[1384.42 --> 1384.92]  Oh, Angular.
[1385.10 --> 1385.54]  Sorry, sorry.
[1385.76 --> 1386.16]  Yeah.
[1387.00 --> 1387.80]  Yes, Angular.
[1387.80 --> 1396.18]  I believe it is opt-inable, but not the default for their renderer.
[1397.28 --> 1400.02]  So is Angular, that's, okay.
[1401.48 --> 1404.18]  They recently released version 8.
[1404.44 --> 1405.26]  8, yeah.
[1405.90 --> 1409.68]  And that made Ivy available but opt-in.
[1409.68 --> 1410.16]  Okay.
[1411.16 --> 1414.94]  I know very little about Angular to weigh in on anything.
[1415.78 --> 1422.50]  Frankly, it feels to me like on many dimensions, they are catching up.
[1422.94 --> 1427.54]  Some of the other touted benefits are now it's easier to do higher order components and things
[1427.54 --> 1430.38]  like that that have been around in Vue and React for a long time.
[1430.38 --> 1439.40]  I do believe that some of the functionality that exists in Angular around managing large
[1439.40 --> 1444.40]  scale applications, the way they do dependency injection, all of that sort of stuff provides
[1444.40 --> 1447.22]  substantial benefits for people who are doing massive projects.
[1447.22 --> 1454.92]  But yeah, it feels like right now they're in many ways doing kind of the same thing Vue's
[1454.92 --> 1458.88]  doing with the functions API of playing catch up to innovations that have happened elsewhere
[1458.88 --> 1459.74]  in the ecosystem.
[1460.26 --> 1466.40]  I think they also with Ivy, like I know I haven't used Angular and I don't know much about the
[1466.40 --> 1468.50]  ecosystem, but I've heard people talk about it.
[1468.50 --> 1477.72]  And Ivy also is, I think tree shaking is like top priority in Ivy, which means that, which
[1477.72 --> 1483.56]  again, results in faster performance because your bundle size is smaller and it can remove
[1483.56 --> 1485.44]  unused pieces of code and so on.
[1485.60 --> 1486.98]  Load times are great.
[1488.60 --> 1496.04]  I'm not 100% sure how, but I think, does it have anything to do with how things get compiled?
[1496.04 --> 1498.54]  Like, has that changed with this?
[1499.74 --> 1501.72]  I think so.
[1501.82 --> 1504.26]  Because one of the things touted is faster compilation.
[1505.04 --> 1510.34]  But anyway, this is definitely outside of any of our expertises, it looks like.
[1510.48 --> 1513.96]  If you are an Angular expert, I would love to hear from you a little bit more about how
[1513.96 --> 1514.44]  this works.
[1514.92 --> 1518.96]  So you can jump in to the JS Party Slack channel.
[1519.18 --> 1520.92]  You can tweet at me or at JS Party.
[1520.92 --> 1526.38]  I think there's some interesting stuff going on in that world, but I feel like I'm kind
[1526.38 --> 1527.16]  of outside of it.
[1527.84 --> 1535.46]  But because Angular is still quite, quite, quite widely used, especially at larger enterprises,
[1535.74 --> 1540.62]  I felt we would be negligent if we did not bring it up.
[1541.30 --> 1541.70]  Oh, for sure.
[1541.78 --> 1541.94]  Yeah.
[1541.94 --> 1547.12]  It seems that Ivy is a new rendering pipeline in Vue Engine.
[1548.18 --> 1551.18]  So yeah, the compilation and stuff has changed.
[1551.92 --> 1556.90]  One last thing that I think is really interesting going on in front-end frameworks right now is
[1556.90 --> 1561.04]  this idea of compile-time frameworks.
[1561.44 --> 1563.64]  The one in particular I'm thinking of is Svelte.
[1563.76 --> 1565.66]  Chris, you mentioned that you played around with it some.
[1565.72 --> 1567.10]  Do you want to talk to us about Svelte?
[1567.10 --> 1576.46]  Oh, I mean, there's really not a whole lot I can say except that I was working on an app.
[1577.20 --> 1582.96]  I was just kind of playing around, trying to get something working with Node, Serial Port,
[1583.02 --> 1583.70]  and Electron.
[1583.70 --> 1595.92]  And I wanted to try a framework and didn't want to get into a huge toolchain like with
[1595.92 --> 1601.42]  Create React app or, you know, views to toolchain is sizable.
[1601.84 --> 1605.14]  And all these boilerplates drive me nuts, but that's another thing.
[1605.20 --> 1606.54]  So I didn't want to use a boilerplate.
[1607.10 --> 1612.60]  I found something very simple with Svelte.
[1612.60 --> 1620.92]  It's basically you have like a roll-up config or something like that, and you run the thing
[1620.92 --> 1622.44]  and it compiles the thing.
[1622.54 --> 1626.94]  And you look at your code, it is like the dead simple.
[1627.14 --> 1628.66]  It's kind of like view, right?
[1628.76 --> 1636.66]  Where you have this, I think it's a .svelte file, which is kind of analogous to a .vue file
[1636.66 --> 1641.94]  where you have your script, you have your styles, you have your markup in there.
[1642.68 --> 1652.98]  It is so just straightforward and simple and elegant and just like, wow, how easy can this be?
[1652.98 --> 1663.30]  And I was just kind of, my brain melted a little bit just because it was far and away the most straightforward
[1663.30 --> 1667.04]  and easy to understand framework that I'd used in a long, long time.
[1667.04 --> 1674.22]  And I think definitely people should take a closer look at Svelte.
[1675.36 --> 1680.36]  From that end of things, I mean, I felt like the architecture of the project,
[1680.50 --> 1686.08]  because what's different about Svelte as far as I understand is essentially it has no runtime.
[1686.54 --> 1687.94]  It's just a compiler.
[1687.94 --> 1696.56]  And you write this code that follows these conventions and it poops out a bundle
[1696.56 --> 1701.56]  and markup and whatever it needs to do and it runs.
[1701.72 --> 1708.10]  And the bundle sizes are very small and there's not a lot of startup overhead
[1708.10 --> 1710.34]  because it doesn't have to bootstrap all this stuff.
[1710.54 --> 1715.22]  It's just kind of incredible and a great idea.
[1715.22 --> 1718.56]  And I feel like frameworks are going to start moving in that direction
[1718.56 --> 1726.14]  where they kind of, they get rid of this whole overhead of loading a runtime in your browser
[1726.14 --> 1727.26]  or what have you.
[1727.80 --> 1734.08]  And it's just simply compiling down to minimal vanilla JavaScript.
[1735.14 --> 1738.96]  But because of that architecture, they could optimize for,
[1739.08 --> 1741.78]  well, what's the simplest straightforward thing we can do?
[1741.78 --> 1745.10]  Let's look at what's been successful in the past.
[1745.22 --> 1749.78]  Like, you know, people talk about how easy Vue is to understand
[1749.78 --> 1753.40]  for somebody who's really new to JavaScript or web development.
[1753.68 --> 1759.70]  And they went with that idea, I think, and just kind of let's make this even easier
[1759.70 --> 1761.42]  and just simple and straightforward.
[1763.16 --> 1765.90]  Yeah, I was just really impressed with Svelte.
[1766.64 --> 1770.26]  You know, I don't really build too many web apps.
[1770.26 --> 1774.08]  If I do, they are of the hobby variety.
[1774.54 --> 1778.12]  So, but I'm definitely going to take a look at it
[1778.12 --> 1782.46]  and keep, I'm going to keep working with it on this particular project
[1782.46 --> 1784.34]  because it's awesome.
[1784.98 --> 1785.16]  Yeah.
[1785.46 --> 1790.38]  Svelte also has a, like, server-side rendering framework called SAPA.
[1790.38 --> 1793.70]  That's really cool.
[1793.84 --> 1799.46]  If you want to do server-side rendering or using, like, a Node.js backend and so on.
[1800.40 --> 1801.30]  It's pretty cool.
[1801.66 --> 1802.88]  It's really easy to use.
[1803.24 --> 1804.36]  It's also super small.
[1804.94 --> 1811.78]  I think it's, according to the website, it is 39.9 kilobyte zipped,
[1812.32 --> 1813.28]  which is pretty small.
[1813.28 --> 1816.04]  Way smaller than React.
[1816.34 --> 1819.32]  Not sure about Vue, but definitely smaller than React.
[1819.38 --> 1822.42]  And I think they argue that they don't have to do code splitting
[1822.42 --> 1825.62]  and stuff like that because of the way that the compilation works.
[1826.14 --> 1829.02]  And so it's incredibly performant and efficient.
[1829.82 --> 1834.22]  Yeah, I was, I noticed that and I didn't pick it up
[1834.22 --> 1838.52]  because it's an Electron app that needs to use a native module,
[1838.52 --> 1843.24]  which can be kind of a heroining experience.
[1843.74 --> 1846.00]  And if you have a dev server running in Node
[1846.00 --> 1850.48]  and you need to use a native module, you're SOL.
[1850.90 --> 1856.50]  And so, you know, I tried to use, like, next.js.
[1856.94 --> 1859.18]  I tried to use nuxt.js.
[1859.40 --> 1861.32]  And neither of these things worked for me
[1861.32 --> 1862.90]  because I needed that native module.
[1863.20 --> 1865.04]  And if the dev server is running in Node,
[1865.04 --> 1867.10]  well, the native module is compiled for Electron.
[1867.10 --> 1871.40]  I mean, you know, it's water and oil and it just doesn't work.
[1871.74 --> 1875.38]  So, but yeah, that definitely looks like a pretty cool
[1875.38 --> 1877.82]  server-side framework.
[1878.22 --> 1878.48]  What is it?
[1878.74 --> 1879.14]  Sapa?
[1879.38 --> 1879.74]  Sapper?
[1880.48 --> 1880.88]  Sapper.
[1881.42 --> 1881.82]  Sapper.
[1882.28 --> 1886.90]  And with that, I think we can wrap up this segment,
[1887.04 --> 1887.82]  the Framework Wars.
[1888.00 --> 1889.46]  This was our first try on it.
[1889.82 --> 1891.60]  So listeners, let us know.
[1891.70 --> 1892.36]  Give us some feedback.
[1892.58 --> 1893.14]  Did you like it?
[1893.18 --> 1893.92]  Did you not like it?
[1893.94 --> 1894.60]  Was this useful?
[1894.60 --> 1896.50]  When we come back from our break,
[1896.52 --> 1898.92]  we will be talking about some pro tips,
[1899.18 --> 1902.92]  things you can use today to make your life,
[1903.00 --> 1904.90]  your development, what have you, better.
[1905.44 --> 1906.50]  Talk to you on the other side.
[1906.50 --> 1919.66]  This episode is brought to you by Keen.
[1919.98 --> 1921.80]  Keen makes customer-facing metrics simple.
[1922.18 --> 1927.34]  It's a platform that gives you powerful in-product analytics fast with minimal development time.
[1927.62 --> 1932.76]  For example, a DIY solution to build out customer-facing metrics in your product could take six months or more.
[1932.76 --> 1934.78]  And with Keen, you can be up and running it the same day.
[1934.78 --> 1938.88]  The Keen platform lets you stream events to easily collect and enrich your data,
[1939.24 --> 1942.32]  compute with embeddable answers, insights, and metrics,
[1942.70 --> 1946.00]  access controls so you can design role-based access to your data,
[1946.32 --> 1949.84]  and of course, a visualization layer to create stunning charts.
[1950.28 --> 1953.18]  And we have a special offer just for our JS Party listeners.
[1953.66 --> 1958.74]  Go to keen.io slash jsparty and get your first 30 days of Keen for free.
[1958.74 --> 1963.52]  And as a bonus for checking out a 15-minute demo of Keen's customer-facing metrics,
[1963.84 --> 1965.42]  they'll send you a free Keen t-shirt.
[1965.76 --> 1967.98]  Go to keen.io slash jsparty.
[1968.20 --> 1970.40]  Again, keen.io slash jsparty.
[1970.40 --> 1985.56]  Welcome back, JS Partiers.
[1985.82 --> 1991.82]  We are here to talk about pro tips, pro tips from each of our panelists and me.
[1991.90 --> 1996.84]  Now, it looks like Chris and Divya, you both have very technical-related pro tips,
[1996.84 --> 2000.26]  whereas I have kind of an interpersonal one, so let's sandwich me in the middle.
[2000.72 --> 2002.70]  Either of you want to particularly go first?
[2003.08 --> 2003.84]  I can go first.
[2004.40 --> 2009.50]  So recently, I was working in a...
[2009.50 --> 2010.30]  I write JavaScript.
[2010.54 --> 2011.54]  I do not write TypeScript.
[2011.74 --> 2015.34]  And so I'm used to using docstrings.
[2015.34 --> 2017.00]  And so I'm using docstrings.
[2018.10 --> 2029.28]  And I'm seeing that VS Code is giving me some information about types.
[2029.72 --> 2033.12]  And it's able to understand the docstrings and stuff.
[2033.22 --> 2034.06]  So I say, huh, that's neat.
[2035.86 --> 2038.08]  And so I was digging into it more.
[2038.20 --> 2039.98]  And it's like, well, how can I make this work even better?
[2039.98 --> 2051.96]  And so I got kind of OCD about the docstrings and was reading up on VS Code's site about writing.
[2052.20 --> 2060.46]  There's like a guide or two on there about writing JavaScript in VS Code and how it works
[2060.46 --> 2063.40]  and how you can get better integration.
[2063.40 --> 2068.50]  And so one of the things I started doing was in my JavaScript files,
[2068.66 --> 2073.40]  I would put a little directive in a comment called TSCheck.
[2074.04 --> 2075.62]  So it's like at TSCheck.
[2075.78 --> 2082.60]  And so what that does is it enables the TypeScript language server to essentially check your JavaScript.
[2083.06 --> 2092.18]  And so because JavaScript is a subset of TypeScript or TypeScript is a superset of JavaScript or whatever,
[2092.18 --> 2093.88]  because of that.
[2094.04 --> 2099.92]  And when you're writing JavaScript in VS Code, you're actually using the TypeScript service anyway.
[2101.34 --> 2105.70]  So this TSCheck, it enables full type checking of all your JavaScript.
[2106.88 --> 2115.48]  And so it'll give you some little gentle warnings when it finds something it doesn't know about.
[2115.48 --> 2122.40]  And it's got this little, I don't know what they're called, intentions, I think.
[2122.56 --> 2126.34]  That's what they were called in JetBrains anyway.
[2126.56 --> 2133.52]  But so you go and you like hover over the little squiggly and it says, this is in any type.
[2133.60 --> 2138.40]  Do you want to try to determine the type of this by its usage?
[2138.40 --> 2139.22]  And you say yes.
[2139.30 --> 2147.64]  And so it goes and it looks through all your code and it tries to determine what the type is.
[2147.92 --> 2152.72]  And so when it does that, it actually like plops a little doc string in there.
[2152.76 --> 2155.40]  And it's all working with JSDoc.
[2155.40 --> 2164.64]  And so TypeScript supports a few JSDoc tags, just pretty much as many as it really needs, which is not too many.
[2165.32 --> 2173.80]  So you can use TypeScript types in your JSDoc doc string types.
[2173.90 --> 2178.02]  And so I started doing this and I say, wow, this is really neat.
[2178.02 --> 2184.36]  And I can get full type checking just with a few extra doc strings, essentially.
[2184.66 --> 2188.22]  And so eventually I went and there's a setting.
[2188.34 --> 2191.78]  If you make something, it's called a jsconfig.json file.
[2191.90 --> 2193.06]  And I'd seen this file before.
[2193.16 --> 2194.10]  I wasn't sure what it was.
[2194.88 --> 2197.26]  And this sits in your project route.
[2197.62 --> 2205.58]  And it tells the TypeScript language service in VS Code how to check your JavaScript.
[2205.58 --> 2212.94]  And so I configured that and I told it to check all the JavaScript files.
[2213.16 --> 2215.34]  And so that's what it did.
[2215.56 --> 2223.58]  And so it goes through all my source files and finds all the places where the JSDoc doc strings don't match.
[2223.70 --> 2226.06]  It finds all the places where it can't make inferences.
[2226.58 --> 2231.92]  And, of course, it pulls out all these typings from NPM and automatically downloads them.
[2231.92 --> 2237.26]  And so on the main, all the third-party modules I was using already had some types.
[2237.44 --> 2238.82]  And so it knew about all those.
[2238.92 --> 2244.54]  All I had to do was write a few more types in my doc strings.
[2245.14 --> 2254.98]  And so my project that I'm working on, at this point, it's pretty much fully typed using doc strings and TypeScript.
[2254.98 --> 2257.18]  But it's not TypeScript at all.
[2257.26 --> 2259.12]  There's no TypeScript whatsoever.
[2259.82 --> 2262.18]  And it's fully type checked.
[2262.46 --> 2263.92]  And I'm like, wow, that's kind of amazing.
[2265.30 --> 2274.04]  And, in fact, it's like, what's the point of TypeScript anymore if the language server can actually just type check all your JavaScript for you?
[2274.12 --> 2279.98]  And if you have these type definition files, you have doc strings, there's really no need for all that extra syntax.
[2279.98 --> 2289.46]  And at least from my point of view, that's a huge win because I don't really want to get hung up on the extra syntax of TypeScript.
[2289.66 --> 2292.24]  Certainly there's a few things that you probably cannot do.
[2293.22 --> 2295.34]  But I have not run into those yet.
[2296.78 --> 2300.30]  And so, yeah, this is like many, many source files.
[2300.48 --> 2305.88]  It's a relatively large project for a single person to have been working on.
[2305.88 --> 2307.86]  But everything's type checked.
[2308.22 --> 2311.72]  And it's just doc strings if you follow their guide.
[2313.38 --> 2316.72]  And, you know, you can create type definitions.
[2317.22 --> 2322.84]  So, like in TypeScript, you would make an interface to do this sort of thing or a type alias.
[2323.48 --> 2327.28]  In JavaScript, what you do is you use a JS doc type def.
[2327.28 --> 2328.36]  So, it's at type def.
[2328.46 --> 2335.24]  And then you can define, you know, what the base type is and define all the properties or whatever of a particular type.
[2335.98 --> 2342.12]  And I just made it work with type def to define my interfaces.
[2342.78 --> 2344.18]  And, yeah, it's great.
[2344.50 --> 2345.26]  It's awesome.
[2345.26 --> 2357.96]  And as long as I'm talking about it, you know, shout out to Daniel from the TypeScript team who helped me get some of this stuff working a little more quickly.
[2358.38 --> 2366.00]  I was running into performance issues because I essentially had a misconfiguration in this monorepo that I had.
[2366.36 --> 2369.78]  And so, he helped me get that set up.
[2369.86 --> 2372.68]  And now it works just splendidly.
[2372.68 --> 2385.62]  And I totally recommend if you're writing doc strings, you know, if you're using JS doc and you're using VS Code, take a look at that, you know, writing JavaScript in VS Code.
[2386.48 --> 2392.48]  And it'll show you how to set up all your TypeScript settings or what have you.
[2392.86 --> 2399.36]  And get all that type inference just as nice as you would in TypeScript.
[2399.94 --> 2400.92]  And, yeah, it's great.
[2400.92 --> 2403.16]  And that's my big pro tip.
[2403.56 --> 2404.32]  That's awesome.
[2404.70 --> 2404.94]  Yeah.
[2405.08 --> 2406.24]  I had no idea about that.
[2406.66 --> 2417.16]  Yeah, I'm very – yeah, because I feel like there's a lot of times I question why – like, I see the reason for using TypeScript because type inference and type checking is really nice.
[2417.16 --> 2424.56]  But a lot of times it's a huge, like, extra thing for me to do and write things in a completely different manner than I'm used to.
[2425.12 --> 2427.34]  And so, I tend to chuck it to the wayside.
[2427.56 --> 2433.12]  But JS doc is something that is actually really easy to integrate because it's essentially just documenting your function.
[2433.12 --> 2436.96]  And if you could do a lot of the type checking within that, that's super cool.
[2437.46 --> 2437.68]  Yeah.
[2437.86 --> 2439.48]  It speaks, you know, the param.
[2439.88 --> 2442.86]  It speaks the types and return values.
[2443.02 --> 2445.74]  Of course, it supports TypeScript syntax.
[2445.84 --> 2451.46]  It seems to support the Clojure compiler syntax, too, for defining types.
[2451.46 --> 2457.14]  And so, it's pretty loosey-goosey with how you want to write your doc strings.
[2457.56 --> 2459.28]  But the inference works great.
[2459.84 --> 2464.40]  You know, if – all you've got to do is really fill in some holes.
[2465.20 --> 2471.30]  And if you're passing objects around, you need to describe the shape of those objects.
[2471.50 --> 2473.72]  And you're – I mean, that's basically it.
[2474.08 --> 2477.02]  You know, that was the main thing that I needed to do.
[2477.02 --> 2486.54]  Otherwise, if you have a class, like an ES6-style class, it understands everything about that class.
[2486.64 --> 2488.64]  It understands all the methods, the static methods.
[2488.88 --> 2497.70]  It knows when you say, you know, this.foo is bar, it knows that foo is a property of an instance of, you know, whatever class you have.
[2497.82 --> 2499.60]  And the inference is awesome.
[2499.60 --> 2506.26]  And I didn't have to go through everything and, you know, define every return type because it knew.
[2507.02 --> 2511.20]  So, yeah, I've gotten a long way with it and highly recommend it.
[2511.78 --> 2511.92]  Cool.
[2512.46 --> 2512.78]  All right.
[2513.30 --> 2515.50]  I will pick up for the next one.
[2515.60 --> 2519.94]  My set of pro tips is related to talking to users or stakeholders.
[2520.26 --> 2524.32]  I think most engineers have now heard it's important to talk to your users.
[2524.66 --> 2531.98]  And whether or not you have internalized it or not, it is important to talk to your users to understand how they're using and what they need.
[2531.98 --> 2542.86]  But one of the trickiest things, I think, particularly for engineers, is to understand that users are really bad at telling you what they need and what they want.
[2543.52 --> 2545.70]  And they're bad in a kind of particular way.
[2546.56 --> 2554.82]  They will come to you and they'll say something like, I think this project or this thing needs to do X, Y, Z.
[2554.82 --> 2558.74]  And they'll tell you something and they'll tell you what is essentially a solution.
[2558.96 --> 2560.06]  I want this thing.
[2561.44 --> 2563.16]  But users are really bad at solutions.
[2563.36 --> 2564.98]  So this solution will usually be half-baked.
[2565.10 --> 2565.86]  It'll be really weird.
[2566.04 --> 2570.10]  And if you actually build it the way they say it, they'll try it and it won't work and it won't do what they want.
[2570.54 --> 2575.14]  And I'm saying users, but stakeholders or clients are often the same way.
[2575.20 --> 2576.84]  They'll say, I want this.
[2577.02 --> 2577.92]  They'll describe a thing.
[2578.00 --> 2578.66]  You build the thing.
[2578.66 --> 2580.54]  Then they try it and they don't like it.
[2581.38 --> 2586.32]  But where users and stakeholders and people, this is a human thing.
[2586.40 --> 2588.24]  We're very bad at imagining the future in general.
[2588.78 --> 2591.68]  But what we're really good at is describing what our problems are.
[2592.44 --> 2599.28]  And so when somebody comes to you, if you're talking to a user or something like that, and you say, and they say, I think you need X, Y, Z.
[2599.28 --> 2608.68]  Your job as an engineer or a project manager, whatever your role is in this situation, is to try to uncover what is the underlying problem.
[2609.66 --> 2614.58]  So sometimes it's as simple as saying, okay, what's the problem you're trying to solve with that?
[2615.08 --> 2616.04]  Can you show it to me?
[2616.12 --> 2617.62]  Can you tell me more about it?
[2618.44 --> 2620.18]  Sometimes you need to dig a little bit more.
[2620.74 --> 2627.46]  An extremely useful question I found is, you say, what's the most challenging or frustrating thing about X?
[2627.46 --> 2635.32]  And if they've put a situation or a solution in front of you, say, okay, with that, what's the most frustrating thing that you're trying to solve with that?
[2636.00 --> 2648.56]  And use that to kind of uncover the problem, which if you have a really good problem and a really good understanding of the underlying problem, coming up with a solution, you can try a bunch of different solutions.
[2649.04 --> 2653.84]  You can explore the solution space and figure out something that will actually solve that problem very well.
[2653.84 --> 2662.38]  But if you stay at the level of the thing that the user told me or the thing that my client told me, you're going to end up with a really half-baked solution.
[2662.92 --> 2673.20]  So my pro tip is talk to your users, talk to your clients, but use the things they tell you to try to understand their underlying problems, not as this is what they actually want.
[2673.74 --> 2674.92]  And that is my pro tip.
[2675.06 --> 2675.94]  Divya, how about you?
[2676.08 --> 2676.54]  What you got?
[2676.54 --> 2681.46]  I feel like mine is a bit technical, but also built on what you were mentioning.
[2681.78 --> 2684.40]  I think the key part of it is this idea of communicating.
[2685.40 --> 2693.16]  And it's generally, I think, underappreciated in tech, this importance to communicate.
[2693.16 --> 2702.36]  Because everyone just assumes you have to be like elite coder and be very technical and know everything there is to know about code and writing code.
[2702.50 --> 2710.74]  But a lot of the job is just basically like talking to users and stakeholders and coworkers and having those communication things.
[2710.74 --> 2720.04]  So I am usually on the developer experience dev rel team, which means that I work outside of the product team.
[2720.22 --> 2724.16]  I work kind of alongside, but more or less outside.
[2724.54 --> 2728.50]  So they have their own sprint planning and their own review cycles.
[2729.20 --> 2730.88]  And we are kind of outside of that.
[2730.88 --> 2734.24]  And so the last few weeks, I joined recently.
[2734.66 --> 2735.72]  So we're doing product rotation.
[2736.06 --> 2742.60]  So the dev rel developer experience people move into product to work on product.
[2743.76 --> 2754.16]  And my perception of it, interestingly, was that, oh, I'm going to write so much code and be really productive and contribute to the code base and do all of these things.
[2754.16 --> 2760.24]  But I realized that I actually have more meetings now because I'm talking to key stakeholders.
[2760.24 --> 2761.58]  I'm talking to coworkers.
[2761.58 --> 2768.74]  I'm doing a lot of these sync ups with the design team just to make sure that everyone's on the same page and they were on board with things that are happening.
[2769.60 --> 2777.88]  And so that's like just something that is often forgotten that in tech, oftentimes you're actually talking more than you're right.
[2778.16 --> 2782.86]  You're either talking or you're reading other people's code more than you're actually writing code.
[2782.86 --> 2790.78]  Just because there's a lot of work that has happened before you or is happening while you're working alongside you.
[2791.12 --> 2798.02]  And so you have to always be aware because you're not working alone unless you're a freelancer or you have your own projects.
[2798.24 --> 2804.96]  But otherwise, if you're on a team, you constantly have to have that back and forth communication that happens.
[2805.50 --> 2807.76]  If you're a freelancer, you absolutely have to have that.
[2807.76 --> 2812.10]  I mean, yeah, maybe not like direct co-workers.
[2812.10 --> 2814.74]  But yeah, yes.
[2815.14 --> 2820.68]  And so related to that is actually this idea of like Git hygiene.
[2821.64 --> 2828.08]  So I've more or less in my time at Netlify, it's been about a year.
[2828.72 --> 2832.12]  A lot of the projects that I work on tend to be pretty independent.
[2832.64 --> 2835.00]  So it's similar to being an individual contributor.
[2835.20 --> 2836.22]  You're working on code.
[2836.22 --> 2841.14]  You don't really get a lot of review because oftentimes it's demos, it's integrations.
[2841.34 --> 2843.16]  You work with the community a lot.
[2844.18 --> 2847.90]  And so, yeah, there's community review, but it's not as stringent as working on a team.
[2848.60 --> 2861.32]  And so I realized that my Git hygiene has actually gone pretty bad, which is nice because in a way, me being on the product rotation has kind of put me back into the right track of making sure I'm aware of that.
[2861.32 --> 2866.24]  So one of the things is just this idea of merging and squashing and changing history.
[2867.10 --> 2871.30]  And so that often, I don't know, it's like shooting yourself in the foot.
[2871.34 --> 2872.68]  I really like clean history.
[2872.94 --> 2880.72]  And that actually ended up being terrible for me in my time on the product team, which is actually really short.
[2880.72 --> 2891.68]  Because I was working on a specific update to a feature and that, like a lot of things, sometimes the feature set grows.
[2892.08 --> 2895.48]  So they're like, oh, if you're doing this one thing, you also have to do this other thing.
[2895.84 --> 2897.08]  And then you have to do this other thing.
[2897.20 --> 2901.48]  And so what I ended up doing is I branched off of that branch.
[2901.66 --> 2904.96]  So I branched off of master and then I branched off of that branch.
[2905.66 --> 2909.92]  And I think there were like three or four branches of a branch that branched into master.
[2909.92 --> 2915.92]  And I don't know why, but I was so committed to like, yeah, I got this.
[2916.02 --> 2918.12]  I'm going to make sure the history is clean and everything.
[2919.06 --> 2920.98]  And master kept moving forward.
[2921.24 --> 2924.32]  And obviously, I wanted to make sure everything was continuous.
[2924.32 --> 2927.96]  So I changed the history of the main branch, which is horrible.
[2928.16 --> 2929.82]  Like never do that ever, ever, ever.
[2930.20 --> 2935.30]  Because if you change the history of the branch that other branches are branching off of,
[2935.30 --> 2939.70]  you're just in for a nightmare of just nothing is going to resolve.
[2940.34 --> 2945.30]  Every time master moves forward and you do a rebase, you're going to have like infinite merge conflicts.
[2945.78 --> 2946.52]  It's horrible.
[2947.10 --> 2951.82]  So that's something I learned from this experience.
[2951.82 --> 2952.82]  Yeah.
[2952.82 --> 2953.18]  Yeah.
[2954.22 --> 2959.04]  So I think if anything, it's just like have a better sense of working with Git.
[2959.80 --> 2964.24]  Make sure you work in a way, if you're working on a team, understand what the conventions are.
[2964.82 --> 2970.58]  So at Netlify, it's pretty nice because there is a documentation for conventions in terms of how you name branches,
[2970.72 --> 2972.00]  how you branch off of things.
[2972.00 --> 2978.36]  If a branch, if a specific feature is starting to get bigger, you call it a release branch.
[2978.70 --> 2983.72]  And then you make sure that anything branching off of a release branch gets merged in as soon as possible.
[2984.00 --> 2988.10]  Because otherwise, when there are stale branches, it's not fun.
[2988.38 --> 2988.92]  It's not fun.
[2989.48 --> 2996.46]  We had a mini discussion on a different episode about Git histories and whether to squash or not squash.
[2996.60 --> 2998.72]  And we quickly derailed because we could see that.
[2998.78 --> 3001.32]  I mean, this could be a debate episode entirely in itself.
[3001.32 --> 3001.74]  For sure.
[3001.98 --> 3002.56]  For sure.
[3002.72 --> 3008.16]  But I mean, like I was very much on the side with Nick in I really like squashing.
[3008.50 --> 3012.60]  And then this was the one time where I was like, oh my gosh, squashing was the most thing to do.
[3013.58 --> 3015.08]  I think it's just a meta.
[3015.08 --> 3019.90]  It reminds me of metaprogramming in the sense that it feels really cool and slick.
[3020.04 --> 3022.72]  And it makes things so clean and nice and beautiful.
[3023.42 --> 3027.74]  And as you hang yourself with it or shoot yourself in the foot with it a time or two,
[3027.74 --> 3033.20]  you start to value more and more the beauty of explicitness.
[3033.40 --> 3034.20]  Oh, yeah.
[3034.38 --> 3044.04]  And I think it's a matter of making sure you understand why you're doing something and the pros and cons of that decision rather than being dogmatic.
[3044.04 --> 3054.66]  So the reason why this whole debacle happened was because I was so sure of myself that squashing was like, this is how I made sure everything was going to be clean and efficient.
[3054.66 --> 3063.50]  But I didn't think about the ramifications of that decision because if I were to think about it again, I still like squashing.
[3064.12 --> 3070.08]  But if you wanted to squash, you wouldn't change the history if anything is branching off of a branch.
[3070.58 --> 3075.96]  So if you're like master, you have branch A and then you have A prime and whatever else.
[3075.96 --> 3083.38]  Never change the history of A because A prime is related to A and therefore it will cause a lot of issues.
[3083.58 --> 3088.62]  So until A prime gets merged into A, do not ever change history.
[3089.24 --> 3092.68]  And then afterwards, once everything is done and there's only one branch, then sure, whatever.
[3092.84 --> 3094.34]  Change history if you want or not.
[3094.66 --> 3096.38]  But that's the main thing.
[3096.40 --> 3097.60]  It feels so obvious.
[3097.60 --> 3099.90]  It feels like such an obvious thing.
[3099.90 --> 3105.40]  But yeah, that was one of the things that is a learning point for me.
[3106.10 --> 3110.54]  But it's obviously really nice to have that course correction for me.
[3111.20 --> 3114.80]  The other thing that I wanted to note is we've been talking a lot about the frameworks.
[3115.30 --> 3117.84]  And I'm really excited about Vue because I work on Vue a lot.
[3119.28 --> 3124.70]  And from the conversations that we're having, if you're interested in how exactly the implementation of that works,
[3124.70 --> 3134.56]  there is a node module for the functions API that allows you to play around with the functions API as a separate...
[3134.56 --> 3136.70]  You can add it into an existing Vue project.
[3137.92 --> 3138.94]  And you can import it.
[3138.98 --> 3140.98]  I think you would just do like Vue.use.
[3141.12 --> 3142.50]  So it's essentially like a plugin.
[3143.10 --> 3147.04]  So you would plug it in and then you can use it alongside your current Vue code.
[3147.04 --> 3154.46]  And I've done it with projects that I've worked on just to have a better sense of what exactly the functions API is.
[3154.70 --> 3157.54]  I think it also gives you an ability to have an opinion.
[3158.68 --> 3169.14]  Because it's really hard to have a sense of the implications of a feature change without knowing how it translates into code.
[3169.68 --> 3174.12]  And so though there are examples in the RFC of how exactly to use the API,
[3174.12 --> 3181.92]  I think writing it yourself gives you a better sense of how exactly you would use it rather than how someone else would use it.
[3181.92 --> 3182.80]  So yeah.
[3182.90 --> 3188.84]  And obviously like being able to make mistakes within it also gives you a better sense.
[3188.90 --> 3191.42]  Because I would use it liberally everywhere.
[3191.88 --> 3194.30]  And I would be like, maybe I can do it this way and this way.
[3194.40 --> 3199.28]  And I've had chats with the core team and they're like, that's not how we intended it to be used.
[3199.64 --> 3205.80]  But I think that is great because it's a good way for you to experiment with up and coming features.
[3205.80 --> 3208.36]  And then also be able to contribute to that discussion.
[3209.20 --> 3209.46]  Awesome.
[3209.84 --> 3212.94]  I think that makes for a great set of pro tips.
[3213.60 --> 3214.12]  Communication.
[3214.60 --> 3216.26]  And communication with yourself.
[3216.62 --> 3216.88]  With Git.
[3217.52 --> 3217.80]  Yeah.
[3218.06 --> 3218.42]  All right.
[3218.86 --> 3220.58]  Let's call that a segment.
[3220.92 --> 3227.88]  And we will be back shortly with segment three where we're going to do some shout outs to our favorite people and things happening in the community.
[3228.38 --> 3229.32]  Catch you on the other side.
[3229.32 --> 3259.30]  Let's do it.
[3259.32 --> 3261.10]  We get great 24-7 support.
[3261.40 --> 3264.02]  Zeus like powers with native SSDs.
[3264.18 --> 3269.40]  A super fast 40 gigabit per second network and incredibly fast CPUs for processing.
[3269.84 --> 3271.96]  And we trust Leno because they keep it fast.
[3272.12 --> 3273.06]  They keep it simple.
[3273.42 --> 3275.82]  Check them out at Leno.com slash changelog.
[3275.82 --> 3287.52]  Welcome back, JS Party people.
[3287.52 --> 3290.86]  Let's talk about people and things that are awesome in the community.
[3291.26 --> 3292.96]  Chris, why don't you give us your shout outs first?
[3292.96 --> 3308.00]  Hey, so there is there was a experimental feature added to node recently proposed by I want to hope in saying Jan Krems and Guy Bedford actually landed the PR.
[3308.00 --> 3310.98]  But it's a package exports proposal.
[3310.98 --> 3316.44]  And what this thing is, is it's a new field in package.json.
[3316.76 --> 3329.22]  And it lets libraries specifically essentially create aliases of like.
[3329.22 --> 3333.12]  So the best way is probably just to use an example.
[3333.32 --> 3340.22]  So if you've ever used something with a very large API surface like Lodash comes to mind, RxJS.
[3340.30 --> 3346.42]  Sometimes they don't want to just export the whole API from the root module.
[3346.42 --> 3350.66]  So you don't say, you know, give me FUBAR and Baz from RxJS.
[3351.10 --> 3354.84]  If you want the operators, you reach into RxJS forward slash operators.
[3355.22 --> 3357.96]  And so the same with Lodash.
[3358.16 --> 3364.04]  If you want like Lodash FP is like a sub path of Lodash.
[3364.24 --> 3373.86]  But so essentially when you're doing that, when you use the sub path, it's exposing implementation details.
[3373.86 --> 3380.64]  Because in order for that to work, so in order for Lodash forward slash FP to work, one of two things has to be true.
[3381.02 --> 3386.78]  One, there needs to be an FP.js in the root of the Lodash module.
[3386.92 --> 3388.24]  And it must be published as such.
[3389.54 --> 3392.98]  The other thing is there may be a FP directory.
[3392.98 --> 3395.64]  And in that directory is an index.js.
[3395.90 --> 3397.10]  And it has to be published that way.
[3397.58 --> 3402.80]  So what package exports does is it allows a module author to declare,
[3402.80 --> 3407.60]  okay, these are these, I think they call them sub paths.
[3407.76 --> 3409.68]  So these sub paths point to these files.
[3410.34 --> 3418.60]  So you could say something like, okay, if somebody requires my module forward slash foo,
[3419.18 --> 3426.96]  that requirement will map to this other path somewhere in my source files.
[3426.96 --> 3432.92]  And so you don't have to expose the directory structure, which is an implementation detail,
[3432.92 --> 3445.30]  in order to provide those sub paths and allow, you know, your consumers to reach in to some other place in your module and pull things out.
[3445.86 --> 3448.88]  And right now it's experimental, but it's a really great idea.
[3448.88 --> 3455.84]  And, you know, people will kind of rail against aliases.
[3456.34 --> 3463.14]  I've seen this before where they don't like the idea of, well, it makes code hard to find, essentially.
[3463.84 --> 3467.92]  And so, you know, this is for libraries.
[3467.92 --> 3474.64]  So, you know, if you need to reach into a third-party library and it's got this export path in there,
[3474.70 --> 3480.90]  I can see where it might be difficult to actually find the source.
[3481.28 --> 3484.70]  But I'm sure tools will adapt to this.
[3485.30 --> 3486.48]  Right now it's experimental.
[3486.80 --> 3488.54]  You could probably just go ahead and play with it.
[3488.54 --> 3495.76]  But you can't, I mean, yeah, because it's experimental, it's behind a flag.
[3496.06 --> 3503.18]  And you can't really start publishing your things and expect it to work because it's not going to work for everybody yet.
[3503.40 --> 3505.56]  But anyway, a really great idea.
[3505.68 --> 3510.54]  Thank you, Jan and Guy, for the package exports proposal.
[3511.36 --> 3511.82]  Sweet.
[3512.34 --> 3512.96]  Thanks, Chris.
[3514.44 --> 3515.60]  Divya, you want to go next?
[3516.06 --> 3516.34]  Sure.
[3516.34 --> 3520.08]  I think NEJS just happened last week.
[3520.30 --> 3525.60]  And I was listening to the Twitter threads that were happening and people talking about it.
[3525.66 --> 3526.72]  And it seemed really cool.
[3527.14 --> 3530.18]  I'm really excited for the talks that they'd curated.
[3530.38 --> 3531.74]  So this was their last year.
[3532.22 --> 3535.30]  I think it's five years that they've done NEJS now.
[3536.14 --> 3539.22]  And there was a talk particularly, I had no idea.
[3539.38 --> 3543.88]  So last week we talked a little bit about package management and that came up.
[3543.88 --> 3547.58]  And Pika package was one of the things that we discussed.
[3548.00 --> 3553.56]  And the author, Fred Schott, actually spoke at NEJS, which I had no idea that he did.
[3553.76 --> 3556.88]  I only noticed when it was tweeted out that he did.
[3557.42 --> 3559.44]  But I'm really curious to see that talk.
[3559.44 --> 3566.40]  Because I think it accompanies a post that he created maybe last week.
[3566.44 --> 3567.26]  It was very recent.
[3567.40 --> 3568.96]  It was beginning of August sometime.
[3570.24 --> 3572.68]  And so, yeah, I think that's really cool.
[3573.62 --> 3575.18]  NEJS is a wonderful conference.
[3575.30 --> 3577.42]  I'm really sad to see the end of it.
[3577.42 --> 3582.38]  But at the same time, they've done a wonderful, wonderful job with it.
[3582.50 --> 3587.10]  In terms of, I think it's a really great example of a community-driven event.
[3588.84 --> 3591.72]  And, yeah, it's really well received.
[3592.34 --> 3594.28]  I think I've spoken at it before.
[3594.82 --> 3597.68]  My co-worker, Phil Hawkswood, spoke at it this year.
[3597.86 --> 3599.66]  And he had a wonderful experience.
[3599.80 --> 3601.56]  So I've always heard good things about it.
[3601.60 --> 3602.68]  And I've experienced it.
[3602.76 --> 3604.52]  And I can say that it's a great conference.
[3604.52 --> 3608.34]  Unfortunately, you can no longer experience it.
[3609.12 --> 3613.30]  But I look forward to future conferences that are very similar like that.
[3613.64 --> 3616.24]  Yeah, I hope next time Nick is on, we get a little bit of a debrief.
[3616.38 --> 3617.48]  I guess Jared was there, too.
[3617.64 --> 3618.46]  They're both organizers.
[3618.70 --> 3622.70]  So next time we have Nick and Jared on the show, they can get a debrief on NEJS.
[3622.96 --> 3623.36]  Oh, yeah.
[3623.42 --> 3625.30]  I think it'll be good to do a community episode.
[3625.50 --> 3631.36]  Just like how to rally and just like a retro and community and conference things.
[3631.82 --> 3632.58]  That would be really cool.
[3633.14 --> 3633.46]  Awesome.
[3633.46 --> 3634.00]  All right.
[3634.00 --> 3635.14]  Final set of shout outs.
[3635.30 --> 3639.68]  I want to do a couple shout outs to people in the community who are doing a ton of work
[3639.68 --> 3649.02]  to make the tech industry more welcoming and accessible to people and in particularly to
[3649.02 --> 3649.60]  women.
[3649.88 --> 3655.00]  I think we have a long history of having an industry that is very dominated by men.
[3655.66 --> 3657.32]  There's been a big push recently.
[3657.44 --> 3661.66]  I know I can tell when I go to a conference if they've paid attention or not because there
[3661.66 --> 3666.76]  are more and more conferences that really make a big deal out of gender equality and
[3666.76 --> 3673.34]  having not just men and women, but all genders feel welcome dealing with things like having
[3673.34 --> 3676.50]  simple things like what are your preferred pronouns on your tag, things like that.
[3677.30 --> 3678.50]  All sorts of stuff around that.
[3678.58 --> 3684.06]  But there's people really putting a lot of time and energy and investment into making this
[3684.06 --> 3687.14]  industry more welcoming to people who are not just white men.
[3687.14 --> 3688.66]  And I want to shout out a couple.
[3688.76 --> 3694.42]  So first one I want to shout out is the new Ladybug podcast that actually one of our panelists,
[3694.54 --> 3701.70]  Emma Wittekind, is doing along with Kelly Vaughn, Ali Spittel, and Lindsay Kopach.
[3701.70 --> 3703.74]  I probably butchered all of your names.
[3703.84 --> 3704.32]  I apologize.
[3704.96 --> 3707.52]  Though I hope I got Emma's right because I asked her how to pronounce it once.
[3709.50 --> 3711.48]  So that's one thing.
[3711.66 --> 3712.18]  Check it out.
[3712.30 --> 3713.18]  The Ladybug podcast.
[3713.30 --> 3717.08]  They're talking about all sorts of stuff in the tech industry.
[3717.28 --> 3723.08]  They're talking about things that are not just stuff that women run into, but it is also
[3723.08 --> 3728.16]  doing some things about particular challenges that I think women sometimes get hit by a little
[3728.16 --> 3728.60]  bit more.
[3728.60 --> 3732.70]  But more than that, they're just talking about the tech industry from a women's perspective,
[3732.70 --> 3738.10]  which is something that we need a lot of because as much progress as we've made, there's a lot
[3738.10 --> 3739.74]  of white dudes like me out here.
[3740.72 --> 3747.68]  The other person I want to call out who's doing some great work in that space is, I think of
[3747.68 --> 3748.96]  her as Lady Lee, Tracy Lee.
[3750.86 --> 3755.48]  She's the CEO of This.Labs, but she's done some really interesting things in terms of curating
[3755.48 --> 3758.32]  women in tech to help improve their visibility.
[3758.64 --> 3765.52]  So if you are like me and love the Twitters and you want to find some amazing women in
[3765.52 --> 3769.58]  tech who are doing awesome things, go check out Lady Lee's Fempire list.
[3770.62 --> 3772.30]  And there's just a lot of really, really cool people.
[3773.22 --> 3778.32]  I'm focusing on women in tech right now, but broadly, I want to advocate for expanding the
[3778.32 --> 3781.78]  sets of people that you follow to people who have different perspectives and different
[3781.78 --> 3782.24]  backgrounds.
[3782.88 --> 3787.00]  You know, if you are a white woman, find some black men to follow.
[3787.16 --> 3791.86]  If you're a white dude like me, find some women, find some folks who are of different
[3791.86 --> 3796.54]  backgrounds, Latin American, African American, and folks from outside the country.
[3796.86 --> 3800.98]  When I was traveling recently, I discovered I was overseas.
[3801.70 --> 3805.68]  I was offset from all of the time zone wise.
[3805.78 --> 3810.80]  I was off by like nine hours and I discovered, holy smokes, my feed is extremely US centric.
[3810.80 --> 3816.92]  I don't have those perspectives of people who are even similar to me, but in different
[3816.92 --> 3821.54]  countries, you know, in Europe and people who are, who have very different backgrounds.
[3821.66 --> 3826.82]  So I highly recommend looking for seeking out people with perspectives different from yours
[3826.82 --> 3828.84]  to, to follow.
[3829.38 --> 3832.14]  So yeah, those are my quick shout outs.
[3832.44 --> 3837.18]  And with that, I think we are done with this episode.
[3837.18 --> 3841.94]  We have covered, thank you for joining us for our experiment with the framework wars for
[3841.94 --> 3842.74]  our pro tips.
[3843.08 --> 3847.98]  And now closing with shout outs, do send us some feedback on what you thought of the framework
[3847.98 --> 3850.18]  wars segment, and we'll catch you next week.
[3850.18 --> 3852.54]  All right.
[3852.54 --> 3854.44]  Thank you for tuning in to JS party this week.
[3854.44 --> 3857.48]  Tune in live on Thursdays at 1 PM.
[3857.56 --> 3860.60]  U S Eastern at change law.com slash live.
[3861.08 --> 3863.62]  Join the community and slack with us in real time during the shows.
[3863.70 --> 3868.02]  Head to change law.com slash community and do us a favor, share this show with a friend
[3868.02 --> 3871.30]  where you don't have a podcast going to overcast and favorite it.
[3871.30 --> 3875.90]  And thank you to fastly our bandwidth partner and the fastly.com to learn more.
[3876.26 --> 3878.92]  And we move fast to fix things around here at change law because of roll bar.
[3879.08 --> 3880.82]  Check them out at rollbar.com.
[3880.92 --> 3885.10]  We're hosted on Leno cloud servers at the leno.com slash change law.
[3885.18 --> 3886.58]  Check them out and support this show.
[3886.70 --> 3891.30]  Our music is produced by break master cylinder, and you can find more shows just like this
[3891.30 --> 3892.46]  at change law.com.
[3892.58 --> 3893.58]  Thanks for tuning in.
[3893.86 --> 3894.60]  We'll see you next week.
[3901.30 --> 3902.30]  Bye.
