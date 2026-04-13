**Jerold Santo:** Welcome back, everyone, to another fun episode of JS Party. Jerold here, joined today by two of my friends, Nick Nisi and Across Aboukhadijeh (you just know him as Across). What#39;s up, guys?

**Nick Nisi:** Hey!

**Across Aboukhadijeh:** Thaddeus?!

**Jerold Santo:** JS Party is up, that#39;s what#39;s up, and we have a fun segment show. Three segments we would like to bring; some of my favourites, as IN#39;VE put this show together - Story of the Week, which we#39;LL start off with, and then Explain It Like IN#39;m Five. Quick spoiler for that - we#39;re going to explain torrent, we#39;re going to explain CORS... IN#39;m not going to explain either of those things, IN#39;m going to learn about them. And then we#39;re gonna finish off with shout-outs. So that#39;s what you can expect from this episode.

For those who Haven#39;t listened before, Story of the Week is a moment in time wherein we take turns sharing what we believe is the most important, or the biggest story of the week, or it could be an article that we read that was impactful... It can really be anything, but we#39;re talking about things going on, or things that have happened recently, what they are, why they#39;re important, and what we think about them. So that#39;s what we#39;LL do first, and we#39;LL kick off with Across... What is your story of the week, friend?

**Across Aboukhadijeh:** I think the obvious story of the week is the Prescript NPM installer fiasco... But I think IN#39;LL leave that one to you, Jerold, because I think you#39;re gonna talk about that. IN#39;LL say something related to that, which is not in the JavaScript world, but it#39;s in the cyber-security world.

There#39;s this story about an Insider Logic Bomb that caught my eye. The idea was this guy who is not a very smart criminal decided that he was going to put a logic bomb inside some spreadsheet that he created for this company... And the idea is this spreadsheet had some custom scripts inside that would update the orders in the spreadsheet. He worked there for years, but wanted to basically ensure that they would have to keep hiring him to come and work there further in the future... So he included this little time bomb that would make the code stop working on a certain date. It#39;s super-evil, because then they basically had to call him up and say quit;Hey, the code ISN#39;t working. Do you want to come back in here for some more contracting work?quit; He just did this repeatedly and kept collecting fees from this...

**Jerold Santo:** Oh, wow.

**Across Aboukhadijeh:** Really, really devious.

**Jerold Santo:** \[04:02\] So that#39;s job security right there. The moral of the story is if you#39;re-writing software, and you need job security, put in a logic bomb... No, do not do this.

**Across Aboukhadijeh:** No. He got in big troubles.

**Jerold Santo:** How did they catch him? How did they figure out eventually? Because you#39;d think he would just come back in, do the work, and then leave the bomb there, but do you know how they found out?

**Across Aboukhadijeh:** I done#39;t know, IN#39;m not sure how they#39;VE found out. We can link to the story and there#39;s probably more information there. It#39;s funny, because he was not very smart, because he made it so explicit... But if you think about complicated software - and this is not an intentional thing, but people make a lot of complicated software that ends up having effectively the same outcome; the code needs to be constantly worked on... And I would argue it#39;s not that different, in a way, from what this guy did. Obviously, the intent is important; he obviously intended to do that thing. But if you just think about your decisions that you make in regard to how complicated stuff is and how many moving parts, you can really make certain decisions that just sort of doom a project to be buggy and complicated, and need a bunch of work forever... Or you can make decisions that -- you can choose really solid software, software that#39;s been around for 10–15 years, that#39;s less shiny and less new, where we know how it works and you done#39;t have this kind of problem... So I done#39;t know. It#39;s interesting.

**Jerold Santo:** It reminds me of the guy who outsourced his entire job... Do you guys remember that story? A software developer who secretly outsourced all of his coding work overseas, and managed a team of random to fake his job, I think for like up to a year. This is a while back... He just would#39;t do anything; he turned his job into basically managing this team of remote coders to act like he#39;s doing his job and to get all of those things done... And he would play Solitaire, or whatever he would do instead.

**Across Aboukhadijeh:** I remember that. I think the way he got caught was that somebody in IT saw that a bunch of connections was coming from India or whatever, and he did#39;t work there; he was working in a different city, different place, so they were like quit;What are you doing, dude?quit;

**Jerold Santo:**quit;What are you doing, man?quit; This also makes me wonder about spreadsheets, and how much -- like, are spreadsheets Turing complete? They probably are... First, they#39;re amazing. Microsoft Excel may be the most impactful piece of software in human history thus far, for many good reasons, and some entrenched reasons, but just the amount of productivity that people can get out of the concept and implementation of a spreadsheet is amazing... But it may be too much power to wield if you can write custom scripts inside a spreadsheet cell, or whatever this guy did, in order to hide logic bombs... It#39;s like, you#39;re supposed to just do sum, and average, and these simple calculations, but we#39;re-writing programs inside our spreadsheets.

**Nick Nisi:** He probably would have been saved by just using Pages, or something where the scripts would#39;t work.

