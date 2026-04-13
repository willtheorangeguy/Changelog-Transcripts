[0.00 --> 10.02]  Welcome to Practical AI.
[10.44 --> 17.50]  If you work with artificial intelligence, aspire to, or are curious how AI-related technologies
[17.50 --> 20.78]  are changing the world, this is the show for you.
[21.46 --> 26.34]  Thank you to our partners for helping us bring you practical AI each and every week.
[26.34 --> 31.32]  FASI.com, fly.io, and typesense.org.
[34.64 --> 39.96]  Hello, it's your co-host, Daniel here.
[40.08 --> 45.70]  Just wanted to let you know about an awesome event that's coming up this December of 2023.
[46.08 --> 48.40]  It's called the Advent of Gen AI.
[48.74 --> 54.22]  It's a hackathon that's being put on by Intel's liftoff program and Prediction Guard,
[54.22 --> 58.74]  and it's going to be a seven-day journey into the world of generative AI.
[59.46 --> 63.52]  You're going to get access to some really cool hardware from Intel.
[63.78 --> 70.96]  You'll also get access to run prompts through the latest open access LLMs via Prediction Guard.
[71.50 --> 77.00]  And every day of the challenge, you'll get a new chance to show your generative AI skills
[77.00 --> 78.78]  and learn a bunch of cool stuff.
[78.92 --> 80.92]  So I encourage you to register.
[81.28 --> 82.20]  It's totally free.
[82.20 --> 89.00]  You can take part and learn all of the cool generative AI things that you're hearing about on this podcast.
[89.52 --> 93.06]  Find out more at adventofgenai.com.
[93.28 --> 96.26]  That's adventofgenai.com.
[96.26 --> 116.52]  Welcome to another episode of Practical AI.
[116.86 --> 118.50]  This is Daniel Whitenack.
[118.50 --> 126.30]  I am the founder at Prediction Guard, and I'm joined as always by Chris Benson, who is a tech strategist at Lockheed Martin.
[126.54 --> 127.22]  How are you doing, Chris?
[127.36 --> 128.38]  Doing very well, Daniel.
[128.46 --> 129.12]  How's it going today?
[129.66 --> 130.78]  Oh, it's going great.
[130.92 --> 137.66]  You know, as our listeners know, or at least the ones that have listened to a lot of our shows,
[138.06 --> 141.70]  my wife owns a business, which is an e-commerce business.
[141.82 --> 142.52]  It's quite a business.
[142.52 --> 153.42]  And next week, as we're recording this, for those listening at a future date, next week is Thanksgiving here in the U.S., which means next Friday, basically,
[153.80 --> 164.84]  well, it's already sort of started, but next Friday to that following week, Black Friday, Cyber Monday, is a huge retail and e-commerce extravaganza in our world.
[164.84 --> 180.18]  And so I'm really excited because leading up into that today, we've got the expert with us, Russ Mashmeyer from Shopify, who is project lead for spatial commerce and Magic Labs at Shopify.
[180.48 --> 181.02]  Welcome, Russ.
[181.36 --> 182.34]  Hey, thanks, guys.
[182.44 --> 183.80]  I'm super excited to be here.
[184.16 --> 187.98]  It's been cool to follow along with the podcast and just super stoked to chat with you guys today.
[188.48 --> 189.30]  Yeah, for sure.
[189.30 --> 206.54]  Well, I'm coming into this super excited because over the past, well, it's been 10 years, my wife's business, and at least nine of those years, they've been on Shopify, which means I have been in Shopify.
[207.10 --> 209.12]  I've dug into all the data behind.
[209.34 --> 211.00]  I've worked with the Shopify API.
[211.36 --> 216.80]  I've built chatbots on top of Shopify to sign up wholesale customers.
[216.80 --> 220.66]  I've dug into the liquid code on the site.
[220.82 --> 226.44]  So I'm all about whatever I can learn from you today and hear about what's going on at Shopify.
[226.80 --> 228.82]  I am super excited.
[229.26 --> 231.76]  I didn't even know he was that much into it, Russ.
[232.86 --> 242.90]  Well, when you're the husband of an e-commerce entrepreneur and you're also a data scientist, occasionally favors are asked.
[243.58 --> 245.54]  I'm feeling very third wheel now.
[245.54 --> 246.46]  I just wanted you to know.
[246.80 --> 259.82]  Well, over that time, it's been cool to see how Shopify has added so many amazing features and is really powering a lot of huge brands, not only small brands, but larger brands.
[260.38 --> 262.72]  I'm sure you all are gearing up for a great...
[262.72 --> 268.68]  First off, I just have to ask, what is the week leading up to Black Friday, Cyber Monday like at Shopify?
[269.32 --> 271.92]  You know, it's very busy, as you can imagine.
[272.28 --> 273.98]  I was going to say, what a loaded question.
[273.98 --> 277.94]  It's the kickoff to the biggest shopping season of the year.
[278.62 --> 283.24]  Shopify powers just an enormous amount of that holiday shopping season.
[283.88 --> 286.48]  So you can imagine the teams internally are prepping for it.
[286.56 --> 297.44]  They are getting products like locked in place and just, you know, operating at their optimal, maximal performances just to support the load that's coming in this upcoming weekend.
[297.44 --> 309.56]  But, you know, every year we also launch this really cool live globe that's a 3D visualization of all the live data and orders happening all around the globe in real time.
[309.66 --> 312.78]  So you see, like, you know, orders streaming around this globe.
[312.96 --> 317.14]  And so this year, I've been also helping to lead some of those efforts.
[317.26 --> 320.36]  I'm really excited for that to get its annual debut this year.
[320.36 --> 324.22]  You might see some ideas we talk about today appear in there.
[324.42 --> 324.66]  Cool.
[325.22 --> 329.78]  Yeah, it's like the live view of Santa going around the world at light speed.
[329.96 --> 330.36]  There you go.
[330.94 --> 332.90]  Totally the Santa map for entrepreneurship.
[332.90 --> 337.94]  There's all sorts of interesting things that Shopify is doing.
[337.94 --> 345.32]  But specifically here, we're talking about AI and what you're doing in regards to that.
[345.60 --> 358.94]  Maybe as we jump into that, could you describe a little bit from a person that's embedded in this kind of e-commerce world and seeing what a lot of people are doing in various industries, various stores?
[358.94 --> 367.18]  How do you view the impact of AI on e-commerce specifically right now and kind of where it's headed?
[367.40 --> 372.68]  Like, where are we seeing the biggest impact in terms of AI right now in e-commerce?
[372.90 --> 380.94]  And I know we're going to be talking about some of the recent things you've done, but kind of across the board, how does it look to you and what are people thinking about?
[380.94 --> 397.32]  Yeah, I mean, Shopify was pretty early in kind of this new wave of AI capability to say like, hey, whoa, like this is a completely new class of possibility for the tools that we make for merchants and the shopping experiences that our platform provides on the other end to shoppers.
[397.86 --> 403.52]  And Shopify is really just kind of here to make commerce accessible and entrepreneurship accessible to everyone.
[403.52 --> 408.96]  And we're really excited about these tools as a way to kind of further democratize entrepreneurship.
[409.40 --> 419.98]  There are so many things you have to create and produce and ideas to develop and knowledge to gain about markets and positioning and strategy and branding.
[420.58 --> 427.24]  There are so many tasks that entrepreneurs have to learn and develop along the road to building a successful business.
[427.24 --> 439.30]  And LLMs, generative AI are all incredibly powerful tools to help accelerate that learning curve for new merchants and to help them kind of get up that curve faster and build better businesses.
[440.04 --> 440.54]  I'm curious.
[440.80 --> 446.52]  We all hear, you know, us consumers in the world, we hear about AI impacting retail and stuff.
[446.52 --> 457.46]  But for those of us who don't have as much of a view on it, can you kind of talk about how you've seen retail change in these years since AI is really the last few years with AI really kind of getting in everywhere?
[457.94 --> 460.44]  What are some of the things that might surprise people?
[460.92 --> 466.10]  You know, they kind of know there's AI there in the background, but they don't really know how it plays or what it is.
[466.44 --> 467.92]  You know, surprise us a little bit.
[467.96 --> 470.96]  Like, what's something I go, oh, wow, I didn't realize that.
[470.96 --> 476.50]  Well, you know, I mean, we started by just like adopting these tools in our engineering practice to begin with.
[476.64 --> 483.22]  We got some of the early previews of Copilot and started using that to help accelerate some of our development work early on.
[483.40 --> 489.44]  But really the place where we've seen it have the biggest impact in the near term is on tools for merchants.
[489.72 --> 499.10]  You know, like when we think about who our core customers are as Shopify, it's the merchants who we power with our platform and enable them to do really creative, amazing things.
[499.10 --> 501.88]  You know, at this scale that they never maybe thought was possible for them.
[502.02 --> 502.20]  Right.
[502.78 --> 515.40]  And AI is, again, like sort of a way to accelerate that work and give them more time back to, you know, instead of spending an hour and a half, like trying to craft the perfect product description, because you're not totally sure exactly what makes a good product description.
[515.40 --> 524.30]  You know, last year at our winter edition, we shipped a really simple tool where you just like enter in like a couple of raw details about your product and hit the magic button.
[524.50 --> 533.46]  And it just writes a well-crafted narrative product description that speaks to product benefits and all the great standard practices of writing a good product description.
[533.60 --> 536.92]  And you get that in seconds versus an hour of human toil.
[536.92 --> 545.56]  And so the place where we've seen AI really have the biggest impact early on is just in accelerating the work that merchants are already doing and allowing them for.
[546.52 --> 550.92]  And well, I guess it's e-commerce, but also like web content development.
[550.92 --> 554.62]  It's a very like multimodal thing, right?
[554.66 --> 556.56]  Like you've got these product descriptions.
[556.56 --> 557.68]  That's part of it.
[558.02 --> 559.68]  You've got product imagery.
[559.68 --> 561.92]  You've got website layout.
[561.92 --> 567.28]  You've got potentially ads and integration with like other platforms.
[567.46 --> 576.98]  Talk a little bit about like within that space, because there's so many, as you mentioned, there's so many tasks to address within that space.
[576.98 --> 591.22]  As Shopify kind of looks at the merchant experience, how have you narrowed down on the particular problem sets that merchants really want to hand off versus like those things?
[591.22 --> 599.18]  I know also from just being in it, like, you know, marketing teams love to get in there and tweak things and like be part of the process.
[599.18 --> 606.30]  But they also really don't want to do certain things, too, or things that are just kind of grunt work, essentially.
[606.30 --> 608.90]  That sounds like it's coming from experience right there.
[609.00 --> 609.16]  Yeah.
[609.46 --> 609.78]  Yeah.
[610.70 --> 620.24]  I mean, we have a word that we use at Shopify, you know, toil, this idea of like work that kind of has to be done, but isn't desirable work to do.
[620.48 --> 623.14]  And so we look for toil that merchants do.
[623.24 --> 635.08]  And so we spend an enormous amount of time sitting down with merchants, talking with them about how they use our platform, what they want more out of our platform, what they wish they could be doing with their business, what they are doing with their business.
[635.08 --> 640.52]  And from that, we've learned a ton about, you know, what are the ways that merchants would like to spend their time?
[640.78 --> 644.58]  And then what are the ways that they just kind of have to, because that's the way the world works right now.
[645.18 --> 655.08]  And so I think the opportunity for us is to find those moments and to build tools, like particularly magic tools, into those spaces that just sort of like make that go away.
[655.08 --> 667.00]  And when we do that, what we hope is that merchants will take that extra time that they have, that hour that they got back, not spending on that one product description or that one blog post or that one email headline.
[667.16 --> 668.88]  They're like, ah, should I use A or B?
[668.96 --> 669.62]  I don't know.
[670.10 --> 679.52]  And just give them a really easy tool to generate that content, make it really high quality, give them the control to adjust if needed, and then publish it really quickly.
[679.52 --> 683.58]  You already mentioned one of those, this sort of product description thing.
[683.80 --> 692.30]  Are there a couple other ones that you could kind of highlight just to give a sense of the breadth of how this technology is applicable in the space?
[692.30 --> 697.16]  So we've launched this suite of tools that we call Shopify magic, right?
[697.20 --> 701.88]  It's our free suite of AI enabled features across our whole Shopify admin.
[701.98 --> 704.52]  And these things crop up in a few different places.
[704.74 --> 710.16]  It can sort of help you take the power of your own data and make it work better for you.
[710.36 --> 716.76]  And, you know, we've applied that in places like email headline subject writing for marketing emails and things like that.
[716.82 --> 720.12]  We've leveraged it in the context of generating blog content.
[720.12 --> 722.46]  Obviously, product descriptions is another.
[723.04 --> 728.98]  And we're obviously really excited about some of the early work that we've also done in the image generation space.
[729.38 --> 733.48]  We recently released a hugging face space that I'm super excited to dig into more.
[733.64 --> 741.96]  I'm sure a little bit later, you know, when you think about a storefront and the kind of content merchants need to produce, it really falls generally into one of two categories.
[742.14 --> 744.28]  It's either text or it's images.
[744.60 --> 748.66]  We're really excited about both of these spaces and helping accelerate merchants there.
[748.66 --> 756.88]  I know Daniel has used the tools a lot, but if you had someone who was a novice and they were getting into business and let's say they're starting it now.
[757.12 --> 758.34]  So they haven't been doing it.
[758.64 --> 759.38]  It's a new store.
[759.48 --> 765.06]  Chris is going to sell what like socks to fund your animal charity.
[765.34 --> 766.14]  Raccoon socks.
[766.28 --> 766.60]  There you go.
[766.84 --> 767.50]  Raccoon socks.
[767.64 --> 768.04]  There you go.
[768.12 --> 768.60]  I like it.
[769.02 --> 770.34]  Christmassy raccoon socks.
[770.44 --> 770.88]  How's that?
[771.10 --> 773.24]  Well, keep the raccoons out of my trash cans.
[773.50 --> 774.20]  Well, the socks.
[774.46 --> 775.20]  That what they do?
[775.20 --> 778.20]  If you want them to, that's no problem.
[779.30 --> 784.64]  For those who are going, what just happened on the show in the world away from technology and AI?
[784.74 --> 789.02]  I'm a wildlife rehabber and right now I have 20 raccoons at my house.
[789.22 --> 790.74]  So that's what that's all about.
[790.92 --> 792.72]  It's a full Christmas party.
[792.88 --> 793.38]  It's a full.
[793.54 --> 793.94]  Yeah.
[794.06 --> 795.58]  Oh, it's quite a Christmas party.
[795.64 --> 797.28]  You put 20 raccoons loose in a room.
[797.36 --> 797.70]  Oh boy.
[797.92 --> 798.32]  Yeah.
[798.32 --> 798.76]  Okay.
[799.42 --> 803.48]  So back to my back to my new store that I just opened up.
[803.78 --> 804.66]  I'm excited.
[804.94 --> 807.74]  I don't have Daniel's depth of experience at this.
[808.12 --> 810.24]  What are all of the amazing things?
[810.34 --> 812.86]  I'm either by myself or I don't have a lot of help.
[813.26 --> 814.80]  Everyone's tossed me to the wolves.
[814.96 --> 818.54]  I've come to Shopify because I know you have all these magical tools.
[818.90 --> 822.76]  Can you tell me a little bit about that experience from a merchant standpoint?
[823.18 --> 825.16]  Like on day one, what am I getting into?
[825.24 --> 827.04]  How should I think about it a little bit?
[827.04 --> 831.76]  And what are those, how do those AI tools directly impact what I want to start doing today?
[832.06 --> 832.74]  Yeah, totally.
[833.22 --> 837.42]  Well, I mean, I think from a merchant's perspective, if they were to log into the admin today,
[837.66 --> 841.90]  you know, I don't think they'd be overwhelmed with like the amount of AI tools, you know,
[841.90 --> 845.74]  sort of all over the, I think today we really started with a focused approach that feels
[845.74 --> 851.08]  super seamless and integrated into just the activities that merchants are already doing.
[851.26 --> 853.14]  For example, auto descriptions.
[853.14 --> 854.34]  Let's say, you know, you're a merchant.
[854.48 --> 856.22]  You've just started building your storefront.
[856.22 --> 860.84]  Like you're super excited to like get that up, put a great face out on the web.
[860.84 --> 864.36]  And you're starting to build out your product catalog.
[864.76 --> 867.62]  You're starting to think about, you know, how do I merchandise my products?
[867.64 --> 868.70]  How do I talk about them?
[868.76 --> 869.44]  You're a new merchant.
[869.54 --> 870.76]  You haven't really done this before.
[870.82 --> 874.28]  You don't know what the best practices are for product descriptions.
[874.56 --> 879.50]  Or, you know, if you want to create some SEO content, kind of market your brand and product
[879.50 --> 880.78]  expertise in the space.
[880.78 --> 885.24]  You can go into your product detail editing page for a product you want to add.
[885.24 --> 887.00]  Just drag and drop your images.
[887.24 --> 890.92]  One of the really cool things, and I'll say this because I'm also product lead for spatial
[890.92 --> 895.84]  commerce, is you can also drag and drop 3D models into that image bin and it'll handle
[895.84 --> 896.70]  it beautifully.
[896.96 --> 899.08]  So there's some cool stuff going down the line with that.
[899.08 --> 900.54]  Raccoon 3D models.
[900.68 --> 901.28]  That's awesome.
[902.06 --> 903.72]  This is going to be an awesome site, Chris.
[904.42 --> 905.50]  Looking forward to it.
[905.58 --> 907.98]  If you've got 3D models, drop them in there too.
[908.16 --> 911.20]  Those will display on your product detail page on your web storefront.
[911.36 --> 915.00]  And then when you get to that, like that challenge of like, okay, now I've got to write a product
[915.00 --> 915.30]  description.
[915.40 --> 916.68]  Oh gosh, I haven't thought this through.
[916.80 --> 918.22]  I'm not really a copywriter.
[918.82 --> 922.42]  You know, I went to business school and maybe I can write things, but like, I don't know what,
[922.54 --> 923.94]  what's a good product description?
[924.08 --> 925.12]  What does that even look like?
[925.12 --> 930.80]  I could go and spend, you know, an hour, two hours doing Google searches and combing through
[930.80 --> 936.38]  results and sort of like collating my own idea of what makes a good practice for product
[936.38 --> 936.88]  descriptions.
[936.88 --> 943.06]  Or I could just click on that like lovely little sparkle button after entering in like, oh,
[943.08 --> 943.68]  it's white.
[943.82 --> 945.12]  It's, you know, these dimensions.
[945.12 --> 947.42]  It's got these materials and just like, boom.
[947.96 --> 952.02]  And you've got this incredible, you know, text description of your product.
[952.02 --> 953.92]  It pulls from your product title.
[953.92 --> 957.36]  So like, you know, if you've mentioned that it's like this kind of product or this category,
[957.36 --> 962.20]  it gathers all that context initially and then brings that to bear on the description
[962.20 --> 962.96]  that it writes.
[963.36 --> 967.24]  You'll have the ability to pick what tone you want that description to have.
[967.32 --> 971.32]  So we give the version some ability to kind of shape like, oh, do I want this to feel
[971.32 --> 972.36]  sophisticated?
[972.74 --> 974.12]  Do I want it to feel fun?
[974.24 --> 978.76]  Do I want it to feel like there's deep expertise behind this product description?
[978.76 --> 985.68]  And so I think those really simple tools just kind of placed seamlessly into the UI exactly
[985.68 --> 990.80]  where the merchant is kind of doing these activities today anyway is really kind of the powerful
[990.80 --> 993.92]  first step that we want to take to introduce merchants to these new tools.
[994.02 --> 996.92]  And then we'll expand from there in some pretty powerful ways.
[996.92 --> 1003.02]  What's up, friends?
[1003.24 --> 1006.54]  AI continues to be integrated into every facet of our lives.
[1006.68 --> 1010.16]  And that remains true because you can now index your database with AI.
[1010.32 --> 1013.70]  You can write more code, become that 10Xer you always wanted to be.
[1014.00 --> 1018.16]  And you can even draft a letter for a lease on an apartment or a new property.
[1018.58 --> 1020.10]  AI is everywhere.
[1020.10 --> 1025.72]  And it might be time for us to start questioning, is AI our friend or our worst enemy?
[1026.12 --> 1030.62]  And that's the focus of the three-part season opener of the award-winning podcast called
[1030.62 --> 1031.46]  Trace Route Podcast.
[1032.10 --> 1035.78]  You can listen and follow the new season of Trace Route starting November 2nd on Apple,
[1035.96 --> 1038.18]  Spotify, or wherever you get your podcasts.
[1038.62 --> 1041.90]  And this show is all about the humanity and the hardware that shapes our digital world.
[1042.20 --> 1046.78]  In every episode of Trace Route, a team of technologists seeks to untangle the complex
[1046.78 --> 1048.62]  question, who shapes the internet?
[1048.62 --> 1054.28]  Seasons 1 and 2 gave us a crucial understanding of the inner workings of technology while revealing
[1054.28 --> 1055.76]  the human element behind tech.
[1056.12 --> 1060.60]  And Season 3 tackles not just AI questions, but also how can we use technology to preserve
[1060.60 --> 1061.04]  the earth?
[1061.34 --> 1063.34]  Who influences the technology that gets made?
[1063.70 --> 1066.28]  And what happened to the flying cars we were promised?
[1066.70 --> 1070.74]  I think it's safe to say that the future of AI is both exciting and terrifying.
[1070.94 --> 1075.02]  So it's interesting to hear the perspectives of experts in the field.
[1075.02 --> 1080.22]  Listen and follow this new season of Trace Route starting November 2nd on Apple, Spotify,
[1080.52 --> 1082.44]  or wherever you get your podcasts.
[1082.44 --> 1102.94]  I think how we initially started chatting back and forth was at least partially because seeing
[1102.94 --> 1108.44]  this hugging face space, which is really cool that you all put up and I know got a lot of
[1108.44 --> 1114.90]  attention partially in the merchant world, but also in the AI world around the community
[1114.90 --> 1119.12]  that's being built around open source AI tools on hugging face.
[1119.42 --> 1123.82]  And you have a space there that had to do with product photography.
[1124.60 --> 1130.46]  Before we go into the technology, the space, kind of how this works, could you kind of describe
[1130.46 --> 1134.72]  a little bit of the motivation behind this project?
[1135.08 --> 1141.40]  Because you mentioned product photography, but people might not, if they haven't been exposed
[1141.40 --> 1147.22]  to kind of e-commerce as much or worked on their own e-commerce store, they might not realize
[1147.22 --> 1151.84]  kind of what product photography means and some of the challenges around it.
[1151.92 --> 1156.48]  So could you kind of set up the motivation for this before we hop into the technical pieces?
[1156.48 --> 1157.74]  Yeah, absolutely.
[1158.14 --> 1164.96]  So merchants spend an enormous amount of time and money generating visual media that's like
[1164.96 --> 1170.74]  compelling, that gets people excited about their products, either the details in the design
[1170.74 --> 1174.66]  or the lifestyle that it might afford, you know, whoever buys it.
[1174.82 --> 1180.58]  And these images are really core to what drives a lot of commerce online, whether it's advertising
[1180.58 --> 1186.38]  or whether it's building out an attractive storefront, like a web storefront, or whether it's appearing
[1186.38 --> 1189.38]  in various channels, you know, in different marketplaces as well.
[1189.80 --> 1195.22]  But not least of which is on the product detail page, where somebody has landed a shopper and
[1195.22 --> 1197.32]  ostensibly they're interested in this product.
[1197.32 --> 1203.50]  And the job of those images in that context is to do the best job possible, painting a picture
[1203.50 --> 1208.44]  of what like that product looks like in somebody's life, as well as all of the details about the
[1208.44 --> 1208.70]  product.
[1209.00 --> 1213.90]  And early on, you know, last year, when Stable Diffusion and other open source image models
[1213.90 --> 1220.96]  started to land, I got really excited about a future where you could imagine merchants just
[1220.96 --> 1227.12]  being incredibly more agile and cost efficient in how they create these images.
[1227.88 --> 1230.02]  And so we started digging in pretty quickly.
[1230.28 --> 1233.94]  We played with Dreambooth as soon as that was available in Stable Diffusion.
[1234.18 --> 1239.72]  And we started to see like, actually, could we train a Dreambooth model that could encapsulate
[1239.72 --> 1244.02]  the concept of a product and recreate it in high fidelity over and over and over again?
[1244.18 --> 1245.52]  And that's like the dream, right?
[1246.42 --> 1249.30]  And we're getting closer and closer to that, but we weren't quite there yet.
[1249.54 --> 1254.28]  But some of those early explorations proved beneficial to understanding the space, understanding
[1254.28 --> 1258.86]  the technology, and thinking a little bit more deeply about some simpler ways that we might
[1258.86 --> 1260.62]  be able to bring this to market in the near term.
[1261.12 --> 1266.22]  When you think about the opportunity for image gen in commerce, I mean, it's massive, right?
[1266.22 --> 1271.28]  And the ability, the promise of being able to recreate your product in high fidelity in
[1271.28 --> 1273.24]  any scenario is kind of the dream.
[1273.68 --> 1277.94]  You know, you could imagine at requesting any kind of lifestyle or product detail image
[1277.94 --> 1282.20]  and just in seconds getting that out the other end to use in your storefront or to use in
[1282.20 --> 1285.58]  blog content or to use in advertisements about your product.
[1286.06 --> 1288.90]  And that's incredibly powerful because commerce is always changing.
[1289.04 --> 1290.12]  Taste is always changing.
[1290.78 --> 1296.04]  Seasonality is a huge piece of commerce and thinking about how do you merchandise and
[1296.04 --> 1300.60]  market your products differently in the spring versus the fall and keeping up with the amount
[1300.60 --> 1306.24]  of imagery just required to drive that part of your business is really challenging.
[1306.80 --> 1312.30]  I think the reason that we got really excited is that we saw an opportunity to take the existing
[1312.30 --> 1318.70]  imagery that merchants had either from past photo shoots or from humble like at-home photography
[1318.70 --> 1322.52]  with their kind of mobile cameras set up on their kitchen counter or whatever they might
[1322.52 --> 1329.10]  have access to and give them a tool that could not really change any pixel of the product
[1329.10 --> 1333.92]  itself, but otherwise completely reinvent the reality around that product.
[1334.08 --> 1337.90]  And so we started to work on, you've seen a lot of examples of this out in the market,
[1338.00 --> 1342.66]  but I think the key problem that we saw with a lot of these early examples of this where
[1342.66 --> 1348.52]  you sort of, you do object segmentation to select the product and keep it, you know, sacred.
[1348.52 --> 1353.12]  You don't touch any of the pixels that you sort of guard and mask there, but then all the pixels
[1353.12 --> 1357.62]  in the background you reimagine with AI. And what we saw with most of these early tools,
[1357.70 --> 1363.74]  as I said, was that there was this real disjoint appearance between the product that got masked and
[1363.74 --> 1368.52]  safeguarded and the reality that was created around it. The camera angle, like it looked like,
[1368.62 --> 1372.82]  oh, well, this one was taken from above, but the original product image was from straight on and
[1372.82 --> 1378.04]  there's no grounding shadows and there's no realistic reflections of the product in the environment.
[1378.04 --> 1382.54]  The pixels of the product and the pixels of the environment aren't speaking to each other.
[1382.74 --> 1387.24]  They don't know, one hand doesn't know what the other is doing. And so they can't knit those
[1387.24 --> 1392.74]  pixels, those moments of grounding around the product that really sell the illusion that it's
[1392.74 --> 1398.82]  part of this other reality. Those shadows, those ground reflections, seeing maybe some of the light
[1398.82 --> 1405.32]  of the scene hit the product object itself. And so we wanted to really tackle those grounding
[1405.32 --> 1410.00]  problems that we saw in a lot of these early examples. And so I'm happy to dig into all the
[1410.00 --> 1414.34]  technical details of kind of how we're into that, but that was really the opportunity that we saw was
[1414.34 --> 1419.58]  to begin to bring some of this magic to merchants really early before we're even yet to that perfect
[1419.58 --> 1424.32]  personalization of you upload a bunch of images of your product and now it produces them again
[1424.32 --> 1429.22]  perfectly at the other end. We can begin to bring really powerful tools to merchants in the space
[1429.22 --> 1431.04]  already, even with techniques like this.
[1431.04 --> 1435.76]  And just as a point of clarification, when you say grounding in this case, you're kind of talking
[1435.76 --> 1442.30]  about that visual context going across different as opposed to technical grounding with a model and
[1442.30 --> 1444.66]  such, just because we talk about both on the show.
[1445.06 --> 1449.74]  Yeah, no, it's a great clarification. Yes. And purely talking about sort of the visual aspects of
[1449.74 --> 1454.92]  the output image and making that product feel seated in the new reality in some visual way.
[1454.92 --> 1462.90]  Before we hop into more of the details about how you actually accomplish this, I'm wondering how you
[1462.90 --> 1469.26]  see the kind of state of open source generative models in comparison to maybe some of the other
[1469.26 --> 1474.92]  platforms that are out there that do enable amazing things, but not in an open source way.
[1474.98 --> 1480.74]  It sounds like at least for your team, I don't know if it was kind of personally important to you and
[1480.74 --> 1485.74]  your team to kind of leverage some of this open technology, or it was just like these things
[1485.74 --> 1490.38]  are openly available, they're licensed permissively for our use, and they're enabling things that we
[1490.38 --> 1497.26]  couldn't do before. How do you view kind of the state of generative AI on the image side specifically?
[1497.42 --> 1504.24]  Because we've talked a lot in recent weeks about the text side of things and how maybe text
[1504.24 --> 1510.66]  generation models that are open compare in certain ways or other ways to close models. But I'm
[1510.66 --> 1516.24]  wondering from a team that's actually used this kind of image generation models that are open
[1516.24 --> 1522.04]  and licensed permissively, what was that experience like for you? It sounds like this grounding element
[1522.04 --> 1527.28]  was one thing that you had to deal with, but what was it like for you generally to kind of work through
[1527.28 --> 1533.28]  the details of getting the model, figuring out how to run it, figuring out how to scale it, maybe
[1533.28 --> 1537.08]  that sort of stuff? Could you kind of describe a little bit of that process?
[1537.08 --> 1542.34]  This is a really early field. So we're still figuring out what the tools need to look like
[1542.34 --> 1548.38]  and how to work efficiently. We were working on some of these early ideas in a very sort of falling
[1548.38 --> 1554.34]  over ourselves way in some notebooks, trying to collaborate and work together and just not sort
[1554.34 --> 1559.98]  of seeing the pace that we wanted to see in sort of our iteration speed. Our team is, you know,
[1559.98 --> 1565.32]  works really quickly, we work on kind of these three week sprints to just very rapidly prototype and
[1565.32 --> 1569.96]  understand a new technology space and develop, you know, some kind of potentially useful concept there.
[1570.58 --> 1578.86]  And so we needed a way to move faster. And Toby, the CEO at Shopify is incredibly technically adept.
[1579.18 --> 1584.28]  He's an incredible developer in his own right, and was really interested in some of the image gen work
[1584.28 --> 1590.10]  that we were doing in the early phases, and suggested that we pick up this new tool called ComfyUI,
[1590.10 --> 1596.30]  which is an open source tool. So we're big fans of open source at Shopify. It's why we shared to
[1596.30 --> 1601.88]  Hugging Face, because we want to contribute back to that community. You can go take our pipeline and do
[1601.88 --> 1606.70]  something with it. It's up on Hugging Face. And so we're really excited about open source and obviously
[1606.70 --> 1611.44]  the capability of other providers as well. And, you know, our objective is always to bring the best
[1611.44 --> 1616.98]  technology to our merchants, whether it's open source or buy a closed provider. So we're really excited
[1616.98 --> 1621.76]  about all contributors in the space and what tools we can build for merchants with them.
[1622.30 --> 1628.24]  So we focused a lot on SD in the early days, and we were excited when Stable Diffusion XL launched.
[1628.40 --> 1633.42]  And that's actually the model that underpins our Hugging Face space. We've done a lot of work
[1633.42 --> 1639.62]  with Stable Diffusion in all of its iterations, as we've explored this space and are excited to
[1639.62 --> 1644.38]  continue to work with it and obviously build amazing new stuff with it. But yeah, I mean,
[1644.38 --> 1649.54]  I think we used Comfy UI. We dug into it. I think what we loved about it is that it's this node-based
[1649.54 --> 1655.30]  UI. I come from the design world originally for product and UI design. And there was this much
[1655.30 --> 1660.54]  loved tool originally from Apple, but it got hacked by a bunch of prototypers called Quartz Composer.
[1661.04 --> 1665.80]  It's a node-based interface with a bunch of like little modules that do little conversion jobs and
[1665.80 --> 1670.64]  you can wire them together in these sort of larger machines and recompose and move things around
[1670.64 --> 1675.58]  really quickly and rewire them and change the sort of constant values and very quickly build these
[1675.58 --> 1681.64]  very complex computing machines in a visual way. And so for me and for our team, that was a really
[1681.64 --> 1687.22]  powerful tool for us to accelerate our process. And we began building these machines, this pipeline that
[1687.22 --> 1692.28]  we ended up putting up on Hugging Face in Comfy UI and iterating there. And when we had it to a great
[1692.28 --> 1697.84]  place, we pulled that code into Hugging Face, you know, sort of rebuilt everything, ground up with the
[1697.84 --> 1703.06]  models hosted on Hugging Face and sort of encapsulated the pipeline there. But we were able to iterate
[1703.06 --> 1709.70]  super quickly and visually this way and see exactly what every piece of the machine was doing at each
[1709.70 --> 1716.88]  run. It's really interesting because you're taking new capabilities in the AI space with a large
[1716.88 --> 1722.26]  business that's, you know, running and you're trying to kind of do the uptake while absorbing the
[1722.26 --> 1727.50]  technology at the same time. And as you pointed out, you know, your CEO brought Comfy UI to your
[1727.50 --> 1733.26]  attention. As you're doing these activities as a business owner in general, like the folks that are
[1733.26 --> 1739.78]  there, how do you decide to make investments in certain areas with these new technologies and decide
[1739.78 --> 1745.62]  because, you know, there's the pull and push of, well, direct AI isn't our business. Our business is to
[1745.62 --> 1750.16]  make the best platform for all these merchants. And yet there's all these new capabilities out there,
[1750.16 --> 1755.64]  but they're not mature enough. You brought an example to bear a second ago. That's a complex
[1755.64 --> 1761.30]  set of business processes to work through and figure out what's the right level. How does Spotify
[1761.30 --> 1767.84]  think about that, you and others there, in terms of like, is this a step too far to go on a particular
[1767.84 --> 1772.48]  leap or this is appropriate, like Comfy UI turned out to be? How do you make those choices?
[1773.24 --> 1780.14]  It's a jungle. And one of the tools that we've used is really our Magic Labs team. So early on,
[1780.16 --> 1786.30]  at the end, well, actually rather at the end of 2022, as we began to see some of the rapid
[1786.30 --> 1791.14]  advancements in LLMs begin to take shape and the product possibilities became clear,
[1791.68 --> 1797.08]  we started our early efforts around product descriptions and generating those on the fly
[1797.08 --> 1803.18]  for merchants. And early on, it was really about saying, okay, what are the things that this tool,
[1803.82 --> 1809.60]  this new technology is going to obviously be capable of, right? With maybe a little prompt engineering,
[1809.60 --> 1813.42]  you know, we'll figure it out. But like, what seems to be well within its grasp,
[1813.42 --> 1819.20]  but also of maximum time saving value to merchants and product descriptions was like that perfect bend
[1819.20 --> 1823.58]  diagram out of the gate, right? It was just kind of obvious to everybody. It was like, oh, so much we
[1823.58 --> 1829.38]  know, I already know so much toil is spent. Just creative writing is something that can probably be
[1829.38 --> 1834.20]  written pretty quickly, if you have the necessary context and best practices and all that stuff.
[1834.20 --> 1837.86]  So we got to work on that. And we shipped that super quickly. I think we turned that around from
[1837.86 --> 1843.20]  concept and team assembly to launching at winter editions in about two months. And so it was just
[1843.20 --> 1848.06]  an incredible accelerated, you know, one of those moments, right, where just the right people and
[1848.06 --> 1852.98]  the right technology and the right opportunity come together. And pretty rapidly out of that,
[1853.20 --> 1859.38]  we formed the magic team at Shopify to sort of help invest more deeply in these AI technologies and
[1859.38 --> 1863.34]  figure out all of the places and all of the ways we wanted to leverage these new capabilities
[1863.34 --> 1867.96]  across the admin to help accelerate what merchants were doing. And so we've continued to work on a
[1867.96 --> 1872.32]  bunch of different ideas there, not least of which is some of the image gen work that we've done.
[1872.40 --> 1878.80]  And the way that we kind of work through this space, because there is so much going on, like every
[1878.80 --> 1886.32]  week, you've got to weed through at least a half dozen, like groundbreaking papers all over the map.
[1886.32 --> 1892.32]  And so a big part of the process is connecting to that fire hose of what's happening so that you never
[1892.32 --> 1898.42]  lose sight of like, a paper that might completely change how we think about serving our merchants,
[1898.60 --> 1902.92]  and then weeding through those and just sort of logging them as you go. Like I've got a Twitter
[1902.92 --> 1910.76]  bookmarks folder that's just so deep, that I get back to periodically and sort of pull, pull things
[1910.76 --> 1915.70]  that sort of feel like they have remaining value out of and surface to the team and surface to the
[1915.70 --> 1921.56]  company and start discussions around. And within Magic Labs, our small team has been iterating on
[1921.56 --> 1927.52]  this three week cycle to just digest all of these new technologies, all of these capabilities. Every
[1927.52 --> 1933.94]  three weeks, we pick up a new one, we have no roadmap, we just we have areas of curiosity. And every three
[1933.94 --> 1938.74]  weeks, we look at what's out on the table in the world. And we say, what's the most exciting or
[1938.74 --> 1944.02]  potentially impactful thing for commerce and our merchants next, based on what we see here,
[1944.02 --> 1949.68]  and we pick what we want to work on within a day. And we're prototyping by, you know, day two or three,
[1949.68 --> 1954.86]  after having like picked up either a new piece of hardware or open to, you know, some open source
[1954.86 --> 1960.10]  code on GitHub to get started. And we're prototyping. And within three weeks, we've gotten to the end of
[1960.10 --> 1965.84]  that process, we've got a deliverable that like proves either disproves that something we hoped could be
[1965.84 --> 1970.64]  possible is actually not possible. And here are the reasons why. And here's now what we're looking for
[1970.64 --> 1976.70]  in the next iteration of this technology. Or quite often, actually, there is a path here, here's what
[1976.70 --> 1983.66]  it looks like, here's how we we might shape this. And from there, tons of internal teams are eager and
[1983.66 --> 1988.64]  interested in hungry and sort of like how to rethink their products or how to leverage these technologies
[1988.64 --> 1993.82]  for their particular challenge with merchants. We're really lucky to just be working in an
[1993.82 --> 1998.14]  organization that gives us really fertile ground to just kind of bring these technologies and what
[1998.14 --> 2003.74]  we're learning about them to a really wide set of problems that all seem very tractable based on
[2003.74 --> 2006.68]  the trajectory in what we're seeing in the tech right now.
[2006.68 --> 2013.34]  Well, Russ, I really appreciated your perspective on kind of how, how your team is thinking about
[2013.34 --> 2018.54]  processing a lot of these advancements that we're seeing in technology and tools so rapidly,
[2018.54 --> 2022.70]  which is definitely hard to keep up with. But I love how you're thinking about these
[2022.70 --> 2028.64]  short cycles of work and thinking about what what could be impactful. I'm wondering if we could kind
[2028.64 --> 2033.92]  of revisit this problem of grounding with these product images, because I think some people might
[2033.92 --> 2040.84]  really be interested in that. And I'm wondering to start with that, could you just rephrase the kind
[2040.84 --> 2048.84]  of main problem of this grounding for people that are kind of new to this and walk us into like how you
[2048.84 --> 2055.64]  identified this problem and thought about coming up with a solution to it? Because I could see a whole
[2055.64 --> 2061.54]  spectrum of things here, right? Like there's a hierarchy of ways to do this, everything from, oh, we just need to
[2061.54 --> 2070.26]  make our prompt better to we need to retrain a model from scratch that's Shopify stable diffusion or
[2070.26 --> 2079.38]  Shopify GPT for for this, right? And and yeah, exactly. Shopify fusion. Yeah, obviously, that ladder of the
[2079.38 --> 2084.22]  spectrum. I think there's very few people that get to that level of the hierarchy when they're solving
[2084.22 --> 2091.42]  these problems. But it is hard sometimes for people to parse out where along that spectrum from playing with
[2091.42 --> 2098.44]  your prompts to maybe chaining to like creating some pre processing post processing to fine tuning to
[2098.44 --> 2103.94]  training your own model. Where is it reasonable for us to land on that spectrum? That's something for
[2103.94 --> 2108.96]  people that's really, in my experience, hard for them to parse out. So how did that work out for you
[2108.96 --> 2114.44]  all in this case, maybe starting with rephrasing that problem of grounding and then getting into how
[2114.44 --> 2118.92]  you started thinking about how you might solve it? From the highest level, it's like if you're a merchant,
[2118.92 --> 2123.36]  right, and you're just starting out, and you've got some products that you're really excited about,
[2123.40 --> 2127.16]  either you've sourced them from like a really great provider, or you make them yourself,
[2127.16 --> 2132.20]  you don't have all the resources that you know, somebody with operating business and scale,
[2132.44 --> 2137.78]  and lots of employees and tons of capital can deploy, you know, to build a business, you know,
[2137.78 --> 2143.06]  by hiring contractors and all those things. And if you're this merchant, and you've got, you know,
[2143.08 --> 2147.26]  you can take photos at home, or you've got maybe like some photos from a previous shoot,
[2147.26 --> 2152.10]  you paid your friend to do, and they're pretty good. But they're not quite like helping your brand
[2152.10 --> 2157.64]  sing, you're looking for something to help you get over that. You're looking for that tool that's
[2157.64 --> 2162.52]  going to help take the the media that you have and turn it into the media that you want.
[2163.26 --> 2167.08]  And your first thought is like, Oh, my gosh, AI, like, of course, like AI is gonna unlock that.
[2167.12 --> 2170.84]  This was our first thought is like, well, if we can just train a model to know exactly what your
[2170.84 --> 2175.08]  product looks like, great, you can just create it over and over. And again, we're getting closer to that,
[2175.08 --> 2179.36]  but we're not quite there. And short of that, like, we're looking for ways to help merchants
[2179.36 --> 2185.24]  still realize this elevate this creative elevation of the creative materials that they do have,
[2185.48 --> 2190.74]  right. And it turns out that a lot of merchants have pretty good photography, it's almost there,
[2190.86 --> 2194.10]  right? Either because they took it at home with their mobile camera, and they just don't have a
[2194.10 --> 2199.40]  whole lighting studio set up, or, or they're just not sure like how best to art direct an image
[2199.40 --> 2207.62]  so that it feels tantalizing to look at, and drives purchase behavior. And so we saw a path where you
[2207.62 --> 2213.72]  can, of course, crop out and save the product pixels from the original image that you took,
[2213.88 --> 2220.66]  and keep those sacred, and eliminate the challenge of getting AI to recreate the product again, which is
[2220.66 --> 2226.32]  a very specific thing, right? It's got details, it's got your logo on it. And AI has a hard time holding
[2226.32 --> 2231.16]  on to some of those details at times. But it can be fantastic at creating the background, right,
[2231.22 --> 2238.46]  the not centerpiece of your image, to create a new elevated environment around it. And so we saw an
[2238.46 --> 2244.00]  opportunity to kind of take that path and give merchants an early tool as personalization matures,
[2244.00 --> 2248.76]  as we get to that point, eventually, that can begin to help them unlock some of the value in their
[2248.76 --> 2254.94]  existing image media, their humble kitchen countertop photography. And so by building this pipeline,
[2254.94 --> 2261.84]  where we're able to hold and keep your product pixels intact, and not change those, we keep those
[2261.84 --> 2267.18]  details intact. And yet we can magically create this world around it. When we started this journey,
[2267.80 --> 2272.52]  what we saw was, okay, we were like, okay, great, we'll take control net, and with stable diffusion,
[2272.76 --> 2277.12]  and we'll combine these things, we'll use the depth of your original image, and then we'll just ask it
[2277.12 --> 2281.52]  for a new background, and it'll come out the other end, and it'll be great. But what happens when you
[2281.52 --> 2286.84]  sort of segment out your product image, and keep control net from really understanding what's in
[2286.84 --> 2291.58]  there, so it doesn't change anything, it begins to lose an understanding of how to fill in the
[2291.58 --> 2296.32]  details around that object to make it look like it's a part of the environment that it's been creating.
[2296.84 --> 2302.64]  So it loses its shadows, it loses its tabletop surface reflections, because it's actually kind
[2302.64 --> 2306.76]  of forgotten in a weird way that there's even an object there at all. So it doesn't,
[2306.76 --> 2313.12]  in whatever way you can say an AI model thinks, it doesn't have the triggers to generate those ground
[2313.12 --> 2318.74]  shadows and surface reflections in the sea it creates around the product. And so that was the
[2318.74 --> 2323.52]  first key obstacle that we saw when we started moving down this pipeline of trying to help merchants
[2323.52 --> 2328.02]  take their existing product photos and just kind of create new rich realities around them.
[2328.24 --> 2332.38]  So we had to solve that grounding problem, there were no shadows, there were no good ground
[2332.38 --> 2338.82]  reflections, the camera angles were off, like, you'd get a kind of tabletop scene background for a
[2338.82 --> 2344.48]  front on, you know, product photo, and it just it looks wrong. You see it immediately, of course.
[2344.96 --> 2348.68]  And so we started tinkering and trying to figure out how to get that to work. And it actually turned
[2348.68 --> 2354.52]  out to be kind of a multivariate approach. We had to think about prompting, we had to think about how do
[2354.52 --> 2360.18]  we structure a good prompt, just so that we get a good result, even without all the fancy stuff we want to
[2360.18 --> 2365.88]  do in the in between, right. And it turns out, one of the key things we learned was that you need to
[2365.88 --> 2370.82]  start with a declaration of what your foreground object is, what your product is in the shot. And
[2370.82 --> 2374.90]  if you can get a really good description of that, then your prompt is already starting out in a really
[2374.90 --> 2379.84]  good grounded spot. Obviously, adding stylistic language like commercial product photography,
[2380.50 --> 2384.86]  you know, high quality, all those sort of like little tricks of early image models that will
[2384.86 --> 2389.46]  eventually like pass away. But you know, we injected a few of those into the prompt as well,
[2389.46 --> 2394.26]  you start with that product description. And then the next key line has to be some kind of
[2394.26 --> 2399.16]  grounding description of how it's been placed in the environment. Without that description,
[2399.16 --> 2403.74]  you don't get those shadows, you don't get those table reflections, even with all the cool additional
[2403.74 --> 2408.32]  sort of support for that functionality we've built in. And so you need that grounding. And then finally,
[2408.32 --> 2411.08]  you can describe the scene that you want in that background.
[2411.66 --> 2412.38]  It's a great description.
[2412.82 --> 2417.34]  It really is. I'm really enjoying this. But I wanted to ask a couple of questions to make sure
[2417.34 --> 2421.58]  it sounds like when the way you were starting when you're kind of talking about the product pixels and
[2421.58 --> 2426.28]  pulling those out almost in my mind, I was almost thinking of it in an old fashioned way, like like
[2426.28 --> 2431.16]  a Photoshop mask or something where you're masking out the product. And then you're trying to bring all
[2431.16 --> 2437.46]  the goodness of the contextual understanding of the models in the thing that I think surprised me in
[2437.46 --> 2443.16]  there was was kind of if you talk about that, that initial masking, I wasn't surprised when you talked
[2443.16 --> 2447.70]  about finding the description for the background and everything. But I was a little bit about the
[2447.70 --> 2452.56]  thing being masked, if you will, the product itself. How do you think about that? If you're,
[2452.68 --> 2456.40]  as you're going through the process, and you're saying, I need that description, like, could you
[2456.40 --> 2461.34]  describe that step a little bit? Because I was, I'm trying to kind of really grok that one. But it
[2461.34 --> 2462.52]  sounds really interesting to me.
[2462.96 --> 2468.02]  I think it's probably helpful to work backward from really what we deliver to stable diffusion as a model
[2468.02 --> 2471.72]  to generate the output that we get from it in the end, and then kind of work back really,
[2471.72 --> 2475.38]  like, okay, well, then how do we assemble all of that input to then get it in the model, right?
[2475.64 --> 2475.80]  Sure.
[2476.04 --> 2480.40]  So at the end of our pipeline, once we processed all the prompts you've put in and the image you
[2480.40 --> 2485.48]  uploaded of your original product, all that stuff, really what we're delivering to stable diffusion in
[2485.48 --> 2493.56]  the end is a masked depth map of your original product, and a little bit of a bloom at the very
[2493.56 --> 2498.52]  bottom where it might make connection with the scene with the original scene around it.
[2498.66 --> 2500.76]  Could that be like a shadow when you say that?
[2500.76 --> 2505.12]  Kind of like, yeah, sort of like a little bit of that shadow. Maybe, you know, if it's a table
[2505.12 --> 2509.22]  reflection, you'll get a little bit of that table reflection. And what we found was that that
[2509.22 --> 2517.12]  little hack is just enough context, that little like gradient of additional depth info as you leave
[2517.12 --> 2523.42]  the product pixels is just the right amount of grounding information that stable diffusion and
[2523.42 --> 2528.22]  control net need to be like, oh, there's a shadow there. Oh, and I see the angle of the table is this
[2528.22 --> 2533.28]  way. And oh, I see the, you know, the camera angle is kind of like this. And all of that together,
[2533.46 --> 2540.98]  collectively gives stable diffusion, the context that it needs to then paint a grounded scene around
[2540.98 --> 2546.08]  that product in high fidelity. And of course, we're generating a new product in that resulting
[2546.08 --> 2551.68]  image, but we do a composite in the end. And those pixels, because we're using depth control net,
[2552.04 --> 2556.32]  adhere very closely to the original product pixels. So when we do the paste over in the end,
[2556.32 --> 2559.78]  you never see the sort of like hallucinated product pixels in the background.
[2560.58 --> 2565.24]  It's so interesting. I think what one question that would be really interesting for our listeners
[2565.24 --> 2571.36]  and for me, from a selfish perspective is like, how does one because I think a lot of people play
[2571.36 --> 2576.56]  with these models, they can pull down and, you know, figure out control net, reasonable enough.
[2576.56 --> 2582.52]  But then this like connection of this like little hack, as you described it, in some ways,
[2582.52 --> 2587.48]  after you have something like that, it like it seems simple enough to describe like why that would
[2587.48 --> 2594.08]  work. And it's like a cool hack. But to get to it, it's like, how do you come up with that,
[2594.08 --> 2600.30]  I think is what is in a lot of people's mind. And some of it for me, I know, like, a lot of times I
[2600.30 --> 2605.32]  bang my head against the wall one day, and like, I sleep on it. And in the shower in the morning,
[2605.32 --> 2610.90]  it's just like, whatever that that idea comes. But I'm curious, from your perspective, from your
[2610.90 --> 2617.42]  team's perspective, how did that happen? And what sort of environment exists that would promote this
[2617.42 --> 2623.08]  sort of hacking of because you're not retraining a whole model here, you're kind of using what is
[2623.08 --> 2628.12]  off the shelf, but using it in an extremely powerful way, but in a very creative way that
[2628.12 --> 2632.94]  is creative, not in the sense of training a new model, but creative in the sense of how you're using
[2632.94 --> 2635.36]  the existing model, which I think is really intriguing.
[2636.08 --> 2641.10]  This really was just kind of the perfect workshop product where we had just a bunch of like
[2641.10 --> 2645.00]  brilliant people who kind of understood these models enough had played with them enough,
[2645.44 --> 2650.32]  knew and had seen enough of what they were capable of from different demos and other things to
[2650.32 --> 2656.52]  have a real opinion about what was possible and kind of what wasn't. And when we started the journey
[2656.52 --> 2661.38]  and started building the machine, right, and trying to figure out what is this? How should this work?
[2661.38 --> 2667.68]  How do all the pieces fit together? We knew that there were hundreds of these little amazing AI
[2667.68 --> 2672.70]  machines that could be plugged into and turned into bigger machines that do even more powerful
[2672.70 --> 2676.00]  things. And it's just about figuring out like, what's the sequence? What are the pieces? What
[2676.00 --> 2681.76]  are the core problems? And it's just, how do you get to that iteration speed where you can try
[2681.76 --> 2688.02]  something? It's why I fell in with web dev, like in the early, early days of like web standards and 2.0,
[2688.02 --> 2692.82]  like you could code something and see it immediately. Okay, that didn't work. Go back, code it again,
[2692.96 --> 2696.22]  see it immediately. Okay, no, that didn't work. Go back, code it immediately, see it again. And getting
[2696.22 --> 2700.52]  into that state, and that's really what the open source tool ComfyUI really unlocked for us was,
[2700.74 --> 2706.40]  you know, and GPUs still take a few seconds to deliver images. So it wasn't perfect, rapid fire iteration,
[2706.86 --> 2713.02]  but way faster than trying to do it all remotely and trying to, you know, ComfyUI dramatically
[2713.02 --> 2718.68]  accelerated our ability to kind of like build this more complex machine because it was so easy to
[2718.68 --> 2723.30]  configure and reconfigure and try a thing and wire it a different way. And then that didn't work.
[2723.38 --> 2727.34]  You'd wire it a different way. You see the results. You're like, oh, wait, that's new, but different,
[2727.34 --> 2732.24]  but not what I want. But isn't that interesting? And then, oh, maybe I have a hunch about why that
[2732.24 --> 2736.50]  happened. And like, you pull that back into something else. And you know, you unlock something,
[2736.60 --> 2741.10]  not because you had some like amazing insight, but just because you've tried enough stuff,
[2741.10 --> 2745.96]  and you've seen enough weirdness and been like, there was something there that was weird that
[2745.96 --> 2750.30]  shouldn't have happened. And something surprised me and I want to understand it. And that's how
[2750.30 --> 2753.84]  just like the, you know, it just unfolds that way. And eventually you're like, you start to connect
[2753.84 --> 2757.10]  all these little discoveries you make as you're like, why did that happen? Why did that happen?
[2757.18 --> 2761.80]  Why did that happen? And sooner or later, you end up with something that works. It's kind of magic.
[2762.36 --> 2766.44]  It is a kind of magic as a queen fan that fit right in there as well.
[2766.44 --> 2772.60]  Um, I'm still almost stuck on that creative epiphany that you had a moment ago. That's
[2772.60 --> 2778.92]  really, I found that really interesting that, that you came upon that as you're looking at this
[2778.92 --> 2784.74]  set of technologies evolving over the years ahead, as the organization is maturing with these
[2784.74 --> 2790.16]  technologies and you have this amazing creative capability in your humans, in your organization
[2790.16 --> 2795.74]  that can use these tools. Where's all this going? As we wind up this conversation, what, you know,
[2795.74 --> 2800.86]  how, how are you thinking about the future? What are you excited about that? What do you not have
[2800.86 --> 2804.90]  yet that you wish you had in your fingers right now? How's your thinking about that?
[2805.52 --> 2809.92]  I hate when people think about shopping, they don't always like jump to think about technology.
[2810.34 --> 2817.36]  But if you think about how technology has impacted commerce over the years, commerce and our culture
[2817.36 --> 2823.60]  around it and how it works is always inherently tied to like the wave of technology that we're
[2823.60 --> 2829.80]  experiencing, you know, whether you're talking about IBM cash register, adding machines, or whether
[2829.80 --> 2836.02]  you're talking about mass media and the creation of kind of mega brands, or you're talking about the
[2836.02 --> 2841.48]  evolution to the internet and sort of the democratization of commerce and connecting with
[2841.48 --> 2848.04]  niche audiences. The culture around commerce always evolves around technology. It's why I'm so excited
[2848.04 --> 2853.22]  to be working at the intersection of these new technologies at a company like Shopify, because,
[2853.36 --> 2859.42]  you know, they are so directly related. And as we kind of think about the future of technology and sort
[2859.42 --> 2865.88]  of where this is all going, I get really excited about AI being an incredible driver of personalization
[2865.88 --> 2871.80]  in commerce. You know, when I go to some of my favorite stores, the person behind the desk,
[2871.80 --> 2877.38]  like knows me, they recognize me, they remember what I bought last time, we have a conversation about it,
[2877.38 --> 2882.70]  like I can ask questions of the new line or the new products or ask them to help me find stuff that
[2882.70 --> 2887.82]  I might really enjoy based on what they know I've bought in the past. And, and that's all an experience
[2887.82 --> 2893.46]  that I can get at an in person store today, because like the person there knows me, I'm really excited
[2893.46 --> 2899.84]  about a future where our online commerce experiences become a little bit more like that, where we visit an
[2899.84 --> 2905.76]  online store, and it knows who we are, and it helps us find the stuff that we'll be most interested in.
[2905.76 --> 2911.22]  And even, you know, really exciting things like being able to visualize myself in different clothes,
[2911.22 --> 2917.44]  I might want to buy live in a browser, like that kind of stuff is in the future, out ahead of us.
[2917.54 --> 2922.80]  And so I'm really excited about a future where AI helps bring these kinds of personalized,
[2923.62 --> 2928.48]  one to one customized shopping experiences to merchants and helps them bring that to their shoppers.
[2928.48 --> 2935.00]  That's awesome. Well, I'm, I'm definitely looking forward to seeing the things that your team comes
[2935.00 --> 2941.48]  up with moving towards the future and just really appreciate you taking time out of what must be an
[2941.48 --> 2947.84]  incredibly busy week leading up to Black Friday, Cyber Monday at Shopify. But yeah, thank you so much
[2947.84 --> 2954.00]  for the work you and your team are doing, Russ. Hope to hope to have you on a future show to see some of
[2954.00 --> 2958.26]  those things you just mentioned become reality. Thanks so much for joining us. Awesome. Thanks,
[2958.34 --> 2960.06]  Chris. Thanks, Daniel. Really appreciate it.
[2960.06 --> 2976.44]  Thank you for listening to Practical AI. Your next step is to subscribe now, if you haven't already. And if
[2976.44 --> 2981.20]  you're a longtime listener of the show, help us reach more people by sharing Practical AI with your
[2981.20 --> 2986.36]  friends and colleagues. Thanks once again to Fastly and Fly for partnering with us to bring you all
[2986.36 --> 2993.06]  Change Talk podcasts. Check out what they're up to at Fastly.com and Fly.io. And to our Beat Freakin'
[2993.06 --> 2998.60]  residents, Breakmaster Cylinder for continuously cranking out the best beats in the biz. That's all for now.
[2998.86 --> 3000.04]  We'll talk to you again next time.
