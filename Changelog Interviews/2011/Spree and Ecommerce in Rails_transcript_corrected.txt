[0.00 → 18.42] Welcome to the Changelog episode 0.6.9.
[18.54 → 19.56] I'm Adam Stachowiak.
[19.86 → 20.66] And I'm Wynne Netherlands.
[20.84 → 22.04] This is the Changelog Wikipedia.
[22.28 → 23.40] It's fresh and new and open source.
[23.92 → 26.54] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.72 → 27.66] We're also on GitHub.
[27.66 → 29.56] Head to GitHub.com slash explore.
[29.66 → 33.52] You'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[34.08 → 37.60] If you're on Twitter, follow Changelog Show and me, Adam Stack.
[37.92 → 40.30] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.04 → 48.78] On an episode this week, talk to the guys over at Spree, Sean and Brian, about the recent funding round and the latest developments with Spree.
[49.34 → 52.24] You know, this is some perfect news for the up-sports community.
[52.24 → 58.36] I mean, on top of this funding, as well as Accelerator's recent 15 mid, this is exciting news.
[58.82 → 65.88] Yeah, it's fun to watch projects get some backing, allow them to do some things they normally wouldn't get to do.
[66.10 → 68.24] Spreeing is one of those for the Spree community.
[69.10 → 72.44] There's going to be a conference February 15th, 16th in New York City.
[72.92 → 74.20] I hope to see you there.
[74.58 → 75.68] Excellent lineup of speakers.
[75.68 → 81.24] And if you really want to make it, it's not a bad price out of $99 to get registered.
[81.38 → 82.46] That is a cheap conference.
[82.72 → 83.94] That's a perfect conference ticket.
[84.52 → 85.32] Excited to be there.
[85.40 → 86.22] It's a fun episode this week.
[86.26 → 86.84] Should we get to it?
[86.98 → 87.68] Let's do it.
[96.38 → 99.72] I'm chatting today with Sean Schofield and Brian Quinn from the Spree Project.
[99.72 → 103.94] So, Sean, you first want to introduce yourself and your role over at Spree.
[103.94 → 106.66] I'm Sean Schofield.
[106.78 → 114.78] I'm the creator of Spree and co-founder of Spree Commerce and CEO at the new company that we've just established.
[115.72 → 116.96] Brian, what's your role over there?
[118.30 → 123.68] I'm the CTO of Spree Commerce, Inc. and a longtime contributor to Spree.
[124.28 → 128.34] So, for those that don't know, Sean, why don't you give a little background about the Spree Project and what it is?
[128.34 → 138.46] The Spree Project is an open source e-commerce platform for Ruby on Rails that started about a little over four years ago.
[138.58 → 141.34] And an original name was called Railcard.
[141.90 → 144.94] So, it's kind of evolved to this point.
[145.18 → 147.96] And I can give you a little more background later if you want to know more about the history.
[148.24 → 148.88] So, how long?
[148.88 → 149.52] That's the gist of it.
[149.60 → 150.90] How long ago was it Railcard?
[150.90 → 151.92] Over four years ago.
[152.64 → 160.24] I think the first blog post to the Spree user mailing list was over four years ago, a little over four years ago.
[160.56 → 163.72] It's gone, I guess, through a couple of transformations.
[163.96 → 165.42] It's now a Rails engine, right?
[166.20 → 166.42] Yeah.
[166.66 → 166.84] Yeah.
[166.84 → 169.88] We've steadily kind of evolved with Rails.
[170.74 → 177.46] And in some cases, maybe even influenced the direction Rails has gone in subtle but important ways.
[177.74 → 182.82] So, we were definitely a proponent of more engines and that kind of functionality in Rails.
[183.02 → 186.78] And the core team listened, which was good.
[186.98 → 189.40] So, how big was the move to Rails 3.1 for Spree?
[192.14 → 193.76] Brian, do you want to handle that one since you did the best?
[193.76 → 194.32] Yeah, sure.
[194.32 → 202.08] Sure. It was a pretty big job because prior to Rails 3, we had been using kind of our own version of extensions,
[202.42 → 206.08] which were basically engines, but they were kind of shoehorned into Rails.
[206.16 → 211.88] So, we had a very kind of rough food process and it was a pretty rough experience.
[212.54 → 216.74] So, with the move to Rails 3, then we were able to basically back out all that code
[216.74 → 220.74] and just completely embrace the Rails 3 style of engines.
[220.74 → 225.00] So, yeah, it was a pretty massive change, all right.
[225.58 → 228.30] I think it started around Hailstone in Baltimore.
[228.48 → 230.60] It was the first time in the first Hailstone Baltimore.
[230.76 → 235.72] It was when we actually started working on it when we managed to get some time together at the excellent Bacon there.
[236.46 → 240.74] So, yeah, it took, I think we were about nine months actually working on that release
[240.74 → 245.28] until we got the 0.30 release, which was the first one to support Rails 3.
[245.28 → 249.42] And Rails 3.1 was almost as complicated, it turned out.
[250.92 → 257.38] Yeah, absolutely, because the asset pipeline and other features like that really took us a while to get it integrated.
[257.54 → 261.68] I think we probably jumped on the Rails 3.1 migration a little bit too early
[261.68 → 267.10] because the core team were still settling down on exactly what Sprockets was doing and what features were where.
[267.10 → 271.28] So, we were kind of chasing the mark for a few weeks there until it settled down.
[271.36 → 279.16] But it seems to be pretty solid now that our latest 0.70.1 release is fully Rails 3.1.1 compliant.
[279.32 → 281.92] So, the Rails 3.1 asset pipeline is a two-edged sword.
[282.30 → 287.74] It streamlines a lot of the asset generation and makes assets first-class citizens of the project.
[288.06 → 293.52] But also, it comes with attacks for developers, I guess, during development mode where it's much slower.
[293.52 → 300.06] Yeah, absolutely. And one of the great things about the asset pipeline and how it works with engines
[300.06 → 305.98] is it gives you great modularity in that an engine can bring along a little piece of JavaScript or a CSS file
[305.98 → 311.16] and they can all just marry in together into the final assets for the project.
[311.34 → 313.52] So, it's definitely phenomenal in that respect.
[313.64 → 316.10] But yeah, you do pay a price in terms of development performance.
[316.34 → 320.16] But there is a rate task now that will allow you to pre-compile your assets
[320.16 → 321.84] if you're not working on them in development mode.
[321.84 → 325.24] So, you can completely pretty much remove the penalty for performance there.
[326.52 → 331.98] So, Rails engines, I guess, for those that don't know, take advantage of open types in Rails
[331.98 → 337.72] so that you can include models, views, controllers from an engine
[337.72 → 342.80] and override them in your own project and really exploit that feature of Ruby.
[343.46 → 349.04] Talk a bit about how many different touchpoints are in the application
[349.04 → 350.74] that you can customize to suit your needs.
[350.74 → 351.00] Yeah.
[351.84 → 352.28] Yeah.
[353.28 → 356.96] Well, like you said, an engine is really just a Rails application.
[357.36 → 361.36] So, it provides that mechanism to bundle in all your controllers and models.
[362.04 → 365.96] And then, basically, we kind of add in this extra layer that we call decorators,
[366.34 → 368.86] which is a pretty common idiom for development,
[369.52 → 372.46] where you can basically take a class, like, say, the product model,
[372.46 → 377.30] and open it up, change whatever methods or add methods that you need to add to it,
[377.58 → 379.72] you know, extend it with new associations or whatever.
[379.90 → 385.20] So, your host application takes in Spree as an engine and then, you know,
[385.24 → 387.72] can bend it to your exact requirements.
[387.72 → 393.74] And then, there's a huge collection of extensions, like third-party extensions that are available
[393.74 → 399.38] and listed on our website that you can go and pull down extra features like wish lists and social integration.
[400.06 → 402.88] There are countless other extensions I've already written.
[402.88 → 406.24] And so, you can also tie those in at the same time into your host application
[406.24 → 408.98] and customize it exactly the way you want to.
[409.02 → 412.12] So, beyond that, Spree is also not just a monolithic gem.
[412.36 → 414.88] It's made up of parts that you can use à la carte, right?
[415.92 → 416.24] Yeah.
[416.30 → 417.76] And I just want to add on the engines' thing.
[417.84 → 421.86] I think that the engines' development in Rails was, like, super important.
[422.12 → 425.64] Like, and I think we're only just starting to see some of the benefits of it.
[425.64 → 436.52] Like, they started out, I mean, there was a project called Engines, like, that was a separate sort of unrelated project with the same name.
[437.66 → 442.48] That, you know, initially, I think, was disparaged a bit, you know, by DHH and others.
[442.56 → 443.76] They didn't want that part of Rails.
[443.90 → 451.66] But, ultimately, they came around to something that was pretty close to what people were doing outside the Rails project.
[451.66 → 457.70] Radiant, in particular, had adopted an extension mechanism that, you know, that influenced us.
[457.84 → 462.26] And that, in turn, influenced, you know, the direction, I think, that the Rails team went.
[462.54 → 469.38] But we're only just now starting to see people really kind of, I think, the documentation was fairly limited.
[469.64 → 474.32] And just, I don't know, it just took people a while to kind of grasp what the power of, you know, engines really means.
[474.38 → 480.44] And now we're starting to see some of the more major Rails open source projects moving to engines.
[480.44 → 482.38] Like, you know, Devise has been, I guess, an engine for a little while.
[482.48 → 488.48] But, you know, projects like Radiant and Refinery and now there's, like, this forum and Rails admin.
[488.66 → 490.94] I'm starting to see more and more engines.
[491.30 → 494.40] And now we're going to start to see what can happen when you combine them all.
[495.30 → 498.98] And I think that's, you know, that's been a huge, you know, development for Rails.
[499.68 → 501.52] You mentioned Devise.
[501.66 → 504.12] I guess Devise is part of Spree with Spree Auth.
[504.52 → 507.98] What other popular plugins make up the architecture for Spree?
[507.98 → 515.48] We're using, is it Seminary for paging?
[515.58 → 515.78] Paginate.
[516.12 → 522.92] Yeah, we were using will paginate dependencies because Rails 3 actually helped us in that way because so many things broke at Rails 3.
[523.08 → 530.88] And then we just didn't, you know, we ended up kind of coming up with our own Rails 3 compatible solution or moving to, you know,
[530.88 → 540.54] that was a big consolidation of our dependencies because a lot of older projects just never got upgraded, never made it, you know.
[541.64 → 545.80] That was like will paginate finally kind of got there, but it took a long time.
[545.84 → 549.34] So that's why we moved to Seminary and Search Logic.
[549.48 → 553.24] You know, others, we just kind of end up abandoning because, you know,
[553.24 → 559.10] they had stalled out a little bit, I guess, in terms of momentum and so that was a period of consolidation for us.
[560.08 → 564.18] Yeah, it makes our job easier too as we're, you know, migrating between versions of Rails.
[564.32 → 571.12] The less dependence we have on third-party gems, the less kind of forking and waiting around for libraries to get updated
[571.12 → 576.08] or, you know, taking on a big job of updating a library, like for our Rails 3 migration.
[576.50 → 581.62] We were using James Colic's resource controller, and we had to port that to Rails 3.
[581.74 → 584.86] And that was in itself one of the biggest jobs of the Rails 3 migration.
[585.12 → 589.24] So as we're slowly kind of taking away as many dependencies as possible
[589.24 → 594.98] and we're trying to keep Spree almost as, like, a simple Rails application as possible
[594.98 → 598.88] so to make our migrations easier between versions.
[598.88 → 602.04] But we do use a couple of other interesting gems like State Machine.
[602.98 → 603.54] Oh, yeah, yeah.
[603.54 → 605.26] It's a good extension.
[605.40 → 608.48] We use it for our checkout kind of State Machine, basically.
[609.20 → 613.70] We also use Active Merchant, of course, from Shopify, which is a good gateway library.
[614.52 → 619.40] Yeah, Active Merchant and Plugin a Week State Machine are good about updating, you know.
[620.52 → 623.32] They're very active communities, and they're good about updating to the newest Rails
[623.32 → 625.08] so we don't have a problem depending on them.
[625.84 → 628.08] So quite a number of models here in Spree.
[628.08 → 633.08] If you go to the Spree core app models folder, I guess the good news is you can customize those
[633.08 → 635.16] if there's overlap with your application.
[635.28 → 638.42] I'm curious, for most people when they're creating a Spree project,
[638.60 → 643.20] is it adding storefront features to an existing application
[643.20 → 646.28] or are they starting with the store and building an application around it?
[647.08 → 649.56] It's primarily been used up until now.
[649.56 → 656.74] You know, it's primarily worked best as a standalone store that maybe then you add features around.
[657.58 → 659.80] I mean, that's kind of been the bias, I guess.
[661.08 → 664.44] But we are, you know, there's no reason why that needs to be the case.
[664.56 → 669.62] There have been cases where there have been really mature Rails applications that Spree has been integrated in,
[669.62 → 672.14] but that's always been more difficult than it should be.
[673.60 → 678.38] But again, with engines and now name spacing that's supported in Rails 3.1,
[678.94 → 687.32] you know, there's some perfect opportunities to kind of break that assumption that the store is going to come first.
[687.32 → 695.06] So we're definitely very interested in being able to integrate with Refinery, Radiant, you know, browser, CMS,
[695.26 → 696.82] all the different open source CMSs.
[697.28 → 701.16] There's been a lot, since I started Spree, one of the first questions on the user list was like,
[701.18 → 702.44] can I combine this with Radiant, you know?
[702.50 → 706.54] And people ask about every other week for that functionality.
[707.00 → 712.78] So the good news is that that will be a lot, that will be a reality soon.
[712.78 → 719.66] And because with engines, you can just drop them in any particular order, and it doesn't matter.
[719.76 → 725.56] But that's a pretty complicated exercise to really, because Spree is not some little widget that you drop into WordPress.
[725.80 → 729.14] Like it's a huge, you know, full-featured e-commerce engine and there's a lot.
[729.56 → 737.38] There's authorization and authentication and admin stuff, reporting, and there are just a lot of interdependent pieces.
[737.38 → 744.90] So the Rails is now sophisticated enough, and we now refined Spree enough so that this should be possible.
[745.76 → 750.38] So Spree's had a couple, I guess, corporate sponsors over its lifespan.
[751.26 → 755.84] But just recently, you guys formed Spree Commerce, the company behind Spree.
[756.00 → 758.20] So why don't you talk a bit about that news?
[759.04 → 759.34] Sure.
[759.34 → 767.04] Well, you know, I began, Spree began as, when I was a freelance consultant.
[767.18 → 775.04] So it really, and it really still solves that, you know, it's still working on solving that problem that I noticed when I was first doing e-commerce.
[776.56 → 784.72] But over time, and then I was employed, you know, by a couple different people that were interested in what we were doing.
[784.72 → 789.28] And, you know, and it kind of being associated with that project brought them some, you know, business.
[790.46 → 801.88] But then really became big enough that I could justify kind of starting at Rails Dog, which was a, well, Rails Dog was originally a blog and named after my dog.
[801.98 → 805.58] And then it just sort of evolved into a company.
[806.12 → 812.50] Ultimately, I didn't want a company that I didn't own or control to be sort of affiliated with the project anymore.
[812.50 → 816.94] So I just set it up as, like, I'm going to kind of self-sponsor the project.
[818.14 → 820.12] And that was, like, sort of intermediate kind of step.
[820.36 → 823.38] And then it quickly became, like, wow, there's enough interest in here.
[823.46 → 826.62] I could probably just start a consulting company just around doing Spree work.
[827.20 → 833.04] So it kind of morphed into Rails Dog, the consulting company, and we did that.
[833.04 → 837.60] And Brian is a long-time contributor through open source.
[838.48 → 840.26] And then he joined us at Rails Dog.
[840.48 → 843.72] And so he was with me at the very – he was, like, the first employee at Rails Dog.
[844.52 → 851.12] And then we just recently started this new company as a vehicle for the investment.
[851.54 → 853.54] And the separation there is really consulting.
[853.68 → 855.48] And Rails Dog is still, like, a consulting company.
[856.12 → 859.74] The new company – besides, you know, investors aren't interested in consulting.
[859.74 → 863.26] They didn't really, you know, help us build the consulting business.
[863.38 → 865.56] So we didn't really feel like we needed to cut them in on that.
[866.42 → 876.82] And, you know, we wanted the ability – the whole point of getting the money was to really have the ability to focus on Spree and the product in the community and not the short-term kind of needs of clients.
[876.82 → 887.44] So there is this new company, Spree Commerce, Inc., which is now a custodian of the Spree source code and the current benefactor.
[888.44 → 894.46] So when you mentioned getting the money, you're referring to the recent $1.5 million seed funding round led by True Ventures?
[895.36 → 896.16] Yes, I am.
[897.22 → 897.92] That's exciting.
[899.00 → 899.56] Yes.
[900.00 → 900.42] Yes.
[900.90 → 901.80] So how are you going to spend that?
[901.80 → 906.08] Well, we've got a lot of different ideas.
[906.20 → 912.06] I mean, believe it or not, like, the money can be spent and can be spent fairly quickly if one is not strategic about it.
[912.24 → 918.16] So – but our main thing is, like, there are a lot of, I guess, public goods.
[918.50 → 920.38] You know, in the – I'm going to have an econ background.
[920.58 → 927.24] So, like, in public goods kind of context, things that, you know, the free market would not take care of by itself.
[927.24 → 936.16] Like, so, i.e., you know, clients aren't going to pay for better documentation because once their documentation exists, everyone can benefit from it.
[936.34 → 941.52] And they don't – you know, they're not going to benefit proportionately to what it would cost to create it.
[941.94 → 951.22] So, you know, but once we create a really great ecosystem, like, with documentation and, you know, videos and other tutorials and things like this, then everybody can benefit.
[951.22 → 958.92] So that's an example of where, hey, you know, we definitely plan to invest a lot more – I think we have pretty good documentation for an open source project.
[959.10 → 965.08] But, you know, now we can, you know, really put more into documentation, training, answering, you know, questions on user lists.
[965.10 → 966.30] We can dedicate a lot of resources.
[967.14 → 972.28] So that's, like, the first priority is to continue to nurture our growing ecosystem.
[972.28 → 983.98] And we have some ideas we can talk about a little bit later in the conference, like I mentioned before we got on, that thinking about a conference and some other ideas for the money.
[984.14 → 985.84] So, yes, let's talk about that.
[985.92 → 987.82] When's the big date?
[988.38 → 994.16] So we're going to do our first ever Spreeing in New York City next February.
[994.30 → 996.32] It'll be February 15th and 16th.
[996.32 → 1001.60] And so the site should be up by the time this airs, spreeconf.com.
[1002.84 → 1003.74] And –
[1003.74 → 1007.28] Is this geared towards developers or business folk or both?
[1007.28 → 1015.60] Yes, it's geared towards – I think it's geared towards developers, but also it would be appropriate for business owners that want to learn more about Spree.
[1015.74 → 1018.42] There'll be something for everybody and there'll be opportunities to learn there.
[1018.42 → 1031.32] The first day, the 15th of February, will be training, and we're going to do a full day of training on – we'll probably break it up into half a day of Rails and a half a day on Spree.
[1031.72 → 1033.28] And then the second day will be talks.
[1035.26 → 1039.30] The training – so, you know, if you want to learn more about Spree, there'll be the training.
[1039.46 → 1040.50] We'll have a hackathon.
[1040.78 → 1044.06] You know, all the Spree – well, or most of the Spree Corps people will be there.
[1044.14 → 1045.22] Myself and Brian will be there.
[1045.22 → 1049.60] And there'll be a couple talks, like, you know, a little bit more geared towards Spree.
[1049.78 → 1056.22] But then there'll be a lot of talks that are just going to be talking about general topics of Rails interest.
[1056.38 → 1059.68] So if you're in the New York City area, or you want to come.
[1059.88 → 1062.78] So, Won, you are scheduled to speak as well?
[1062.86 → 1063.44] I would love to.
[1063.96 → 1064.16] Yeah.
[1064.60 → 1068.66] So – but we haven't discussed the topic, but, you know, we've pencilled you in there.
[1068.80 → 1073.80] So, you know, like I think maybe we'll try to maybe put things in a little bit of a Spree context when possible.
[1073.80 → 1077.06] But, you know, I'd like to see some talks on CoffeeScript.
[1077.42 → 1082.50] And, you know, we have a guy that's probably going to do a talk on recommendation engines.
[1082.80 → 1095.08] And, I mean, you know, recommendations and the kind of algorithms that go into that and some of the kind of just general problems behind that sort of area are, you know, I think would be of interest to anybody, you know, doing Rails work, not just Spree people.
[1095.08 → 1098.38] So it's going to be kind of a crossover sort of thing.
[1098.46 → 1102.86] Our community isn't large enough really to warrant like a three-day Rails cone extravaganza.
[1104.14 → 1108.80] And we're going to have some cool speakers and interesting people there.
[1108.90 → 1110.94] So Bree Pettish is going to be doing our keynote speaker.
[1111.04 → 1112.18] He's the CEO of Maker Bot.
[1112.18 → 1115.56] So really cool company.
[1115.70 → 1117.16] It's really popular with the tech nerds.
[1117.34 → 1120.18] And he's going to do a demonstration and talk.
[1120.30 → 1125.34] And so I think it'll be cool just to go and, you know, see him do his thing.
[1125.64 → 1131.46] But, you know, Scotch O'Con and some of the other usual people that you see at the, you know, regional Ruby conferences will be there too.
[1131.74 → 1134.00] So and GitHub's throwing the party afterwards.
[1134.14 → 1135.72] So definitely come by and see us.
[1136.20 → 1136.80] Definitely worth it.
[1136.80 → 1141.02] I see Sticker Mule is in your success stories showcase on Spree Commerce.
[1141.02 → 1143.58] Yeah, the Sticker Mule guys will be there too if you've ever bought stickers from them.
[1143.74 → 1143.84] Come.
[1144.84 → 1146.42] Love the stickers from Sticker Mule.
[1147.08 → 1147.44] Yeah.
[1147.94 → 1150.30] They're probably our favourite Spree client.
[1150.80 → 1154.12] I mean, we love all our clients at Rails.com.
[1154.70 → 1159.86] So what's the largest installation that you know of for Spree?
[1160.72 → 1161.00] Okay.
[1161.34 → 1162.76] So let's see.
[1162.82 → 1163.16] Largest.
[1163.16 → 1171.66] Well, the largest – there are two large ones that use Spree to some degree or another.
[1171.78 → 1172.94] So one would be Shoe Dazzle.
[1175.62 → 1179.10] And Shoe Dazzle is a huge company.
[1179.34 → 1182.14] I think they're doing something like – this is not inside information, just whatever.
[1182.24 → 1185.78] It's rumoured to be $100 million a year in sales and shoes.
[1185.94 → 1187.52] And that's Kim Kardashian's, like, shoe company.
[1187.52 → 1195.82] So they had a Rails custom – a custom Rails solution, and they moved to Spree quite a while ago, like an older version of Spree.
[1196.04 → 1197.82] And they've customized it heavily since.
[1198.00 → 1204.26] So, I mean, it's not like, oh, if you installed Spree, you will be able to build Shoe Dazzle overnight or whatever.
[1204.42 → 1206.00] I mean, there's obviously a lot goes on top of it.
[1206.52 → 1210.02] But that's, like, a pretty big name client that's using it.
[1210.02 → 1214.10] The other is Second Life.
[1214.44 → 1215.14] Yeah, Second Life.
[1215.28 → 1221.64] So they are using a very customized version of Spree, even more so than Shoe Dazzle.
[1221.76 → 1230.04] But one thing I know that's fairly intact – and, again, these guys started early, you know, when Spree was a lot rougher.
[1230.20 → 1235.64] One thing that remains definitely intact, I've heard, in the Second Life installation was the data model.
[1235.64 → 1242.70] So you mentioned all the models, and you can kind of pick and choose, but interestingly, we get a lot of compliments on, oh, the data model is perfect.
[1242.80 → 1248.20] Like, that was, like, a big part of what they decided to use on that particular installation.
[1248.76 → 1255.42] But, you know, so we can go – so Spree is certainly suitable to either jumpstart or actually run, like, a very big, huge business.
[1255.42 → 1260.68] But, you know, there's also – we've got people who do, you know, a few thousand bucks a month in sales.
[1260.86 → 1266.66] And then I think a good standard, you know, would be $25,000, $50,000 a month.
[1266.72 → 1270.24] There are a lot of stores that run in that range, some several hundred thousand.
[1271.16 → 1274.42] I mean, I won't get into the, you know, names with figures, but –
[1275.18 → 1278.68] So what sort of ecosystem is cropping up around Spree for extensions and themes?
[1278.68 → 1285.56] Well, the extension kind of ecosystem is pretty vibrant and pretty popular right now.
[1285.68 → 1289.90] Like, if you go on to GitHub and just search for repositories, they start with Spree underscore.
[1290.54 → 1294.68] I think they get about 600 different repos, and that's not including forks.
[1295.02 → 1301.56] So, like, because Spree has supported extensions since one of its earliest versions, you know, there's always been a lot of activity there.
[1301.56 → 1311.04] And pretty much every kind of problem that you need to solve on a regular basis for an e-commerce store has been solved for one version of Spree or another.
[1311.54 → 1319.62] I guess one issue there really is, you know, with any open source project is as the core product rolls forward, not all the extensions follow along.
[1319.72 → 1324.92] So there's obviously a big maintenance overhead there to support, you know, the huge community of extensions.
[1324.92 → 1337.72] But we maintain a pretty large collection of about 20 extensions that we classify as official extensions that, you know, get used an awful lot by the majority of stores, but yet don't warrant being in core itself.
[1338.24 → 1346.18] Stuff like Spree Social, which gives you integration with Omni Auth, so you can log on with Facebook and Twitter and other sources like that.
[1346.18 → 1356.38] There's Spree Active Shipping, which integrates with FedEx and UPS and USPS and all those other shipping APIs.
[1358.00 → 1361.46] There are countless others, PayPal Express-related products.
[1361.70 → 1362.36] That's a problem.
[1362.38 → 1362.80] You name it.
[1362.88 → 1371.56] Basically, somebody has already written an extension, and we've taken over a few of them as important extensions to maintain them going forward.
[1371.56 → 1378.28] So we also have a project called Rails Dog Radio, which is kind of a large sample store of Spree.
[1378.46 → 1386.42] So it uses Spree, the core product, and then I think about six of the official extensions and then a custom team as well all rolled into one.
[1386.98 → 1392.58] And as part of our upgrade process for every version of Spree, we basically use it for dog flooding.
[1392.64 → 1396.98] So we go, and we upgrade the Rails Dog Radio store to use the latest version of Spree.
[1396.98 → 1403.04] And then that kind of gets us started on upgrading all the official extensions.
[1403.56 → 1407.26] So the source for the Rails Dog Radio source is available on GitHub as well.
[1407.50 → 1409.36] We give you links for that and whatever.
[1410.88 → 1413.74] And yeah, so the Rails Dog Radio team is one of the first kind of...
[1413.74 → 1415.92] The theming is a relatively new feature in Spree.
[1416.04 → 1417.88] It only came about with the...
[1417.88 → 1420.80] Well, with 070 release, which is only a couple of weeks old.
[1420.80 → 1424.86] So the Rails Dog Radio team is one of the first teams to put on Spree.
[1425.06 → 1429.58] And that's something we're actively looking at is building out more team extensions.
[1430.28 → 1437.50] But in Spree terminology, a team and an extension is the same thing, except a team really only changes the front end, doesn't have any...
[1437.50 → 1438.96] Doesn't bring any logic with it.
[1439.78 → 1446.38] Yeah, so I wanted to go back to a couple of things Brian just mentioned, because it ties into the venture funding that we discussed before.
[1446.38 → 1448.40] Or, you know, the Rails Dog Radio, which is...
[1448.40 → 1450.16] So that is the official, like, online demo.
[1450.28 → 1452.10] So, like, it's like a fancier...
[1452.10 → 1455.22] You know, Spree is pretty bare bones when you install it, and intentionally so.
[1455.58 → 1457.62] So you can kind of add the theory as well.
[1457.66 → 1461.86] You can just tweak the UI with a theme and add extensions that you want.
[1462.64 → 1467.20] But, you know, there were two problems with just leaving it that way.
[1467.30 → 1471.66] One is that, you know, it's hard to tell people, like, but it can do so much more.
[1471.74 → 1472.50] Just trust us.
[1472.50 → 1478.50] So, you know, we wanted to kind of sort of demonstrate, and then also people, you know, didn't want to...
[1479.24 → 1482.88] And also, I think, you know, it was helpful to kind of show, give people a jump start.
[1483.04 → 1488.68] So, you know, we decided to build this Rails Dog Radio and make it open source.
[1488.88 → 1493.86] So that's all open source, but you can see it online, and then you can also just, you know, get it from GitHub and use it as a starting point.
[1494.26 → 1499.50] All it is a gem file, you know, pretty much that references a bunch of other Spree engines, and it kind of shows you...
[1499.50 → 1501.84] It's like a reference implementation of Spree, I guess.
[1501.96 → 1504.84] But, you know, it took us a long time to do that.
[1504.88 → 1513.14] We did that through Rails Dog, and, you know, with some of the proceeds, you know, basically, you know, because we had to pay the engineers who were working on it.
[1513.14 → 1516.08] I mean, and the artists who designed it and things and whatever.
[1516.42 → 1518.14] You know, we had to...
[1518.68 → 1526.72] It took us a long time to get to the point where we could do that because we're just so busy, you know, taking care of our clients, which is, you know, what we should be doing when we're consultants.
[1526.98 → 1530.60] So, you know, that would have gotten going a lot faster.
[1530.76 → 1534.18] And then there are things that still need to be done, which is like, hey, we need a lot more themes.
[1534.18 → 1536.70] We need better curation of the extensions.
[1537.02 → 1541.32] Like, there are, you know, outdated versions of almost everything you need at least.
[1541.48 → 1544.84] But, you know, will it run on my version of Spree that I need?
[1545.40 → 1547.32] You know, maybe, maybe not.
[1547.44 → 1550.16] And so that's definitely going to be a point of emphasis for us, you know.
[1550.18 → 1551.18] And again, you know, having...
[1551.86 → 1553.36] No client is going to pay for that.
[1553.44 → 1555.54] So that's something that's really important.
[1555.86 → 1556.18] But...
[1556.18 → 1557.68] And now we can do.
[1558.60 → 1563.32] Do you have anyone actually trying to buy things from Rails Dog Radio and wondering why other products don't ship?
[1563.32 → 1564.08] Yeah, occasionally.
[1566.00 → 1568.06] We try to warn them that it's not a real store.
[1568.62 → 1570.42] I don't even know if it takes real credit cards.
[1571.98 → 1572.66] I don't know.
[1572.76 → 1572.94] Yeah.
[1573.08 → 1573.64] But sorry.
[1574.42 → 1575.70] We'll issue a refund promptly.
[1576.12 → 1576.62] No, there's really...
[1576.62 → 1577.76] Nobody's cards are getting charged.
[1577.94 → 1578.82] So, yeah.
[1578.98 → 1579.24] I know.
[1579.48 → 1579.70] Whatever.
[1579.84 → 1580.50] We do our best.
[1580.66 → 1581.96] So you do have...
[1581.96 → 1585.28] This is the online sandbox, but you do have an admin view of this, too.
[1585.28 → 1591.44] If you want to unfurl your own sandbox, you've got a script that will crank up a new Heroku instance for them and email it.
[1591.52 → 1591.84] Yeah, yeah.
[1591.84 → 1591.92] Yeah.
[1592.34 → 1593.38] So now that won't...
[1593.38 → 1597.76] So you won't get a Rails Dog Radio one, but maybe we'll change that in the future.
[1597.86 → 1600.84] But the thing with Rails Dog Radio is there's a huge actual product.
[1601.20 → 1602.24] So our friends...
[1602.24 → 1602.90] I should plug them.
[1603.00 → 1603.10] Okay.
[1603.14 → 1607.34] So if you do want a satellite radio, you should go to tssradio.com.
[1607.34 → 1612.64] And, you know, they were nice enough to donate the product inventory.
[1612.64 → 1614.64] So, you know, we really...
[1614.64 → 1616.94] A big problem with e-commerce is not having enough real data.
[1616.94 → 1624.04] So we used a ton of real product data and SKUs and things like this just to make it kind of realistic.
[1625.56 → 1626.78] And so that's...
[1626.78 → 1628.44] So that was nice.
[1628.60 → 1633.74] And eventually, you know, people have been asking us, we just have to sanitize the data to make sure there's nothing in there that shouldn't be in there.
[1633.74 → 1636.22] And we'll probably make that open source, too, the data set.
[1636.48 → 1638.18] But, yeah.
[1638.30 → 1641.50] So people want to be able to see the back-end admin functionality.
[1642.00 → 1643.20] And that's often very difficult.
[1643.34 → 1644.48] But all you have to do is plug in your email.
[1644.80 → 1647.08] And, like you said, it'll spin up a Heroku instance.
[1647.20 → 1649.12] It won't be Rails Dog Radio, but you'll be able to log in.
[1649.40 → 1656.88] And, you know, like a lot of these demos for open source stuff, you know, just like Spree included, it used to be like every half hour or hour we wipe out the database, you know.
[1656.88 → 1668.52] So this way you get 14 days to kind of just play with it and, you know, your data and your work won't be wiped out, and you can kind of just show it to a client, noodle around on it, you know, just to get an idea for how it works.
[1669.86 → 1681.74] So the only thing I was disappointed with, I kicked the tires on that last night, does I guess I was expecting, since I used the same email address, to have ownership on the GitHub or the Heroku repo and that deal.
[1681.90 → 1682.82] That would have been a nice touch.
[1682.82 → 1690.02] Yeah, there's one tiny technical flaw there is we use Amazon S3 for the image attachments.
[1690.48 → 1692.44] So our S3 credentials are tied into the account.
[1692.66 → 1699.20] So we haven't quite put the effort into work around that solution where we can, like, transfer ownership to a different account.
[1699.26 → 1701.86] But that's definitely something we might look at in the future.
[1701.86 → 1705.28] So, Brian, before we started recording, we were talking a little bit about Spree Under the Hood.
[1705.40 → 1708.74] And one of the components was one of your projects, Deface.
[1708.84 → 1711.10] Why don't you give a quick overview of what it does?
[1711.10 → 1720.48] Sure. Well, yeah, so Deface is like a generic Rails 3 library that basically solves a big problem we had.
[1720.56 → 1731.74] Well, not a big problem, but a problem we had with Spree, earlier versions of Spree, where obviously it ships with a large amount of views, you know, for all the back end and for the relatively basic front end.
[1731.74 → 1737.14] And a lot of times, you know, when you're customizing Spree, you just want to make one small change.
[1737.26 → 1743.22] You want to, you know, add in an extra button here or, you know, add an extra column to a table or something relatively trivial.
[1743.22 → 1753.70] And while we did have kind of helper hooks kind of dribble all over the place in the views to try and help you kind of hook stuff in there, invariably it was never in the right place.
[1754.14 → 1760.86] And, like, during my time at Rails Dog, I literally designed hundreds of Spree stores and, like, constantly putted my head up against this problem.
[1760.86 → 1766.82] So Deface was kind of my pet project to solve my own, scratch my own edge of the true open source sense.
[1767.64 → 1773.30] So what Deface lets you do is, well, first, what I was just getting rid of the hooks from the views.
[1773.30 → 1790.06] And basically, you can target a view in Rails and basically, using CSS selectors, you can target any element on the page, be it, you know, a DIV tag or actual ERP Ruby code itself.
[1790.46 → 1795.88] And you can substitute that then with a different snippet of code or render a partial into the file.
[1795.88 → 1799.96] So it's a pretty complicated process.
[1800.08 → 1802.12] It took me a while to figure out exactly how to make it work.
[1802.12 → 1810.92] But under the hood of Deface, it basically hooks into the Action View part of Rails.
[1811.08 → 1820.56] And when it's actually compiling the template from the file on the disk, it hooks in there and grabs the source and basically does some parsing on the source of the ERP file
[1820.56 → 1826.46] and converts it into basically XML that then is passed off to Nokogiri.
[1826.74 → 1834.30] And then you can use, you know, all the power of Nokogiri's amazing CSS selectors to target anything within that file and make changes.
[1834.30 → 1838.16] You can, you know, insert after, insert before, you know, replace, replace contents.
[1838.66 → 1840.04] You can set attributes on tags.
[1840.16 → 1842.22] You can just completely remove something from the file.
[1843.18 → 1849.10] And then it kind of decompiles it back into proper ERP code and then just hands it back to Rails.
[1849.10 → 1851.62] Rails and then, you know, Rails renders the view accordingly.
[1851.88 → 1858.14] So it basically removes the need of having to, you know, copy over an entire view to customize it.
[1858.54 → 1864.72] Or it also gives you the ability then to kind of layer up changes one after the other.
[1865.06 → 1870.68] So, you know, say like this brief social extension could include a link to log in via Facebook.
[1870.68 → 1881.36] And then the Rails log radio team can come along later, retarget that override and make some more changes after that to, you know, changes colour or whatever, add in some extra tags or something like that.
[1881.46 → 1889.14] So it basically makes views as customizable as possible without ever having to touch the underlying view.
[1889.14 → 1899.40] So, and the benefit there is that when Spree upgrades between versions, you know, you don't have to go back and, you know, look at all the views you've overridden and try and merge in the changes or anything like that.
[1899.52 → 1906.50] You know, provided that the original HTML hasn't changed too much, you know, your hook will still work, and it will still catch on to the same place in the file.
[1906.50 → 1915.46] And the face then also gives you this kind of what I call upgrade protection where you can pass in the original markup that you're replacing.
[1915.98 → 1926.76] So if the face notices a change, you know, if you upgrade Spree and then when the override is happening, the face notices that, well, the original HTML doesn't match what you say it should match, then it will warn you.
[1927.00 → 1930.60] So you get kind of built-in protection that way too.
[1930.62 → 1933.12] So it's essentially monkey patching your views.
[1933.12 → 1939.04] Basically, yeah, it's like taking the decorator pattern for, you know, it's like classy battle for your views.
[1939.16 → 1939.88] Yeah, that's it exactly.
[1940.34 → 1945.20] So sadly, the README says ERA only, no Hall support.
[1946.50 → 1955.12] Yeah, well, there's a big issue there is it's impossible to get Hall into, you know, some sort of XML representation that Nokogiri could handle.
[1955.12 → 1965.84] So that kind of sank that possibility unless somebody is willing to write a CSS selector library for Hall in maybe a while before the face supports it.
[1966.08 → 1971.12] But we are looking at allowing you to supply Hall as the replacement markup.
[1972.28 → 1974.28] So that may appease the Hall gods.
[1975.10 → 1975.22] Yeah.
[1975.32 → 1980.10] So you could you could just say, hey, replace this section with this snippet of Hall.
[1980.34 → 1980.70] Basically.
[1981.12 → 1981.26] Yeah.
[1981.62 → 1981.96] Gotcha.
[1981.96 → 1986.26] Now, I'm finding I'm using a lot more engines and projects these days.
[1986.40 → 1993.44] And it seems like the common thread around all of these is I want to turn off the entire view layer from a lot of these projects.
[1993.44 → 1996.84] I'm finding that models and controllers are pretty well thought through.
[1996.98 → 2002.12] But views tend to be very project specific and a lot of times just not very well written.
[2003.12 → 2003.28] Yeah.
[2003.42 → 2003.50] Yeah.
[2004.54 → 2005.26] Sorry, Sean.
[2005.34 → 2007.68] That's technically true for Spree as well.
[2007.68 → 2009.60] And we kind of make that point.
[2009.90 → 2015.24] We keep the front end of Spree very, very basic because everybody wants their store to look different.
[2015.40 → 2022.04] So we put, no, we just have a very semantic, very basic, easy to start front end in terms of views that you can customize.
[2022.30 → 2025.52] But invariably, most people will almost throw that completely away.
[2025.94 → 2027.94] But then the inverse of that is the back end.
[2028.12 → 2030.12] You know, it's a very full feature back end.
[2030.46 → 2031.48] It looks pretty nice.
[2031.48 → 2035.60] And people don't really care too much about what their back end looks like.
[2035.66 → 2043.54] They just want to get in there and process orders and, you know, deliver shipments and edit products and do all the fun jobs of running an e-commerce store.
[2044.06 → 2053.82] So that's where Deface really shines in that it lets you just, you know, make your small little changes to the admin side of things without, you know, shooting yourself in the front for future upgrades, basically.
[2053.82 → 2063.74] So we've actually, when kind of in tandem with this Deface and Rails Dog radio effort, we actually took the views, the front end views in Spree.
[2063.82 → 2067.52] They were already pretty plain, and we made them really plain.
[2067.62 → 2072.90] In fact, when people started seeing the code, they thought that the asset pipeline was broke because there was like no styling.
[2073.32 → 2082.10] And, you know, we're going to have to put, in fact, we're going to have to put some kind of theme, you know, we're going to have to just put a default theme in there just so people don't freak out totally when they see it.
[2082.10 → 2086.06] Because, you know, we really went with a very semantic HTML.
[2086.74 → 2092.02] We took, you know, we took that to the extreme and was like, all right, you know what, like people, this is, the views really are a throwaway.
[2092.26 → 2096.54] So, but if we made them, you know, basic enough, you could probably leverage them with a theme.
[2097.12 → 2098.04] So that's what we've done.
[2098.12 → 2106.18] So we totally, I agree that the front end stuff, particularly customer facing stuff is way too specific.
[2106.42 → 2107.94] I mean, it's not even a question of writing a good view.
[2107.94 → 2112.98] It's just, you know, the needs are just too specific for any one particular store.
[2113.14 → 2114.56] So we assume you're going to throw that away.
[2115.36 → 2119.66] So I would imagine a big piece of this project is just communicating news out to the community.
[2119.84 → 2122.74] So you mentioned hiring someone for that role.
[2122.82 → 2123.78] What's the latest on that?
[2124.68 → 2124.94] Yeah.
[2125.08 → 2130.28] So, you know, we're really pleased to have hired new community managers.
[2130.48 → 2133.82] So starting in a couple of days here will be Ryan Big.
[2133.82 → 2138.24] Um, so your audience, some of your audiences at least would be familiar with him.
[2138.46 → 2138.66] Oh, yes.
[2139.16 → 2139.46] Yeah.
[2139.90 → 2146.02] Um, so, uh, Ruby Hero, uh, award winner last year and Rails 3 in action, et cetera, et cetera.
[2146.16 → 2156.38] And, you know, so, um, I mean, really the ideal, uh, community manager, you know, when I look at the criteria, so we were very, you know, fortunate to get him.
[2156.38 → 2163.04] He, he was working on a spree project when I contacted him and, uh, we just happened to kind of catch him at the right time.
[2163.04 → 2172.10] And, um, you know, but his dedication to really making open source awesome and helping people learn and all of that.
[2172.14 → 2177.04] I mean, there's, you'd be hard-pressed to find a better person for that job in, in almost any programming language.
[2177.04 → 2182.50] So, so great guy, very technical and, but also very helpful and supportive.
[2182.50 → 2189.32] And we really want to try to, so hiring a community manager in general was an effort, you know, was a goal of ours with the funding.
[2189.32 → 2196.28] And interestingly, you'd be surprised that like the idea came from somebody sort of on the VC side of it, right?
[2196.30 → 2199.16] Like a business type person told me, Hey, you should hire a community manager.
[2199.16 → 2205.10] So, um, it's cool that, you know, it's not all like, um, and we were like, yeah, absolutely.
[2205.22 → 2208.98] I mean, and, and Brian and I are really, you know, doing a lot of the running the community.
[2209.08 → 2210.94] We have a couple other core members that help as well.
[2211.00 → 2217.14] And, but this guy, you know, Ryan will be just, that'll be 100% his job.
[2217.14 → 2217.36] Right.
[2217.40 → 2226.80] So, you know, we'll continue to help and, and, you know, both in a, you know, on the for people who have the paid support and the free community, you know, IRC and mailing list and stuff.
[2226.80 → 2232.86] But, you know, um, we wanted somebody who's, uh, you know, whose sole job was, is to help the community.
[2232.86 → 2238.80] And, and, um, you know, we could use some more Ryan big love for our documentation.
[2239.70 → 2245.88] Um, and he's already, you know, he hasn't started, and he's already, you know, he's already helping a lot with a name spacing issue.
[2245.88 → 2250.12] Uh, so he, he's already got several dozen commits, uh, under his belt, and he hasn't even started.
[2250.12 → 2253.44] So we're, uh, hoping for great things from him.
[2253.44 → 2255.46] Well, congratulations to you and to Ryan.
[2255.46 → 2257.28] And that definitely would be win-win.
[2257.54 → 2261.16] See that, uh, TB Dubs is also a backer and an advisor.
[2261.38 → 2266.74] I want to know if he has given you grief over your, um, lack of semantic versioning.
[2267.64 → 2268.84] Um, you're talking about Mambo?
[2269.54 → 2269.86] Yes.
[2270.26 → 2272.60] With, uh, you know, you're at Spree 07.
[2273.14 → 2274.16] Oh no, he hasn't.
[2274.22 → 2274.32] No.
[2274.36 → 2275.28] Is that a big thing for him?
[2275.34 → 2275.48] Yeah.
[2275.48 → 2277.76] If you go to semver.org, that's E-M-V-E-R.
[2278.02 → 2281.12] So basically, if it's a production, it should be 1.0.
[2281.18 → 2282.28] We are guilty of this as well.
[2282.54 → 2282.56] So.
[2282.70 → 2282.90] Okay.
[2282.94 → 2284.16] No, it will be, it will be.
[2284.16 → 2288.74] So the next version will be, you know, uh, well, whatever within the end of the year,
[2288.78 → 2289.80] we're going to be at 1.0.
[2290.80 → 2294.22] Cause there's a 0.80 that's, so we're, we're working on the 1.0 now.
[2294.22 → 2298.00] So like within, by the time this broadcast airs, the master branch will probably be labelled
[2298.00 → 2298.44] 1.0.
[2298.44 → 2302.54] And, you know, we just kind of, it just cut the naming just kind of got away with us.
[2302.58 → 2308.78] We had 0.1, 2, and we got to 0.9, and then we weren't ready.
[2308.78 → 2310.06] So we were like, okay, 0.10.
[2311.16 → 2315.14] Um, and you know, we wanted to reserve the right to make major changes.
[2315.14 → 2317.10] I guess we could have done 1.0, 2.0, 3.0.
[2317.80 → 2322.86] Um, but it really took a couple of years to kind of, you know, I mean, it was running production,
[2322.86 → 2327.68] but we were never fully satisfied and, and, you know, we're, we're there now.
[2327.72 → 2332.12] Like we feel like it'll, it'll keep moving forward, but soon everybody will be happy with
[2332.12 → 2334.28] a 1.0, uh, release.
[2334.28 → 2335.18] You know, we do the same thing.
[2335.24 → 2340.42] This will be episode 0.6.9, and we get, uh, tweets at least once a week, you know, your
[2340.42 → 2341.74] version numbers aren't semantic.
[2341.74 → 2342.06] Yeah.
[2342.20 → 2347.36] So, yeah, well, uh, you know, whatever we're doing our best, but, um, you know, we didn't
[2347.36 → 2349.66] want to signal that it was beta software really.
[2349.74 → 2352.72] I mean, you know, like this is, I guess in the Google, you know, sort of like extended
[2352.72 → 2353.06] beta.
[2353.88 → 2360.98] Um, and, but you know, like, I do feel like we've reached this 1.0 point where it's like, okay,
[2360.98 → 2364.24] we're going to make a little bit of disruption here where the namespace and things.
[2364.38 → 2369.22] You know, break a couple more things and, you know, well, we'll get people, um, straightened
[2369.22 → 2369.38] out.
[2369.44 → 2372.38] But, but I think like rails and spree have converged a lot.
[2372.40 → 2375.76] Like there were so many things that we were doing that rails wasn't doing.
[2375.76 → 2379.12] And, you know, we're in a lot more alignment with rails now.
[2379.12 → 2381.94] Like, so we were just, this is going back to this engine discussion.
[2382.00 → 2383.28] You know, we had our own extension system.
[2384.18 → 2387.22] It, you know, it would have been fine if we had nothing, and then we could have just used
[2387.22 → 2387.84] rails engines.
[2387.84 → 2392.20] But since we had something that was almost like rails engines, we had a lot of work to back
[2392.20 → 2392.56] it out.
[2392.56 → 2397.02] And, you know, with the I 18 and stuff, you know, we were using globe, we were using
[2397.02 → 2398.00] globalize, right, Brian?
[2398.12 → 2405.42] Like, you know, before, before it really became part of rails, I 18 and, um, you know, so there
[2405.42 → 2408.06] were a lot of things that we were doing that were kind of ahead of the curve.
[2408.06 → 2410.84] I mean, that we were, we were, we weren't, you know, leading the charge.
[2410.88 → 2412.48] We were just kind of taking other people's great stuff.
[2412.48 → 2417.80] But, you know, uh, a lot of that we've kind of rails has sort of caught up to some of those
[2417.80 → 2418.52] great ideas.
[2419.24 → 2423.92] And I think we're closer in sync with, um, what rails is doing.
[2424.02 → 2426.88] I think rails is kind of stabilizing too.
[2427.10 → 2428.90] So I think, you know, it's, it's time now.
[2428.98 → 2429.12] Yeah.
[2429.20 → 2432.14] I mean, there are probably people who aren't going to use it because it's not one else.
[2432.14 → 2433.46] So we should probably fix it.
[2433.46 → 2435.62] So we're to the point of the show.
[2435.68 → 2440.38] Now we're going to ask you kind of turn it around and ask each of you, what is on your
[2440.38 → 2446.48] open source radar and what project other than spree that when you have a spare Saturday
[2446.48 → 2447.82] afternoon, what do you like to hack on?
[2449.10 → 2449.92] Yeah, sure.
[2449.92 → 2457.92] So, um, I've been working, um, on a an extension to the face recently, um, that uses an external
[2457.92 → 2462.28] library, which is called a ACE, which is the Ajax, uh, cloud nine editors.
[2462.28 → 2470.60] And it basically gives you, uh, kind of very rich, uh, browser based, um, syntax highlighting
[2470.60 → 2476.92] editor for stuff like CSS and, uh, JavaScript and, uh, uh, HTML and stuff like that.
[2477.20 → 2479.04] So yeah, it's, it's a pretty cool project.
[2479.28 → 2482.76] Is that going to, Brian, is that going to make its way into the, the theme editor for spree
[2482.76 → 2483.14] eventually?
[2483.30 → 2484.74] Is that, that's where it's going.
[2484.86 → 2485.00] Yeah.
[2485.18 → 2485.38] Yeah.
[2485.38 → 2488.76] So yeah, Brian also has a pretty cool theme editor for deface that he's working on.
[2488.76 → 2492.26] So, um, uh, you know, other, I mean,
[2492.28 → 2499.02] now that I'm running the company and, and full bore on spree, I don't look at as much
[2499.02 → 2500.56] open source as I should, probably.
[2500.76 → 2505.44] But I think there's some, some projects that are on my radar, um, that you will probably
[2505.44 → 2509.86] see in a spree context soon are, um, well, I've always been kind of interested in radiant
[2509.86 → 2513.84] and now more so, or not more so, but more recently refinery.
[2513.84 → 2520.12] Um, so at rails dog, they use refinery for a, a non-spree project and, um, refinery has
[2520.12 → 2521.28] been very aggressive about moving.
[2521.28 → 2524.32] It's in many ways, it's a project that's similar to spree.
[2524.42 → 2525.38] So I would keep an eye on that one.
[2525.50 → 2527.34] Like it, it's been going on for a few years.
[2527.34 → 2532.58] They have over a hundred contributors, you know, they're dedicated guys that are, and they're
[2532.58 → 2537.84] doing a lot of, um, they're keeping up with rails and, you know, it's just very active.
[2537.84 → 2543.84] And I think there's a big cry from the CMS community for, oh, we need better e-commerce
[2543.84 → 2544.58] and vice versa.
[2544.58 → 2547.74] So I think, you know, there are some interesting possibilities there.
[2548.16 → 2554.08] Um, the other thing is I'm interested in, um, uh, rails admin, one of your previous guests,
[2554.24 → 2557.10] a recent guest, Eric, uh, I won't pronounce his last name.
[2557.20 → 2557.64] Michael's over.
[2559.02 → 2559.38] Yeah.
[2559.44 → 2559.94] Michael's over.
[2560.14 → 2564.40] Um, he, uh, I think he's onto something there.
[2564.44 → 2565.74] I mean, there are some interesting projects.
[2565.74 → 2571.40] Um, I don't know that we can use rails admin for spree, but we'll probably end up borrowing
[2571.40 → 2572.10] some from it.
[2572.16 → 2578.86] And, you know, in general, I have an interest in, um, uh, an Uber sort of admin and admin,
[2579.10 → 2582.56] you know, that could be pluggable, that could be really used across engines, I think.
[2582.72 → 2588.46] So that, that's probably the biggest barrier to integrating with, um, radiant or refinery
[2588.46 → 2594.58] or browser or any other CMS is like, you know, anything that requires authentication, um, or
[2594.58 → 2599.62] authorization, it's, it's going to be a little bit of an issue until we solve this problem.
[2599.80 → 2604.22] So, you know, um, having some kind of generic interface that you can then plug your security
[2604.22 → 2607.70] mechanism of your choice in and then plug in spree and refinery and whatever.
[2607.98 → 2609.02] I think that'll be cool.
[2609.02 → 2611.28] And I know, um, Ryan was sort of excited about that.
[2611.28 → 2615.68] So, so that's an open, new open source project that we'll probably start that we, that you
[2615.68 → 2617.38] can look for and that we'll want help with.
[2617.38 → 2621.32] And we'll probably be borrowing, you know, from Rails admin and some of the other cool
[2621.32 → 2622.38] stuff that people are working on.
[2622.66 → 2626.74] Well, the Django guys are laughing at us because they have a lot of that out of the box, but
[2626.74 → 2631.38] hopefully the Rails community can pick a winner in this space, and we can get some, uh, nice,
[2631.54 → 2632.32] easy to use admin.
[2632.32 → 2636.92] I'm not that familiar with Django, but I would certainly not laugh at that at any point.
[2636.98 → 2637.78] I think it's a great idea.
[2637.94 → 2642.96] I mean, I remember Yehuda Katz at, you know, Hailstone, were you on the Vegas one, um, win?
[2644.00 → 2644.64] I was, yes.
[2644.64 → 2645.84] You were there, I saw you there, you spoke.
[2646.38 → 2651.54] So, um, you know, Yehuda gave his talk and he was talking about, um, Django, I think
[2651.54 → 2655.22] specifically, and he was saying that, you know, we should build on the, on the shoulders
[2655.22 → 2658.40] of those who come before us, no matter how small or something, some kind of reference
[2658.40 → 2660.68] to stature there.
[2661.04 → 2663.04] But, uh, yeah, a good idea is a good idea.
[2663.04 → 2664.00] I mean, and there's good.
[2664.20 → 2666.40] I meant laughing because Django has this out of the box.
[2666.54 → 2667.08] I think we need to.
[2667.08 → 2667.72] Oh, I know, I know.
[2667.84 → 2672.04] And people would, you know, deride other frameworks and things, but hey, there might be things that
[2672.04 → 2675.66] aren't good about Django, but I think, you know, if they've, and I don't know much about
[2675.66 → 2678.88] it, but if they have got that, yeah, that's, that's something that we, we should be taking
[2678.88 → 2679.50] a page out of.
[2679.58 → 2683.46] And I mean, Yehuda made a big point of that and saying, hey, we need to have their elements
[2683.46 → 2687.62] of these communities that are, that are perfect and things they're doing that we should
[2687.62 → 2688.96] shoot, you know, uh, build on.
[2689.00 → 2691.80] And that was something that he very much envisioned when he was talking about the Rails 3
[2691.80 → 2693.68] engines a few years ago now.
[2693.68 → 2698.70] And, you know, WordPress and other communities like, you know, one of our advisors is, um,
[2698.70 → 2700.72] Dries Bayard, the creator of, um, Drupal.
[2700.82 → 2704.70] He's, he's an advisor to the not to the Spree project, but to the Spree company.
[2705.04 → 2710.26] And, you know, I mean, I've always been an admirer of the Drupal ecosystem and I mean,
[2710.26 → 2716.10] not, not all of it, but, and I'm not a big PHP fan, but they've got a great, huge, vibrant
[2716.10 → 2720.92] ecosystem that powers like, you know, a big part of the internet and same with the WordPress
[2720.92 → 2721.26] guys.
[2721.32 → 2725.88] And, you know, the people who, um, our investors are the same investors behind WordPress.
[2726.00 → 2729.34] So I definitely think that we have a lot to learn from other open source projects.
[2729.34 → 2733.16] That's a big, you know, the, the better, you know, the more we kind of accept that the
[2733.16 → 2734.44] better our, our stuff will be.
[2734.64 → 2738.10] Well, we're definitely excited about the news, uh, the, uh, the venture funding, hopefully
[2738.10 → 2743.84] it'll, uh, lead to some better docs and, uh, a little bit more of a community curation
[2743.84 → 2749.46] as, uh, staffing, uh, permits, but we look forward to the upcoming conference and, uh, keep
[2749.46 → 2751.36] us posted on, uh, the roadmap for spree.
[2751.92 → 2752.30] Yeah.
[2752.32 → 2754.68] We look forward to being enthralled by your, your talk.
[2756.78 → 2757.38] Pressure's on.
[2757.70 → 2758.42] No pressure.
[2758.96 → 2759.50] All right.
[2759.54 → 2759.98] Thanks fellas.
[2760.52 → 2760.82] All right.
[2760.82 → 2761.16] Thank you.
[2761.16 → 2761.22] Thank you.
[2779.46 → 2792.04] Thank you.
[2792.14 → 2792.82] Thank you.
[2792.82 → 2822.80] Thank you.