**Jerold Santo:** Yeah, exactly. [laughs]

**Nick Nisi:** No Pages, Numbers.

**Jerold Santo:** Numbers. Well, they definitely would#39;t work in Pages, but...

**Across Aboukhadijeh:** It#39;s amazing what people can build with spreadsheets. I saw a chart recently that was showing the popularity of various programming languages relative to each other, and Excel was one of the programming languages, and basically all the vertical space was Excel, and then all the programming languages were these little tiny blips that barely registered on the chart. So it is actually quite empowering to a lot of people to be able to just use Excel and get work done.

**Jerold Santo:** Yeah, and it#39;s an uphill battle to replace such systems with more appropriate custom software that handles all the edge cases and does things quit;the right aliquot;, because a lot of reasons, one of which is like you#39;re now constraining the person, whereas they were previously free, and they were getting their job done; now you#39;re replacing their tool that liberated them and allowed them to be productive, with something which is more constrained, by design... But there#39;s a lot of backlash against that.

\[08:08\] There#39;s entire companies that just go around, and they basically replace spreadsheets with databases. They write web apps that are CRUD apps, that are replacing spreadsheets that have been running the business for years. It#39;s a whole industry.

**Across Aboukhadijeh:** I think we should give spreadsheets their due though. In some ways, they are actually just better than programming languages. If you think about how you start with the data first... You actually can start typing stuff into boxes, and even if you never write a formula at all, it#39;s just useful; you can start laying things out and seeing your data... Whereas with programming, you actually start with the machinery that processes the data, and you almost never really see the data in its intermediate stages. I might have got this idea from Bret Victory#39;s blog post, but... It#39;s this idea that programming is sort of this machinery for turning data from one format into another format, and you done#39;t actually ever see that happening when you#39;re coding; it#39;s all in your mind.

Your mind is basically simulating the interpreter. You#39;re trying to be a computer, basically, when you#39;re looking at your code. You#39;re imagining quit;What is this line going to do to the data? What is the next line going to do to the data?quit;, and you#39;re just stepping through in your mind... Whereas Excel - you can actually just see all the intermediate stages laid out there, because you put the intermediate cells there, and you can see that it#39;s working. It#39;s actually better, in a lot of ways...

**Jerold Santo:** Yeah. Nick, you do a lot of web apps for companies... Do you do any data modelling in your work? And if so, do you use Excel as a prototype? IN#39;VE done it in the past - tables and rows... A good place to start a database table is just to throw some stuff into Excel, and then eventually turn it into a data model.

**Nick Nisi:** I done#39;t... I open Excel and variants as little as I possibly can. I done#39;t know, my eyes just kind of glaze over when I look at them. That said, IN#39;VE been using this new note-taking app that basically has simpler spreadsheets than Excel as one of its main features... And kind of what Across said, it#39;s really blown my mind, because you can throw this notes data into a table, and then you can create different views to view the data as like a Kanban board, or as a timeline view, or these other views, but you#39;re always just working with the same underlying data... And it#39;s something that I would never do on my own.

I would never take my notes and write up something that can show me all of these different ways of looking at information about it. So it#39;s really empowering, being able to take that and then just immediately have it... So working from the data and being able to simply build out what I want to see and get the most information out of that data without having to write an entire application to do it.

**Jerold Santo:** And I bet it#39;s called Notion.

**Nick Nisi:** It is.

**Jerold Santo:** That#39;s hilarious... We have just started using Notion here around Changelog, even to collaborate with Adam, and Cody and me.

**Nick Nisi:** Nice.

**Jerold Santo:** IN#39;m having the exact same experience that you#39;re having. Literally last week I just started using it; I think Adam was using it before then. I know it#39;s Notion, because you sent me a link to a thing, to a page... There#39;s publicly-shareable pages, even though it#39;s an internal kind of thing.

**Nick Nisi:** Yeah.

**Jerold Santo:** Yeah, very interesting piece of software. It#39;s one of these things that#39;s so free-form, that it can be -- it#39;s kind of the paradox of choice, or the thing that freezes you, like quit;Okay, where do I go from here?quit;, but they provide some templates. But then that freedom also provides creativity, and it#39;s very interesting software. Different from other things that IN#39;VE used.

Speaking of spreadsheets, there#39;s a lot of people that are using spreadsheets as their back-ends. There#39;s Airtable, which is interesting, and then a lot of people are just building API integrations with Google Sheets, and basically providing web app front-ends to Google Sheets.

**Nick Nisi:** \[11:51\] I have done that.

**Jerold Santo:** Have you done that?

**Nick Nisi:** Yeah. For an RSVP for like a baby shower, or something... Just a really simple way to build out a custom front-end and then get the data to where it needs to go without me having to think about it too much.

**Jerold Santo:** Yeah... Talk about a logic bomb; throw it in there on your baby shower. Boom, it#39;s a boy. Alright, anything else on Across#39; inside logic bombs? Links to these things spoken about in the show notes. Nick did locate the BBC article, all about a U.S. employee outsourcing his job (it was to China), so if you want to read about that, it#39;s in the show notes.

