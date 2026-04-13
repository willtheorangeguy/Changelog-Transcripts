[0.00 --> 12.40]  This is JS Party, your weekly celebration of JavaScript and the web.
[12.40 --> 15.18]  If you like this show, you will love the changelog.
[15.46 --> 20.80]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome talk show.
[21.00 --> 23.48]  That's a lot like JS Party, now that I'm thinking about it.
[23.76 --> 27.24]  Find us by searching for the changelog wherever you listen to podcasts.
[27.56 --> 29.44]  Big thanks to our partners at Fly.io.
[29.86 --> 32.80]  Launch your app in five minutes or less all around the world.
[33.10 --> 34.92]  Learn how at Fly.io.
[35.16 --> 37.24]  Okay, hey, it is party time, y'all.
[39.46 --> 40.34]  What's up, friends?
[40.50 --> 43.52]  I'm here with Kurt Mackey, co-founder and CEO of Fly.
[43.68 --> 44.86]  As you know, we love Fly.
[45.12 --> 47.68]  That is the home of changelog.com.
[48.04 --> 50.34]  But Kurt, I want to know how you explain Fly to developers.
[50.64 --> 52.06]  Do you tell them a story first?
[52.34 --> 52.84]  How do you do it?
[52.84 --> 58.52]  I kind of change how I explain it based on almost like the generation of developer I'm talking to.
[58.70 --> 65.56]  So like for me, I built and shipped apps on Heroku, which if you've never used Heroku, is roughly like building and shipping an app on Vercel today.
[65.74 --> 68.38]  It's just it's 2024 instead of 2008 or whatever.
[68.58 --> 71.54]  And what frustrated me about doing that was I didn't, I got stuck.
[71.54 --> 75.32]  You can build and ship a Rails app with a Postgres on Heroku.
[75.46 --> 78.44]  The same way you can build and ship an XJS app on Vercel.
[78.78 --> 88.10]  But as soon as you want to do something interesting, like as soon as you want to, at the time, I think one of the things I ran into is like I wanted to add what used to be like kind of the basis for Elasticsearch.
[88.18 --> 89.94]  I want to do full text search in my applications.
[90.48 --> 94.66]  You kind of hit this wall with something like Heroku where you can't really do that.
[94.66 --> 103.30]  I think lately we've seen it with like people wanting to add LLMs kind of inference stuff to their applications on Vercel or Heroku or Cloudflare or whoever these days.
[103.66 --> 107.14]  They've started like releasing abstractions that sort of let you do this.
[107.26 --> 112.98]  But I can't just run the model I'd run locally on these black box platforms that are very specialized.
[113.32 --> 116.78]  For the people my age, it's always like Heroku was great, but I outgrew it.
[116.98 --> 123.66]  And one of the things that I felt like I should be able to do when I was using Heroku was like run my app close to people in Tokyo for users that were in Tokyo.
[123.66 --> 124.86]  And that was never possible.
[125.26 --> 129.28]  For modern generation devs, it's a lot more Vercel based.
[129.46 --> 133.32]  It's a lot like Vercel is great right up until you hit one of their hard line boundaries.
[133.86 --> 134.62]  And then you're kind of stuck.
[134.72 --> 135.34]  There's the other one.
[135.46 --> 136.84]  We've had someone within the company.
[137.22 --> 141.68]  I can't remember the name of this game, but the tagline was like five minutes to start forever to master.
[142.02 --> 149.42]  It's sort of how we're pitching fly is like you can get an app going in five minutes, but there's so much depth to the platform that you're never going to run out of things you can do with it.
[149.42 --> 169.30]  So unlike AWS or Heroku or Vercel, which are all great platforms, the cool thing we love here at ChangeLog most about Fly is that no matter what we want to do on the platform, we have primitives, we have abilities, and we as developers can charge our own mission on Fly.
[169.30 --> 173.80]  It is a no limits platform built for developers, and we think you should try it out.
[173.90 --> 176.48]  Go to fly.io to learn more.
[176.96 --> 178.36]  Launch your app in five minutes.
[178.68 --> 179.36]  Too easy.
[179.80 --> 181.84]  Once again, fly.io.
[181.84 --> 205.58]  All right.
[205.66 --> 207.90]  We are here live at React Summit.
[208.04 --> 209.50]  I'm K-Ball from JSParty.
[209.50 --> 211.44]  I'm joined by my co-host here.
[211.74 --> 212.16]  I'm Nick.
[212.32 --> 212.80]  Oh, hoi, hoi.
[213.24 --> 213.70]  Hoi, hoi.
[213.76 --> 217.10]  And we have a special guest here today with us.
[217.16 --> 218.38]  Tom, why don't you introduce yourself?
[218.64 --> 219.08]  Hey, everyone.
[219.28 --> 220.00]  I'm Tom O'Kino.
[220.44 --> 227.56]  I was a part of the founding team of React at Facebook Now Meta, and these days I'm the chief product officer at Vercel.
[228.32 --> 232.26]  Given that we are at React Summit, I'm sure we have to go into the story.
[232.38 --> 237.48]  So tell us a little bit behind the scenes, you know, what was it like getting React started?
[237.48 --> 237.96]  Yeah.
[238.58 --> 239.82]  Well, how long do you want?
[240.24 --> 241.42]  What version do you want?
[241.46 --> 242.48]  How long do you want me to speak for?
[242.54 --> 244.76]  I could go for five minutes or five hours.
[245.34 --> 247.64]  I mean, you've told this story again and again.
[247.70 --> 249.22]  We got to start with it, but let's keep it tight.
[249.30 --> 253.80]  And then we'll try to get into, like, what are some of the behind the scenes stuff that maybe hasn't come out before.
[254.02 --> 254.82]  Yeah, sounds good.
[254.82 --> 260.46]  And so in the early days, I think we were exploring a number of different ways to build web applications.
[260.80 --> 267.72]  And on the sort of ad side of our business, we had some more sophisticated applications than, you know, on the consumer side.
[268.38 --> 273.44]  And, you know, the way that we were kind of building those at the time was the same way that everybody was building web apps.
[273.44 --> 275.24]  It was sort of a client-side MVC.
[275.24 --> 281.08]  It was not, you know, dissimilar to something like Backbone or Ember or Angular at the time.
[281.60 --> 285.44]  And, you know, an engineer came along and he's like, look, this code is very hard to maintain.
[285.68 --> 287.78]  As our team grows, we're moving very slowly.
[288.04 --> 291.32]  Nobody wants to touch that thousand-line model over there.
[291.46 --> 293.38]  Like, you know, only two people can touch that.
[293.84 --> 295.54]  And so he thought there was a better way.
[296.08 --> 300.92]  He was inspired by a bunch of things that we had already been doing in other parts of the business.
[300.92 --> 306.12]  But from that, a prototype of an early version of what would eventually become React was born.
[306.62 --> 315.28]  At the time, I think we didn't have the right home in the company inside of the ads business to sort of, like, you know, incubate that type of new technology.
[315.84 --> 326.64]  So Jordan came over and talked to some of us on the product infrastructure team where we built frameworks and technologies that enabled other developers to be more efficient and build higher quality stuff.
[327.14 --> 328.22]  We gave it five minutes.
[328.52 --> 330.12]  We tried to build some things with it.
[330.12 --> 332.86]  We knew there was something important there.
[333.38 --> 335.34]  And that's when we kind of started to double down.
[335.68 --> 340.22]  And, you know, the rest you can hear about in the documentary or in one of the other interviews.
[340.22 --> 349.84]  But, yeah, it was very much a, you know, grew out of this organic sort of need, this emergent need for a simpler way of thinking about and developing our apps.
[350.56 --> 356.38]  So I'm curious, in ads before that, were you using something that's familiar?
[356.54 --> 358.22]  Was it more like an in-house solution?
[358.22 --> 361.64]  I'm just curious, like, what drove the need to React?
[362.06 --> 365.22]  Yeah, it was something in-house, but it was not unfamiliar.
[366.22 --> 372.20]  I mean, one of the people that co-created our in-house framework, which was called Bolt, was a core contributor to Backbone.
[372.20 --> 377.18]  We also had, you know, folks from the sort of like Dojo Mobile team.
[377.38 --> 382.06]  Like, we were very much like in the soup of the JavaScript ecosystem at the time.
[382.62 --> 389.70]  And so, yeah, I would compare our sort of in-house framework to sort of like Backbone with a different way of doing the sort of view layer.
[389.70 --> 391.44]  And it was good, very good.
[391.66 --> 393.58]  And we used it for a very long time.
[393.66 --> 403.36]  And it wasn't until our team started to get bigger and our app started to get sort of pathologically complex that we started to need a simpler model, no pun intended.
[403.86 --> 407.88]  We had these massive controllers and these massive models that, like, nobody really wanted to touch.
[407.92 --> 408.66]  So many inputs.
[408.66 --> 411.94]  And, you know, we couldn't make changes with confidence.
[412.44 --> 412.58]  Right.
[412.76 --> 419.06]  And so, you know, that's when you're kind of looking at it and you're like, okay, I think there's maybe a simpler way to do this.
[419.50 --> 419.96]  So, yeah.
[420.82 --> 428.52]  Well, and one of the things that React introduced that was so different, and that I remember, you were at that JSConf when it was announced, right?
[428.52 --> 432.48]  And you announced and you talk about, all right, we're going to put JSX in here.
[432.58 --> 434.76]  We're going to have everything in one component.
[434.88 --> 436.06]  We're not going to separate concerns.
[436.54 --> 437.94]  And it was panned.
[438.10 --> 438.34]  Yeah.
[438.34 --> 440.34]  Like, I remember, I was not at the conference.
[440.46 --> 445.04]  You were, but I just remember the ripple effects coming out and people were like, what the heck is this?
[445.56 --> 445.84]  Yeah.
[445.90 --> 450.52]  When Jordan and I introduced it at that conference, I remember it vividly.
[450.96 --> 460.70]  You know, one of the things we wanted to focus on was the sort of syntax and how this thing that was very familiar to us, we thought would be also familiar to the rest of the world.
[460.70 --> 467.34]  It's like, look, your HTML, the way that you want to think about your components, you don't have to use these nested JSON structures and all this stuff.
[467.34 --> 468.24]  Look, it just looks like it just looks like it's just wrong.
[468.72 --> 474.16]  But the sort of conversation ended up becoming about this mixing of technologies.
[474.60 --> 478.96]  And at the time, it was like, no, no, no, the whole industry is moving towards a separation of concerns.
[479.26 --> 479.52]  Yes.
[479.52 --> 480.82]  And you guys are mashing them together.
[480.88 --> 481.88]  And we're like, wait, wait, wait.
[481.96 --> 482.92]  This is one concern.
[483.12 --> 484.10]  It's my component.
[484.28 --> 485.44]  It's my UI.
[485.44 --> 492.86]  And so I think what we, the biggest thing we did wrong there was we didn't actually start with the problems that we were trying to solve.
[492.94 --> 494.36]  We just started with our solution.
[494.80 --> 494.92]  Yeah.
[494.92 --> 502.16]  So luckily Pete Hunt, I think later this same year at JSConf EU, did a much better job of like teeing up the problem.
[502.84 --> 504.26]  Here's what we were experiencing.
[504.52 --> 510.10]  As our applications got more complicated, as our models got super big, people didn't want to make changes to them.
[510.50 --> 517.64]  We wanted loose coupling between components so that those components could be used in lots of places, but high cohesion between them.
[517.68 --> 518.38]  So how do you do that?
[518.38 --> 523.02]  And it's with the seam between components, which is the props boundary and all these other things.
[523.38 --> 525.56]  So he did a much better job of teeing up the problem.
[525.72 --> 528.54]  And then I think it was more well accepted.
[528.66 --> 531.24]  People were willing to kind of give it five minutes after that point.
[531.62 --> 534.30]  But I'm glad that there wasn't like a stampeding herd of adoption.
[534.50 --> 535.10]  This is amazing.
[535.28 --> 539.36]  At no point in React's history have we ever said, you know, behold, this is the answer.
[539.46 --> 540.36]  We've finally done it.
[540.68 --> 543.72]  It's always been about, you know, sort of like here's the problems we were facing.
[543.96 --> 546.12]  Here's one solution that worked pretty well for us.
[546.12 --> 548.36]  If you have the same problems, let's chat.
[548.50 --> 550.34]  If not, you know, no worries.
[550.46 --> 552.00]  There's lots of good solutions out there.
[552.46 --> 561.00]  But I'm glad that, you know, Pete came through and, you know, restored faith in the sort of engineering team that Jordan and I were attempting to represent.
[561.48 --> 563.94]  Because the team was great and the tech was novel.
[564.16 --> 565.40]  Something interesting and important.
[566.12 --> 571.94]  Yeah, I think it really, like being there, I had a tweet in the React documentary that was negative towards it.
[571.94 --> 578.02]  And it was because, like, that separation of concerns, you know, everything was pushed towards that.
[578.14 --> 587.00]  And then, like, also just creating this new JSX syntax that, like, wasn't real JavaScript at the time felt a little weird and strange.
[587.00 --> 592.62]  But I think that the key piece, like, looking back that was missing was that component mindset.
[592.96 --> 594.72]  Like, we just weren't thinking in terms of components.
[595.16 --> 597.78]  We're thinking, like, for me, I was in Backbone in those days.
[597.98 --> 605.82]  And it was really more thinking about in terms of, you know, the model that is, the view that I'm specifically showing, which at the time was usually like a page.
[605.98 --> 606.72]  Yeah, that's right.
[606.82 --> 610.14]  The views, you know, in our applications ended up being massive.
[610.14 --> 613.80]  And then the models that needed to power those views were massive.
[613.96 --> 614.90]  And you can break them up.
[614.98 --> 618.00]  You can say, like, okay, now I have multiple models that feed up into this thing.
[618.08 --> 619.64]  And now I have multiple views.
[619.88 --> 630.86]  But everybody was thinking about things from a sort of, like, I don't know, top down rather than a sort of the component as the atom inside out sort of mentality.
[631.10 --> 634.66]  And that was the big shift was we're going to define a seam.
[634.82 --> 636.46]  And I can do anything I want inside of this seam.
[636.46 --> 639.18]  But the contract with the rest of the application is intact.
[639.18 --> 642.00]  And, you know, we could have done a better job of telling that story.
[642.12 --> 643.26]  But it worked out okay in the end.
[643.58 --> 648.80]  Well, and that approach to decomposing user interfaces has taken over the world, right?
[648.92 --> 652.40]  Like, everything is now using component-oriented development.
[652.64 --> 654.38]  Whether it's using JSX or something else.
[654.58 --> 659.82]  Whether, I mean, even if you're still doing separation of concerns in the traditional way, you're still thinking about it as components.
[660.00 --> 660.30]  That's right.
[660.30 --> 668.36]  Yeah, the day that Swift UI was announced, I remember writing Jordan and saying, you know, congratulations, man.
[668.50 --> 669.48]  You know, we did it.
[669.70 --> 669.92]  Yeah.
[669.92 --> 683.24]  The thing that we were so against was this idea that engineers should spend their time manually manipulating views, updating things based on new information coming in.
[683.74 --> 686.32]  And we just wanted the framework to be able to take care of that for you.
[686.32 --> 690.50]  And now, across every platform, every UI behaves that way.
[690.66 --> 695.58]  We have a declarative way of describing what our components and our UI should look like at any point in time.
[695.78 --> 698.02]  And you trust the framework to keep it up to date.
[698.48 --> 704.44]  We never will find that button and turn the text red or set its state to disabled manually ever again.
[704.44 --> 705.72]  And I think that's progress.
[707.00 --> 714.52]  When React was first coming out and, like, that first version, it really was just focused on kind of the view layer and, like, displaying things.
[714.58 --> 716.54]  You know, here's the props and here's how they're going to be displayed.
[716.96 --> 718.90]  And then here's the interactions between them.
[719.32 --> 726.22]  Was that a conscious decision to keep it very limited to that and not to spread out into more, like, state business logic?
[726.52 --> 730.66]  Yeah, I think it was sort of an implementation detail leaking out.
[730.66 --> 737.44]  I think, you know, we wanted to do one thing really well, but more importantly, we just had all this other stuff that this was sitting on top of.
[737.58 --> 739.50]  We had a way of doing data fetching at Facebook.
[739.70 --> 742.76]  We had a way of doing, you know, basically everything.
[742.90 --> 744.96]  Our router was, like, a server-based router.
[745.18 --> 749.36]  Like, we really didn't need to solve all of the concerns.
[749.98 --> 754.54]  But over time, what happened is the community ended up filling in all the gaps.
[755.00 --> 757.40]  We needed a router, and then React Router came around.
[757.66 --> 759.70]  You know, React needed server-side rendering.
[759.70 --> 765.12]  And then I think, like, Pinterest was maybe the first company to build a server-side renderer that would work.
[765.48 --> 770.10]  Because Facebook didn't run JavaScript on the server at the time, and so we weren't investing in server-side rendering.
[770.34 --> 773.72]  But the architecture was very much designed with server-side rendering in mind.
[774.26 --> 780.22]  So you needed all of these things, you know, state management libraries and different types of integrations.
[780.70 --> 782.84]  And the community really filled in the gaps.
[782.84 --> 791.58]  And then I think the goal for the core team over time was to make it so that all of these things that were built on top of React could get thinner and thinner.
[792.16 --> 799.62]  They didn't have to be so sophisticated because the framework would take care of more of the, like, atomic, low-level complexities for you.
[799.62 --> 806.72]  So that your framework that sits on top of this library that's growing in size could be thinner and thinner, but just as expressive.
[806.72 --> 815.00]  So, yeah, I mean, there was no sort of intentional, oh, let's not worry about any of that because the community will fill it in.
[815.04 --> 821.50]  It was like, well, that's not what we need to solve, so we'll kind of, like, create an opportunity for the world to fill in the gaps.
[821.94 --> 825.42]  And that's when I think, you know, React, we introduced it very clearly as a library.
[825.64 --> 826.90]  Is this a library or a framework?
[827.00 --> 827.58]  It's not a framework.
[827.70 --> 828.72]  It doesn't do everything for you.
[829.22 --> 832.04]  Ember was batteries included, and that was beautiful.
[832.20 --> 833.32]  Angular was the same way.
[833.72 --> 834.72]  Here's how you do testing.
[834.90 --> 835.92]  Here's how you do data fetching.
[835.96 --> 836.66]  Here's how you do routing.
[837.02 --> 838.90]  We were just like, nah, this is just your views.
[839.44 --> 844.18]  And a lot of the early adoption of React actually used it in conjunction with, like, backbone models.
[844.52 --> 854.50]  So there was even a strong relationship between, I mean, Instagram did this in the early days where we had backbone feeding into React views, and it was just an easier way to do your view layer.
[855.34 --> 863.08]  And I think that that probably really helped with the adoption of it, too, just because it was a simple way to do it, and it wasn't prescribing this is the one way to do it.
[863.08 --> 869.86]  And people got to really experiment, and then these new experiments just flooded the market with all sorts of different ways to do it.
[869.90 --> 870.90]  That's exactly right.
[870.96 --> 874.02]  I think there's sort of two reasons that React really took off.
[874.40 --> 877.14]  One was you could adopt it extremely incrementally.
[877.36 --> 881.68]  One part of your page, not even one page in your app, one piece of your page.
[881.68 --> 884.66]  And the other thing was the other direction.
[884.90 --> 887.94]  So it included these escape hatches from the early days.
[888.10 --> 894.56]  And I remember we had one of these things where we had this very sophisticated autocomplete widget that no one wanted to reimplement.
[894.92 --> 896.58]  It was just really complicated.
[897.40 --> 909.74]  And so there was this function in React that said find DOM node, and it would get you the DOM node that you needed, and then you could decorate it with whatever existing sort of jQuery-like application code you had or behavior you had.
[909.74 --> 911.48]  And then you could mix and match.
[911.88 --> 921.14]  And so because we created sort of escape hatches and incremental adoption for our own needs, by the way, this wasn't a strategy like this is how we'll get.
[921.38 --> 923.76]  No one ever cared about React adoption at Facebook.
[923.90 --> 927.88]  No one ever took a goal on a number of external React users.
[927.88 --> 936.88]  But we needed to build these things for ourselves, and it turned out those are the things that made it possible for other companies to try it and then eventually expand their usage.
[937.98 --> 939.98]  So you were at Facebook.
[941.06 --> 943.02]  React at Facebook is for their own needs.
[943.12 --> 943.88]  Now you've moved on.
[944.02 --> 952.10]  You're at Vercel, which is also supporting a lot of these open source, front-end movements, but perhaps a little bit more self-interestedly in some ways.
[952.10 --> 953.62]  There is a business there, yeah.
[953.74 --> 956.24]  It's very interesting, the contrast.
[956.52 --> 965.32]  One of the things I've loved about being at Vercel versus Facebook was Facebook had a business that was over there that was funding everything that we needed to do,
[965.44 --> 970.52]  and it was enough for us to make our own engineers more efficient, to level up the quality of our applications.
[970.52 --> 976.56]  But we didn't really have to concern ourselves with how other companies are adopting our technologies.
[976.74 --> 979.60]  So that means that, you know, we collaborate.
[979.92 --> 981.20]  We build an open source community.
[981.42 --> 985.46]  We benefit from, you know, recruiting and thought leadership and all these things.
[985.90 --> 991.10]  But there was no sort of like, you know, on the balance sheet, here's the value that we derive.
[991.10 --> 1000.56]  And I think being able to invest in open source technologies from the angle of there's kind of a business that's funding the open source development,
[1000.94 --> 1007.80]  but I'm more directly connected to the customers has been a really, you know, enlightening and great experience.
[1008.26 --> 1017.86]  We now can talk about business outcomes for our customers and how the sort of frameworks and the technologies that we built led to those business outcomes.
[1017.86 --> 1022.84]  But one of the things that both companies kind of have in common is Facebook famously said,
[1023.32 --> 1027.02]  we don't make money to build, or we don't build services to make money.
[1027.36 --> 1029.58]  We make money so we can keep building better services.
[1030.30 --> 1033.68]  And Vercel is kind of the same way now with open source investment.
[1034.14 --> 1035.84]  We don't build Next.js to make money.
[1036.24 --> 1040.16]  We have a business that makes money so that we can keep funding Next.js development.
[1040.90 --> 1046.88]  And I like being more directly connected to the customers and seeing the ways that our framework improvements
[1046.88 --> 1052.44]  enable them to achieve better business outcomes, which is a much more direct link than I had at Facebook.
[1052.96 --> 1060.74]  So you said the need for React kind of came out of this like very complicated JavaScript application
[1060.74 --> 1065.68]  that those of us who are older remember all of these like the spaghetti was the way, right?
[1065.72 --> 1067.14]  And you're like trying to track the dependencies.
[1067.84 --> 1073.76]  And so React kind of reimagined that, broke that down, filled the gap there.
[1073.76 --> 1080.96]  Where do you see right now that same kind of, if anywhere, like places where people are getting stuck,
[1081.16 --> 1084.88]  where like there needs to be some sort of reimagining of the paradigm?
[1085.38 --> 1092.68]  Yeah, I think the biggest shift that we saw was in moving a lot of that application complexity into components,
[1093.06 --> 1096.38]  where those components primarily contain, or not primarily,
[1096.38 --> 1102.44]  but those components contain everything that they need in order to exist inside of a larger application and on their own.
[1102.80 --> 1107.02]  We just moved a lot of the complexity into those components, but on the client.
[1107.64 --> 1112.12]  And we moved so much of the application onto the client that I think we've had like a five-year run
[1112.12 --> 1116.60]  of like single-page apps that like show a loading spinner or a series of loading spinners.
[1116.60 --> 1120.78]  And then they fetch their own data from wherever it's coming from.
[1121.22 --> 1126.56]  And that led to a better developer experience, but admittedly, probably not the right user experience.
[1126.90 --> 1129.94]  And there's things that you can do in order to coalesce the data fetching
[1129.94 --> 1132.62]  and make sure that you don't have waterfalls in your app.
[1132.78 --> 1134.68]  But it's kind of manual. It's not the default.
[1135.50 --> 1138.86]  So I think the biggest shift we have is moving some of the work back to the server
[1138.86 --> 1140.88]  when it belongs on the server.
[1140.88 --> 1142.62]  You're doing data fetching code.
[1142.74 --> 1147.18]  You're doing anything that hits a database or touches secrets or anything.
[1147.68 --> 1150.92]  And you can leave that code where it belongs and then ship a thinner client.
[1151.56 --> 1155.44]  And the thing that I'm kind of most excited about is using both the server and the client
[1155.44 --> 1156.76]  for the things that they're best at.
[1157.12 --> 1161.18]  Client is best for interactivity and real-time, immediate, optimistic feedback.
[1161.56 --> 1165.36]  But the server is best for sort of orchestrating data fetching and coalescing things
[1165.36 --> 1169.98]  and sort of making it so that we have an efficient stream of updates coming to the page.
[1169.98 --> 1173.06]  And so I think when you have a static shell
[1173.06 --> 1176.06]  and then you stream in the dynamic bits of your app,
[1176.40 --> 1179.78]  but you keep everything interactive as the streams come in,
[1179.82 --> 1183.88]  I think that's kind of the north star for web application delivery.
[1184.44 --> 1186.62]  And that's the shift we're seeing with, like, React server components.
[1186.96 --> 1191.98]  So we're far closer to the beginning of the RSC journey than the end there.
[1192.36 --> 1194.26]  And that's the shift I'm most excited about.
[1194.26 --> 1198.34]  But then I think there's also this renaissance of sort of, like,
[1198.40 --> 1204.02]  wanting to support in a more native way other devices and other platforms
[1204.02 --> 1205.26]  that have been coming online.
[1205.50 --> 1207.04]  It's not just about mobile anymore.
[1207.22 --> 1211.42]  It's also about, you know, TVs and AR, VR, et cetera.
[1211.58 --> 1214.92]  So we're going to see a proliferation of new clients that you want to support.
[1215.38 --> 1219.20]  And my hope is that this blend of the benefits of the server
[1219.20 --> 1223.74]  and the benefits of the client won't be lost as we move to all these new platforms.
[1224.62 --> 1226.88]  It really seems like trying to get the best of both worlds
[1226.88 --> 1230.90]  in terms of developer experience and user experience.
[1231.16 --> 1231.44]  Yeah.
[1231.70 --> 1233.72]  One of the things I feel really strongly about is
[1233.72 --> 1236.98]  developer experience was never a goal on its own.
[1237.80 --> 1241.86]  Developer experience is always in service of creating a better user experience.
[1242.08 --> 1245.04]  The reason that we needed to improve the developer experience
[1245.04 --> 1247.82]  in sort of our, you know, sophisticated ads code base
[1247.82 --> 1250.84]  was because we needed engineers to be able to keep iterating on it
[1250.84 --> 1254.38]  and making improvements based on customer feedback and what we saw.
[1254.90 --> 1257.10]  So it wasn't like we were like, oh, we just want to clean this up
[1257.10 --> 1259.54]  so we can, you know, have a better time ourselves.
[1259.72 --> 1263.68]  It was, it's necessary in order to deliver the best user experience possible.
[1264.22 --> 1267.88]  So I think anybody who says that these things trade off against each other,
[1268.30 --> 1270.40]  I think they can, but they shouldn't.
[1270.40 --> 1275.58]  We need to make the defaults for anything that any framework outputs
[1275.58 --> 1279.92]  significantly higher quality and sort of raise the baseline for everything.
[1280.60 --> 1284.42]  One of our goals is, you know, sort of level up the entire web.
[1284.48 --> 1286.16]  We want to make the web better.
[1286.58 --> 1288.18]  I want to use software that feels great,
[1288.86 --> 1291.48]  not software that looks like it was cobbled together really quickly.
[1291.94 --> 1293.42]  Even if you can develop it quickly,
[1293.54 --> 1295.26]  that doesn't mean it has to feel like crap.
[1295.82 --> 1299.28]  So, yeah, developer experience in service of a great user experience.
[1299.28 --> 1302.02]  So you were around for the beginning of React
[1302.02 --> 1304.40]  and kind of bringing that into the limelight
[1304.40 --> 1308.40]  and getting all of the popularity that it has and shaping the industry.
[1308.90 --> 1312.06]  And now, years later, you're at Vercel doing Next.
[1312.32 --> 1315.62]  Do you see that as like a continuation of React
[1315.62 --> 1321.20]  or a way to shape React for like 2024 and beyond,
[1321.40 --> 1325.50]  like the modern, the way that you might have built React in today's world
[1325.50 --> 1326.96]  as opposed to 10 years ago?
[1326.96 --> 1330.56]  So in many ways, you know, I think that what we're doing at Vercel
[1330.56 --> 1335.52]  is sort of inevitable and React is an important piece of that,
[1335.64 --> 1338.52]  but not the sort of high order bit.
[1338.76 --> 1340.26]  So let me describe what I mean by that.
[1340.58 --> 1343.68]  Generally speaking, it's very hard to change developer behavior,
[1344.12 --> 1345.52]  but if you can do it,
[1345.84 --> 1349.12]  it affords you this ability to do some other interesting stuff.
[1349.12 --> 1354.52]  And one of the things that I really like about the sort of arc of Vercel
[1354.52 --> 1358.06]  is I believe that this is sort of like a human progress element here.
[1358.62 --> 1361.78]  There used to be, you know, and I'm talking about managed infrastructure,
[1362.00 --> 1363.62]  so just to like not bury the lead.
[1363.94 --> 1365.86]  We used to literally, when I joined Facebook,
[1365.86 --> 1369.88]  we had teams that drove to data centers and rack-mounted machines.
[1369.88 --> 1372.78]  And, you know, I knew that team.
[1373.02 --> 1375.88]  The infrastructure team would like drive and rack-mount machines
[1375.88 --> 1377.92]  and connect it to the internet and call ISPs.
[1378.92 --> 1381.20]  And then, you know, eventually AWS comes along.
[1381.98 --> 1384.76]  And, you know, you don't have to do that anymore.
[1384.90 --> 1385.80]  Somebody's already done that,
[1385.84 --> 1387.80]  and now we can provision compute on demand.
[1388.24 --> 1389.74]  You just log into the console.
[1390.00 --> 1391.30]  You say how many machines you need.
[1391.38 --> 1392.12]  You configure them.
[1392.66 --> 1394.34]  And then something like Vercel comes along,
[1394.40 --> 1396.56]  and no one has to do that anymore.
[1396.56 --> 1399.18]  So the arc is sort of like human progress happens
[1399.18 --> 1402.38]  when you take something that a small set of specialists can do,
[1402.46 --> 1403.70]  only a small set of specialists.
[1403.98 --> 1405.40]  You make it so anyone can do it,
[1405.76 --> 1407.24]  and then you make it so no one has to.
[1407.92 --> 1411.94]  And the reason I'm so interested in this arc for technology
[1411.94 --> 1414.54]  is because I've seen time and time again
[1414.54 --> 1418.54]  many, many companies do what I've described
[1418.54 --> 1421.44]  as undifferentiated heat loss engineering.
[1422.10 --> 1425.26]  You're doing the same thing over and over
[1425.26 --> 1427.36]  across lots of different companies
[1427.36 --> 1429.82]  where you're provisioning compute manually.
[1430.14 --> 1431.82]  You anticipate a spike
[1431.82 --> 1433.88]  because of some event that's happening,
[1434.06 --> 1435.72]  so you provision some more manually,
[1436.10 --> 1438.02]  or you build a script that sort of, like,
[1438.04 --> 1439.68]  tries to do this automatically for you,
[1440.14 --> 1442.34]  but then you didn't handle automatic failover.
[1442.48 --> 1444.02]  So, like, what if this data center goes down,
[1444.08 --> 1446.08]  now you have to have somebody log in and do this thing,
[1446.10 --> 1447.12]  and you didn't handle what happens
[1447.12 --> 1448.56]  when you, like, deploy your app,
[1449.02 --> 1451.12]  and then you, you know, somebody's using it actively,
[1451.12 --> 1452.38]  and then everything breaks.
[1452.38 --> 1454.84]  So you didn't handle deployment skew,
[1455.02 --> 1456.84]  and there's all this stuff,
[1457.00 --> 1458.72]  and most of the software in the world,
[1459.16 --> 1462.22]  because every company is doing the same thing,
[1462.48 --> 1464.28]  they're not thinking about it as holistically
[1464.28 --> 1468.36]  or as completely as Google or Facebook or now Vercel.
[1469.10 --> 1470.56]  And so what we're trying to do at Vercel
[1470.56 --> 1472.40]  is make it so that all of the concerns
[1472.40 --> 1475.72]  associated with provisioning compute,
[1476.24 --> 1478.24]  configuring your data center
[1478.24 --> 1479.64]  or your infrastructure primitives,
[1479.64 --> 1481.64]  all of that is handled for you automatically.
[1482.20 --> 1484.86]  And the reason I'm so interested in Next.js and React
[1484.86 --> 1486.78]  is because one of the only ways
[1486.78 --> 1490.34]  that we can define infrastructure for you
[1490.34 --> 1491.78]  automatically on demand
[1491.78 --> 1494.26]  is by having the framework define that infrastructure.
[1494.82 --> 1497.18]  So we can certainly do it with more than just Next.js,
[1497.64 --> 1500.26]  but we have to conform to some sort of a scene
[1500.26 --> 1501.76]  that describes to the system
[1501.76 --> 1503.62]  how to provision infrastructure on demand.
[1503.62 --> 1506.34]  And so that's where framework-defined infrastructure
[1506.34 --> 1509.52]  comes from and the build output API
[1509.52 --> 1511.06]  and a bunch of other primitives.
[1511.48 --> 1514.42]  So very much sort of innovating with Next.js
[1514.42 --> 1516.40]  and Vercel's managed infrastructure,
[1516.72 --> 1519.12]  but then generalizing after the fact.
[1519.20 --> 1520.56]  So again, this is another case
[1520.56 --> 1522.16]  where we want high cohesion
[1522.16 --> 1524.38]  between the infrastructure and the framework,
[1524.92 --> 1525.92]  very high cohesion,
[1526.10 --> 1527.50]  so we build them and develop them
[1527.50 --> 1528.52]  and innovate on them in tandem,
[1529.04 --> 1530.42]  but we want loose coupling,
[1530.80 --> 1533.42]  so we really clearly define the scene between the two.
[1533.42 --> 1534.56]  This is the build output API.
[1534.96 --> 1536.58]  If your framework that you invent today
[1536.58 --> 1537.92]  conforms to the build output API,
[1538.24 --> 1539.36]  Vercel's managed infrastructure
[1539.36 --> 1541.54]  can deploy it for you on demand and autoscale it.
[1542.12 --> 1544.04]  And the same thing goes for the infrastructure.
[1544.40 --> 1546.32]  The infrastructure is influenced by,
[1546.80 --> 1548.34]  but decoupled from,
[1548.56 --> 1550.36]  so that it can be used to deploy anything,
[1550.48 --> 1552.40]  including Python and PHP very soon.
[1552.90 --> 1555.96]  So yeah, we're kind of like building managed infrastructure
[1555.96 --> 1559.56]  that is influenced by the code that you write
[1559.56 --> 1563.28]  so that no one has to manually provision compute again.
[1563.42 --> 1565.48]  There's something really interesting there
[1565.48 --> 1568.98]  in terms of like creating constraints for your architecture
[1568.98 --> 1573.20]  that then enable you to automatically infer
[1573.20 --> 1574.90]  a set of different things.
[1575.24 --> 1576.20]  I'm curious,
[1576.46 --> 1577.50]  because I'm not super familiar
[1577.50 --> 1579.30]  with the build output API or anything.
[1579.54 --> 1581.52]  What are, at a high level,
[1581.64 --> 1583.18]  if I'm not using Next.js,
[1583.48 --> 1584.90]  maybe because it'll deal with it for me,
[1584.96 --> 1586.44]  what are the constraints I need to put
[1586.44 --> 1588.12]  on my software architecture
[1588.12 --> 1591.64]  that allow you to automatically scale and manage it?
[1591.90 --> 1594.20]  Yeah, at the most sort of rudimentary level
[1594.20 --> 1596.90]  is this idea that when a page loads
[1596.90 --> 1598.38]  or when an application is loaded,
[1598.96 --> 1602.20]  is this specific resource static or dynamic?
[1602.74 --> 1605.04]  Is this something that can be loaded from a CDN,
[1605.12 --> 1606.06]  loaded from a cache,
[1606.52 --> 1609.48]  replicated out to, you know, dozens of regions
[1609.48 --> 1612.16]  so that it can be just delivered directly to the browser,
[1612.16 --> 1614.54]  or is this something that requires some compute?
[1615.10 --> 1616.02]  So is this dynamic?
[1616.56 --> 1617.32]  And if it's dynamic,
[1617.46 --> 1619.96]  let's say it's a cart or a user profile
[1619.96 --> 1622.58]  or, you know, some information about the visitor,
[1623.12 --> 1624.20]  then you'll need to provision
[1624.20 --> 1626.16]  some type of compute on demand.
[1626.36 --> 1629.16]  And that could come from a sort of like base layer of compute
[1629.16 --> 1630.54]  or it could come from, you know,
[1630.60 --> 1632.20]  on-demand serverless functions.
[1632.84 --> 1636.20]  We're sort of redefining the way that you think about that
[1636.20 --> 1639.60]  to be a much more fluid boundary between the two.
[1640.06 --> 1641.40]  So you don't have to think about
[1641.40 --> 1644.46]  whether something is going to be on-demand serverless
[1644.46 --> 1645.76]  or come from base compute.
[1646.20 --> 1648.32]  You just think about whether it's dynamic or not.
[1648.70 --> 1650.04]  And then when you tell the framework,
[1650.24 --> 1651.38]  when you tell the managed infrastructure,
[1651.52 --> 1652.94]  hey, this is a dynamic piece,
[1653.40 --> 1655.62]  it will provision the necessary compute
[1655.62 --> 1657.60]  in a very efficient way.
[1658.22 --> 1661.16]  There's a very like high-level static versus dynamic,
[1661.28 --> 1662.44]  but there's more flavors.
[1662.44 --> 1664.38]  Like what's your caching strategy
[1664.38 --> 1666.24]  and how do you mix these things?
[1666.58 --> 1669.16]  Well, and how do you think about stateful resources, right?
[1669.46 --> 1671.64]  Especially if you go beyond the simple databases.
[1672.44 --> 1673.20]  Yeah, that's right.
[1673.36 --> 1675.82]  And what we want to enable is anybody
[1675.82 --> 1678.04]  to pull in any stateful resources,
[1678.68 --> 1681.74]  whether it's databases and any dynamic resources.
[1681.94 --> 1684.28]  So backends, I mean, AI apps are huge these days.
[1684.46 --> 1687.48]  We need efficient compute, efficient on-demand compute
[1687.48 --> 1691.32]  for talking to long-lived LLM outputs, right,
[1691.34 --> 1692.90]  that are streaming responses back.
[1692.98 --> 1695.66]  This is not the like go fetch rows
[1695.66 --> 1697.30]  from the database of yore, right,
[1697.32 --> 1698.54]  where you just like synchronously
[1698.54 --> 1700.30]  just fetch some rows from a database.
[1700.48 --> 1702.12]  Now we have like much more sophisticated,
[1702.84 --> 1705.12]  stateful and dynamic backends,
[1705.18 --> 1706.70]  and we need to be able to connect to all of them.
[1707.10 --> 1710.20]  So let's maybe dive in on that LLM side a little bit.
[1710.84 --> 1711.50]  I'm curious.
[1711.66 --> 1714.14]  So this is a space that is very hot.
[1714.56 --> 1717.10]  It's also a space where most of the apps out there are,
[1717.34 --> 1719.40]  I don't know if we're PG or not, but terrible.
[1719.78 --> 1720.72]  We'll use that word.
[1721.32 --> 1724.28]  I mean, just because we're still trying to understand
[1724.28 --> 1725.24]  what are the primitives?
[1725.24 --> 1727.26]  What are the pieces that actually make sense
[1727.26 --> 1728.62]  for an LLM-based application?
[1729.02 --> 1730.58]  I know y'all are diving into that
[1730.58 --> 1732.44]  with things like v0 and things like that.
[1732.56 --> 1736.88]  What is your perception of what the application layer needs?
[1736.96 --> 1738.80]  We've had tremendous development at the model layer,
[1738.90 --> 1741.92]  but what does the application layer need to be for LLM success?
[1742.56 --> 1744.16]  Yeah, a few thoughts here.
[1744.36 --> 1746.24]  First is that we're far closer
[1746.24 --> 1749.86]  to the sort of beginning of that journey as well than the end.
[1749.86 --> 1754.36]  And I think we're seeing right now LLMs level up developers.
[1755.00 --> 1757.94]  Every developer now is like a super developer
[1757.94 --> 1759.28]  because you can move much faster.
[1759.70 --> 1762.94]  But I think I'm more interested in the UX side of things.
[1763.48 --> 1767.06]  And so one kind of innovation here is this idea of LLMs
[1767.06 --> 1770.50]  not just outputting static content,
[1770.82 --> 1772.34]  so images and text,
[1772.34 --> 1776.60]  but also outputting dynamic applications.
[1776.60 --> 1776.94]  Generative UI.
[1777.42 --> 1777.94]  That's right.
[1778.16 --> 1780.60]  So GenUI, I think this idea that,
[1780.72 --> 1781.86]  you know, in the simplest form,
[1781.96 --> 1782.80]  this is a chatbot,
[1782.90 --> 1785.32]  but you can interact with some of the messages that come back.
[1785.48 --> 1786.34]  Great, we've seen that.
[1786.76 --> 1788.78]  But what happens when we apply GenUI
[1788.78 --> 1792.34]  into places where very complicated UI
[1793.04 --> 1796.20]  wasn't previously progressively disclosed?
[1796.66 --> 1798.36]  I think it will make our applications,
[1798.78 --> 1799.84]  if we do this right,
[1800.28 --> 1802.10]  much more approachable,
[1802.70 --> 1805.06]  but the sort of full sophistication of those applications
[1805.06 --> 1806.56]  can be disclosed progressively.
[1807.40 --> 1808.40]  And, you know,
[1808.50 --> 1810.14]  we used to have physical buttons
[1810.14 --> 1812.06]  for everything that you wanted to do on a radio.
[1812.66 --> 1814.50]  Then we got soft buttons
[1814.50 --> 1816.82]  that would be context-aware and give you an option.
[1817.28 --> 1819.10]  Then we got touchscreens that would say,
[1819.18 --> 1821.16]  okay, here's all the stuff you can just touch on the screen,
[1821.22 --> 1824.36]  and the screen had a hard-coded set of sort of UIs
[1824.36 --> 1825.40]  that you could sift through.
[1826.20 --> 1829.46]  And now I think we will be able to have on-demand UI,
[1829.66 --> 1831.86]  and it'll still conform to conventional patterns.
[1832.12 --> 1833.26]  A button needs to look like a button,
[1833.66 --> 1836.76]  but it'll be able to be custom-tailored for your experience,
[1837.02 --> 1840.44]  which I think will end up being much less,
[1842.00 --> 1843.86]  you know, software can be much less overwhelming.
[1844.10 --> 1845.58]  I remember the first time I opened Photoshop,
[1845.86 --> 1847.06]  or like Framer has this too,
[1847.18 --> 1849.36]  where like there's just all these panels and buttons
[1849.36 --> 1850.58]  and menus and all this stuff,
[1850.62 --> 1850.88]  and it's like,
[1851.10 --> 1853.24]  do I need to know about all of this up front?
[1853.24 --> 1857.46]  And so I think with GenUI and with, you know,
[1857.62 --> 1860.30]  the sort of like modern era of UX development,
[1860.46 --> 1862.54]  we will be able to progressively disclose that stuff,
[1862.90 --> 1864.60]  contextually when you need it,
[1864.92 --> 1866.28]  and not sort of up front.
[1866.94 --> 1868.08]  So I'm excited about that.
[1868.54 --> 1870.50]  I'm also excited about the idea that like,
[1870.88 --> 1874.14]  I don't know, LLMs are better at raising the baseline
[1874.14 --> 1876.56]  for everyone than I think most.
[1877.16 --> 1878.34]  And so what that means is like,
[1878.90 --> 1880.24]  hey, now that we finally have
[1880.24 --> 1881.92]  a really great feeling date picker,
[1882.50 --> 1883.46]  let's use that,
[1883.66 --> 1885.06]  or let's use, you know,
[1885.14 --> 1887.36]  let's let the like top date pickers compete
[1887.36 --> 1889.50]  so that I never get into that situation where like,
[1889.56 --> 1891.58]  oh God, like I can't select,
[1891.80 --> 1893.86]  you know, have to click 15 times in order to get to,
[1894.02 --> 1896.44]  so I think like we'll be able to more quickly,
[1896.76 --> 1897.58]  I hope,
[1898.04 --> 1900.48]  zero in on like optimal user experiences,
[1900.48 --> 1902.62]  especially on different modes, right?
[1902.68 --> 1904.64]  So if I'm on mobile versus desktop,
[1905.18 --> 1906.62]  I hope that we will be able to level up
[1906.62 --> 1908.22]  the user experience across the board.
[1908.54 --> 1910.36]  I don't want LLMs to contribute
[1910.36 --> 1912.64]  to a proliferation of low quality apps.
[1912.96 --> 1915.50]  I really want to see LLMs enable us all
[1915.50 --> 1917.88]  to improve quality and raise the quality floor
[1917.88 --> 1920.00]  for all software that we all use.
[1920.68 --> 1920.80]  Yeah.
[1921.04 --> 1923.30]  I love what you talked about there of like,
[1923.46 --> 1924.82]  an LLM integrated application
[1924.82 --> 1926.46]  doesn't have to just be a chat bot.
[1926.66 --> 1927.10]  That's right.
[1927.28 --> 1928.56]  Do these other things.
[1928.56 --> 1931.52]  And I think there's a transformation
[1931.52 --> 1933.64]  similar to what you were talking about with React,
[1933.76 --> 1936.00]  where you move from a mode
[1936.00 --> 1937.44]  where you're very imperative.
[1937.68 --> 1938.28]  You're having to say,
[1938.36 --> 1939.04]  this data goes here,
[1939.10 --> 1939.78]  this data goes here,
[1939.82 --> 1941.26]  to something that is much more declarative.
[1941.92 --> 1943.12]  Here's what I want to happen.
[1943.44 --> 1943.78]  That's right.
[1943.84 --> 1945.30]  The compiler takes care of all of that.
[1945.40 --> 1947.56]  And some of the best Gen AI applications
[1948.20 --> 1949.30]  I've seen do something similar,
[1949.38 --> 1950.54]  where they take a user interface
[1950.54 --> 1951.98]  that used to be very imperative,
[1952.56 --> 1953.74]  thinking some of Adobe's tools.
[1953.80 --> 1954.80]  Yeah, that's right.
[1954.82 --> 1956.06]  I used to have to do this,
[1956.14 --> 1957.12]  color here, do this.
[1957.12 --> 1960.60]  And now I say, make it look like a sky background.
[1960.90 --> 1961.14]  That's right.
[1961.14 --> 1962.08]  And it will just do it.
[1962.58 --> 1963.20]  Yeah, that's right.
[1963.30 --> 1965.66]  So it was declarative UI, right?
[1965.76 --> 1967.66]  React sort of pioneered this idea
[1967.66 --> 1970.10]  of describe what your application looks like
[1970.10 --> 1971.84]  at any point in time.
[1972.06 --> 1973.92]  And maybe the era of LLMs,
[1974.08 --> 1975.24]  just to connect to the analogy,
[1975.40 --> 1977.38]  is describe your application
[1977.38 --> 1979.12]  at any point in time.
[1979.12 --> 1980.82]  So it's not just what it looks like now.
[1981.12 --> 1982.46]  Now it's how it behaves.
[1983.20 --> 1985.24]  You know, there's a tweet going around
[1985.24 --> 1987.38]  with use AI, you know, when.
[1987.76 --> 1988.62]  And actually, like,
[1988.70 --> 1991.48]  I think that directive is not that far off.
[1991.68 --> 1992.72]  You'll kind of describe
[1992.72 --> 1994.24]  what your application's supposed to do.
[1994.34 --> 1996.16]  And if we can ensure that the same,
[1996.30 --> 1997.80]  you know, predictable behavior
[1997.80 --> 1998.78]  and outcomes happen,
[1999.22 --> 1999.94]  we'll be able to,
[2000.14 --> 2001.26]  we're in this sort of era,
[2001.40 --> 2003.04]  entering the era of personal software,
[2003.12 --> 2003.44]  I think.
[2003.80 --> 2004.34]  So we'll see.
[2004.92 --> 2006.58]  Yeah, and I think to Cable's analogy
[2006.58 --> 2008.14]  of, like, you know,
[2008.16 --> 2009.10]  being able to just quickly
[2009.10 --> 2009.88]  replace the sky,
[2009.96 --> 2011.06]  like one thing we were talking about
[2011.06 --> 2011.90]  last night was, like,
[2012.34 --> 2013.32]  we could both do that
[2013.32 --> 2014.42]  and get two different skies.
[2014.76 --> 2014.96]  Yeah.
[2014.96 --> 2015.52]  Right now.
[2015.68 --> 2016.86]  But talking to you,
[2016.92 --> 2017.68]  I think, like,
[2018.24 --> 2020.70]  and, like, maybe using Gen AI
[2020.70 --> 2022.14]  or not Gen AI,
[2022.22 --> 2024.88]  but just AI to help you guide
[2024.88 --> 2026.52]  through the deterministic outcomes
[2026.52 --> 2026.98]  that you want.
[2027.06 --> 2028.24]  So don't give me everything
[2028.24 --> 2028.96]  in Facebook right,
[2029.06 --> 2030.92]  or sorry, in Photoshop right away.
[2031.40 --> 2032.58]  But when I describe
[2032.58 --> 2033.58]  what I want to do,
[2033.58 --> 2034.38]  you can point me
[2034.38 --> 2035.16]  at the right tools
[2035.16 --> 2036.54]  and kind of catch at a funnel
[2036.54 --> 2038.14]  with how I might,
[2038.74 --> 2039.72]  how anyone might, like,
[2039.88 --> 2040.60]  describe what they want
[2040.60 --> 2041.74]  and then push me
[2041.74 --> 2042.46]  to the right tools.
[2042.74 --> 2042.92]  Yeah.
[2043.32 --> 2044.14]  Progressive disclosure
[2044.14 --> 2044.78]  of complexity.
[2044.94 --> 2045.68]  Yeah, I like that.
[2045.94 --> 2046.90]  Shifting gears slightly,
[2047.02 --> 2048.68]  so we're here at React Summit.
[2049.24 --> 2050.30]  All sorts of interesting
[2050.30 --> 2051.34]  things going on.
[2051.50 --> 2052.62]  You're here, obviously,
[2052.74 --> 2053.68]  speaking, talking to us,
[2053.74 --> 2054.20]  doing these things.
[2054.80 --> 2055.78]  What is your sense
[2055.78 --> 2057.98]  of conferences, 2024?
[2058.30 --> 2059.10]  We've gone through this,
[2059.18 --> 2059.42]  you know,
[2059.44 --> 2061.02]  whole dynamic of, like,
[2061.50 --> 2062.46]  okay, pandemic,
[2062.46 --> 2063.48]  nobody's going to anything.
[2063.62 --> 2064.32]  Virtual conference,
[2064.40 --> 2065.92]  virtual conferences are miserable.
[2066.14 --> 2067.68]  Like, all these different things,
[2067.78 --> 2068.52]  they're not miserable.
[2068.94 --> 2069.72]  They're good,
[2070.08 --> 2071.28]  but they're not the same.
[2071.46 --> 2071.72]  That's right.
[2071.72 --> 2073.68]  So how would you talk
[2073.68 --> 2074.66]  to folks who are saying,
[2074.76 --> 2076.16]  oh, I'm not at React Summit.
[2076.16 --> 2077.18]  I'm watching this virtually.
[2077.64 --> 2078.38]  Should I go?
[2078.50 --> 2079.22]  Why should I go?
[2079.42 --> 2080.08]  What is...
[2080.08 --> 2080.82]  It doesn't need
[2080.82 --> 2082.52]  to be necessarily this one,
[2082.66 --> 2083.44]  but I think, like,
[2083.48 --> 2084.96]  getting together in person
[2084.96 --> 2086.34]  with people in the field
[2086.34 --> 2087.36]  in the same space
[2087.36 --> 2088.72]  and sharing ideas
[2088.72 --> 2089.84]  and building off of each other,
[2089.90 --> 2090.98]  that's what the magic is.
[2091.24 --> 2091.86]  When we created
[2091.86 --> 2093.16]  the first React Conf,
[2093.30 --> 2094.44]  like, 2015,
[2094.66 --> 2095.26]  we started working on it
[2095.26 --> 2095.76]  in 2014,
[2096.38 --> 2097.24]  I think our goal
[2097.24 --> 2097.86]  was to, like,
[2097.92 --> 2099.00]  bring some of the community
[2099.00 --> 2100.70]  together and, like,
[2100.86 --> 2101.16]  you know,
[2101.24 --> 2101.74]  tell some,
[2101.88 --> 2102.88]  here's the latest updates.
[2103.36 --> 2104.18]  But the value
[2104.18 --> 2105.04]  that we got out of it
[2105.04 --> 2106.20]  was we literally built
[2106.20 --> 2107.80]  lifelong friendships.
[2108.38 --> 2109.44]  And many of the people
[2109.44 --> 2110.60]  that you still see speaking
[2110.60 --> 2111.70]  at all of these conferences
[2111.70 --> 2113.28]  today and now
[2113.28 --> 2114.10]  in the industry,
[2114.70 --> 2115.86]  their first conference,
[2115.86 --> 2117.30]  their first React-related conference
[2117.30 --> 2118.20]  was React Conf,
[2118.60 --> 2119.84]  and now they're all sort of
[2119.84 --> 2121.12]  bonded over that experience.
[2121.84 --> 2122.84]  So I, you know,
[2123.16 --> 2124.42]  pandemic hit all of us
[2124.42 --> 2124.78]  very hard.
[2124.90 --> 2125.34]  I think, like,
[2125.62 --> 2127.34]  I thrive on collaborating
[2127.34 --> 2128.84]  in person with folks,
[2129.30 --> 2131.98]  and I really missed it.
[2132.30 --> 2133.76]  So it's really good to be here.
[2133.82 --> 2135.36]  Even just this morning so far,
[2135.72 --> 2136.74]  leading up to this sort of,
[2136.78 --> 2137.54]  like, opening ceremony
[2137.54 --> 2138.82]  is just all of the conversations
[2138.82 --> 2140.36]  and just hearing what people
[2140.36 --> 2141.26]  are working on
[2141.26 --> 2142.68]  and what they build,
[2142.78 --> 2143.56]  and, yeah,
[2143.58 --> 2144.64]  you can't replace that.
[2144.64 --> 2146.76]  So even if it's a local meetup,
[2146.98 --> 2147.18]  you know,
[2147.18 --> 2148.68]  get out and connect with people.
[2149.02 --> 2150.18]  Support your local meetups.
[2150.40 --> 2150.96]  Yeah, I agree.
[2151.14 --> 2151.58]  Absolutely.
[2152.36 --> 2154.90]  I think we're just about at time.
[2155.02 --> 2155.60]  Anything you want
[2155.60 --> 2156.36]  to leave people with?
[2157.16 --> 2157.78]  You know,
[2157.88 --> 2159.02]  I think it's been
[2159.02 --> 2161.18]  a fun journey so far,
[2161.34 --> 2162.70]  watching the evolution
[2162.70 --> 2163.38]  of React
[2163.38 --> 2164.28]  and the community
[2164.28 --> 2165.16]  and the sort of families
[2165.16 --> 2166.54]  of technologies around this.
[2166.92 --> 2168.10]  I think one of the things
[2168.10 --> 2169.52]  that I was very excited about
[2169.52 --> 2171.72]  that I didn't necessarily see
[2171.72 --> 2172.34]  as a goal
[2172.34 --> 2173.90]  in the early days of React
[2173.90 --> 2175.34]  was how it sort of
[2175.34 --> 2176.32]  reignited interest
[2176.32 --> 2177.72]  in the web as a platform.
[2178.46 --> 2178.86]  Yes.
[2178.94 --> 2180.10]  And so I'm really, like,
[2180.56 --> 2181.66]  heartened by all of the
[2181.66 --> 2182.68]  active development
[2182.68 --> 2183.32]  and innovation
[2183.32 --> 2184.14]  happening on the web
[2184.14 --> 2184.70]  as a platform.
[2185.26 --> 2185.98]  And so, you know,
[2186.26 --> 2187.24]  I'm a big proponent
[2187.24 --> 2189.04]  of sort of making the web win.
[2189.80 --> 2190.70]  The web is where
[2190.70 --> 2191.46]  I cut my teeth,
[2191.52 --> 2192.84]  and I know a lot of us as well,
[2193.26 --> 2194.50]  ever since the Mutools days
[2194.50 --> 2195.50]  or even before that,
[2195.88 --> 2197.00]  prototype and dojo
[2197.00 --> 2197.66]  and all that stuff.
[2197.66 --> 2198.60]  So, you know,
[2198.64 --> 2200.22]  big fan of investing,
[2200.44 --> 2201.18]  continued investment
[2201.18 --> 2202.10]  in web technologies
[2202.10 --> 2203.46]  and the web platform
[2203.46 --> 2204.62]  and, you know,
[2204.72 --> 2205.70]  happy and excited
[2205.70 --> 2206.82]  to connect with anybody
[2206.82 --> 2207.82]  who shares that passion.
[2208.20 --> 2209.30]  So, yeah.
[2209.44 --> 2210.46]  Thanks, guys, for having me.
[2210.66 --> 2210.98]  Thank you.
[2211.24 --> 2211.68]  Thank you.
[2214.88 --> 2215.74]  Well, friends,
[2215.84 --> 2216.88]  I'm here with a friend of mine,
[2216.98 --> 2217.52]  Michael Greenwich,
[2217.60 --> 2219.26]  co-founder and CEO
[2219.26 --> 2220.34]  of WorkOS.
[2220.94 --> 2221.88]  We're big fans
[2221.88 --> 2222.86]  of WorkOS here.
[2222.98 --> 2223.56]  Michael, tell me
[2223.56 --> 2224.54]  about AuthKit.
[2225.02 --> 2225.76]  What is this?
[2225.92 --> 2226.56]  How does it work?
[2226.82 --> 2227.48]  Why'd you make it?
[2227.66 --> 2229.02]  WorkOS has been building stuff
[2229.02 --> 2229.90]  in authentication
[2229.90 --> 2230.78]  for a long time,
[2230.86 --> 2231.66]  since the very beginning.
[2231.96 --> 2233.26]  But we really focused initially
[2233.26 --> 2234.70]  on just enterprise auth,
[2234.86 --> 2235.56]  single sign-on,
[2235.68 --> 2236.68]  SAML authentication.
[2237.06 --> 2237.98]  But a year or two into that,
[2238.06 --> 2239.04]  we heard from more people
[2239.04 --> 2239.76]  that they wanted
[2239.76 --> 2241.14]  all the auth stuff covered.
[2241.44 --> 2242.14]  Two-factor auth,
[2242.34 --> 2243.08]  password auth,
[2243.34 --> 2243.54]  you know,
[2243.58 --> 2245.70]  with blocking passwords
[2245.70 --> 2246.58]  that have been reused.
[2246.70 --> 2247.58]  They wanted auth
[2247.58 --> 2248.10]  with, you know,
[2248.14 --> 2249.32]  other third-party systems.
[2249.74 --> 2250.60]  And they wanted really
[2250.60 --> 2251.42]  WorkOS to handle
[2251.42 --> 2252.48]  all the business logic
[2252.48 --> 2253.46]  around tying together
[2253.46 --> 2253.98]  identities,
[2254.58 --> 2255.30]  provisioning users,
[2255.30 --> 2256.90]  and even more advanced things
[2256.90 --> 2258.58]  like role-based access control
[2258.58 --> 2259.20]  and permissions.
[2259.74 --> 2260.50]  So we started thinking
[2260.50 --> 2261.20]  about that more,
[2261.28 --> 2262.06]  how we could offer it
[2262.06 --> 2262.64]  as an API.
[2263.14 --> 2264.34]  And then we realized
[2264.34 --> 2265.20]  we had this amazing
[2265.20 --> 2266.72]  experience with Radix,
[2266.80 --> 2267.88]  with this API,
[2268.56 --> 2270.44]  really the component system
[2270.44 --> 2271.68]  for building front-end
[2271.68 --> 2273.08]  experiences for developers.
[2273.62 --> 2274.64]  Radix is downloaded
[2274.64 --> 2275.66]  tens of millions of times
[2275.66 --> 2276.26]  every month
[2276.26 --> 2277.48]  for doing exactly this.
[2277.66 --> 2278.32]  So we glued those
[2278.32 --> 2279.00]  two things together
[2279.00 --> 2280.10]  and we built AuthKit.
[2280.34 --> 2281.48]  So AuthKit is the easiest way
[2281.48 --> 2282.84]  to add Auth to any app,
[2283.10 --> 2283.92]  not just Next.js
[2283.92 --> 2284.48]  if you're building
[2284.48 --> 2285.52]  a Rails app
[2285.52 --> 2286.50]  or a Django app
[2286.50 --> 2287.70]  or a just straight-up
[2287.70 --> 2288.72]  Express app or something.
[2289.08 --> 2289.74]  It comes with
[2289.74 --> 2290.86]  a hosted login box.
[2291.06 --> 2292.54]  So you can customize that,
[2292.62 --> 2293.30]  you can style it.
[2293.50 --> 2294.26]  You can build your own
[2294.26 --> 2295.08]  login experience too.
[2295.16 --> 2296.16]  It's extremely modular.
[2296.38 --> 2296.96]  You can just use
[2296.96 --> 2297.84]  the backend APIs
[2297.84 --> 2298.88]  in a headless fashion.
[2299.12 --> 2299.90]  But out of the box,
[2299.96 --> 2300.78]  it gives you everything
[2300.78 --> 2301.86]  you need to be able
[2301.86 --> 2302.58]  to serve customers.
[2302.80 --> 2303.72]  And it's tied into
[2303.72 --> 2304.62]  the WorkOS platform
[2304.62 --> 2305.66]  so you can really,
[2305.82 --> 2306.58]  really quickly add
[2306.58 --> 2307.56]  any enterprise features
[2307.56 --> 2307.92]  you need.
[2308.22 --> 2309.02]  So we have a lot of companies
[2309.02 --> 2309.86]  that start using it
[2309.86 --> 2310.80]  because they anticipate
[2310.80 --> 2311.86]  they're going to grow up market
[2311.86 --> 2313.12]  and want to serve enterprise.
[2313.60 --> 2314.72]  And they don't want to have
[2314.72 --> 2315.44]  to re-architect
[2315.44 --> 2316.44]  their Auth stack
[2316.44 --> 2317.26]  when they do that.
[2317.52 --> 2318.18]  So it's kind of a way
[2318.18 --> 2319.48]  to like future-proof
[2319.48 --> 2320.30]  your Auth system
[2320.30 --> 2321.74]  for your future growth.
[2321.90 --> 2322.46]  And we have people
[2322.46 --> 2323.02]  that have done that.
[2323.20 --> 2324.06]  People that started off
[2324.06 --> 2324.38]  and they're like,
[2324.42 --> 2325.32]  oh, I'm just kicking the tires.
[2325.42 --> 2326.04]  I'm just doing this.
[2326.10 --> 2326.90]  And then poof,
[2327.14 --> 2328.26]  their app gets a bunch of traction,
[2328.54 --> 2329.00]  starts growing.
[2329.10 --> 2329.52]  It's awesome.
[2330.24 --> 2331.78]  And they go close Coinbase
[2331.78 --> 2332.40]  or Disney
[2332.40 --> 2333.70]  or United Airlines
[2333.70 --> 2334.12]  or, you know,
[2334.14 --> 2335.46]  it's like a major customer.
[2335.74 --> 2336.76]  And instead of saying,
[2336.90 --> 2338.00]  oh, no, sorry,
[2338.00 --> 2338.72]  we don't have any
[2338.72 --> 2339.64]  of these enterprise things
[2339.64 --> 2340.08]  and we're going to have
[2340.08 --> 2341.00]  to rebuild everything.
[2341.20 --> 2342.70]  Just go into the WorkOS dashboard
[2342.70 --> 2343.42]  and check a box
[2343.42 --> 2344.22]  and you're done.
[2344.82 --> 2345.34]  Aside from the fact
[2345.34 --> 2346.94]  that AuthKit is just awesome,
[2347.24 --> 2348.32]  the real awesome thing
[2348.32 --> 2349.46]  is that it is free
[2349.46 --> 2352.58]  for up to 1 million users.
[2353.36 --> 2355.18]  Yes, 1 million monthly
[2355.18 --> 2356.08]  active users
[2356.08 --> 2357.68]  are included in this
[2357.68 --> 2358.48]  out of the gate.
[2358.70 --> 2360.34]  So use it from day one.
[2360.42 --> 2361.76]  And when you need to scale
[2361.76 --> 2362.58]  to enterprise,
[2362.92 --> 2363.88]  you're already ready.
[2363.98 --> 2364.60]  Too easy.
[2364.94 --> 2365.56]  You can learn more
[2365.56 --> 2366.88]  at authkit.com
[2366.88 --> 2367.56]  or, of course,
[2367.82 --> 2369.50]  WorkOS.com.
[2369.74 --> 2370.46]  Big fans.
[2370.70 --> 2371.24]  Check it out.
[2371.56 --> 2372.42]  1 million users
[2372.42 --> 2373.34]  for free.
[2373.66 --> 2373.92]  Wow.
[2374.26 --> 2375.58]  WorkOS.com
[2375.58 --> 2377.72]  or authkit.com.
[2382.94 --> 2384.00]  What's up, friends
[2384.00 --> 2384.94]  and party people?
[2385.12 --> 2385.82]  Adam here.
[2385.82 --> 2388.24]  I'm sitting with Danny Grant,
[2388.54 --> 2389.94]  co-founder and CEO
[2389.94 --> 2391.46]  of Jam.dev,
[2391.52 --> 2392.34]  one of our new sponsors.
[2392.86 --> 2393.66]  Yes, Jam.dev
[2393.66 --> 2395.46]  is one-click bug reports
[2395.46 --> 2396.88]  that devs love.
[2397.18 --> 2398.02]  It's just too easy.
[2398.38 --> 2399.52]  Get Jam for free today
[2399.52 --> 2401.46]  at jam.dev.
[2401.78 --> 2402.20]  So, Danny,
[2402.28 --> 2403.16]  how do you explain
[2403.16 --> 2404.32]  what Jam is
[2404.32 --> 2405.48]  and how it helps teams
[2405.48 --> 2406.12]  be more effective?
[2406.66 --> 2408.08]  Jam is the fastest way
[2408.08 --> 2409.30]  to capture a bug
[2409.30 --> 2410.70]  in a way that developers
[2410.70 --> 2411.92]  can debug it faster.
[2412.24 --> 2413.84]  It's a browser plugin
[2413.84 --> 2415.06]  that hooks into DevTools
[2415.06 --> 2416.06]  so when anyone
[2416.06 --> 2416.60]  on your team
[2416.60 --> 2417.34]  spots a bug,
[2417.66 --> 2418.90]  they can one-click capture
[2418.90 --> 2420.14]  what happened on the screen
[2420.14 --> 2421.90]  plus everything in DevTools.
[2422.22 --> 2422.86]  Console logs,
[2423.00 --> 2423.68]  network requests,
[2423.94 --> 2424.72]  session information,
[2425.02 --> 2425.74]  and it grabs it
[2425.74 --> 2426.40]  into a link
[2426.40 --> 2427.16]  so that when you
[2427.16 --> 2428.02]  open up the ticket,
[2428.36 --> 2429.56]  you have every single thing
[2429.56 --> 2430.32]  you need to debug.
[2430.46 --> 2431.32]  You don't have to ask
[2431.32 --> 2432.64]  a single follow-up question.
[2432.98 --> 2433.78]  This is for teams
[2433.78 --> 2434.62]  who want to spend
[2434.62 --> 2435.34]  their time building
[2435.34 --> 2436.14]  new features,
[2436.30 --> 2437.52]  not fixing old ones.
[2437.68 --> 2439.06]  I think that the most impact
[2439.06 --> 2439.82]  a software engineer
[2439.82 --> 2440.46]  can have
[2440.46 --> 2442.08]  is on building the future
[2442.08 --> 2443.32]  for their customers.
[2443.32 --> 2445.20]  It's on making things easier.
[2445.42 --> 2446.80]  It's building what's next.
[2447.22 --> 2448.38]  And so we want to make sure
[2448.38 --> 2449.00]  that you're not spending
[2449.00 --> 2449.88]  your whole afternoon
[2449.88 --> 2451.50]  just trying to repro a bug.
[2451.82 --> 2452.20]  Instead,
[2452.42 --> 2453.38]  you have everything you need
[2453.38 --> 2454.16]  to just get started.
[2454.54 --> 2455.18]  Okay, friends,
[2455.26 --> 2457.10]  go to jam.dev
[2457.10 --> 2457.94]  and learn more about
[2457.94 --> 2458.58]  what Jam is doing
[2458.58 --> 2459.56]  for teams to make
[2459.56 --> 2460.36]  bug reporting
[2460.36 --> 2461.98]  and all that fun stuff
[2461.98 --> 2462.78]  super easy,
[2462.90 --> 2463.66]  super fast.
[2464.12 --> 2465.22]  Get Jam for free today.
[2465.64 --> 2466.94]  Jam.dev.
[2467.16 --> 2467.72]  Again,
[2468.06 --> 2469.28]  jam.dev.
[2473.32 --> 2475.20]  Ahoy hoy.
[2475.56 --> 2476.86]  We are here at React Summit.
[2477.06 --> 2478.20]  My name is Nick Neesey
[2478.20 --> 2479.26]  and I'm here with K-Ball.
[2479.34 --> 2480.06]  K-Ball, how's it going?
[2480.32 --> 2481.06]  Going good.
[2481.24 --> 2482.24]  Excited to be here
[2482.24 --> 2483.78]  as we've been.
[2484.62 --> 2485.62]  It's been a long,
[2485.70 --> 2487.16]  very fun day at React Summit
[2487.16 --> 2488.60]  and we are joined by
[2488.60 --> 2489.10]  the one,
[2489.24 --> 2489.62]  the only,
[2489.76 --> 2490.34]  Shruti Kapoor.
[2490.46 --> 2491.22]  Shruti, how are you doing?
[2491.42 --> 2492.06]  I'm doing well.
[2492.10 --> 2492.78]  How are you doing, Nick?
[2492.84 --> 2493.88]  I'm doing fantastic.
[2493.88 --> 2494.64]  Now that you're here.
[2496.22 --> 2497.60]  I tend to have that effect
[2497.60 --> 2498.08]  on people.
[2499.08 --> 2499.80]  For sure.
[2500.02 --> 2501.06]  Please, tell us a little bit
[2501.06 --> 2501.58]  about yourself.
[2501.82 --> 2502.06]  Yeah.
[2502.28 --> 2503.36]  I'm a front-end engineer
[2503.36 --> 2504.12]  at Slack.
[2504.28 --> 2506.00]  I build web applications,
[2506.64 --> 2507.60]  help them scale.
[2508.04 --> 2509.36]  I mostly work in React
[2509.36 --> 2510.84]  so I also speak about React
[2510.84 --> 2511.14]  a lot,
[2511.20 --> 2511.88]  which is why I'm here.
[2512.08 --> 2512.44]  Nice.
[2512.48 --> 2513.12]  I've heard of React.
[2513.50 --> 2514.38]  Yeah, React, right?
[2514.90 --> 2515.62]  React library.
[2516.44 --> 2517.62]  Some people have heard of it.
[2517.72 --> 2518.02]  Yeah.
[2518.18 --> 2519.62]  Yeah, it's an app topic
[2519.62 --> 2520.76]  for React Summit for sure.
[2522.28 --> 2522.72]  So,
[2523.00 --> 2524.18]  you gave a talk today.
[2524.26 --> 2524.94]  What was your talk about?
[2525.24 --> 2526.00]  Yeah, my talk was about
[2526.00 --> 2526.94]  everything you need to know
[2526.94 --> 2527.88]  about React 19.
[2528.06 --> 2528.36]  Nice.
[2528.54 --> 2529.56]  And the reason why
[2529.56 --> 2530.38]  I did this talk is
[2530.38 --> 2531.24]  I feel like every time
[2531.24 --> 2532.26]  a new version of React
[2532.26 --> 2532.84]  comes out,
[2533.26 --> 2534.44]  a little bit of me is like,
[2534.52 --> 2534.98]  ah,
[2535.22 --> 2538.80]  and then the other half
[2538.80 --> 2539.16]  is like,
[2539.22 --> 2539.62]  oh my God,
[2539.70 --> 2540.14]  new version,
[2540.26 --> 2540.96]  new shiny thing,
[2541.04 --> 2541.62]  let's do it.
[2542.08 --> 2542.36]  So,
[2542.50 --> 2543.34]  I was giving this talk
[2543.34 --> 2544.12]  to kind of explain
[2544.12 --> 2545.04]  what are the new features
[2545.04 --> 2545.84]  that developers need
[2545.84 --> 2546.68]  to be aware of,
[2547.08 --> 2547.86]  especially like
[2547.86 --> 2548.72]  client-side developers
[2548.72 --> 2549.34]  because there's a lot
[2549.34 --> 2550.14]  of client-side code
[2550.14 --> 2550.74]  that's come out
[2550.74 --> 2551.58]  with React 19.
[2551.96 --> 2552.12]  So,
[2552.12 --> 2552.72]  what are some things
[2552.72 --> 2553.68]  you need to be aware of?
[2554.02 --> 2554.98]  React 19 is still
[2554.98 --> 2555.90]  in RC stage
[2555.90 --> 2556.56]  as of now,
[2556.74 --> 2557.92]  so it's nice
[2557.92 --> 2559.14]  to kind of be aware
[2559.14 --> 2559.96]  of these things now
[2559.96 --> 2560.94]  so you can think about
[2560.94 --> 2561.34]  how you're going to
[2561.34 --> 2562.38]  upgrade your code later on.
[2562.42 --> 2562.62]  Yeah.
[2563.02 --> 2563.24]  So,
[2563.72 --> 2564.94]  this is a perfect topic
[2564.94 --> 2566.74]  because I'm a React developer.
[2567.28 --> 2568.38]  I haven't paid a lot
[2568.38 --> 2568.74]  of attention
[2568.74 --> 2570.74]  to React 19 specifically,
[2571.36 --> 2572.12]  but I know that like
[2572.12 --> 2572.62]  there's,
[2573.10 --> 2574.24]  just from my perspective,
[2574.36 --> 2574.54]  I guess,
[2574.56 --> 2575.30]  I'm speaking for me,
[2575.64 --> 2576.32]  there's a little bit
[2576.32 --> 2576.84]  of confusion
[2576.84 --> 2577.56]  because you've got
[2577.56 --> 2578.44]  like React 19,
[2578.74 --> 2579.78]  you've got React server
[2579.78 --> 2580.22]  components,
[2580.22 --> 2581.44]  and you've got React compiler.
[2581.60 --> 2583.00]  Is that all React 19?
[2583.38 --> 2583.54]  Oh,
[2583.60 --> 2584.08]  great question.
[2584.24 --> 2584.38]  So,
[2584.56 --> 2585.58]  React server components,
[2585.92 --> 2586.60]  React compiler,
[2587.04 --> 2588.16]  and even React actions
[2588.16 --> 2589.10]  that's now come out
[2589.10 --> 2589.94]  with React 19,
[2590.16 --> 2590.70]  I would say
[2590.70 --> 2591.48]  it's kind of all
[2591.48 --> 2592.18]  like features,
[2592.30 --> 2592.96]  you can call them.
[2593.10 --> 2593.34]  So,
[2593.40 --> 2594.20]  React server components,
[2594.36 --> 2594.72]  compiler,
[2595.02 --> 2595.84]  which is actually a plugin,
[2596.40 --> 2597.70]  and React actions,
[2597.84 --> 2598.70]  they're all kind of features.
[2599.10 --> 2600.14]  React 19 is the version
[2600.14 --> 2601.68]  of React that now
[2601.68 --> 2602.68]  makes React server
[2602.68 --> 2603.52]  components stable,
[2604.42 --> 2604.70]  brings,
[2604.86 --> 2605.94]  introduces React actions,
[2605.94 --> 2607.36]  and also introduces
[2607.36 --> 2608.04]  React compiler
[2608.04 --> 2608.68]  as a plugin,
[2609.08 --> 2609.82]  but React 19
[2609.82 --> 2610.26]  is kind of like
[2610.26 --> 2610.80]  the version,
[2611.32 --> 2612.04]  and these are kind of
[2612.04 --> 2612.82]  like small features
[2612.82 --> 2613.58]  in it.
[2613.58 --> 2613.84]  Okay.
[2613.90 --> 2614.44]  You kind of think
[2614.44 --> 2615.12]  of that that way.
[2615.78 --> 2616.60]  React server components
[2616.60 --> 2617.28]  was introduced
[2617.28 --> 2618.98]  around 18-ish,
[2619.20 --> 2619.80]  so they've been around
[2619.80 --> 2620.28]  for a while,
[2620.46 --> 2621.44]  although they weren't
[2621.44 --> 2622.14]  stable at the time,
[2622.18 --> 2622.94]  but now they're stable.
[2623.30 --> 2623.54]  Okay,
[2623.78 --> 2624.54]  and there's some confusion
[2624.54 --> 2625.52]  too because like
[2625.52 --> 2626.52]  I almost think of those
[2626.52 --> 2627.70]  more as like a next feature
[2627.70 --> 2628.68]  just because of the,
[2628.86 --> 2629.84]  that being the only
[2629.84 --> 2631.00]  implementation right now,
[2631.10 --> 2632.52]  so the lines are blurred
[2632.52 --> 2633.58]  is what I'm trying to say.
[2633.78 --> 2633.86]  Yeah.
[2634.00 --> 2634.94]  Thank you for helping me
[2634.94 --> 2635.92]  to make sense of that.
[2635.94 --> 2636.44]  Yeah, you know,
[2636.54 --> 2640.00]  it's such a funny thing
[2640.00 --> 2641.06]  because today I was
[2641.06 --> 2641.70]  leading the panel
[2641.70 --> 2642.82]  of future of React,
[2642.92 --> 2643.58]  and I asked the same
[2643.58 --> 2644.00]  question,
[2644.36 --> 2644.92]  and I said,
[2645.56 --> 2646.76]  it feels like Next.js
[2646.76 --> 2647.36]  is kind of like
[2647.36 --> 2648.82]  the favored framework
[2648.82 --> 2649.78]  that React is choosing,
[2649.88 --> 2650.56]  so how do you feel
[2650.56 --> 2651.52]  about Next.js being
[2651.52 --> 2652.28]  the place where
[2652.28 --> 2653.04]  all of the new features
[2653.04 --> 2653.46]  are coming?
[2653.80 --> 2654.32]  And you're right,
[2654.42 --> 2655.40]  like even for new developers,
[2655.50 --> 2656.14]  it can feel that
[2656.14 --> 2657.28]  all of these are new features,
[2657.66 --> 2658.20]  which is something
[2658.20 --> 2659.06]  I felt as well
[2659.06 --> 2660.20]  when I was just starting
[2660.20 --> 2660.88]  out with React
[2660.88 --> 2661.58]  back in the day
[2661.58 --> 2662.70]  when React and Redux
[2662.70 --> 2663.84]  were like this coupled thing,
[2664.24 --> 2664.80]  and so I thought
[2664.80 --> 2665.86]  every React thing
[2665.86 --> 2666.88]  is actually a Redux thing
[2666.88 --> 2667.18]  as well,
[2667.26 --> 2667.62]  and I was like,
[2667.72 --> 2668.34]  React and Redux,
[2668.42 --> 2668.92]  they just come
[2668.92 --> 2670.04]  in a package together,
[2670.18 --> 2670.86]  but instead they're
[2670.86 --> 2672.04]  actually two different libraries.
[2672.44 --> 2672.96]  So you're right,
[2673.04 --> 2673.52]  that can kind of
[2673.52 --> 2674.20]  give that impression.
[2674.82 --> 2676.36]  So because I think
[2676.36 --> 2678.42]  RSCs have been around
[2678.42 --> 2679.04]  for a while,
[2679.12 --> 2679.98]  they're a little more familiar,
[2680.18 --> 2681.90]  but Actions is something new
[2681.90 --> 2683.12]  that I'm not sure
[2683.12 --> 2684.14]  folks have heard about.
[2684.22 --> 2684.74]  Do you want to explain
[2684.74 --> 2685.58]  kind of what that is
[2685.58 --> 2686.28]  and what it gets you
[2686.28 --> 2686.78]  as a developer?
[2687.14 --> 2688.08]  Yeah, so Actions
[2688.08 --> 2689.10]  is kind of the way
[2689.10 --> 2690.18]  you can write async
[2690.18 --> 2691.82]  transitions as a function.
[2692.26 --> 2692.72]  Basically,
[2692.90 --> 2693.94]  to simplify it,
[2694.08 --> 2695.24]  we all know forms,
[2695.30 --> 2696.20]  we've been handling forms
[2696.20 --> 2696.92]  for a long time,
[2696.92 --> 2698.34]  but the only way
[2698.34 --> 2698.94]  that we've known
[2698.94 --> 2700.44]  to submit a form
[2700.44 --> 2701.18]  is by having
[2701.18 --> 2701.96]  like a click handler,
[2702.52 --> 2702.72]  right?
[2702.82 --> 2704.74]  So we have like a form,
[2704.84 --> 2705.60]  we'll have like a button,
[2705.78 --> 2706.44]  and then we'll attach
[2706.44 --> 2707.10]  like a handle submit
[2707.10 --> 2707.72]  to the form,
[2707.80 --> 2708.84]  or we'll have like an onclick
[2708.84 --> 2709.52]  and we'll attach
[2709.52 --> 2710.36]  a handle submit to it.
[2710.52 --> 2711.14]  That's the way
[2711.14 --> 2712.24]  we've known to submit forms.
[2712.68 --> 2713.78]  But now with React,
[2713.92 --> 2714.56]  Actions,
[2714.70 --> 2715.88]  it is now letting you
[2715.88 --> 2716.74]  submit the form
[2716.74 --> 2717.46]  as an action.
[2717.88 --> 2718.78]  So now it's introducing
[2718.78 --> 2720.86]  this new DOM method
[2720.86 --> 2721.56]  called Action.
[2722.20 --> 2723.20]  And so instead of now
[2723.20 --> 2724.68]  having like a form submit,
[2724.68 --> 2726.50]  or like form onclick submit,
[2726.74 --> 2727.52]  you can just have
[2727.52 --> 2728.32]  a form action,
[2728.80 --> 2729.64]  and that takes care
[2729.64 --> 2730.44]  of submitting the form
[2730.44 --> 2731.70]  when you hit the submit button,
[2732.14 --> 2733.26]  showing you pending state.
[2733.70 --> 2735.10]  So actions,
[2735.36 --> 2736.18]  as a definition,
[2736.58 --> 2737.30]  are just functions
[2737.30 --> 2738.66]  that use async transitions,
[2738.90 --> 2740.20]  but really their use
[2740.20 --> 2742.68]  is to help submit forms easier.
[2743.30 --> 2744.30]  And this is all client-side?
[2744.54 --> 2745.58]  This is all client-side,
[2745.76 --> 2746.92]  but actions are also
[2746.92 --> 2748.46]  supported on the server,
[2748.76 --> 2749.58]  so you can also create
[2749.58 --> 2750.60]  server actions as well.
[2750.84 --> 2751.54]  Same idea,
[2751.64 --> 2752.40]  you create an action,
[2752.72 --> 2753.44]  you just define it
[2753.44 --> 2754.26]  as a server action,
[2754.72 --> 2755.40]  but it can be used
[2755.40 --> 2756.14]  on the client-side
[2756.14 --> 2756.74]  or it can be used
[2756.74 --> 2757.72]  on the server-side as well.
[2758.54 --> 2759.58]  Well, I think one of the things
[2759.58 --> 2760.84]  you mentioned there,
[2760.90 --> 2762.10]  a word that I'm going to pull out
[2762.10 --> 2763.58]  is transitions, right?
[2763.64 --> 2765.82]  Because I think submitting forms,
[2766.00 --> 2767.28]  we all know how to submit forms,
[2767.40 --> 2769.64]  but there's so many different states
[2769.64 --> 2770.68]  along the way.
[2770.86 --> 2770.98]  Yeah.
[2770.98 --> 2772.36]  And I think from what I've seen,
[2772.44 --> 2772.70]  at least,
[2772.80 --> 2774.82]  they somehow smooth the way
[2774.82 --> 2776.88]  for showing those transitions.
[2777.24 --> 2777.44]  Yeah.
[2777.96 --> 2780.72]  I think here when I say transition,
[2780.72 --> 2783.16]  I specifically refer to
[2783.16 --> 2784.58]  start transition hook,
[2784.70 --> 2786.10]  which was introduced in React 18.
[2786.60 --> 2787.56]  And with React 19,
[2787.76 --> 2788.64]  now you can actually have
[2788.64 --> 2789.56]  like an async function
[2789.56 --> 2791.22]  within the start transition hook
[2791.22 --> 2791.54]  as well,
[2791.60 --> 2792.38]  which is also a change
[2792.38 --> 2793.08]  of React 19.
[2793.46 --> 2794.92]  And that specific bit
[2794.92 --> 2796.20]  is what React defines
[2796.20 --> 2797.06]  as kind of actions.
[2797.56 --> 2798.78]  But the question here is,
[2798.88 --> 2800.60]  transition within a form,
[2800.72 --> 2802.48]  I think is what you were referring to
[2802.48 --> 2803.90]  is what are the different states
[2803.90 --> 2805.06]  of how a form is being submitted.
[2805.06 --> 2806.34]  So a form,
[2806.60 --> 2807.34]  you enter fields
[2807.34 --> 2808.36]  and then you send it
[2808.36 --> 2809.04]  over to the server.
[2809.24 --> 2810.10]  And while you're sending,
[2810.46 --> 2811.82]  it's in sort of an appending state,
[2811.98 --> 2813.16]  as in the form data
[2813.16 --> 2813.82]  is being submitted,
[2814.30 --> 2815.36]  the server is going to verify
[2815.36 --> 2815.96]  and it's going to send
[2815.96 --> 2816.66]  that data back.
[2816.88 --> 2817.68]  So in that state,
[2817.70 --> 2818.94]  it's kind of in the pending state.
[2819.14 --> 2819.94]  And do you use this
[2819.94 --> 2821.16]  to handle error conditions
[2821.16 --> 2822.10]  and stuff as well?
[2822.44 --> 2822.60]  Yeah.
[2822.72 --> 2823.44]  So you can use that
[2823.44 --> 2824.66]  to handle error conditions
[2824.66 --> 2825.16]  as well.
[2825.50 --> 2826.22]  I'm trying to think
[2826.22 --> 2828.44]  if the hook actually gives you
[2828.44 --> 2828.86]  error back.
[2828.92 --> 2829.60]  I don't think it does,
[2829.86 --> 2830.52]  but it can be used
[2830.52 --> 2832.18]  to handle error conditions
[2832.18 --> 2832.64]  as well.
[2832.64 --> 2833.32]  All right.
[2833.38 --> 2835.38]  So RSCs, actions.
[2836.64 --> 2837.16]  Compiler.
[2837.48 --> 2837.96]  Compiler.
[2838.10 --> 2838.88]  Which is a big one.
[2839.22 --> 2840.16]  Do you want to talk about that?
[2840.44 --> 2840.74]  Sure.
[2841.14 --> 2841.32]  Yeah.
[2841.70 --> 2842.76]  So compiler actually
[2842.76 --> 2843.54]  is a plugin
[2843.54 --> 2844.22]  that is introduced
[2844.22 --> 2845.38]  in React 19.
[2845.88 --> 2846.52]  I think one thing
[2846.52 --> 2847.68]  that people kind of confuse with
[2847.68 --> 2848.70]  is that React 19
[2848.70 --> 2849.82]  comes with compiler
[2849.82 --> 2851.84]  embedded within React 19,
[2852.02 --> 2852.98]  but it's actually a plugin.
[2853.18 --> 2854.28]  So you get React 19
[2854.28 --> 2856.28]  and you can get React compiler
[2856.28 --> 2856.86]  separately.
[2857.12 --> 2858.02]  It has been introduced
[2858.02 --> 2859.68]  together in the conference,
[2859.86 --> 2860.82]  so people kind of confuse
[2860.82 --> 2861.90]  that it's part of the package,
[2862.00 --> 2862.46]  but it's not.
[2862.98 --> 2863.84]  Compiler basically
[2863.84 --> 2865.00]  is the way React
[2865.00 --> 2866.46]  can auto-compile code
[2866.46 --> 2866.78]  for you
[2866.78 --> 2867.98]  and auto-memoize code
[2867.98 --> 2868.36]  for you,
[2868.66 --> 2869.50]  which basically means
[2869.50 --> 2870.48]  that as of now,
[2870.56 --> 2871.50]  the way we kind of
[2871.50 --> 2872.32]  optimize our code
[2872.32 --> 2873.56]  is by having used memos,
[2873.70 --> 2874.46]  used callbacks,
[2874.86 --> 2875.42]  React memo.
[2875.74 --> 2876.24]  Going forward
[2876.24 --> 2877.04]  with React 19,
[2877.14 --> 2877.50]  we don't need
[2877.50 --> 2878.20]  to do that anymore
[2878.20 --> 2879.16]  because with the help
[2879.16 --> 2879.84]  of React compiler,
[2879.98 --> 2880.38]  we'll be able
[2880.38 --> 2881.52]  to auto-memoize our code.
[2882.98 --> 2883.72]  It's a plugin.
[2883.82 --> 2884.94]  How do you opt into that?
[2885.16 --> 2886.32]  So you can opt into that
[2886.32 --> 2887.38]  by installing as a Babel
[2887.38 --> 2887.68]  plugin,
[2887.78 --> 2888.36]  and it gets part
[2888.36 --> 2889.36]  of like your Webpack config,
[2889.36 --> 2891.54]  and then once
[2891.54 --> 2892.36]  React compiler
[2892.36 --> 2892.88]  starts looking
[2892.88 --> 2893.38]  at your file,
[2893.44 --> 2894.68]  it's going to auto-optimize it,
[2895.06 --> 2896.26]  and you don't need
[2896.26 --> 2897.38]  to do anything after that.
[2897.50 --> 2898.44]  So once you've installed it,
[2898.46 --> 2899.02]  it's good to go.
[2899.30 --> 2900.46]  You can opt out of it,
[2900.52 --> 2901.24]  but to opt in,
[2901.24 --> 2901.56]  you don't need
[2901.56 --> 2902.10]  to do anything
[2902.10 --> 2903.22]  after installing it.
[2903.22 --> 2903.62]  Okay.
[2904.20 --> 2905.54]  And you said a Babel plugin.
[2905.68 --> 2906.34]  What if you're using
[2906.34 --> 2906.98]  something like Vite?
[2907.60 --> 2908.50]  I think there is
[2908.50 --> 2909.90]  an option for Vite as well.
[2910.76 --> 2911.44]  Actually, no.
[2911.76 --> 2912.34]  I take that back.
[2912.64 --> 2913.02]  With Vite,
[2913.12 --> 2914.34]  it's also working.
[2914.44 --> 2915.42]  I have a Vite project,
[2915.68 --> 2916.98]  so it works perfectly.
[2917.16 --> 2917.96]  Just a Babel plugin
[2917.96 --> 2918.60]  works perfectly
[2918.60 --> 2919.38]  with Vite as well.
[2919.58 --> 2919.82]  Awesome.
[2920.08 --> 2920.66]  Okay, cool.
[2921.34 --> 2922.14]  And then there's also
[2922.14 --> 2923.16]  the use hook.
[2923.42 --> 2924.68]  Is that part of React 19?
[2925.06 --> 2925.40]  Yes.
[2925.78 --> 2927.10]  Use is a really great one
[2927.10 --> 2927.74]  because I feel like
[2927.74 --> 2928.46]  it's so confusing
[2928.46 --> 2929.16]  because it sounds
[2929.16 --> 2930.70]  like a hook,
[2930.94 --> 2931.62]  acts like a hook,
[2931.68 --> 2932.36]  but is not a hook.
[2932.36 --> 2933.32]  It's actually an API.
[2933.92 --> 2934.64]  And I think the difference
[2934.64 --> 2935.44]  between...
[2936.50 --> 2937.18]  Let's pause on that
[2937.18 --> 2937.54]  for a minute.
[2938.02 --> 2939.14]  So what use does
[2939.14 --> 2940.24]  is it helps you
[2940.24 --> 2941.30]  read resources.
[2941.80 --> 2942.58]  I think the way
[2942.58 --> 2943.40]  it kind of reads
[2943.40 --> 2944.60]  in code is very intuitive.
[2944.86 --> 2945.30]  So let's say
[2945.30 --> 2946.38]  that you have a context.
[2946.68 --> 2947.16]  Let's say you have
[2947.16 --> 2947.90]  like theme context.
[2948.04 --> 2948.58]  This is how you like
[2948.58 --> 2949.28]  read current theme,
[2949.36 --> 2950.28]  dark mode, light mode.
[2950.98 --> 2951.74]  What you can do
[2951.74 --> 2952.34]  is you can say
[2952.34 --> 2953.96]  const theme equals use
[2953.96 --> 2955.86]  and then your context provider,
[2955.96 --> 2957.20]  so like theme context.
[2957.64 --> 2958.58]  And so now you're actually
[2958.58 --> 2959.04]  reading through
[2959.04 --> 2959.88]  a context provider
[2959.88 --> 2961.22]  by just using use.
[2961.30 --> 2962.06]  So you don't have to like
[2962.06 --> 2963.18]  embed your code
[2963.18 --> 2964.22]  within the context provider.
[2964.36 --> 2965.08]  So that's really neat.
[2965.36 --> 2965.98]  Oh, cool.
[2966.24 --> 2967.12]  So you don't have to like
[2967.12 --> 2967.96]  only have it
[2967.96 --> 2968.88]  within the components.
[2968.98 --> 2969.68]  You can actually have it
[2969.68 --> 2970.10]  like somewhere
[2970.10 --> 2971.38]  as a hook as well.
[2971.50 --> 2972.26]  So it kind of behaves
[2972.26 --> 2972.78]  like a hook,
[2973.06 --> 2973.98]  but it's not a hook.
[2975.02 --> 2976.44]  And because it's not a hook,
[2976.50 --> 2977.36]  it doesn't follow
[2977.36 --> 2979.12]  the same rules of hook.
[2979.76 --> 2981.02]  So, yeah.
[2981.78 --> 2984.24]  So I have not dug into use,
[2984.34 --> 2985.56]  so I'm like live
[2985.56 --> 2986.40]  exploring this now.
[2986.40 --> 2987.26]  So if I'm understanding
[2987.26 --> 2987.68]  correctly,
[2987.68 --> 2988.56]  it's a way to sort of
[2988.56 --> 2990.26]  pull in context
[2990.26 --> 2991.94]  without having to be
[2991.94 --> 2994.06]  in a nested component tree.
[2994.48 --> 2995.30]  So you can sort of
[2995.30 --> 2996.24]  compose context
[2996.24 --> 2996.82]  in different ways
[2996.82 --> 2997.44]  rather than having
[2997.44 --> 2998.64]  to be purely hierarchical.
[2999.02 --> 2999.38]  Correct.
[2999.70 --> 3001.20]  And it's a way
[3001.20 --> 3002.34]  to read resources,
[3002.72 --> 3003.80]  context being one of them.
[3004.26 --> 3005.52]  So context is an example,
[3005.64 --> 3006.08]  but promises
[3006.08 --> 3007.04]  are also an example.
[3007.50 --> 3008.16]  Promises sent by
[3008.16 --> 3009.26]  like a suspense library
[3009.26 --> 3010.72]  is also an example.
[3010.80 --> 3012.06]  So could it replace
[3012.06 --> 3013.86]  something like a React query?
[3014.54 --> 3016.86]  I think React query...
[3016.86 --> 3017.52]  For at least
[3017.52 --> 3018.26]  simple use cases.
[3018.26 --> 3019.10]  Yes, yes.
[3019.24 --> 3020.42]  I think for a simple use case
[3020.42 --> 3022.98]  like reading a context
[3022.98 --> 3024.40]  or like reading
[3024.40 --> 3025.86]  like a suspend rendered promise,
[3026.06 --> 3026.36]  yes.
[3026.96 --> 3027.82]  But React query
[3027.82 --> 3029.16]  does a lot more than that.
[3029.30 --> 3029.50]  Yeah.
[3029.70 --> 3032.30]  So I don't want to say yes,
[3032.68 --> 3033.88]  but yes.
[3036.08 --> 3037.62]  For very simple use cases,
[3037.62 --> 3038.10]  I guess.
[3038.72 --> 3038.82]  Yeah.
[3039.04 --> 3039.40]  Well,
[3040.08 --> 3040.82]  coming into it,
[3040.86 --> 3041.40]  it sounds like
[3041.40 --> 3042.94]  you can sort of put it
[3042.94 --> 3043.84]  in line in your component
[3043.84 --> 3045.02]  but it's going to deal
[3045.02 --> 3046.86]  with an asynchronous thing.
[3046.96 --> 3047.30]  Exactly.
[3047.66 --> 3048.12]  And make,
[3048.24 --> 3048.94]  you know,
[3049.18 --> 3049.88]  React rendering
[3049.88 --> 3051.14]  work all nicely with that
[3051.14 --> 3052.48]  rather than having to embed that
[3052.48 --> 3053.50]  into like a use effect
[3053.50 --> 3054.16]  or a callback
[3054.16 --> 3055.14]  or something like that.
[3055.24 --> 3055.38]  Yeah.
[3055.84 --> 3056.56]  So use is,
[3056.72 --> 3057.96]  because it's like an API itself,
[3058.04 --> 3058.66]  you can have it
[3058.66 --> 3060.72]  within your component itself.
[3060.80 --> 3061.60]  You don't need to embed it
[3061.60 --> 3062.38]  within another hook.
[3063.10 --> 3064.14]  And because it's not a hook,
[3064.18 --> 3065.38]  you can also call it conditionally.
[3065.42 --> 3066.04]  So you can have like
[3066.04 --> 3067.00]  multiple hooks at the top
[3067.00 --> 3067.78]  and then you can have,
[3068.12 --> 3068.98]  because it's an API,
[3069.12 --> 3069.64]  it's not a hook,
[3069.68 --> 3070.20]  you can have it
[3070.20 --> 3071.00]  at the bottom somewhere
[3071.00 --> 3072.02]  in the component as well.
[3072.12 --> 3073.20]  So you don't need
[3073.20 --> 3074.18]  to have it at the very top.
[3075.36 --> 3075.82]  Interesting.
[3076.10 --> 3076.76]  So in some way,
[3076.86 --> 3078.32]  I'm now speculating,
[3078.50 --> 3079.58]  but does it kind of,
[3080.16 --> 3081.50]  it hooks into the,
[3081.88 --> 3083.16]  see what I did there?
[3083.38 --> 3085.30]  It hooks into the rendering path.
[3085.48 --> 3085.64]  Yes.
[3085.70 --> 3086.30]  Right, so that
[3086.30 --> 3088.20]  your React component rendering
[3088.20 --> 3089.04]  may be suspended
[3089.04 --> 3090.28]  as it waits for this thing
[3090.28 --> 3090.84]  or it's going to do
[3090.84 --> 3091.46]  a placeholder
[3091.46 --> 3092.52]  or something like that.
[3092.72 --> 3093.30]  I don't know
[3093.30 --> 3094.02]  the inner workings
[3094.02 --> 3094.64]  of use API,
[3094.76 --> 3095.20]  to be honest,
[3095.24 --> 3095.86]  so I can't say
[3095.86 --> 3096.80]  if it actually suspends
[3096.80 --> 3097.80]  the rendering path.
[3098.22 --> 3099.04]  But because it's waiting
[3099.04 --> 3100.34]  for an async promise
[3100.34 --> 3100.90]  to come back,
[3100.96 --> 3101.76]  I want to say yes,
[3102.06 --> 3103.54]  but I am not sure
[3103.54 --> 3104.58]  how it works
[3104.58 --> 3105.02]  in the background,
[3105.14 --> 3106.66]  so I don't know.
[3107.08 --> 3108.04]  What happens
[3108.04 --> 3108.98]  on your screen
[3108.98 --> 3109.58]  while you're waiting
[3109.58 --> 3110.18]  for that resource
[3110.18 --> 3110.76]  to come back?
[3110.92 --> 3111.40]  I don't know.
[3111.56 --> 3112.10]  Good question.
[3112.68 --> 3112.88]  I mean,
[3112.88 --> 3113.70]  it's a context promise
[3113.70 --> 3114.26]  is what I've,
[3114.34 --> 3115.00]  it's a context
[3115.00 --> 3115.70]  what I've checked
[3115.70 --> 3118.18]  and I haven't really seen
[3118.18 --> 3119.26]  any loader screen
[3119.26 --> 3120.16]  or anything like that.
[3120.32 --> 3121.30]  It's been pretty instantaneous.
[3121.96 --> 3122.46]  I don't know.
[3122.68 --> 3123.42]  That's a good question.
[3124.16 --> 3125.50]  Speaking of loader screens,
[3125.50 --> 3125.84]  I think,
[3126.68 --> 3127.08]  no,
[3127.16 --> 3127.94]  I'm still trying
[3127.94 --> 3128.72]  to remember exactly
[3128.72 --> 3129.90]  what was in React 19,
[3130.02 --> 3130.40]  but there was
[3130.40 --> 3131.34]  some sort of drama
[3131.34 --> 3133.14]  around something
[3133.14 --> 3134.02]  related to suspense
[3134.02 --> 3135.46]  or things around that.
[3135.54 --> 3135.98]  Where did that
[3135.98 --> 3136.82]  end up falling out?
[3137.18 --> 3137.48]  Yes,
[3137.56 --> 3139.06]  there was concerns
[3139.06 --> 3140.04]  about suspense
[3140.04 --> 3142.06]  kind of basically
[3142.06 --> 3144.22]  breaking the way
[3144.22 --> 3145.30]  it works right now.
[3145.84 --> 3146.68]  So basically,
[3146.68 --> 3147.22]  what happened
[3147.22 --> 3149.18]  is that suspense components,
[3149.34 --> 3149.82]  if you have like
[3149.82 --> 3150.66]  four different components
[3150.66 --> 3151.52]  in a suspend boundary,
[3151.92 --> 3152.52]  they would all
[3152.52 --> 3153.38]  kind of resolve
[3153.38 --> 3154.78]  and then they would
[3154.78 --> 3155.40]  all kind of resolve
[3155.40 --> 3157.00]  in async pattern,
[3157.14 --> 3157.58]  so they would all
[3157.58 --> 3158.48]  resolve at their own time.
[3158.96 --> 3159.24]  However,
[3159.48 --> 3161.12]  with React 19,
[3161.26 --> 3161.88]  what was happening,
[3162.06 --> 3162.68]  and I think this was
[3162.68 --> 3163.50]  because of the compiler,
[3163.92 --> 3164.58]  if I'm not wrong,
[3165.10 --> 3166.42]  this was actually causing
[3166.42 --> 3167.26]  React,
[3167.82 --> 3169.00]  this was also causing
[3169.00 --> 3170.20]  suspense to kind of
[3170.20 --> 3171.34]  act as a waterfall.
[3171.64 --> 3172.18]  So if you have
[3172.18 --> 3172.90]  like four components,
[3173.24 --> 3173.96]  the first would finish
[3173.96 --> 3174.38]  and the second
[3174.38 --> 3174.76]  and the third
[3174.76 --> 3175.24]  and the fourth,
[3175.52 --> 3175.94]  and so it was
[3175.94 --> 3177.08]  taking incredibly long.
[3177.76 --> 3178.44]  This PR has now
[3178.44 --> 3179.00]  been reverted,
[3179.20 --> 3179.84]  so it's no longer
[3179.84 --> 3181.56]  part of like React 19
[3181.56 --> 3181.92]  anymore,
[3182.12 --> 3183.18]  so that problem
[3183.18 --> 3183.96]  has been fixed
[3183.96 --> 3185.84]  or reverted back.
[3186.66 --> 3188.62]  So kind of a rough
[3188.62 --> 3189.48]  transition into
[3189.48 --> 3190.24]  another topic,
[3190.62 --> 3191.86]  but we've been
[3191.86 --> 3192.40]  talking a lot
[3192.40 --> 3193.04]  about AI.
[3193.48 --> 3194.54]  We've heard a lot
[3194.54 --> 3195.38]  about it at this conference,
[3195.46 --> 3195.90]  we've seen a lot
[3195.90 --> 3197.28]  of great examples,
[3197.70 --> 3199.08]  and we've been
[3199.08 --> 3200.76]  discussing with other
[3200.76 --> 3201.48]  folks about like
[3201.48 --> 3202.40]  learning and,
[3202.46 --> 3202.92]  you know,
[3202.96 --> 3203.56]  coming up to speed
[3203.56 --> 3205.20]  with AI and the world
[3205.20 --> 3205.56]  now,
[3205.70 --> 3206.56]  and I'm just curious,
[3206.70 --> 3207.38]  like since we've been
[3207.38 --> 3208.06]  talking about these
[3208.06 --> 3209.00]  brand new features
[3209.00 --> 3209.84]  of React 19,
[3210.68 --> 3212.32]  and like for React 19
[3212.32 --> 3213.44]  and for other frameworks
[3213.44 --> 3214.42]  as they evolve
[3214.42 --> 3215.30]  and come out
[3215.30 --> 3215.84]  with new features,
[3216.10 --> 3217.34]  do you see their adoption
[3217.34 --> 3218.02]  being delayed
[3218.02 --> 3219.88]  because LLMs might not
[3219.88 --> 3221.16]  know about the features
[3221.16 --> 3221.76]  in React 19
[3221.76 --> 3222.32]  for a little bit?
[3223.02 --> 3223.82]  Short answer,
[3223.90 --> 3224.08]  no.
[3225.96 --> 3226.88]  Long answer.
[3227.92 --> 3229.12]  Let me put it this way.
[3229.74 --> 3231.16]  I think the people
[3231.16 --> 3233.54]  who are using LLMs
[3233.54 --> 3234.46]  have a different
[3234.46 --> 3235.84]  use case in mind
[3235.84 --> 3237.02]  as compared
[3237.02 --> 3237.70]  to the people
[3237.70 --> 3238.70]  who are adopting
[3238.70 --> 3239.46]  these features.
[3240.46 --> 3241.80]  So I'm guessing
[3241.80 --> 3242.46]  when you're thinking
[3242.46 --> 3242.98]  of LLMs,
[3243.06 --> 3243.60]  you're thinking of
[3243.60 --> 3245.26]  tools like Cursor AI,
[3245.68 --> 3246.20]  you're thinking of
[3246.20 --> 3247.56]  tools like Copilot.
[3247.78 --> 3248.74]  We're just asking
[3248.74 --> 3249.68]  ChatGPT, like,
[3249.74 --> 3250.48]  hey, how do I use
[3250.48 --> 3251.18]  the use hook?
[3251.34 --> 3251.62]  Yeah.
[3251.86 --> 3253.86]  So I inherently
[3253.86 --> 3255.64]  don't trust these tools
[3255.64 --> 3256.66]  to kind of give you
[3256.66 --> 3258.38]  the best optimized way
[3258.38 --> 3259.72]  of rendering your component,
[3260.30 --> 3261.10]  and I think that's true
[3261.10 --> 3262.46]  for most of these tools.
[3262.74 --> 3263.50]  They are a good
[3263.50 --> 3265.08]  starting point to,
[3265.92 --> 3266.74]  especially with Cursor,
[3266.78 --> 3267.24]  for example.
[3267.24 --> 3268.30]  It's a good starting point
[3268.30 --> 3268.86]  to write out
[3268.86 --> 3269.52]  skeleton code,
[3269.70 --> 3270.42]  and from there
[3270.42 --> 3271.00]  you can optimize
[3271.00 --> 3271.42]  your code,
[3271.50 --> 3272.30]  make it look nice,
[3272.40 --> 3273.36]  make it correct.
[3273.76 --> 3274.30]  Most of the times
[3274.30 --> 3276.22]  as a developer
[3276.22 --> 3276.98]  you have to validate
[3276.98 --> 3277.50]  your code,
[3277.72 --> 3279.54]  and you should
[3279.54 --> 3280.24]  validate your code
[3280.24 --> 3280.84]  if you're getting
[3280.84 --> 3282.02]  any of the code
[3282.02 --> 3283.18]  out of these AI tools.
[3284.06 --> 3284.88]  You need to validate
[3284.88 --> 3286.08]  code coming out of me, too.
[3287.68 --> 3288.12]  Absolutely.
[3288.62 --> 3289.42]  That's why we have
[3289.42 --> 3290.06]  PR reviews.
[3290.58 --> 3290.96]  However,
[3291.32 --> 3292.50]  I think because
[3292.50 --> 3293.36]  it's a starting point,
[3293.42 --> 3294.66]  it's not the final product,
[3294.88 --> 3295.88]  or it's not the final
[3295.88 --> 3296.74]  state of your code.
[3297.20 --> 3297.82]  I don't think
[3297.82 --> 3298.16]  the adoption
[3298.16 --> 3298.82]  will be delayed
[3298.82 --> 3299.42]  because the people
[3299.42 --> 3300.04]  who are building
[3300.04 --> 3301.18]  these components,
[3301.74 --> 3302.38]  when it comes
[3302.38 --> 3303.10]  to optimizations,
[3303.24 --> 3304.02]  they would reach out
[3304.02 --> 3304.88]  to React compiler
[3304.88 --> 3306.34]  or use hooks
[3306.34 --> 3307.18]  and things like that
[3307.18 --> 3308.06]  to optimize
[3308.06 --> 3309.56]  instead of just waiting
[3309.56 --> 3310.70]  on what the AI
[3310.70 --> 3311.44]  has given them,
[3311.70 --> 3313.20]  at least as of now.
[3314.12 --> 3315.24]  So even if React 19
[3315.24 --> 3316.38]  is introduced tomorrow,
[3316.50 --> 3317.30]  I do not feel
[3317.30 --> 3318.06]  that it will actually
[3318.06 --> 3318.60]  delay us.
[3319.26 --> 3319.66]  I agree.
[3319.66 --> 3321.38]  It was a rough transition.
[3323.72 --> 3324.72]  But good question,
[3324.80 --> 3325.10]  actually.
[3326.00 --> 3327.20]  It's on people's minds,
[3327.26 --> 3327.38]  right?
[3327.44 --> 3328.78]  Because that is
[3328.78 --> 3329.76]  kind of now
[3329.76 --> 3330.28]  the first place
[3330.28 --> 3330.98]  I go when I have
[3330.98 --> 3331.34]  questions,
[3331.62 --> 3332.30]  just because I don't
[3332.30 --> 3333.50]  have to add a lot of,
[3334.30 --> 3335.30]  I don't have to think
[3335.30 --> 3335.98]  in terms of how
[3335.98 --> 3336.86]  would I Google for this.
[3336.94 --> 3337.72]  I can just throw
[3337.72 --> 3338.70]  the context that I have
[3338.70 --> 3339.12]  at it,
[3339.40 --> 3340.14]  and it can kind of
[3340.14 --> 3340.90]  figure it out.
[3340.90 --> 3341.98]  Use the information
[3341.98 --> 3342.48]  out of it.
[3342.48 --> 3342.60]  Yeah.
[3343.20 --> 3343.86]  So where did they
[3343.86 --> 3344.84]  have React context
[3344.84 --> 3345.22]  in use?
[3345.54 --> 3346.24]  There we go.
[3347.16 --> 3348.18]  So how are you
[3348.18 --> 3349.74]  using AI in your
[3349.74 --> 3350.48]  coding these days?
[3351.06 --> 3352.38]  I am using it
[3352.38 --> 3353.04]  as a tool.
[3354.88 --> 3355.50]  I mean,
[3355.54 --> 3356.72]  it's perfect for use
[3356.72 --> 3357.72]  because it's really
[3357.72 --> 3358.18]  slow,
[3358.32 --> 3358.78]  so you're going to
[3358.78 --> 3359.52]  have to wrap it,
[3359.58 --> 3359.96]  I promise.
[3360.72 --> 3361.56]  There you go.
[3362.04 --> 3363.30]  I love these puns.
[3363.88 --> 3365.40]  I am using
[3365.40 --> 3367.08]  Cursor AI a lot.
[3367.26 --> 3368.16]  I'm a big fan,
[3368.60 --> 3370.14]  and you feel
[3370.14 --> 3371.08]  so happy about it.
[3371.88 --> 3372.64]  This is our
[3372.64 --> 3373.48]  fourth interview today,
[3373.78 --> 3374.50]  and everybody
[3374.50 --> 3375.34]  has said that.
[3375.50 --> 3375.72]  Really?
[3376.14 --> 3376.78]  He uses it
[3376.78 --> 3377.22]  all the time,
[3377.34 --> 3378.04]  and I am just
[3378.04 --> 3378.66]  sitting here like,
[3378.72 --> 3379.34]  what's Cursor?
[3379.80 --> 3380.28]  Sign up.
[3380.42 --> 3381.04]  Sign up.
[3381.56 --> 3382.52]  There's other tools
[3382.52 --> 3382.98]  as well,
[3383.08 --> 3383.82]  which kind of,
[3383.92 --> 3384.42]  like Augment
[3384.42 --> 3385.10]  is doing the same
[3385.10 --> 3385.48]  thing,
[3386.02 --> 3386.92]  and I think why
[3386.92 --> 3387.70]  I really like it
[3387.70 --> 3388.54]  is because it's
[3388.54 --> 3389.44]  reduced my time
[3389.44 --> 3390.12]  to write code
[3390.12 --> 3390.70]  so much.
[3390.82 --> 3391.68]  I think I just
[3391.68 --> 3392.30]  posted like two
[3392.30 --> 3392.70]  days ago.
[3392.86 --> 3393.44]  I was building
[3393.44 --> 3394.38]  a side project,
[3394.86 --> 3395.52]  and typically
[3395.52 --> 3396.14]  that kind of stuff
[3396.14 --> 3396.58]  would take me
[3396.58 --> 3396.98]  like a week
[3396.98 --> 3397.50]  to ship out,
[3397.60 --> 3398.08]  but with the help
[3398.08 --> 3398.54]  of Cursor,
[3398.58 --> 3399.04]  I was able to
[3399.04 --> 3399.92]  get something up
[3399.92 --> 3400.24]  and running
[3400.24 --> 3400.92]  within two days
[3400.92 --> 3402.94]  and even bring it
[3402.94 --> 3403.62]  to a demo-able
[3403.62 --> 3403.92]  state,
[3404.04 --> 3404.70]  and that is so
[3404.70 --> 3405.08]  awesome,
[3405.20 --> 3406.18]  just having the
[3406.18 --> 3407.20]  ability to quickly
[3407.20 --> 3408.02]  refactor your code
[3408.02 --> 3408.36]  out,
[3408.68 --> 3409.24]  tell the chat
[3409.24 --> 3409.54]  command,
[3409.72 --> 3409.78]  like,
[3409.82 --> 3409.90]  hey,
[3409.94 --> 3410.52]  I'm getting this
[3410.52 --> 3410.74]  bug,
[3410.80 --> 3411.36]  this is the bug.
[3411.56 --> 3412.06]  This is something
[3412.06 --> 3412.48]  that you would
[3412.48 --> 3413.10]  typically do with
[3413.10 --> 3414.20]  chat GPT before,
[3414.40 --> 3415.32]  but now having
[3415.32 --> 3416.04]  this code tool
[3416.04 --> 3416.28]  to,
[3416.52 --> 3416.64]  like,
[3416.76 --> 3417.80]  which is right
[3417.80 --> 3418.06]  there,
[3418.12 --> 3418.64]  it has all the
[3418.64 --> 3419.04]  context,
[3419.36 --> 3419.84]  I think it's,
[3419.92 --> 3420.06]  like,
[3420.12 --> 3420.76]  increased my
[3420.76 --> 3421.44]  performance a lot
[3421.44 --> 3421.68]  more.
[3422.26 --> 3422.48]  Yeah,
[3422.60 --> 3423.14]  that makes sense.
[3423.48 --> 3423.90]  I just wish
[3423.90 --> 3424.26]  they would have
[3424.26 --> 3425.08]  worked NeoVim
[3425.08 --> 3425.54]  rather than
[3425.54 --> 3426.00]  VietzCode.
[3426.00 --> 3429.58]  So,
[3429.94 --> 3430.98]  we aren't at
[3430.98 --> 3431.96]  CursorConf.
[3432.14 --> 3432.34]  No.
[3432.68 --> 3433.44]  As much as it
[3433.44 --> 3433.94]  seems like we
[3433.94 --> 3434.38]  might be,
[3434.48 --> 3434.98]  we are at
[3434.98 --> 3435.78]  ReactConf.
[3435.88 --> 3436.22]  I'm kind of
[3436.22 --> 3436.56]  curious,
[3436.72 --> 3437.08]  how has your
[3437.08 --> 3437.54]  experience of
[3437.54 --> 3438.00]  the conference
[3438.00 --> 3438.30]  been,
[3438.46 --> 3439.56]  what is it
[3439.56 --> 3440.08]  like for you
[3440.08 --> 3440.44]  coming to
[3440.44 --> 3440.82]  something like
[3440.82 --> 3441.04]  this?
[3441.34 --> 3441.66]  Yeah,
[3441.94 --> 3443.12]  it has been a
[3443.12 --> 3443.86]  really wonderful
[3443.86 --> 3444.44]  experience.
[3445.10 --> 3445.76]  I think the
[3445.76 --> 3446.30]  conference,
[3447.02 --> 3448.26]  the audience
[3448.26 --> 3449.00]  has been really
[3449.00 --> 3450.08]  receptive to the
[3450.08 --> 3450.74]  new features of
[3450.74 --> 3451.36]  React 19.
[3452.02 --> 3452.82]  I feel like
[3452.82 --> 3453.48]  when you kind
[3453.48 --> 3453.66]  of,
[3453.92 --> 3454.46]  when there's a
[3454.46 --> 3454.80]  new feature
[3454.80 --> 3455.32]  comes out,
[3455.40 --> 3455.70]  when there's a
[3455.70 --> 3456.06]  new version
[3456.06 --> 3456.50]  comes out,
[3456.56 --> 3457.08]  people have a
[3457.08 --> 3457.38]  lot of
[3457.38 --> 3458.10]  resistance to
[3458.10 --> 3458.30]  it.
[3458.82 --> 3459.88]  But I've seen
[3459.88 --> 3460.40]  a lot of
[3460.40 --> 3461.42]  excitement in
[3461.42 --> 3461.98]  the audience
[3461.98 --> 3462.66]  members about
[3462.66 --> 3462.98]  the new
[3462.98 --> 3463.48]  features.
[3464.24 --> 3464.80]  All of the
[3464.80 --> 3465.20]  talks have
[3465.20 --> 3465.74]  been amazing,
[3465.90 --> 3466.40]  so I've had
[3466.40 --> 3466.90]  a really great
[3466.90 --> 3467.24]  time.
[3467.60 --> 3467.98]  I think one
[3467.98 --> 3468.34]  of the best
[3468.34 --> 3469.32]  features or
[3469.32 --> 3469.66]  one of the
[3469.66 --> 3470.04]  best things
[3470.04 --> 3470.48]  about coming
[3470.48 --> 3471.02]  to a conference
[3471.02 --> 3471.60]  is being able
[3471.60 --> 3472.02]  to talk to
[3472.02 --> 3472.86]  people one-on-one
[3472.86 --> 3474.00]  and hanging
[3474.00 --> 3474.44]  out with your
[3474.44 --> 3474.94]  friends, but
[3474.94 --> 3475.70]  also like meeting
[3475.70 --> 3476.30]  new people,
[3476.48 --> 3477.26]  which I feel
[3477.26 --> 3478.42]  like this
[3478.42 --> 3479.04]  conference has
[3479.04 --> 3479.42]  been really
[3479.42 --> 3479.84]  great at
[3479.84 --> 3480.14]  because I've
[3480.14 --> 3480.66]  met so many
[3480.66 --> 3481.34]  amazing people.
[3482.00 --> 3482.42]  So,
[3482.56 --> 3483.34]  very positive
[3483.34 --> 3483.90]  experience.
[3483.90 --> 3484.58]  It's been
[3484.58 --> 3485.00]  wonderful.
[3485.56 --> 3486.28]  And having
[3486.28 --> 3486.76]  this kind of
[3486.76 --> 3487.14]  backdrop.
[3487.58 --> 3487.94]  I know,
[3488.00 --> 3488.18]  right?
[3488.94 --> 3489.54]  Where else
[3489.54 --> 3489.90]  can you get
[3489.90 --> 3490.10]  that?
[3490.74 --> 3491.04]  So you
[3491.04 --> 3491.28]  mentioned
[3491.28 --> 3491.78]  meeting new
[3491.78 --> 3492.16]  people, and
[3492.16 --> 3492.52]  I think one
[3492.52 --> 3493.34]  of the fun
[3493.34 --> 3494.04]  things is we've
[3494.04 --> 3495.20]  met both very
[3495.20 --> 3496.02]  experienced people
[3496.02 --> 3497.30]  and some folks
[3497.30 --> 3497.68]  who are like
[3497.68 --> 3498.54]  brand new to
[3498.54 --> 3499.28]  JavaScript, and
[3499.28 --> 3499.76]  they're kind of
[3499.76 --> 3500.42]  all here.
[3500.58 --> 3501.30]  And I know one
[3501.30 --> 3502.04]  of your interests
[3502.04 --> 3502.94]  is around how
[3502.94 --> 3503.66]  you kind of help
[3503.66 --> 3504.30]  these people who
[3504.30 --> 3506.06]  are newer to
[3506.06 --> 3506.26]  JavaScript.
[3506.28 --> 3506.68]  I won't say
[3506.68 --> 3507.56]  necessarily new
[3507.56 --> 3508.26]  to coding, but
[3508.26 --> 3509.04]  newer to JavaScript
[3509.04 --> 3510.38]  or newer to the
[3510.38 --> 3511.06]  tech industry and
[3511.06 --> 3511.68]  help them bring
[3511.68 --> 3512.06]  along.
[3512.06 --> 3513.24]  So I'm curious
[3513.24 --> 3513.94]  how you think
[3513.94 --> 3515.36]  about that
[3515.36 --> 3516.34]  community building
[3516.34 --> 3517.60]  and mentorship
[3517.60 --> 3518.74]  aspect of things.
[3518.90 --> 3519.12]  Yeah.
[3519.64 --> 3520.80]  I feel like when
[3520.80 --> 3521.84]  we are going
[3521.84 --> 3522.30]  through a hard
[3522.30 --> 3522.96]  time, we often
[3522.96 --> 3523.64]  feel like we're
[3523.64 --> 3524.44]  kind of alone in
[3524.44 --> 3526.02]  this, and nobody
[3526.02 --> 3527.54]  else is going
[3527.54 --> 3528.06]  through the same
[3528.06 --> 3528.70]  stuff that we're
[3528.70 --> 3529.36]  going, and we're
[3529.36 --> 3530.44]  probably like an
[3530.44 --> 3531.62]  imposter, we're not
[3531.62 --> 3533.04]  well suited to be
[3533.04 --> 3533.76]  here, and everybody
[3533.76 --> 3534.50]  else is amazing.
[3535.00 --> 3535.68]  And I think one of
[3535.68 --> 3536.32]  the things that I've
[3536.32 --> 3537.08]  been doing a lot
[3537.08 --> 3537.76]  with the fireside
[3537.76 --> 3538.62]  chats that I host
[3538.62 --> 3540.12]  is bringing people
[3540.12 --> 3540.80]  from the community
[3540.80 --> 3541.84]  and talking to
[3541.84 --> 3542.28]  them about the
[3542.28 --> 3542.84]  challenges that
[3542.84 --> 3543.74]  they've been facing
[3543.74 --> 3544.58]  as well, but also
[3544.58 --> 3545.50]  sharing this kind
[3545.50 --> 3546.62]  of vulnerable side
[3546.62 --> 3547.92]  of people who
[3547.92 --> 3549.56]  usually are put on
[3549.56 --> 3550.72]  pedestals and
[3550.72 --> 3551.58]  showing people that
[3551.58 --> 3552.18]  there is a human
[3552.18 --> 3552.98]  side to everybody,
[3553.08 --> 3553.58]  and everybody's
[3553.58 --> 3554.12]  kind of been going
[3554.12 --> 3554.72]  through challenges
[3554.72 --> 3555.24]  themselves.
[3555.96 --> 3556.36]  So kind of
[3556.36 --> 3557.30]  showing, I feel
[3557.30 --> 3558.64]  like people are,
[3559.04 --> 3559.94]  when we go through
[3559.94 --> 3560.68]  our struggles, we
[3560.68 --> 3561.50]  often look at these
[3561.50 --> 3563.12]  awesome people who
[3563.12 --> 3563.86]  have so much
[3563.86 --> 3564.56]  experience, and we
[3564.56 --> 3565.44]  think like, oh,
[3565.48 --> 3566.92]  they've always been
[3566.92 --> 3567.42]  successful.
[3567.42 --> 3568.26]  there's no way
[3568.26 --> 3568.84]  that they feel
[3568.84 --> 3569.54]  like an imposter.
[3569.92 --> 3570.38]  But then when you
[3570.38 --> 3572.00]  talk to folks, and
[3572.00 --> 3573.92]  you realize that they
[3573.92 --> 3574.66]  feel like that pretty
[3574.66 --> 3575.82]  much every day, every
[3575.82 --> 3577.48]  week, I think that's
[3577.48 --> 3578.38]  really like a humbling
[3578.38 --> 3579.76]  experience and an
[3579.76 --> 3580.62]  eye-opening moment.
[3580.86 --> 3582.24]  I felt, so for my
[3582.24 --> 3583.48]  experience, or like
[3583.48 --> 3585.00]  for my mentorship
[3585.00 --> 3586.16]  experience, I've always
[3586.16 --> 3587.10]  tried to be like that
[3587.10 --> 3589.46]  empathetic coach and
[3589.46 --> 3590.28]  telling people that
[3590.28 --> 3591.84]  you're not alone, and
[3591.84 --> 3592.88]  if you're facing a
[3592.88 --> 3593.94]  problem today, most
[3593.94 --> 3595.24]  likely it's true that
[3595.24 --> 3596.66]  somebody else is facing
[3596.66 --> 3597.74]  the same problem as
[3597.74 --> 3598.54]  well, so you're not
[3598.54 --> 3599.70]  alone, no matter what
[3599.70 --> 3600.28]  you're going through.
[3600.80 --> 3602.02]  Yeah, I love that.
[3602.32 --> 3602.66]  I feel like an
[3602.66 --> 3603.40]  imposter right now.
[3604.76 --> 3605.50]  It's like getting
[3605.50 --> 3606.38]  behind the social
[3606.38 --> 3607.32]  media view of it,
[3607.36 --> 3607.50]  right?
[3607.58 --> 3607.86]  Exactly.
[3607.86 --> 3608.34]  It's like, no,
[3608.42 --> 3609.58]  they're just as
[3609.58 --> 3610.48]  dysfunctional as I am.
[3610.54 --> 3610.86]  Exactly.
[3610.86 --> 3611.34]  You don't want the
[3611.34 --> 3612.58]  Instagram like perfect
[3612.58 --> 3613.22]  thing.
[3613.36 --> 3614.36]  You want to see, oh,
[3614.40 --> 3615.06]  this was actually a
[3615.06 --> 3616.38]  lot of work, or like,
[3616.90 --> 3617.98]  I was really stuck on
[3617.98 --> 3619.04]  this typo for a week.
[3619.04 --> 3619.36]  Exactly.
[3619.60 --> 3620.14]  No idea.
[3620.46 --> 3621.18]  It was one line,
[3621.28 --> 3621.50]  you know.
[3621.56 --> 3622.38]  Yeah, exactly.
[3622.60 --> 3623.26]  You were missing a
[3623.26 --> 3623.74]  semicolon.
[3624.12 --> 3624.72]  You should have asked
[3624.72 --> 3625.08]  a cursor.
[3626.66 --> 3628.16]  After this.
[3628.50 --> 3628.62]  Okay.
[3629.70 --> 3630.58]  Maybe it did not
[3630.58 --> 3631.52]  have the most updated
[3631.52 --> 3632.40]  LLM, so.
[3632.54 --> 3632.76]  Yeah.
[3634.40 --> 3635.14]  But, you know,
[3635.24 --> 3636.08]  like you were
[3636.08 --> 3636.82]  talking about this,
[3637.14 --> 3638.36]  you feel like you're
[3638.36 --> 3639.20]  stuck on this one line
[3639.20 --> 3640.04]  of code for so long,
[3640.08 --> 3640.56]  and you feel like,
[3640.62 --> 3641.54]  oh, my God, I'm so
[3641.54 --> 3641.86]  stupid.
[3642.08 --> 3642.84]  But then when you talk
[3642.84 --> 3643.90]  to, like, your staff
[3643.90 --> 3644.64]  engineer, and they're
[3644.64 --> 3645.90]  like, oh, yeah, I
[3645.90 --> 3646.76]  couldn't finish that
[3646.76 --> 3647.78]  feature for, like, two
[3647.78 --> 3648.58]  weeks because I was
[3648.58 --> 3649.48]  stuck on that one line
[3649.48 --> 3649.84]  of code.
[3649.88 --> 3650.92]  You're like, what?
[3651.32 --> 3651.74]  You never do?
[3651.74 --> 3652.56]  We are so stupid.
[3652.56 --> 3653.36]  Yeah, exactly.
[3653.36 --> 3654.14]  Yeah, exactly.
[3654.34 --> 3655.06]  You'd be like, what?
[3655.18 --> 3656.04]  That happens with you,
[3656.16 --> 3656.32]  too?
[3656.40 --> 3656.64]  Yeah.
[3657.80 --> 3659.00]  Yeah, I would wager
[3659.00 --> 3659.82]  there's not a single
[3659.82 --> 3660.72]  developer out there
[3660.72 --> 3662.08]  who has not felt stupid
[3662.08 --> 3663.32]  about their code.
[3663.48 --> 3663.88]  Exactly.
[3664.02 --> 3664.24]  Oh, yeah.
[3664.90 --> 3665.34]  Exactly.
[3665.48 --> 3666.58]  We are not our code.
[3666.80 --> 3667.72]  We are much more
[3667.72 --> 3668.16]  than that.
[3668.64 --> 3669.48]  Yeah, for sure.
[3671.28 --> 3672.24]  We're not the code
[3672.24 --> 3672.66]  we write.
[3673.02 --> 3674.10]  Or the code we prompt
[3674.10 --> 3675.06]  the LLM to write.
[3675.22 --> 3675.56]  Yes.
[3675.56 --> 3679.82]  Oh, dear.
[3680.18 --> 3681.46]  So what brings you to,
[3681.74 --> 3682.56]  like, what keeps you
[3682.56 --> 3683.54]  coming to conferences?
[3684.10 --> 3685.30]  Is it the people,
[3685.44 --> 3686.06]  the connections?
[3686.52 --> 3687.48]  What is it specifically?
[3687.98 --> 3688.94]  I think one thing that
[3688.94 --> 3689.66]  I really like about
[3689.66 --> 3690.84]  conferences is that it
[3690.84 --> 3691.78]  kind of gives me a
[3691.78 --> 3692.82]  deadline to learn
[3692.82 --> 3693.30]  something.
[3694.06 --> 3694.74]  Conference-driven
[3694.74 --> 3695.14]  development.
[3695.14 --> 3695.70]  Conference-driven
[3695.70 --> 3696.06]  development.
[3696.44 --> 3696.62]  Exactly.
[3697.84 --> 3698.58]  I'm glad I'm not
[3698.58 --> 3698.84]  alone.
[3699.56 --> 3700.00]  Exactly.
[3700.88 --> 3702.38]  Like, today I was
[3702.38 --> 3703.02]  giving a talk about
[3703.02 --> 3703.64]  React 19.
[3704.12 --> 3704.80]  I've given this talk
[3704.80 --> 3705.54]  before, but I'm
[3705.54 --> 3706.14]  but something
[3706.14 --> 3707.12]  different that I did
[3707.12 --> 3708.94]  in this talk added a
[3708.94 --> 3710.06]  bit more context about
[3710.06 --> 3710.96]  React compiler.
[3711.44 --> 3712.50]  And so that encouraged
[3712.50 --> 3713.62]  me to learn about it,
[3713.70 --> 3714.78]  understand it, and share
[3714.78 --> 3715.40]  it with the world.
[3715.76 --> 3716.68]  And I think that really
[3716.68 --> 3717.90]  helps me stay up to date
[3717.90 --> 3718.80]  with, like, React,
[3719.04 --> 3719.64]  with community,
[3719.82 --> 3720.50]  front-end, whatever.
[3721.08 --> 3722.14]  So I really like that.
[3722.24 --> 3723.90]  It helps me still be
[3723.90 --> 3726.42]  active and still enjoy
[3726.42 --> 3727.64]  my job, my, like,
[3727.88 --> 3729.26]  full-time job, and not
[3729.26 --> 3730.24]  feel like I'm in a rut
[3730.24 --> 3731.10]  and just, like, moving
[3731.10 --> 3732.68]  boxes every day on the
[3732.68 --> 3732.98]  screen.
[3733.16 --> 3734.24]  So I'm actually doing
[3734.24 --> 3735.06]  something worthwhile.
[3735.06 --> 3736.80]  And I think, like,
[3736.86 --> 3737.74]  sharing something with
[3737.74 --> 3739.06]  the world and people
[3739.06 --> 3740.14]  coming back and saying,
[3740.28 --> 3740.96]  like, oh, what I shared
[3740.96 --> 3741.78]  was really helpful and
[3741.78 --> 3742.52]  they learned something
[3742.52 --> 3743.64]  new, I think that is
[3743.64 --> 3744.22]  really rewarding.
[3744.96 --> 3746.78]  On the note of staying
[3746.78 --> 3747.90]  motivated in your job,
[3748.08 --> 3749.14]  what are the technical
[3749.14 --> 3749.98]  things that are really
[3749.98 --> 3751.28]  exciting for you right now?
[3751.98 --> 3753.36]  At my job or outside of
[3753.36 --> 3753.74]  my job?
[3754.16 --> 3754.76]  Your call?
[3755.22 --> 3755.42]  Hmm.
[3755.42 --> 3756.96]  So one of the things that
[3756.96 --> 3758.54]  I'm working at Slack is
[3758.54 --> 3759.66]  building a component
[3759.66 --> 3761.44]  library, not library,
[3761.56 --> 3763.04]  building a component that
[3763.04 --> 3764.74]  can be used all across
[3764.74 --> 3765.10]  Slack.
[3765.18 --> 3766.02]  So I work in the design
[3766.02 --> 3767.58]  systems team of Slack and
[3767.58 --> 3768.68]  specifically focusing on
[3768.68 --> 3769.16]  accessibility.
[3770.16 --> 3771.06]  Accessibility is something
[3771.06 --> 3772.30]  that I had not worked on
[3772.30 --> 3773.38]  before and I have been in
[3773.38 --> 3774.22]  the industry for, like, a
[3774.22 --> 3774.50]  decade.
[3775.18 --> 3776.64]  And now at this point,
[3776.74 --> 3777.20]  learning about
[3777.20 --> 3778.38]  accessibility and what it
[3778.38 --> 3778.96]  takes to build an
[3778.96 --> 3779.92]  accessible component from
[3779.92 --> 3781.38]  the get-go itself is such
[3781.38 --> 3783.02]  an eye-opening moment.
[3783.10 --> 3783.96]  I feel like there's so
[3783.96 --> 3785.00]  much that goes behind
[3785.00 --> 3785.78]  building an accessible
[3785.78 --> 3786.30]  component.
[3786.72 --> 3787.64]  And I think it has really
[3787.64 --> 3788.52]  made me a much better
[3788.52 --> 3789.94]  developer because now I'm
[3789.94 --> 3790.62]  thinking about this
[3790.62 --> 3791.72]  component needs to be
[3791.72 --> 3792.86]  accessible from, like, a
[3792.86 --> 3794.68]  visual standpoint, from a
[3794.68 --> 3795.80]  physical standpoint.
[3796.30 --> 3797.36]  People with screen readers
[3797.36 --> 3798.42]  need to be able to use it.
[3798.50 --> 3799.22]  People with keyboards
[3799.22 --> 3800.50]  must be able to use it.
[3800.80 --> 3801.44]  There are people who are
[3801.44 --> 3802.50]  using assistive technology
[3802.50 --> 3803.56]  who must be able to use it.
[3803.82 --> 3804.86]  So I feel like I'm finally
[3804.86 --> 3805.80]  able to use, like, my
[3805.80 --> 3808.12]  technical skills to actually
[3808.12 --> 3809.28]  make somebody's day-to-day
[3809.28 --> 3810.06]  life better.
[3810.44 --> 3811.36]  And that really excites
[3811.38 --> 3811.56]  me.
[3812.14 --> 3812.28]  Yeah.
[3812.42 --> 3813.42]  I love that, too.
[3813.46 --> 3814.32]  And I love, like, the
[3814.32 --> 3815.82]  vulnerability in saying,
[3815.92 --> 3817.06]  like, you know, I've worked
[3817.06 --> 3818.14]  in an industry for 10 years
[3818.14 --> 3818.88]  and really haven't looked
[3818.88 --> 3819.54]  into this much.
[3819.54 --> 3819.68]  Yeah.
[3820.10 --> 3820.86]  It just, like, goes to
[3820.86 --> 3822.74]  show, like, how broad
[3822.74 --> 3824.90]  this field can be, even
[3824.90 --> 3825.58]  when you're just, like,
[3825.62 --> 3826.52]  working on, you know,
[3826.54 --> 3827.86]  specific front-end pieces.
[3828.02 --> 3828.30]  Yeah.
[3828.46 --> 3829.90]  And, like, you really
[3829.90 --> 3831.72]  don't truly dig into
[3831.72 --> 3832.42]  something until you
[3832.42 --> 3833.34]  actually have to.
[3833.44 --> 3834.06]  Because there's so many
[3834.06 --> 3834.60]  things to learn.
[3834.68 --> 3835.32]  There's so much to them.
[3835.32 --> 3835.72]  You have to focus.
[3835.90 --> 3837.00]  And, like, thank you for
[3837.00 --> 3837.94]  sharing that because I feel
[3837.94 --> 3838.66]  the same way and I'm
[3838.66 --> 3839.58]  always, like, you know,
[3839.62 --> 3841.36]  I'm pretty well in
[3841.38 --> 3842.24]  my career and I haven't
[3842.24 --> 3843.34]  done, you know, this and
[3843.34 --> 3843.74]  this.
[3844.02 --> 3845.46]  And it's just because it
[3845.46 --> 3846.54]  has never come up in
[3846.54 --> 3847.56]  specific scenarios.
[3847.80 --> 3848.18]  Absolutely.
[3848.68 --> 3849.78]  And I kind of touched
[3849.78 --> 3850.96]  accessibility in my first
[3850.96 --> 3851.80]  year of development.
[3852.26 --> 3853.32]  But what I'm doing at
[3853.32 --> 3855.08]  Slack right now versus
[3855.08 --> 3856.02]  what I was doing back
[3856.02 --> 3857.10]  then, I think it's so
[3857.10 --> 3857.92]  vastly different.
[3858.48 --> 3859.28]  And the world of
[3859.28 --> 3860.14]  accessibility can be
[3860.14 --> 3861.22]  really complex as well.
[3861.48 --> 3862.54]  And until you, you're
[3862.54 --> 3863.18]  right, like, until you
[3863.18 --> 3863.96]  actually work on
[3863.96 --> 3864.74]  something, you don't
[3864.74 --> 3866.12]  really understand it
[3866.12 --> 3866.38]  fully.
[3866.38 --> 3867.88]  And I think we just have
[3867.88 --> 3868.58]  to, like, cut ourselves
[3868.58 --> 3869.48]  a little bit of slack.
[3873.74 --> 3875.34]  You know, the world of
[3875.34 --> 3876.18]  front-end development is
[3876.18 --> 3877.36]  so fast and changing
[3877.36 --> 3878.26]  and it's so vast.
[3878.44 --> 3879.38]  Like, you cannot keep up
[3879.38 --> 3880.34]  with everything and you
[3880.34 --> 3881.48]  will not be an expert on
[3881.48 --> 3881.94]  everything.
[3882.18 --> 3883.34]  So I think just being
[3883.34 --> 3884.62]  okay with that also takes a
[3884.62 --> 3885.24]  lot of strength.
[3885.42 --> 3886.76]  But it's okay to not know
[3886.76 --> 3887.18]  everything.
[3888.24 --> 3889.14]  Well, and if you're doing
[3889.14 --> 3890.40]  it at the design system
[3890.40 --> 3891.92]  layer, most of the
[3891.92 --> 3893.02]  developers that are going to
[3893.02 --> 3894.14]  use that won't even have
[3894.14 --> 3895.36]  to understand all the
[3895.36 --> 3896.44]  different nuances that
[3896.44 --> 3897.46]  have gone into making it
[3897.46 --> 3898.56]  accessible, they just pull
[3898.56 --> 3899.14]  in your component.
[3899.42 --> 3899.80]  Exactly.
[3900.02 --> 3900.78]  And that's the goal.
[3900.86 --> 3901.66]  Like, that's my goal.
[3901.96 --> 3902.80]  I want to create a
[3902.80 --> 3903.76]  component that they can just
[3903.76 --> 3904.74]  embed and get those
[3904.74 --> 3905.94]  accessibility powers out
[3905.94 --> 3906.40]  of the back.
[3906.48 --> 3907.18]  They don't have to worry
[3907.18 --> 3907.54]  about it.
[3907.74 --> 3908.44]  As long as they're
[3908.44 --> 3908.96]  providing the right
[3908.96 --> 3909.86]  attributes, this will be
[3909.86 --> 3910.30]  good to go.
[3911.34 --> 3912.60]  Will it be exposed via
[3912.60 --> 3913.44]  the BlockKit UI?
[3913.92 --> 3914.68]  It will not be.
[3915.58 --> 3917.28]  You can use it, but it
[3917.28 --> 3917.90]  won't be exposed.
[3917.98 --> 3918.46]  It's going to be an
[3918.46 --> 3919.18]  internal component.
[3919.52 --> 3919.82]  Oh, dear.
[3920.18 --> 3920.44]  Okay.
[3923.02 --> 3923.98]  Good question, though.
[3925.06 --> 3925.92]  You can tell I've been
[3925.92 --> 3927.12]  doing stuff in the Slack.
[3927.98 --> 3928.26]  Yeah.
[3929.10 --> 3930.20]  I have more questions
[3930.20 --> 3930.70]  for you later.
[3930.90 --> 3931.40]  Yeah, okay.
[3933.22 --> 3934.74]  I'm just curious, kind
[3934.74 --> 3935.84]  of shifting gears again.
[3936.56 --> 3937.28]  Rough transition.
[3938.74 --> 3940.00]  Hey, it's late.
[3940.14 --> 3940.40]  All right.
[3940.56 --> 3941.80]  This is like...
[3941.80 --> 3943.70]  No problem at all.
[3943.84 --> 3944.62]  It's late for me, too.
[3944.68 --> 3946.00]  And we're showing our
[3946.00 --> 3948.08]  internal imposters of just
[3948.08 --> 3948.68]  like, wait.
[3949.52 --> 3950.00]  Okay.
[3951.54 --> 3952.60]  I'm just curious, your
[3952.60 --> 3953.94]  thoughts on TypeScript
[3953.94 --> 3954.68]  versus JavaScript.
[3955.22 --> 3955.62]  Oh.
[3956.28 --> 3957.10]  Pet topic.
[3957.42 --> 3957.62]  Yeah.
[3958.08 --> 3958.76]  Spicy take.
[3960.14 --> 3961.00]  So, okay.
[3961.30 --> 3962.94]  I will be very honest.
[3963.58 --> 3965.20]  Before starting TypeScript,
[3965.64 --> 3966.98]  I was like, I don't need
[3966.98 --> 3967.98]  Java in JavaScript.
[3969.76 --> 3970.28]  Yes.
[3971.04 --> 3972.66]  I think the entire
[3972.66 --> 3974.24]  type thing and tightly
[3974.24 --> 3975.28]  typed, all of that,
[3975.74 --> 3976.90]  kind of pissed me off
[3976.90 --> 3978.40]  about it, especially
[3978.40 --> 3979.52]  because JavaScript is
[3979.52 --> 3980.24]  supposed to be loosely
[3980.24 --> 3980.56]  typed.
[3980.56 --> 3981.54]  And that's what brought
[3981.54 --> 3982.10]  me to JavaScript.
[3982.98 --> 3984.20]  Now, having worked with
[3984.20 --> 3986.14]  TypeScript for around
[3986.14 --> 3987.46]  three years, I'm a big
[3987.46 --> 3988.30]  fan of TypeScript,
[3988.72 --> 3989.60]  especially when I'm
[3989.60 --> 3990.44]  working with people
[3990.44 --> 3991.98]  outside of my team,
[3992.04 --> 3992.96]  when it's just not me.
[3993.02 --> 3993.82]  There's other people as
[3993.82 --> 3994.04]  well.
[3994.32 --> 3995.66]  And the reason being,
[3995.90 --> 3996.84]  TypeScript gives you
[3996.84 --> 3998.12]  contract out of the
[3998.12 --> 3999.16]  bat, so you don't have to
[3999.16 --> 4000.88]  specifically provide it.
[4000.88 --> 4002.42]  And it's become a lot
[4002.42 --> 4005.72]  easier to skip errors that
[4005.72 --> 4006.84]  could have been easily
[4006.84 --> 4008.46]  occurring in your code
[4008.46 --> 4009.48]  base because of even
[4009.48 --> 4010.24]  simple things like
[4010.24 --> 4011.38]  undefined or null.
[4011.78 --> 4012.68]  So it's given that
[4012.68 --> 4013.74]  type safety to you, which
[4013.74 --> 4015.14]  is really helpful,
[4015.40 --> 4016.48]  especially when working
[4016.48 --> 4017.52]  across teams.
[4017.90 --> 4018.06]  Yeah.
[4018.24 --> 4018.74]  100%.
[4018.74 --> 4019.90]  The reason I used to
[4019.90 --> 4021.58]  use the Chrome debugger,
[4021.62 --> 4023.02]  for example, was to
[4023.02 --> 4023.82]  figure out what am I
[4023.82 --> 4024.80]  actually passing here.
[4025.12 --> 4025.72]  TypeScript kind of
[4025.72 --> 4026.90]  eliminated that for me.
[4027.08 --> 4027.40]  Right.
[4027.40 --> 4029.38]  I'm curious, you
[4029.38 --> 4030.56]  mentioned the contracts
[4030.56 --> 4032.16]  that it helps you to
[4032.16 --> 4033.20]  keep and create with
[4033.20 --> 4033.58]  your team.
[4033.76 --> 4034.96]  Was that the main thing
[4034.96 --> 4036.00]  that made it click, or
[4036.00 --> 4037.34]  was there some specific
[4037.34 --> 4038.66]  thing that was like,
[4038.72 --> 4039.96]  oh, okay, yeah, I do
[4039.96 --> 4040.78]  get this now.
[4041.00 --> 4041.24]  Yeah.
[4041.46 --> 4042.36]  I think the contract
[4042.36 --> 4043.34]  was a big one because
[4043.34 --> 4044.66]  building a component that
[4044.66 --> 4045.60]  needs to be used by other
[4045.60 --> 4046.38]  people, I think it's
[4046.38 --> 4047.88]  important for me to make
[4047.88 --> 4048.98]  sure that this, for
[4048.98 --> 4049.90]  example, a prop is going
[4049.90 --> 4050.50]  to be supplied.
[4050.96 --> 4052.04]  Like, let's just say I
[4052.04 --> 4052.84]  label, for example.
[4053.14 --> 4054.88]  If I'm expecting this
[4054.88 --> 4055.54]  component to be
[4055.54 --> 4057.00]  accessible, I'm dependent
[4057.00 --> 4058.14]  on you as a developer
[4058.14 --> 4058.78]  to provide that
[4058.78 --> 4059.50]  attribute to me.
[4059.62 --> 4060.56]  And how can I make
[4060.56 --> 4061.80]  sure that that happens
[4061.80 --> 4062.88]  is through TypeScript
[4062.88 --> 4064.16]  types, so I can provide
[4064.16 --> 4064.74]  that as a required
[4064.74 --> 4065.14]  attribute.
[4065.48 --> 4066.22]  So that has really
[4066.22 --> 4067.02]  helped me kind of
[4067.02 --> 4068.06]  understand why TypeScript
[4068.06 --> 4068.92]  is so popular,
[4069.30 --> 4070.22]  especially when people
[4070.22 --> 4070.96]  are working across
[4070.96 --> 4071.32]  teams.
[4071.88 --> 4072.78]  So, yes, I think
[4072.78 --> 4073.56]  type safety is definitely
[4073.56 --> 4074.12]  one of those.
[4074.26 --> 4075.18]  The contract, definitely
[4075.18 --> 4075.74]  one of those.
[4076.66 --> 4077.80]  I like that actually
[4077.80 --> 4078.80]  as an example, too,
[4078.88 --> 4080.00]  around if you want to
[4080.00 --> 4081.04]  make sure that the
[4081.04 --> 4081.76]  thing you're doing is
[4081.76 --> 4083.42]  accessible, instead of
[4083.42 --> 4084.72]  having to remember as
[4084.72 --> 4085.56]  a developer and putting
[4085.56 --> 4086.44]  that burden on the
[4086.44 --> 4087.08]  developer, oh, you've
[4087.08 --> 4087.80]  got to remember to set
[4087.80 --> 4088.54]  this, you've got to set
[4088.54 --> 4089.18]  this, you've got to set
[4089.18 --> 4089.38]  this.
[4089.64 --> 4090.32]  Bake it into the type
[4090.32 --> 4090.68]  system.
[4090.76 --> 4091.12]  Exactly.
[4091.20 --> 4091.70]  It's there.
[4091.90 --> 4093.04]  If it's not there, it
[4093.04 --> 4093.92]  won't compile.
[4094.36 --> 4094.78]  Exactly.
[4095.42 --> 4096.74]  Yeah, and it gives you
[4096.74 --> 4097.00]  that.
[4097.28 --> 4097.98]  You don't even have to
[4097.98 --> 4098.84]  wait for, like, your
[4098.84 --> 4099.74]  code to get pushed or
[4099.74 --> 4099.98]  anything.
[4100.18 --> 4100.92]  It's right there.
[4101.00 --> 4102.00]  Like, you see it as you
[4102.00 --> 4102.26]  type.
[4102.50 --> 4103.22]  Then you need to provide
[4103.22 --> 4104.16]  this required attribute,
[4104.30 --> 4105.14]  which I love.
[4106.14 --> 4106.66]  I'm going to get
[4106.66 --> 4107.36]  typed HTML.
[4107.36 --> 4113.28]  Oh, wow.
[4113.42 --> 4113.68]  Okay.
[4114.48 --> 4115.36]  We're going to the
[4115.36 --> 4116.18]  Java territory of
[4116.18 --> 4117.16]  JavaScript as well.
[4122.04 --> 4123.14]  Oh, dear.
[4123.52 --> 4124.82]  Well, thank you,
[4124.86 --> 4125.12]  Shruti.
[4125.36 --> 4126.04]  Oh, thank you.
[4126.04 --> 4127.62]  And I think, you know,
[4128.32 --> 4129.16]  we can tell we're all
[4129.16 --> 4130.10]  a little punch drunk at
[4130.10 --> 4131.46]  this point and, you
[4131.46 --> 4133.52]  know, ready to get
[4133.52 --> 4134.46]  onto the social parts
[4134.46 --> 4135.20]  of the conference.
[4135.38 --> 4136.22]  Is there anything you
[4136.22 --> 4137.00]  would like to leave
[4137.00 --> 4139.16]  folks with, you know,
[4139.16 --> 4140.10]  coming out of this,
[4140.18 --> 4141.30]  things that you'd like
[4141.30 --> 4142.10]  them to take away?
[4142.86 --> 4143.26]  Yes.
[4143.54 --> 4144.16]  Two things.
[4144.32 --> 4145.32]  I think a lot of people
[4145.32 --> 4146.30]  are very interested in
[4146.30 --> 4147.30]  coming to conferences,
[4147.30 --> 4149.10]  but also kind of see
[4149.10 --> 4150.92]  themselves speaking at
[4150.92 --> 4151.54]  a conference.
[4151.76 --> 4153.32]  But sometimes they feel
[4153.32 --> 4154.70]  overwhelmed, feeling
[4154.70 --> 4156.18]  that that might be a
[4156.18 --> 4157.50]  step for a later date.
[4158.02 --> 4158.96]  I just want to inspire
[4158.96 --> 4159.88]  people and tell them
[4159.88 --> 4160.94]  that the hurdle to
[4160.94 --> 4161.96]  getting there is a lot
[4161.96 --> 4163.04]  lower than you feel.
[4163.20 --> 4164.00]  So you might feel like
[4164.00 --> 4164.70]  you need to have, like,
[4164.92 --> 4165.76]  a polished topic.
[4165.98 --> 4166.88]  You might need to have,
[4166.96 --> 4167.60]  like, the bleeding-edge
[4167.60 --> 4168.82]  technology, or you need
[4168.82 --> 4169.84]  to be, like, really
[4169.84 --> 4170.78]  well-versed with the
[4170.78 --> 4171.52]  stuff that you're about
[4171.52 --> 4171.90]  to do.
[4172.26 --> 4173.62]  But I can tell you that
[4173.62 --> 4175.26]  if you submit a topic,
[4175.36 --> 4176.14]  you have three months
[4176.14 --> 4177.00]  to prepare for that
[4177.00 --> 4178.02]  topic, you will be able
[4178.02 --> 4178.90]  to come up with a talk.
[4179.12 --> 4179.80]  So I want to tell
[4179.80 --> 4180.90]  people, like, giving a
[4180.90 --> 4181.82]  conference talk is a lot
[4181.82 --> 4182.86]  easier than you think.
[4183.14 --> 4184.28]  So apply for your first
[4184.28 --> 4185.36]  conference talk.
[4186.02 --> 4187.18]  It's easier than you think.
[4187.24 --> 4187.76]  You can do it.
[4187.82 --> 4188.54]  I believe in you.
[4188.88 --> 4189.54]  There's a lot of
[4189.54 --> 4190.40]  conferences that happen
[4190.40 --> 4191.40]  online as well, and
[4191.40 --> 4192.02]  they're always looking
[4192.02 --> 4192.60]  for speakers.
[4192.78 --> 4193.30]  There's a lot of
[4193.30 --> 4194.30]  meetups, which is a
[4194.30 --> 4195.00]  really great place to
[4195.00 --> 4195.70]  kind of start speaking
[4195.70 --> 4196.70]  at conferences as well.
[4197.40 --> 4198.52]  So that's number one.
[4198.88 --> 4200.16]  Actually, adding one
[4200.16 --> 4201.26]  more thing to that is
[4201.26 --> 4202.98]  there's a few tips that
[4202.98 --> 4203.98]  I've given on my
[4203.98 --> 4205.40]  YouTube channel, which
[4205.40 --> 4207.58]  can I link a video as
[4207.58 --> 4207.78]  well?
[4208.14 --> 4208.58]  Okay.
[4208.66 --> 4210.28]  So I'll hand the link
[4210.28 --> 4211.60]  over to you, and I
[4211.60 --> 4212.36]  think that'll be a nice
[4212.36 --> 4213.46]  video for people who are
[4213.46 --> 4214.44]  interested in speaking at
[4214.44 --> 4215.94]  conferences but have that
[4215.94 --> 4216.54]  little bit of, like,
[4216.60 --> 4217.74]  imposter, like, oh, I'm not
[4217.74 --> 4218.26]  ready yet.
[4218.64 --> 4219.66]  So I think that'll be a
[4219.66 --> 4220.60]  really nice video for
[4220.60 --> 4220.92]  folks.
[4222.06 --> 4223.18]  The second thing I would
[4223.18 --> 4225.16]  say is that there's a lot
[4225.16 --> 4227.58]  of debate on whether or not
[4227.58 --> 4229.74]  React is still relevant,
[4230.74 --> 4234.36]  still the language or still
[4234.36 --> 4235.56]  the framework of a library
[4235.56 --> 4236.80]  that people should learn,
[4237.30 --> 4238.30]  especially coming out of
[4238.30 --> 4239.46]  boot camps, especially with
[4239.46 --> 4240.92]  AI tools and people feeling
[4240.92 --> 4242.20]  like maybe they don't need
[4242.20 --> 4243.48]  to learn any framework or
[4243.48 --> 4243.78]  library.
[4244.20 --> 4245.80]  I would say React is still
[4245.80 --> 4246.18]  relevant.
[4246.50 --> 4247.34]  It's still the number one
[4247.34 --> 4248.52]  technology that people are
[4248.52 --> 4249.42]  looking for when they're
[4249.42 --> 4249.78]  hiring.
[4250.38 --> 4251.76]  So definitely learn React.
[4251.90 --> 4252.68]  There's a lot of great
[4252.68 --> 4254.32]  courses out there, a lot of
[4254.32 --> 4255.22]  free content on YouTube.
[4255.80 --> 4257.12]  I also have a course on
[4257.12 --> 4258.78]  O'Reilly, which I'll give
[4258.78 --> 4259.44]  the link as well.
[4259.78 --> 4261.00]  But definitely learn React.
[4261.00 --> 4262.34]  It's a really great way to
[4262.34 --> 4264.50]  ensuring that you are, you
[4264.50 --> 4265.52]  have a secure front-end
[4265.52 --> 4266.52]  career, at least for the
[4266.52 --> 4267.24]  next five years.
[4268.36 --> 4268.74]  I agree.
[4269.82 --> 4271.72]  Well, if you get good at
[4271.72 --> 4273.12]  it, you can take those
[4273.12 --> 4273.88]  concepts anywhere.
[4274.10 --> 4274.22]  Yeah.
[4274.28 --> 4274.72]  That's true.
[4275.16 --> 4275.36]  Right.
[4275.48 --> 4277.14]  Like if you get really good
[4277.14 --> 4278.36]  at React, right now that is
[4278.36 --> 4279.14]  the best way to get a
[4279.14 --> 4279.76]  front-end job.
[4280.02 --> 4280.20]  Yeah.
[4280.66 --> 4282.36]  And if in five years the
[4282.36 --> 4284.14]  answer is felt, most of
[4284.14 --> 4285.34]  those core concepts that
[4285.34 --> 4286.58]  you learned in React will
[4286.58 --> 4287.10]  translate.
[4287.32 --> 4287.66]  Absolutely.
[4287.66 --> 4288.24]  Without any difficulty.
[4288.74 --> 4289.88]  And we talked to Tom
[4289.88 --> 4292.20]  Okino earlier today about
[4292.20 --> 4294.26]  just how React was there,
[4294.44 --> 4295.46]  but it's kind of influenced
[4295.46 --> 4296.66]  the whole industry in terms
[4296.66 --> 4297.36]  of like the new frameworks
[4297.36 --> 4298.02]  that are coming out are
[4298.02 --> 4300.50]  still creating the same
[4300.50 --> 4302.02]  core concepts like
[4302.02 --> 4303.90]  component-based development
[4303.90 --> 4304.78]  and things like that.
[4304.96 --> 4306.52]  So it is very transferable.
[4307.60 --> 4307.84]  Yes.
[4308.62 --> 4309.06]  Agreed.
[4309.68 --> 4310.14]  All right.
[4310.38 --> 4312.56]  Well, this has been
[4312.56 --> 4313.42]  Shruti Kapoor.
[4314.12 --> 4315.02]  Thank you so much for
[4315.02 --> 4315.52]  having me.
[4315.64 --> 4316.36]  This is so wonderful.
[4325.46 --> 4336.10]  All right.
[4336.26 --> 4337.86]  That is JS Party for this
[4337.86 --> 4338.16]  week.
[4338.50 --> 4339.82]  Thanks for hanging with us.
[4340.12 --> 4341.62]  Did you know we're having
[4341.62 --> 4343.40]  a year-end merch sale?
[4343.76 --> 4344.10]  Yes.
[4344.26 --> 4345.80]  All Changelog merch is
[4345.80 --> 4347.22]  discounted while supplies
[4347.22 --> 4347.72]  last.
[4348.10 --> 4349.78]  Get yourself or someone you
[4349.78 --> 4351.26]  care about some new threads
[4351.26 --> 4353.20]  for up to 40% off
[4353.20 --> 4355.92]  at merch.changelog.com.
[4356.56 --> 4357.78]  Big thanks once again
[4357.78 --> 4358.40]  to our partners
[4358.40 --> 4359.64]  at Fly.io,
[4360.06 --> 4361.36]  to our longtime sponsors
[4361.36 --> 4361.94]  at Sentry,
[4362.22 --> 4363.22]  use code CHANGELOG,
[4363.54 --> 4364.20]  save 100 bucks
[4364.20 --> 4365.52]  on a Sentry team plan,
[4365.84 --> 4366.58]  and to the one,
[4366.88 --> 4367.44]  the only,
[4367.68 --> 4368.38]  the Beat Freak,
[4368.66 --> 4369.46]  Breakmaster Cylinder.
[4369.86 --> 4370.66]  Thanks BMC.
[4370.82 --> 4371.82]  Our shows wouldn't
[4371.82 --> 4373.26]  bump the same without you.
[4373.52 --> 4374.96]  That's all for now.
[4375.32 --> 4376.30]  But come on back
[4376.30 --> 4378.20]  and party with us again
[4378.20 --> 4379.44]  next week.
[4379.44 --> 4389.84]  Game on.