**Nick Nisi:** Transitioning into your article, Jerold, I think that this could be the vector by which we might see logic bombs, if they ever come to JavaScript.

**Jerold Santo:** IN#39;m linking to a piece of satire which was written by a fellow named Sebastian K. on Medium, where he says quit;No way to prevent this. Only development community where this regularly happens&quot;, and it#39;s an Onion-inspired style... I think The Onion does this about gun-control laws in the United States after major shootings happen. But he#39;s not doing it about gun control, he#39;s doing it about NPM, and IN#39;LL just read this here:

Quit;In the hours following another package disaster on NPM in which a lone developer killed more than dozens of CI builds and caused serious warnings in thousands of others, developers of the only community where this kind of disaster routinely occurs reportedly concluded Monday that there was no way to prevent the disaster from taking place. Quit;This was a terrible tragedy, but sometimes these things just happen and there#39;s nothing anyone can do to stop them, &quot; said full stack developer Bob Donald on Reddit, echoing sentiments expressed by tens of millions of individuals who take part in the programming community where over half the world#39;s most infuriating package management disasters have occurred in the past 9 years and whose members are 200 times more likely to experience unexpected package updates than those of other established communities. Quit;It#39;s a shame, but what can we do? There really was#39;t anything that was going to keep these individuals from snapping and ruining a lot of people#39;s day if that#39;s what they really wanted.quit; At press time, residents of the only big established development community in the world where roughly two package management disasters have occurred every month for the past four years were referring to themselves and their situation as quit;helpless.quit;

So there#39;s your piece of satire... Across, you were linking this up as a story; I started with a satire. I did#39;t know there was an actual event here this week, so... What happened? Tell me about it. IN#39;m assuming there#39;s a malicious package that crept its way into NPM?

**Across Aboukhadijeh:** I think the word quit;malicious&quot; is not the right word to use.

**Jerold Santo:** Okay...

**Across Aboukhadijeh:** That#39;s what everyone#39;s using, but... That#39;s my opinion. So what happened was there was some kind of disagreement between maintainers of a package called Prescript... So this guy gave up the package to the other maintainers, but that package still depended upon some of these dependencies that he was in control of, and he added a logic bomb to... Speaking of logic bombs, it was basically a logic bomb, but it just made it -- I guess you can debate the definition of malicious, but I would say it just made it not work. It was a really tricky logic bomb that made the code not work... And I think the word quit;malicious&quot; to me implies that it was something like malware intended to steal information, or steal people#39;s Bitcoin, or steal personal information, or something like that...

And it seems like it was just some kind of disagreement where that maintainer just wanted to sort of sabotage the other project by making it do nothing. Not to say that#39;s not bad, but it seems like it should be distinct from actual malware, because I would hope no one#39;s actual production systems were affected by this. It should have been caught in CI; when the logic bomb ran, the code would#39;t work, and it would just be caught in CI, before it goes out to everybody.

**Nick Nisi:** We should clarify that that developer does claim that his credentials were stolen, and he did#39;t actually intend to do any of that.

**Across Aboukhadijeh:** That#39;s right, yeah. That#39;s true. The post that everybody#39;s sharing around is actually from the other side. It#39;s unclear what actually happened. It#39;s a quit;he said/she said&quot; situation.

**Jerold Santo:** \[16:03\] Yeah. I want to give props to Sebastian for writing a nice piece of satire on this. It is a recurring event that we#39;re seeing with these issues, and he even lists out five or six things that have happened recently... Well, maybe quit;recently&quot; ISN#39;t fair, because he goes all the way back to left-pad, which is somewhat ancient history at this point, at least in our industry...

But one piece of the metagame here - he has an edit on this post; this post is in the show notes if you want to read it... He says: quit;Besides some personal threats I received in response to this parody/sarcastic joke, IN#39;VE been asked to make suggestions how to fix the problem. Here#39;s an incomplete list...quit; So he goes into some suggested fixed. I done#39;t necessarily wanna focus on those... I wanna focus on the fact that this guy wrote a funny piece of satire and he#39;s getting personal threats about it? Like, what#39;s wrong with us? Can we relax a little bit and have some levity in our community without threatening people? I think that#39;s a shame.

**Across Aboukhadijeh:** Yeah.

**Jerold Santo:** Alright, so now that IN#39;VE scolded everybody... None of us did that, but it just made Across and Nick incredibly uncomfortable, like quit;Yeah, it should#39;t have happened!quit; Let#39;s talk about some TC39 updates. That#39;s a good way to segue... Nick, what have you got? Story of the week.

**Nick Nisi:** Yeah, so actually IN#39;m going to drop this and completely say that the most important thing this week is Chrome 76 now supports the media query prefers-colour-scheme dark. So Safari and Chrome - you can make your websites dark in them now.

**Jerold Santo:** That#39;s huge.

**Nick Nisi:** [laughs] That is interesting, and that did come out this week in Chrome... But let#39;s talk about TC39, because some changes did happen there. First off, some things have moved to stage four, and there#39;s a match-all method on strings, that works just like match, but it will return an iterator for all the matches provided. And then dynamic imports - that#39;s where you call the import keyword as a function, so that you can await that inside of your code and dynamically import something, rather than having to statically import it at the top of your file.

And then finally, Promise.allSettled(). This is a promise that will resolve once all the promises that have been passed to it have settled, meaning they have either resolved or rejected. So it does#39;t care which one, as long as they#39;re all completely resolved; then it will go off.

So those are some things that are in stage four, which means they will probably be part of ES2020 next year, and we#39;LL start seeing them trickle out into browsers... But two more exciting things potentially that moved up to stage three are the bullish coalescing operator and the optional chaining operator. Optional chaining is where you can say -- instead of saying foo.bar.BAZ and having to possibly do a check to make sure that foo exists and then bar exists... So instead of foo. Bar and foo.bar.BAZ, you can just say foo?. Bar?. And it will just return -- I think it returns null, or maybe undefined, if it does#39;t exist. So it won#39;t actually throw an error, it will just exit out. So it#39;s just some syntactic sugar to not have to do that through your code. It#39;LL make your code a little bit more expressive.

And then the bullish coalescing operator is the ??. That will specifically allow you to check for null and undefined, and not return for other false values like zero or empty string. So you can say some variable that you done#39;t know if it#39;s null or undefined, ??, and then maybe a string. And it will return that variable on the left side if it#39;s not null or not undefined, including if it#39;s zero or empty string... And then if it#39;s null or undefined, it will return on the right side of that operator, so whatever the string was in my example.

**Jerold Santo:** That#39;s nice to have if you#39;re trying to set a default value for something, right? Where you say quit;this or that&quot;, and you done#39;t want to match on empty string or zero, because those might be the valid values sent in; but you do wanna match on null or undefined, and set those to something that#39;s sane. Any other cool use cases for that?

First, I love the... What did you say -- is that optional chaining, or what#39;s that called?

**Nick Nisi:** \[20:07\] Yeah, optional chaining.

**Jerold Santo:** Yeah, so that#39;s a very nice piece of syntax, because it does become annoying over time to be checking that foo is here, and foo has bar, and foo and bar can call BAZ... So that#39;s going to be nice for folks. Anything exciting in there for you, Across? Any of these niceties that get you going?

**Across Aboukhadijeh:** IN#39;m excited about the optional chaining as well.

**Jerold Santo:** Yeah. So you said that#39;s stage three; what does the rollout look like? Does it go to stage four and then it#39;s up to the browsers? Is it in some browsers? Help me understand that.

**Nick Nisi:** It#39;s stage three... I think that#39;s when the syntax of it - in this case the ?. And then the ?? For these operators; that syntax is pretty stable, and now they need some actual real-world usage. That#39;s where some browsers will implement it... So we might start seeing this rolling out in the next year. I know optional chaining - but IN#39;m not sure about bullish coalescing one - will be coming into an upcoming version of TypeScript, so you#39;LL be able to use that natively in TypeScript, and then that will backport down to whatever it needs to run in whatever JavaScript you need to run it in.

**Jerold Santo:** What#39;s TypeScript? IN#39;m unfamiliar.

**Nick Nisi:** [laughs] Wow...

**Jerold Santo:** [laughs] Just kidding. No, please... Please, stop.

**Break:** \[21:26\]

**Jerold Santo:** Alright, we are back, and we are excited to explain things to each other as if we were five... Or at least new to a thing. Some of us take this quite literally and apply a five-year-old metaphor, others just try to explain technology in a way that a neophyte or a new person could learn it... So let#39;s see the way Nick tackles CORS. Nick, explain it like we#39;re five, CORS.

**Nick Nisi:** Alright... So CORS, like apple cores... No, CORS as in Cross-Origin Resource Sharing is the topic IN#39;m going to try to explain to a five-year-old, although I probably won#39;t be able to go that far with it, because you do have to know a little bit about how that network request can be made from websites, and things...

**Jerold Santo:** What#39;s a network request? [laughs] What#39;s a website?

**Nick Nisi:** Yeah... So starting there -- that#39;s the problem with this, you have to start from like quit;This is silicon.quit; So it#39;s this way of being able to access a server that is not on the same domain as the location of the website... And this is something that you could#39;t previously do. For example, if I had some JavaScript on NickNisi.com, and I wanted to pull in something from the Changelog website, I would#39;t be able to do an AJAX request to the Changelog website and go grab that.

So some workarounds were being made, things like JSON-P, or JSON with padding, I think, where I could basically put a script tag on my page that would load something from the Changelog website, and the Changelog website would be aware of this, that I was trying to do this, and they would send me a script that was basically just calling a method that I had told them to call, and passing data to that method. Then I could grab the data and use that, because it would call my method back when the script actually loads, and be able to run with that.

\[24:12\] That#39;s all well and good for sites that you can trust, which is probably no site ever, because you#39;re willingly just pulling in a script that can load onto your page and do anything. So it can be dangerous, and then you also have the problem of the site being down, and that would make the script load fail, and all of that. So a simpler method was developers, called CORS, or Cross-Origin Resource Sharing. This allows you to make a request to another site on the internet from your page, in as safe of a way as possible. What it does is it adds in a bunch of checks beforehand, to check to see if the server will actually allow this; if not, then nothing happens. But if the server will allow it, then it has a bunch of other checks.

The main thing that happens when you try and make a CORS request is your browser will add a header to your request; the header will be origin, and it will be whatever your site is, so maybe NickNisi.com. That would be set as the origin, and that#39;s nothing I can change; that would be set by Chrome itself.

Then it would make a request to Changelog.com, and Changelog.com, if they want to accept CORS requests, they have to respond with an Access-Control-Allow-Origin header that matches NickNisi.com, or has an asterisk in there, meaning that it matches everything. Then that way I can make requests between them.

So this is a way for servers to lock that down and say quit;Nope, we won#39;t do any of this, because we won#39;t send that header back.quit; But otherwise, if they want to accept that, then they can do that, and they can specifically do that for just specific sites, which is really cool... And all of this is out of the hands of the JavaScript developer and the browser; this is happening at the browser level, so Chrome is adding in these headers and doing all of this for you.

But it does get a little bit more complicated, because there are two kinds of requests that you can make; there#39;s a simple request and a preflighted request. A simple request would be a request that is using the method get, head or post, and is using only a subset of headers, so things like content language, content type - and with content type, only three different content types; that#39;s multi-form data, form URL encoded, and text plain. And then also one that is not setting up an upload listener, so listening for uploads, or anything like that.

If it matches all of that, then the browser will send the origin with that request, and then the server can respond with the Access-Control-Allow-Origin and the data that they want to respond with, and all is well and good.

But if I wanted to, for example, make a PUT request to the Changelog.com for my website, I can#39;t do that because that#39;s not one of the simple methods, so it would have to be a preflighted request. So what would happen is the browser would send an options request to Changelog.com first, and then that would say quit;What are my options, Changelog? Can I make any kind of requests or not?quit; And then Changelog can respond to that options with the proper Access-Control-Allow-Origin, and if I was trying to make a PUT request, it could respond with another header, Access-Control-Allow-Methods, and have PUT in that. Then that would say quit;Yes, you can make the PUT&quot;, and then I can make my request after that. So it#39;s actually two requests that end up happening.

And again, this is all outside of a JavaScript developer; the browser is making this request first, and then it will make the request that you asked it to. If the server comes back and says quit;No, I done#39;t accept that&quot;, then your request just fails and it does#39;t actually try and make the second request. So it#39;s just a way of controlling what a server can respond to or wants to respond to, and a way for the browser to make those requests in as safe a way as possible.

**Jerold Santo:** \[28:07\] Well done. Across, you mentioned in the break that you#39;re teaching CORS, or you#39;re going to be teaching CORS; is this along the lines of the way you explain it, or do you have any questions around that, or...? What are your thoughts?

**Across Aboukhadijeh:** One obvious question would be quit;Why does#39;t the browser require CORS for putting an image in a page, or putting a script in a page?quit; Because in those cases you can just link to another site and there#39;s no issue. The obvious question is quit;Why the difference between that and other types of requests?quit;

**Nick Nisi:** I have no idea why, but immediately the thing that comes to my head is legacy reasons.

**Across Aboukhadijeh:** Yeah, I think that#39;s pretty much the reason, but... It would be interesting to have someone who had the full context of the historical perspective to share that.

**Jerold Santo:** So it#39;s in place with JSON. If I wanted to grab some JSON off another website, I could#39;t do that. Fonts - definitely many of us have had CORS problems with trying to load fonts off of S3, or web fonts, and they won#39;t load until you go into your S3 bucket and add the CORS headers to the server response... So web fonts, gave request to web fonts are in there, JSON is in there... Image, it makes sense why you would#39;t need images, because there#39;s no -- I mean, Across, IN#39;m sure you can debunk this, but an image should not have any sort of ability to execute malicious things. Maybe if there#39;s vulnerabilities in the formats themselves, I guess...

**Across Aboukhadijeh:** There#39;s one thing that can happen with images - the browser automatically attaches cookies to requests to a site; so if I were to embed, let#39;s say, mail.google.com/some-button-image-that-google-uses, the browser will helpfully attach my Google cookies to that request... And that might change the type of image that the server sends back. So if IN#39;m logged in, it might send one image, and if IN#39;m not logged in, it might send back another image. So that#39;s why the browser does#39;t actually let you see the contents of the response, so I can#39;t actually look at the bits that make up the returned image. I can only embed it in the page, so the user will see one image or the other image, but a site ISN#39;t supposed to be able to go into the image and see what it is, if that makes sense.

**Jerold Santo:**...and glean the information out of it. Yeah, because that#39;s kind of data leak situation, right? You#39;re potentially leaking information if you#39;re logged in versus not, in that example.

**Across Aboukhadijeh:** Yeah. They could change the way CORS -- the problem is they can#39;t break old websites, right?

**Nick Nisi:** Could you fix this with a content security policy, or make things more secure on your site by restricting specifically where scripts can run from?

**Across Aboukhadijeh:** I think one thing is you can look at the size of the image... Say the images that Google returns are different sizes, depending on whether you#39;re logged in or not; now I can actually look at how much the other elements on the page were pushed left or right, and then I can figure out whether you#39;re logged in or not... So yeah, you really do want to prevent - you would want to prevent the image from being loaded entirely, or to at least prevent the cookies from being attached to it; and there are different specs for both of those things.

**Nick Nisi:** IN#39;m trying to find a link; I could swear that I saw a project on GitHub that was a complete chat client over GIFs. So it was just never fully resolving the GIF and being able to send data through that... But I can#39;t find it.

**Across Aboukhadijeh:** That sounds like a perfect Mad Science.

**Jerold Santo:** There is a GIF out there that you#39;LL never resolve; it#39;s called the Hassehloffian Recursion. IN#39;LL just leave it at that. You can go out there and look for that GIF. It will never resolve... But you might enjoy it, or you might hate it.

\[31:50\] Let#39;s move on. Across, you flipped the script on me... You#39;re going to explain the Zoom hack and DNS rebinding, which is not what this document said a few minutes ago... So IN#39;m excited now, because you must be into this one. Explain the Zoom hack to us. We happen to be using Zoom as we speak, so... Yeah, hopefully it#39;s secure now. But go ahead. Like we#39;re five, please.

**Across Aboukhadijeh:** I done#39;t know about that... [laughter] Well, I just thought it would dovetail nicely with Nick#39;s excellent explanation of CORS.

**Jerold Santo:** Absolutely.

**Across Aboukhadijeh:** Because I think that to understand this stuff, you end up needing to explain CORS; and since he#39;s already done that, we can skip that. So what happened with the Zoom chat app was that they installed a server on everyone#39;s computer who has installed the Zoom chat program... And that server is just like a server that#39;s listening on a local host on some port number. Just like when you#39;re developing a website locally, no different; it#39;s just a server that#39;s running on the computer, that anyone who can connect to your computer and knows the port can visit to see the server, to see the server response.

What they did wrong was - first, they did#39;t use CORS. That means that any website on the internet can send a request to this server. So you could be on attacker.com, and that site attacker.com can include (let#39;s say) an image tag in their page and make the source of the image be this local Zoom web server, and the browser will happily make an HTTP request to that server, get back the response and attempt to show it as an image. It#39;s probably not gonna actually render a valid image in that case, but that#39;s still this attacker#39;s website making a request to a server on your computer. The question then is what can that server actually do?

In the case of the Zoom server, it turns out it could join you into a meeting, and it would automatically turn on your mic and camera in that meeting. So in theory, you could be on a site that you done#39;t want people to know you#39;re on, and be auto-joined into a meeting within a second or two... And now this site literally gets a live feed of your face, and maybe you done#39;t want to share that. So it#39;s pretty bad...

This was made worse by the fact that they did#39;t actually use CORS, which would have let them at least -- what they could have done is they could say quit;Okay, this request is coming from attacker.com. We#39;re gonna not actually--quit; Well, so this is slightly different from CORS. CORS says you basically return the response to the browser, and you tell the browser quit;By the way, I only want to allow these domains to use this resource&quot;, and then the browser enforces that for you. This is why I wanted to talk about this Zoom hack, because it#39;s a lesson in actually what CORS can do and what CORS can#39;t do.

What they should#39;VE done in that case is asked the question quit;Which website is making this request to us?quit; and it turns out actually CORS does#39;t help you there. Like I was saying, CORS just says quit;I want this site to be able to see the contents of this resource or not.quit; So what you really want to do is look at a different HTTP header that#39;s included automatically by the browser in the HTTP request, and that#39;s the host header. That#39;d be the referrer... Right? Now IN#39;m confusing myself... This stuff is confusing. No, it#39;s the referrer header, I believe, that tells you where the request is coming from.

Now, it may be the case that Zoom wants to allow any website to try to join you into a meeting, right? Maybe that#39;s like a product decision that they want to make; but then they should prompt you before they join you into the meeting.

I think what they really wanted to do was to say quit;No, you have to visit a Zoom URL, and then only the Zoom site can join you into a meeting.quit; So only the Zoom site should be able to tell the local Zoom web server to open up the Zoom app before you. And if that#39;s what they wanted to do, then what they really need to look at is the source of their request. They need to see that it#39;s coming from the Zoom website.

**Jerold Santo:** \[35:56\] Which that was the point of the feature - you get an email, quit;Hey, this person is inviting you to a Zoom meeting.quit; And there would be a link in the email, you open the link, it would take you to Zoom#39;s website, and if you had the app installed, it would launch your Zoom meeting automatically, using that web server, right?

**Across Aboukhadijeh:** Yup.

**Jerold Santo:** So that was the intent... Which is a legitimate feature. I mean, it#39;s a desirable feature, apparently. I mean, IN#39;VE used it, and it works; you click on the thing, it opens the thing. They wanted to build it for their customers, so it seemed like they had good intentions, but the benefit was far outweighed by the drawbacks of having this -- you#39;re basically installing a backdoor, insofar as there is a locally-accessible web server now on these people#39;s computer, which previously was#39;t there, and which could be accessed remotely or locally.

**Across Aboukhadijeh:** Yeah. And I think IN#39;LL skip explaining DNS rebinding, because I actually think that is a longer explanation than I realized. But it is very interesting. It#39;s a very weird, interesting attack that I think a lot of developers done#39;t know about. Maybe on a future episode.

**Jerold Santo:** Okay. So stay tuned for DNS rebinding. Maybe we#39;LL hook up a link for those interested to read, and then they can critique Across#39; future explanation of what DNS rebinding is... But for now, that#39;s it.

**Across Aboukhadijeh:** We totally failed... We totally failed to explain it to a five-year-old. I done#39;t even think I would understand what I said, so...

**Jerold Santo:** [laughs] Well, let#39;s ask a listener... Did we at least succeed in explaining it to whatever age you are, listener? Let us know on Twitter, @jspartyfm, or Discuss This in Changelog News in your show notes; it#39;LL take you to the JS Party page on Changelog.com, where you can post a comment. Maybe go in there and explain these things better than we did... Or tell us what DNS rebinding is, because I have no idea. That#39;s it for Explain It Like IN#39;m Five.

**Break:** \[37:51\]

**Jerold Santo:** Alright, it is time for our shout-outs. This is where we give shout-outs to people or projects that we think deserve recognition. IN#39;d like to give a shout-out to somebody whose name is difficult for me, but she#39;s an awesome person... Hong PUC Dang. I think she#39;s @hpdang on Twitter and GitHub.

We met her at OSCAN, she was walking around the show floor with these cool little hardware scrolling marquees that were programmable via Bluetooth... And she was out telling people about a community called FOSS Asia. So shout-out to Hong and FOSS Asia.

If you Haven#39;t heard of FOSS Asia, you#39;re a lot like I was. It is the largest -- let me get this right; actually, they just scrolled their marquee... Oh, done#39;t we all hate those scrolling marquees? What are they called, when they slide in a new picture...? Carrousels. We all hate carrousels. FOSS Asia has one; done#39;t hold that against them, it#39;s just a thing... But their statement is quit;Bringing together an inspiring community across borders and ages to form a better future with open technologies and ICT.quit; This is a large, large -- I can#39;t remember the number, but I think it#39;s like a 30,000-people-strong group of Asian software developers.

\[40:10\] I think they are out of Singapore specifically, but all over Asia. They get together and they#39;re doing open source stuff; they#39;re doing a lot of hardware hacking, they have a lot of software projects, and it#39;s a group of people that I had never even heard of as a member of the Western open source community... And there#39;s a huge gap between the East and the West, both geographically, and, you know, with water... And unfortunately, that means there#39;s a gap in our community, and we can hopefully close that and get to know each other. That#39;s what Hong was at OSCAN doing - going around, telling people about FOSS Asia.

There#39;s lots of different ways of getting involved. I think they#39;re up to cool stuff. They have a lot of stuff on GitHub, so check out FOSSAsia.org. Shout-out to Hong for doing the yeoman#39;s work of getting out there and telling people in the United States about this community, which is large, and growing. Check them out and say hi.

Okay, shout-outs... Across, you#39;re up.

**Across Aboukhadijeh:** I want to shout out Neocities, which is an amazing website that#39;s bringing back Geocities-style sites. They give you free website hosting, with zero ads, and they let you put whatever you want up there. So it#39;s just like a static web hosting, and there#39;s a lot of interesting, quirky little sites on there.

The way they put it is they#39;re bringing back the lost individual creativity of the web, which is pretty cool. The guy who created it - his name is Kyle Drake. Really nice guy. He was really sad when Geocities was taken down, and... He actually has a related project to bring back up an archive of all the Geocities sites that folks were able to save before Geocities was shut down. I think right now all that stuff is on the internet archive, but it#39;s not very easy to browse...

So he#39;s about to release a new site called geocities. Gallery, which lets you peruse a huge chunk of the original Geocities sites. I actually helped him get the midis working again, using my midi JavaScript library. So now you get the full glory of the -- and he also had to add back the blink tag, because I think that one was deprecated and removed. It#39;s pretty cool, so shout-outs to Kyle Drake and Neocities, and geocities.gallery.

**Jerold Santo:** It#39;s really cool. So if you build a Neocities site, are you basically just doing HTML, doing stuff right there in the browser, much like Geocities was? Or does it work differently than that?

**Across Aboukhadijeh:** It has an in-browser editor. You can just type the HTML right in, and it does#39;t really get more complicated than that. It does expose people to HTML, which is, of course, one of the benefits, actually, of this approach.

**Jerold Santo:** Very cool. I remember when Geocities was shutting down... And I done#39;t know if Kyle Drake the name rings a bell, but there was somebody who went and crawled the entirety of Geocities, and then I think he eventually turned it over to archive.org. Maybe it was Kyle, but I remember that being a thing, and people were supporting him because -- was it Yahoo! that owned Geocities? They were literally taking the thing down. It had existed in broken window fashion for years, and it was like quit;This is actually going to disappear off the internet&quot;, and there was a movement to save Geocities. It was a fun thing back in the day. I think it ended up on archive.org.

Alright, Nick, your turn.

**Nick Nisi:** My shout-out goes to Nuclide on GitHub, and specifically their project COC.vim. It#39;s a project that IN#39;VE been using for the past couple of weeks, and it#39;s just amazing. COC stands for quit;to conquer of completion&quot;, and it#39;s an Intelligence completion plugin for Vim that makes full use of the language server protocol from VS Code. That means that you can take VS Code plugins that tie into that and port them to Vim, so that you can use them straight within Vim. It#39;s really cool.

\[44:22\] Obviously, the main plugin that I use within there is the server one, so I get the exact same completion that I would get from using VS Code; I get it straight in Vim. And then there#39;s other ones like Prettier, so it#39;LL just automatically run Prettier on my code when I save. There#39;s a plugin that when IN#39;m specifically in a Git commit message in Vim and I type the £ sign, it#39;LL give me a dropdown of all the issues that are open on that repository, so I can autocomplete those... And there#39;s just several other plugins available. There#39;s an emoji plugin... It just really is so cool, being able to take all of this cool hotness from VS Code and bring it over to the one true editor.

**Jerold Santo:** [laughs] You mean Atom? No...

**Nick Nisi:** Yes!

**Jerold Santo:** So Neovim - this is written in TypeScript; does this work with regular Vim? What#39;s Neovim? Do you need to use Neovim and not regular Vim here?

**Nick Nisi:** Neovim is actually not written in TypeScript. It#39;s written in -- oh man, I done#39;t even know... But it#39;s a more modern version of Vim, meaning that the community is a little more open to contributions and to changes, whereas earlier Vim - they#39;re kind of slowing down in some aspects. There was no way to really run asynchronous jobs; so Neovim came along, and they dropped support for a bunch of old cruft, like not needing to run on old Polaris systems, for example... I done#39;t know if that#39;s actually the case, but being able to drop all of that cruft makes the project lighter and makes contributing and welcoming new contributors much easier.

Then they added their own async job support, and then that kind of --

**Jerold Santo:** That got Vim going again, right?

**Nick Nisi:** Yeah. And so they came up with a different approach to async jobs, so now plugins have to support both... But for the most part, as just an end user, Neovim seems much faster; or it did, at least when I started. I Haven#39;t used Vim 8 very much to say that it#39;s gotten much better. IN#39;m sure it has, but IN#39;VE just still kind of stuck with Neovim, because of plugins like this, and others... But I have basically aliased Vim to Neovim or to vim in my shell, just so I done#39;t lose that muscle memory in case I ever switch back. I just type vim for everything.

**Jerold Santo:** Gotta keep your options open there. So Neovim - written mostly in C... 44% of the repo is Vim script though, so there#39;s also some Lua sprinkled in there. That being said, the COC.vim is TypeScript... So does Neovim add some sort of like a JavaScript way of writing these things? Because it used to be you had to write Vim script through Vim plugins, but... Maybe Neovim enables that.

**Nick Nisi:** Yeah... It enables better support for plugins written in other languages.

**Jerold Santo:** Gotcha.

**Nick Nisi:** And then there#39;s packages. On NPM there#39;s a Neovim package, and there#39;s a By in the Vim package for Python. And then you can write your plugins, and they can more easily talk to the native Vim script that#39;s running in Vim itself. So you can make plugins that work much better throughout all of them. I Haven#39;t written a plugin, so IN#39;m just kind of talking and not 100% sure of myself here, but... Yeah.

**Jerold Santo:** Well, that could be our motto here at JS Party: quit;We#39;re not 100% sure, but we#39;re just kind of talking.quit; Awesome shout-outs. It#39;s always fun, we love to give respect to people out there doing cool things, so thank you to FOSS Asia, to Neocities and to COC.vim. Links to those things in the show notes. If you use them or you#39;VE found them from this show, let them know; tell them hi out there on the internet, and thank them for the things they do, and let them know you heard about them here on JS Party.

That#39;s our show for this week. Stay tuned, next week it#39;s a big one - we#39;VE got another debate show. We#39;re going to be talking modern JS tooling. Is modern JS tooling too complicated? Yep? Nope? We find out next week, when Divya and Micheal face off against Across and Chris to answer that question. We#39;LL see you next time!
