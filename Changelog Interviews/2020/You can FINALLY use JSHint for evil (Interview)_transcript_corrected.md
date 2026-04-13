**Jerold Santo:** Alright, we're joined by Mike Pen nisi, maintainer of JSHint. Mike, thanks for coming on Maintainer Spotlight with us.

**Mike Pen nisi:** Thanks for having me.

**Jerold Santo:** So we're here to hear the saga, the JSHint saga, which has been a long one... And now you can finally use it for evil, which is somewhat ironic, but we're going to find out why. First, tell the folks about JSHint's beginnings; because I remember JS Lint, and I remember JSHint, but probably not everybody does. How did JSHint come about, and why did it become popular?

**Mike Pen nisi:** Sure. Yeah, JSHint is a fork of a project that's, as you mentioned, called JS Lint. JS Lint was maintained really as the first probably professional-grade JavaScript linter. It was self-hosted, so it was written in JavaScript, and it was for a lot of folks their introduction to even just the linting... Because you know, we're coming back in the early 2000s - people were just writing their first widgets, having basketballs trail mouse cursors, and stuff like that...

**Jerold Santo:** Right.

**Mike Pen nisi:** So using linting is kind of a novel concept in this space. That's the tool they used. The unfortunate part about that project was it was very opinionated, and kind of emphatically so. So when they determined that things not just were invalid syntax, which are objectively incorrect, but also kind of dangerous patterns, it would just report them as all the same, and there wasn't really anything you could do with that. So you were sort of at the mercy of the maintainer when it came to how you wrote your code. Things that were technically correct would not pass, because they were deemed to be dangerous.

**Jerold Santo:** Right.

**Mike Pen nisi:** \[04:04\] So a lot of folks were not so happy with that, and one of them decided they should make a different project based on it, with those things configurable, so you as the developer writing the code had a little bit more say in what was acceptable and what was not acceptable. So that was Anton Kodaly, and I've probably mispronounced his name. He was actually inspired by Paul Irish, who was quite prolific in the frontend development scene... He decided to fork the project, and so he created JSHint as kind of play on the word JS Lint, and made all those rules that weren't objectively syntactic errors - he made those configurable, so they could be enabled or disabled.

**Jerold Santo:** Yeah. I do remember that, and I'll say, to Anton's credit, I think the name JSHint was a bit of marketing genius, because - we're gonna talk about adoption, and things that lend to open source adoption, or non-adoption, and one thing is making your value proposition very clear from the beginning... And anybody who'd come across JS Lint and had felt the pain of what is sort of a Draconian linter; an overbearing, like you said, configurable linter - when they heard about JSHint... It clicks immediately what this is, in comparison to JS Lint. It's like a fork of that, only instead of it being linting in this heavy-handed way, it's hinting. Even though it's still a linter. But just that name for me immediately made it clear, like "Oh, it's like JS Lint, only I'm going to be able to either configure it, or it's going to be less onerous, and I'm going to like using it a lot more." So I thought that was always a clever name for the project.

**Mike Pen nisi:** Yeah, for sure. And it's interesting too, because hinting is not really a term.

**Jerold Santo:** Right.

**Mike Pen nisi:** Even linting is niche, a bit of jargon, that comes from other software industries. But despite that, you still see it used it in Stack Overflow; people would talk about hinting their code. It's kind of like a legacy reference, even when they're not talking about JSHint specifically.

**Jerold Santo:** Well, that's funny.

**Mike Pen nisi:** So it kind of leaked into the consciousness a little bit.

**Jerold Santo:** Yeah.

**Adam Staravia:** It seems like its pretty kind too, versus being heavy-handed. It's a psychological aspect to just being a little bit more kind with the way you guide people to do better, or to adhere to standards, whatever it may be.

**Jerold Santo:** Right. Versus slapping them on their wrist, or something.

**Adam Staravia:** Yeah. It's definitely kind.

**Jerold Santo:** So how did you get involved? Anton created it... How did you get involved?

**Mike Pen nisi:** Well, it was really coming to bear right when I was getting started in the industry. I was out of school, and started my first real job as a software developer at a small company called Bo coup... And we were all using it there. It was kind of like my first real open source contribution.

I can still remember, it was the tool that we were using, and I felt like it was so neat; like, this is a tool that's telling other JavaScript developers what's right and what's wrong, and like, I've found a bug in that. There was a lot of prestige, it felt like, just inherent in being a linter, because you're kind of authoritative over other developers... So being able to contribute to that was really exciting.

So I made my first contribution and didn't think much of it for many years after that. I started becoming a maintainer just because I was following kind of in my co-worker Rick Waldron's footsteps... And he himself was getting more and more involved, preparing the project for ES6 support. ES6 is the acronym for the revision of the language that was published in 2015. It included a lot of new features; and getting a linter (which is at the heart of it a parser) prepared for a new version of language requires a lot of work.

\[08:02\] Rick had been a long-time member of TC39, which is the standards body for JavaScript... So he was particularly -- he had the interest and the skill and the knowledge to help other parsers prepare. So he was doing that with JSHint, and I was myself following in his footsteps and contributing there, too.

**Adam Staravia:** How far back was that again? How many years ago? This beginning, or this timeframe that you're describing now - how far back was that?

**Mike Pen nisi:** That probably would have been late 2013, early 2014, so 6–7 years ago.

**Jerold Santo:** Yeah, and so around the time that you became very involved, there was this adoption issue which started to manifest... And you've gone on a long, somewhat circuitous, but a path to removing that issue over the years - it's finally become formalized in 2020 - which was to change the license. And the license itself back then - and I'm not sure if this was your choice, or if this was Anton's choice, or whoever's choice it was, was basically an Moresque... It was like MIT Expat, which I'm not sure what Expat is; I read it, but I didn't follow up... Is it MIT with a couple of extra provisions maybe?

**Mike Pen nisi:** No... So I said MIT Expat; you caught me being a bit pedantic, but... It's because MIT is technically a little bit ambiguous, so if you listen to the Free Software Foundation or folks like that, they'll make this distinction, because it may refer to other licenses...

**Jerold Santo:** I see.

**Mike Pen nisi:** But generally, when people say MIT license, they mean the MIT Expat license.

**Jerold Santo:** Okay, fair enough. So it's what we probably commonly think of MIT, plus a clause...

**Mike Pen nisi:** That's right.

**Jerold Santo:** And that clause was "This software shall be used for good, not evil." We could have said it in conjunction, it would have been epic.

**Mike Pen nisi:** We could sing it.

**Jerold Santo:** \[Oh, I can't sing, but please do. \[laughter\] This software shall be used for good, not evil. Was this the only addition to the MIT? Was it MIT plus that clause?

**Mike Pen nisi:** That's right.

**Adam Staravia:** You would think that would not ruffle so many feathers, but it does.

**Jerold Santo:** Yeah. So what did that due to the project?

**Mike Pen nisi:** Well, that's probably going to be what we talk about this whole time, is what that did to the project, but...

**Jerold Santo:** Yeah, it's a big part of it.

**Mike Pen nisi:** In the immediate sense -- well, first, as far as its provenance goes, that was a vestige of the JS Lint project. So that is not something that Anton --

**Jerold Santo:** Oh, it wasn't a decision made by you guys, because you were a fork of JS Lint, so it was in JS Lint.

**Mike Pen nisi:** Right.

**Jerold Santo:** Okay.

**Mike Pen nisi:** So it was subject to the provisions of the original license.

**Jerold Santo:** Gotcha.

**Adam Staravia:** And this is Douglas Crockford thing. He's all about good, not evil. That's his MO.

**Mike Pen nisi:** Right. Crockford - I think it's the first time we mentioned him; so that's Douglas Crockford. He's pretty prolific in this period, and also worked on, for instance, the JSON 2 parser, which - back in the day you had to use a JavaScript library to parse JSON... So he worked on the JSON standard and the reference implementation.

**Jerold Santo:** Right.

**Mike Pen nisi:** So he also made JS Lint... So yeah, he has this license that he applies to a lot of his projects, that is - as we were saying, the MIT license, with this clause. And in an immediate sense, what that does is it essentially makes what is otherwise a really clear and succinct legal contract, which is kind of a thing to be treasured, I'd say, in this world...

**Jerold Santo:** Sounds like it, yeah.

**Mike Pen nisi:** ...it makes a clear and succinct legal contract into something that's really unenforceable and just generally scary to people that take licensing seriously... Because the term "evil" has no real meaning in any court, anywhere. So either you're the type of person that disregards the license and just uses stuff because the source code is available, or you recognize that you're beholden to a contract, and you see in this contract terms that you don't understand.

\[12:04\] So what that means for people that have to, like I said, either take this seriously because they want to, or take it seriously because their legal team forces them to, this says to them "I can't use this project because I don't know what it is that I'm beholden to if I do."

**Jerold Santo:** Right. It just moves it into a vague place. I've heard similar things with people who think they can release their code with no license, and just claim that it's public domain, because public domain doesn't have legal holding in certain countries... So actually no license is worse than -- it's less free than a free license, or permissive license, or whatever license you end up choosing, because it's ambiguous; people are not going to adopt it if they care about licensing. So I've seen people who start with like "This code is hereby issued into the public domain." I feel like SQLite was like that originally, and that's where I heard that, but I could be wrong on the details there... And they end up going back and making it licensed, because a bunch of people rolled in saying "Hey, I'd love to use this, but I can't use public domain. It has to have a license."

**Mike Pen nisi:** Yeah.

**Jerold Santo:** So in this case, it goes from a place where if it was merely MIT -- it's like, the MIT license has been legally vetted and used, and is kind of like out there; it can just be accepted by people that accept that particular license inside their organization. But once it adds that other provision, it's like "Well, no longer that. It's something different."

**Mike Pen nisi:** Yeah.

**Jerold Santo:** And that's just enough to be like "Elm... I'm just not gonna screw with it. This could backfire on me."

**Mike Pen nisi:** Right, right. And it's almost to the point where like -- you know, when people say "Oh, it's MIT with another clause", you will almost wanna push back (at least I do, after years of thinking about this), to say "Don't even start that... If it's MIT with another clause, then it's not MIT." So it's not really useful to talk about it that way, but...

**Jerold Santo:** Right.

**Mike Pen nisi:** Again, with pedantry--you can't help it with a guy that works on a JavaScript parser... So I try to keep that bit of feedback to myself, usually...

**Jerold Santo:** \[laughs\] Well, as software developers, we tend to focus in on the little things, because they sure do make a difference to a computer, right?

**Mike Pen nisi:** Yeah, yeah.

**Jerold Santo:** And they sure do make a difference -- I mean, the legal apparatus is a lot like a computer in its pedantry. You can to be specific, and you have to be clear... So it's worth sweating those particular details, whereas in many contexts of life, you're like "Dude, leave me alone with that. I don't care." But you have to actually care. If you care about licensing, MIT plus that clause changes everything.

**Mike Pen nisi:** Yeah. The way we learned about this was through issues -- it's funny, it was through an issue filed by a contributor that I'd never met before, saying "Please remove that clause." And it's funny, that was filed on GitHub.com, and there are certain parts about how it was filed there, because it's somewhat coincidental... For instance, it was assigned Issue \#1234, which is a kind of nice -- not round number, but...

**Jerold Santo:** Easy to remember.

**Mike Pen nisi:** Yeah. And it was also filed on my birthday of that year, for whatever reason.

**Jerold Santo:** Oh, my...

**Mike Pen nisi:** I was one of those people at that time that didn't really care as much about software licensing, because despite having contributed to the project, I wasn't aware of its license. And now, it's been a long time -- and it's not just because of this, it's also because of (we mentioned before) the Free Software Foundation becoming involved there, and just generally thinking much more deeply about open source and free software, and the distinction between those two, that all this stuff started becoming more and more important to me personally. It's interesting for me to remember the fact that I wasn't aware of that myself, so that makes me much more sympathetic to folks that don't necessarily care as much about licensing when I'm telling this story...

**Jerold Santo:** \[15:58\] How big of a problem do you think this was? So you had people say "Please change the license", right? I think you cite in your essays, which we will link to in our show notes if people want to read the whole story from Mike's keyboard, versus his mouth... You cite in their certain situations, like a WordPress situation and a few other ones, where it's like "We're not using this because of the license." Do you think this was a widespread problem, or do you think most people don't care, and some outliers do?

**Mike Pen nisi:** Yeah, I would say it's definitely more towards the latter, where most people don't care, and some people do. And it's really hard to say for sure. I can say just from the perspective of a maintainer that we lost interest... But there are a lot of reasons that could happen. And it would be easy for me to kind of pass that off as like "Oh, it's all because of the license, and nothing I did as a maintainer, for instance, had anything to do with it." And there are certainly things I did as a maintainer where I wasn't as good a maintainer, or I made some poor choices, for instance, that affected this... But it's a really complicated -- the motivation behind free and open source software is really complex; there's market forces to take into play, and all this stuff... And it's also kind of a feedback loop.

I get into this a little bit in the blog post, but just reflecting on the fact that whatever the reason that a project starts to become less widely used, for open source projects their user base is largely driven by their contributor -- or I should say their contributor base is largely driven by their user base. So if you lose users, you're losing contributors, and it's kind of a vicious cycle in that sense.

So I've focused a lot on the license over the years, but it's important, at least at some point, to acknowledge that there are other reasons why any project, including JSHint, rises and falls. So it can't just possibly be that.

**Adam Staravia:** It's lived out there for a while though, with this license. So to kind of go back to some things you said in -- I think it was your post on why you stuck around, essentially... That your understanding of ethics and free software was growing when you first began to contribute. And I would say that this is an era, given how long the period is with this clause in there, that others - especially corporations and commercial users of open source - will begin to become more educated of licensing, and more concerned (I suppose) over differences. So I would say maybe the curve of adoption and decline potentially was in line with/parallel with external education towards licensing, and scrutinizing, and \[unintelligible 00:18:43.06\] criteria, and whatnot.

**Jerold Santo:** Yeah, maybe.

**Adam Staravia:** So that might be more like a large bump at the beginning, less concerned about licenses. Oh, get more educated about licenses; this is ambiguous, this is vague. Start to turn or pull those out, and use those less, or replace them. So it could be multi-faceted, really. Not just simply the clause, but awareness and education around licensing. Because that's certainly changed a lot in the last eight years.

**Mike Pen nisi:** Yeah.

**Jerold Santo:** And plus, with success and adoption you're going to have -- with an increase in adoption you're going to attract larger entities. So me as a freelance consultant - I wouldn't think twice about... Especially with tooling - JSHint is tooling; it's part of my development flow. But I'm not necessarily shipping any of that code down a website pipeline. I would concern myself so much, especially with the MIT Plus clause.

But once you start attracting larger entities that have legal teams, and that maybe have been through legislation and gotten "Once bitten, twice shy", these larger corporations or organizations are much more aware of the legal dangers than individuals are, just generally speaking... Although there's definitely license nerds out there, as you slowly become one by necessity. You learn these things, and -- hey, I'm kind of a licensing nerd, mostly because of Nadia Offal, Request For Commits, and Micheal Rogers, and just learning about them; it's very fascinating. But that's a very small subset. But I think once you get into the place where your users are spread abroad and are of differing sizes, the bigger users are the ones that are going to say -- or the potential bigger users, who say "We're not going to use this, because they're the ones that care."

**Mike Pen nisi:** \[20:26\] Yeah. And actually, it's kind of perverse in some ways, because -- I'd say it was perversely encouraging, in some ways, to know that people were kind of stepping away from JSHint... Because on the one hand, day-to-day, I'm fixing bugs, I'm implementing features, and I'm responding to a dwindling number of bug reports, for instance... So I'm very much invested in seeing the project be successful, just because it's something that I'm passionate about, and trying to maintain. But at the same time, I'm also knowing that usage is going down because of this reason, so that's kind of demotivating.

But I say "perversely" because at the same time I recognize that the motivation for that is good overall. I'm actually encouraged by the fact that people are thinking more about licenses. So as much as I say "Well, I want my work to be used", I also want people to -- really, I think the more important thing is that people care about licensing. So I've always felt two ways about it, and that's actually what's been most driving for me personally to get this work done - I want to be able to someday walk away from this project in good conscience, and be like "I didn't just dump years of my life into a project that I can't even endorse."

**Break:** \[21:33\]

**Jerold Santo:** So Mike, you mentioned that the license was a problem around adoption and traction, but it wasn't the only problem. Of course, everybody makes mistakes, especially when you're a first-time maintainer, or you haven't maintained something that's so popular... Even long-time maintainers. People make mistakes, and they mismanage, and they have bad days... So we can all help one another by learning from each other's mistakes. I'm curious if you're willing to share a few things that you thought maybe you could have handled better, or reasons why you think JSHint has started to decline, that weren't because of this vague license.

**Mike Pen nisi:** Sure, yeah. I can think of two big ones. One would be JSX support. Many of your listeners will recognize JSX, but for those that don't, it's kind of a derivative of the JavaScript language that was popularized -- well, actually developed and popularized by Facebook to support their React framework for making web applications. So as that framework became popular, folks were increasingly writing code that wasn't quite JavaScript, but it was JSX. So it was JavaScript with additional rules that were syntactically invalid from EMMA, or the official standpoint. So they of course turned at our linter to continue to tell them about bad patterns in their code, except now their code was in a different language.

\[23:57\] So as a maintainer of JSHint, I was pretty reluctant to support JSX. I had a few reasons for this. One, just to get it out of the way, is that I'm no fan of Facebook, the corporation, and so technology that comes out of that place I'm less excited to support on a personal level. JSHint was in my fiefdom, so it wasn't as though I just said "Oh, I don't like Facebook, therefore this project is not going to do it." There were some technical reasons for this as well, which is a little bit of (you could say) baggage in JSHint around its previous efforts to support non-standard editions to the language. JSHint -- actually, Anton (you remember, the original maintainer of JSHint) was employed by Mozilla for a span of time... And during this time, he was very much engaged/involved with the folks at Mozilla that were experimenting with the language, most notably Brendan Eich, who actually wrote the language initially.

So people may not remember this, but Firefox, the web browser that was produced by Mozilla, was putting out an experimental version of JavaScript. They were calling it JavaScript 1.6. So it had additions to the language that preceded that ES6 that we were talking about earlier. And that had some of the same features, but a lot of different features. So it was kind of like a playground for Mozilla, and they were just kind of putting out what they wanted to, just to see what worked, and to see what it would be like. And they were doing it in a somewhat responsible way. It wasn't just like unleashing it on the internet at large. You had to opt in with a script tag that said "Language type is JavaScript/1.6", or something like that, I believe. But still, that required changes to a parser to support, and Anton being so involved and so generally helpful in an interesting tooling, extended JSHint to support a lot of that stuff.

In hindsight, we can see that a lot of this stuff that Mozilla was working on didn't really pan out. But JSHint still maintains a feature flag that they can turn on called MOZ, and MOZ enables JS 1.6 support. So to this day, you can still have array comprehensions in "JavaScript" if you use JSHint. There are a lot of code paths that's just legacy that we're supporting. And this is a bit of a tangent now, but bringing it back to JSX - that was very much in my mind, especially when React was in its early stages. I was thinking "Do I really want to commit this project to all these code paths?"

**Jerold Santo:** Right. "I won't make this mistake again."

**Mike Pen nisi:** Right, right. In retrospect, again, we can see that maybe that was a bit near-sighted, but it probably seems that way because we know how popular React and JSX have become.

**Jerold Santo:** Yeah.

**Mike Pen nisi:** At the time it wasn't as clear; it just seemed like, "Oh, this is a weird HTML inside JavaScript thing. How much do I really want to commit to this?"

**Jerold Santo:** Those are tough decisions, right? Especially, again, "Once bitten, twice shy." You've gone down that path before, and you've seen the results of making what is essentially a bet on something that doesn't come through, and now here comes another one, and it's a non-standard thing, and it's like "Well, how big is this going to get?" I don't know; if we all saw how big React would get or not - I'm sure we all didn't... But especially when you have a bias against Facebook in the first place, you're like "Oh, gosh..." You're maybe hoping this thing goes away. \[laughter\] But it sure has stuck, hasn't it...?

**Mike Pen nisi:** Yeah.

**Jerold Santo:** Yup.

**Mike Pen nisi:** I want to be fair, to say -- you know, it wasn't a decision that you make once and that you're stuck with.

**Jerold Santo:** Sure.

**Mike Pen nisi:** So while it's true, at one point we didn't know it. Even today I could be implementing that. At this point, JSHint is not really relevant - I'll be honest - anymore, so the motivation to do that is very low; it's probably lower than it's ever been, on my part. But getting back to what we were saying before about the...

**Jerold Santo:** \[28:11\] Mistakes.

**Mike Pen nisi:** Well, mistakes, sure, but also even before that, about the vicious cycle... I might not have personally decided to implement JSX, for reasons that were either personal or motivated by experience, but also, we weren't seeing too much clamouring and too many people stepping up to help do that as a contribution either.

**Jerold Santo:** Right.

**Mike Pen nisi:** There's probably some cusp where all the people that in other situations might have been jumping at the chance to implement that in this project, we're also being driven away, and going somewhere else for it.

**Jerold Santo:** Yeah. So it's kind of like what could have been...

**Mike Pen nisi:** Yeah, yeah. Another one though that I should say... There's kind of a really important feature that we just couldn't support architecturally, that a competing project - well, "competing" sounds pretty negative; an alternative project, we'll say - called ESLint did support... Not initially, but I think from pretty early stages, which was this concept of autofixing.

ESLint is another linting project, and it offers this ability for a lot of the problems that it flags, to actually change your code for you. And it does that because it's kind of built from the ground up with a sensitivity to things like that... Well, with a sensitivity for that operation. So in order to do that with JSHint - it was not architected that way by any means. It would be a significant - probably a full rewrite - in order to make something that could intelligently change parts of code in the way that another project does.

So it's almost like -- new iterations on old ideas, they have an inherent advantage in that they're not really bound to some of the false assumptions made when the old idea was first implemented.

**Jerold Santo:** Well, you mentioned relevance and ESLint... So the question that arises in many people's minds, and which you do address in the post, but we addressed it here as well, is "Here you've got this licensing problem, you've got an adoption problem, where it was skyrocketing, now it's levelling out, and you have maybe some features that are lacking..." And here comes another project, which is an alternative - not necessarily a competitor, but an alternative project that has some technical advantages with regard to autofixing. You could have just hopped on the ESLint bandwagon and said "You know what - JSHint was a tool, it was great, it's still there, we're not going to take it off of NPM, but no longer maintained because of these reasons, and I'm gonna start contributing to ESLint starting tomorrow, and just pick that one up and put my efforts there." Why not that?

**Mike Pen nisi:** It's a good question. There are a few reasons. And actually, it's funny you should ask me, because that was very much on the table. Folks that were working on JSHint -- well, one person that was on the maintainer team, Mike Hero, did exactly that. And shortly thereafter, actually, members and maintainers actually contacted us and said "Would you like to do that? Would you like to join the maintainers over at ESLint?" So I was answering this question a number of years ago even. My answer at the time was mostly focused on the idea of the strengths of having alternatives, and the strengths of friendly competition, we'd say... But also, for the same reason that we like to see more browsers out there, more interpretations of the specifications.

\[31:52\] I mentioned how Rick Waldron was involved in TC39. And I didn't say what TC39 was, so my apologies there; that's the standards body that decides what is JavaScript and what is not JavaScript. So it seems to me like the more projects that are actively interpreting that and implementing that and experimenting with it, the better the ecosystem becomes, and the more ideas that come to bear, the less decision-making from a language design perspective is informed by any one implementation. So that's kind of a highfalutin reason to have more than one linter...

**Jerold Santo:** \[laughs\]

**Mike Pen nisi:** I mean, honestly, it is one motivation, but I also have other reasons that are more practical, honestly. Another reason though is that, honestly, I was kind of dug in. I even mentioned this a few minutes ago, the fact that I had already committed so much to this project - I guess you could say both committed as a double entendre there...

**Jerold Santo:** Sure.

**Adam Staravia:** Nice one.

**Mike Pen nisi:** Thank you.

**Jerold Santo:** \[laughs\]

**Mike Pen nisi:** Yeah, I guess that's a long way of saying "pun intended", but whatever...

**Jerold Santo:** Right... It's a fancy way of saying "pun intended."

**Mike Pen nisi:** In any case, I was already so involved that I would have felt kind of bad to just leave that project the way it was, and to have said "Okay, I'm washing my hands of this" and that all the time I'd spent is on something that, like I said, I can't endorse. So I wanted to be able to talk about JSHint in a way where I could feel proud, like "Okay, nobody uses this anymore", but at least it's something that I can say "It's free software." And like I said, that's really important to me personally.

And I guess finally, I felt a little bit of -- this is kind of strange, because no one asked me for this, but I felt some responsibility for all the people that were using JSHint. The MIT license, and the not-MIT license, but the one that we had, both make stipulations about the fact that the maintainers have no liability. So in a legal sense, I didn't have any obligation for the people that were using.

**Jerold Santo:** Right, you weren't obligated.

**Mike Pen nisi:** But I still felt like -- especially for those people that didn't know and that may discover later that they were using this software that goes against some people's ethical codes - I felt like "Wouldn't it be great if I could deliver something for them, eventually?" I could make their projects a little bit more free than it was when I started. So I was kind of motivated to switch out their dependency with a free software dependency, even maybe without them knowing.

**Adam Staravia:** What's the license on ESLint?

**Mike Pen nisi:** I'm almost sure it's MIT.

**Adam Staravia:** I should know this, I asked the question. I don't.

**Jerold Santo:** \[laughs\] You've been sitting over there, googling...?

**Adam Staravia:** Well, I was thinking out loud about it, and I was like "Well, that's probably the best place to go into it." Yeah, it's MIT. Unchanged MIT. So I suppose everything you've just said stands in the shadow of this 7-year process to relicense, right? So in hindsight, maybe back when you made that decision, you didn't think that in 2020, which was many years later, you'd write a post saying "Watching the ship sink", and then talk about seven years relicensing and all the work that took into that... Which is sort of like -- I don't know the details, so you could share that, but it seems like... Maybe in retrospect you could say this, but that it would have been a waste to not have made the decision back then just to move to a licensed version.

So the idea that you have friendly competition and diversity in terms of projects totally makes sense, and I'm not against that one little bit. But the licensing issue was present, and the necessity to unwind that licensing issue was a long road, as noted by your 7-year process.

**Mike Pen nisi:** Yeah, for sure. And maybe -- we can get into this more... The work itself was over the span of seven years, but I don't want to make myself seem too long-suffering, or anything...

**Jerold Santo:** \[35:52\] Right, burdened by it.

**Mike Pen nisi:** ...to say like "Every day I woke up and worked on this license." A lot of it, to be honest, was feet-dragging on my part. I unfortunately don't get into this too much in the blog post, and probably I should have... But a lot of it was uncertainty; just thinking like "Will this work? Is this even legally viable?"

**Jerold Santo:** Right...

**Mike Pen nisi:** You kind of never look sillier when you try to do something subversive and you fail. So a lot of the time I'm just demotivated, and I'm saying, "Yeah, I do want to fix this, but I don't want to fail", and it's a lot of self-doubt and questioning... So yeah - not working on it every single day for the seven years, but it was certainly on my mind for all that time, at least...

**Jerold Santo:** Right. It's kind of like the difference between having a seven-mile journey, and having maybe a half-mile journey, but you don't know which direction to go. Or you're in a bog, and you're moving very slowly. It wasn't seven years of work, but because of confusion, or sometimes you're just like down and out because of the situation, you need to rest or forget about it for a few months, and then you pick it back up again... It drags things out.

Did you know when you said -- first, when was it when you said "Alright, we're going to fix this licensing problem once and for all"? Was that seven years ago, or was that somewhere along the line?

**Mike Pen nisi:** Let's see... Yeah, my apologies; seven years is when I started working with JSHint.

**Jerold Santo:** Gotcha. Okay.

**Mike Pen nisi:** But the licensing itself was probably more like five or so.

**Jerold Santo:** Okay. Ballpark it.

**Mike Pen nisi:** Yeah. Either way...

**Jerold Santo:** And when you started that, did you think "This is going to take us five years"?

**Mike Pen nisi:** No, certainly not.

**Jerold Santo:** There you go. So that helps you make that decision, like "I'm going to fix this." I'm somewhat helping answer Adam's statement of like this was a huge process, and in retrospect maybe like "Was it worth all of that?" Well, it's like, when you start the process you don't know what's in there.

**Adam Staravia:** True.

**Jerold Santo:** So you're not baking that in when you make your decision. If you had known "Five years from now you're finally going to be done with this", you might be like "I'll join ESLint and call it a day."

**Mike Pen nisi:** Yeah...

**Jerold Santo:** So that's a factor.

**Mike Pen nisi:** Yeah.

**Adam Staravia:** And the reason to dive deeper into that is because people are going to listen to this show and think "Wow, I could be in a similar situation." Maybe not a one-to-one, but they could be thinking "There is a competing project or an alternative project to my project, that I'm deeply committed in", you know, double entendre, pun and all... They're into it, and they're thinking "Should I --" and maybe they're having adoption issues. Or seeing a decline, like you saw; or whatever it may be. Churn around the maintainer ship, or contributors, and they're thinking "Maybe my efforts will be more planted if I went with what seems to be more mainstream or seems to be getting the adoption." They might be asking themselves that question, and sort of leaning on your history and experience to answer that question for them. Or at least give them guidance.

**Mike Pen nisi:** Yeah. I think they'll certainly need to take into account their ethical commitments, because that's one part of that whole equation that's really hard to balance. So if it is just about "Oh, this tool is superior and my tool is not. I picked the wrong horse. Okay, I'll change it, or not."

**Jerold Santo:** Sure.

**Mike Pen nisi:** It gets a little bit harder when you're asking yourself what you feel like you should do, what your obligation is, what seems moral; that's a little bit harder to ignore.

**Jerold Santo:** Right. You could be pragmatic on tooling and trends and stuff like that, but if you have a principle, a principle doesn't change based on the amount of effort required to hold it up, right? That's why it's so useful. You've decided morally, ethically, "My principle is X. So whether it takes me 35 minutes or five more years, I'm going to do Y." Then the details of that effort don't really matter. You're like "No, this is the way I'm going."

**Adam Staravia:** Right. I think that's admirable, too. I don't want to leave that without saying that's admirable...

**Jerold Santo:** Totally.

**Adam Staravia:** \[39:58\] ...to stick around and do. Because in the post it was dug in. One thing you had mentioned was you were still internalizing the ethics of free software, your involvement in JSHint, and just how the two trends were inherently oppositional in terms of free software and the licensing issue you were dealing with. And you felt regret about the way you were spending your time. But because of your commitment, your principles, you dug in. It's admirable.

**Mike Pen nisi:** Thanks. False modesty aside, I should also say that it was a fairly interesting project in itself for (as you say) a license nerd, just to be like "What does even look like? What does this involve? What do I have to do?" So I wasn't just flagellating myself for all this time, but also - it's kind of intellectually satisfying to be like "Oh yeah, I guess I do have to do that."

It also drags you into technical challenges that I wasn't expecting. I mentioned I was contributing to a Rails project; that's probably the most Ruby code I'd written in my whole life. So just in terms of contributor license agreement, operationally, to get this done, I was doing other kinds of work. I was maintaining a separate history for the project, that was rebased on top of the free license... And that in itself is a little bit difficult. We use the Git version control system; people who use Git are probably familiar with the cherry-pick command. But even more than that, to replay a merge commit is actually really difficult, because you have to cherry-pick both sides of the merge, and all this stuff... And that was fun, because I really like using Git, and I had to solve that problem. But there are other reasons to keep me going, beyond just my ethical standing. So I'm no saint, or anything like that.

**Adam Staravia:** Well, we draw that distinction because a sentence or two later, in that same part of what you wrote there, you said "I wanted to move on." So we're sort of empathizing with your internal angst, like "I wanted to move on." This is your words. "I wanted to move on, but that would mean all my work had been in service of yet another non-free system. I didn't want the result of my effort to be a project I couldn't endorse", which you said earlier. So there's that empathy there, like you wanted to -- internally, you sort of had this feeling in retrospect (because this was written recently) that you wanted to move on. But something was keeping you involved.

**Mike Pen nisi:** Yeah.

**Break:** \[42:33\]

**Jerold Santo:** So you began this long process, and you weren't sure how long it was going to be or what all it would take. You mentioned a little bit some of the technical difficulties. A lot of it had to do with other people, and like "How do you go about making this change." So you can't simply just edit the README and the license file, or just delete a line... Although that probably would've been nice, right? Just like "Why can't we just delete that line, and then all of our problems are solved?" You can't do that.

**Mike Pen nisi:** I did a few times, just cathartically... But you're right, I wouldn't.

**Jerold Santo:** \[laughs\] Just to git revert, you know... Just make the commit and then feel better, and then put it back...

**Mike Pen nisi:** Yeah.

**Jerold Santo:** Well, maybe address that, as a licensing person, or someone who's gone along this path. Why can't you just change the license and be done with it?

**Mike Pen nisi:** Sure, yeah. Just because that's really the one stipulation of the license - it kind of rides with the code. You have to maintain that along with the code, as long as you maintain that code; so when you fork it, it's still the same project, it's still the same codebase. So you add your additions, but you're still fundamentally contributing to the same codebase, and you're still beholden to that same license.

So the one person that would be able to change it is the author. Originally, when we got this request, that's what Anton - who was still the maintainer at that moment - did, was contact the author of JS Lint and ask "We have people in our project, we forked it, we've added a lot of stuff, we have a lot more contributors... Would you mind if we change license?" And they declined. So that kind of put the kibosh on that particular route.

But one thing that Anton -- Anton did a lot of really smart things, and one of the smart things that Anton did though was he was careful as he contributed to JSHint, and as it grew, to put all new source code into new files. And that included also the tests. So it does get down to a file base level. The license only governs the original source code file that JS Lint was written in. So when you make changes to that file, you're still contributing to it. It's called the JSON license. So you're still contributing to a JSON-licensed file. But if you add another file, then in Node.js you require that file, and that file can be under a different license if you want.

So Anton was very careful from the start; he grew the project, and said "Oh, we need a new module for this. We're going to have a new file", that file was licensed with MIT. And the same goes for the tests. So whenever they started writing tests, all the tests were licensed MIT. And the one oddity about JS Lint that was in our benefit here was that it was maintained as a single JavaScript file, with no tests. That's pretty rare for projects these days. So we naturally were adding a lot more files, so naturally, a lot of the contributions that were coming in were to files that were never licensed with this license in the first place. And all the code that we used to verify the correctness of our code itself didn't need to be relicensed, and could be reused in a context under the terms of the MIT license. So that was another benefit.

**Jerold Santo:** So how did you get that all done? Where did you decide to take it? You couldn't do the first move...

**Mike Pen nisi:** \[48:01\] That's right, yeah. So the kind of next break in the case, you would say, is that somebody -- this is another case where I've never spoken to this person in real life, so I'm going to butcher their last name, but Simon Kai was working with the Eclipse project, which is an editor that your listeners might have even used... But they showed up seemingly out of nowhere on that issue that said "Please change the license", and reported that they had a version of JS Lint that was licensed with just the MIT license. The reason they had that was because back in the day this project called Orion, from the Eclipse Foundation, was distributed with free software, and they somehow received permission to distribute that software as MIT. We don't have access to the discussion that happened to make that possible, but they were granted a version of JS Lint that was MIT-licensed.

So that was really important, because it meant that we could start as though basically all the contributions that had been made to JSHint, we could pretend as though they had been made to an MIT-licensed project. So that way, the original license was no longer necessarily needed to apply.

**Adam Staravia:** Hm... Sneaky. Or... Smart.

**Jerold Santo:** Sneaky smart.

**Adam Staravia:** Sneaky smart.

**Mike Pen nisi:** \[laughs\] Yeah. So from a technical standpoint - this is the fun thing when I tell my parents, I tell my family, or really anyone that isn't in the software development industry about this, as I get to explain a little bit of how Git works... So this is right at the point where their eyes start to glaze over, but I try to bring them back in, because -- you know, as a software developer you think about the process of just maintaining code, and it just being a series of patches... So I explain to folks that "Okay, if I take the basis of what I was working on and say "This is the non-free version, and I have one that's identical, except it's free", then as long as I have all the changes as these series of patches, I could just -- you know, we know the term "replay", but we'd replay those patches on top of the free software version.

So you would say that the result of that is an identical project that is now just free software... So by replaying those changes, you've kind of proven the fact that if you would start in this alternate universe where you had been using the free software version of JS Lint, that you would end up with a free software version of JSHint.

**Adam Staravia:** Yeah. So you have to go in the history of each, essentially the non-free and the free versions of each, and sort of find which commit, or at which date, or which SHA is applicable to that fork, essentially? Because at some point that MIT-licensed version is a representation of, in some history, the non-free.

**Mike Pen nisi:** That's right, yeah. So I went back into the history of JSHint, and that naturally involves all the commits made from JS Lint. So I was able to, in Git terms, rebase JSHint on top of the free software version of JS Lint. And because no one changes the license, there's no risk of conflict. It's not as though I was resolving conflicts because everybody was changing out other parts of the license, or anything like that. We learned our lesson, we weren't really accepting patches to the license at any point.

**Jerold Santo:** Right.

**Adam Staravia:** I'm going to say something funny here. Or at least somewhat funny. So that rebase took five years?

**Mike Pen nisi:** Yeah... \[laughter\] It was a very slow process.

**Adam Staravia:** \[laughs\] To discover it's an option maybe you have taken that long. So is that how you accomplished this goal then, was you discovered this free MIT version of JS Lint, and that's how you accomplished this goal?

**Mike Pen nisi:** I wish... That was the first step. The rebase did take a little while. It took longer than you might expect. It took maybe a day or so, just because it was rebasing a history that -- this is getting in the weeds a little bit, but it was rebasing history that was not really clean. Because there are a lot of branches that were merged, and all these weird things that happened in the history, so rebasing that is not a straightforward operation we use in Git; as good as Git is, it's not perfect, and it's not great at doing that particular thing. So that operation - yeah, it took a day or something, but it did not take seven years.

\[52:17\] The problem after that though - and this is where being licensed or being intellectually curious about this process comes in - is that actually, that rebasing was in some ways invalidating all the patches that we were replaying... Because conceptually, all the people that had contributed to JSHint in the time since - they were contributing, knowingly or not, to a JSON-licensed project, a non-free project. So from a legal standpoint, you would say "Hey, I gave you my code, I gave you my time, and I only did that because I believed for some reason in the JSON license. So when I'm sitting here, rebasing your work, I'm in some way violating a contract or the trust that you had put when you contributed to this."

One might say, in the worst case, "The only reason that I contributed to your project was because I believe in good, and I want to subvert evil. And because you have just changed my contribution to be in a project where that clause is no longer present, you've violated my trust, and you've violated the contract by which I (informally or not) contributed."

So we had solved a big problem by finding this free version of JS Lint and rebasing on top of that... But we still had to reckon with the fact that all these people had contributed, knowingly or not, to a project that was licensed under those terms, and so we needed to get their permission as well. It wasn't just about the original author, but also about all the people that had contributed in the meantime.

**Jerold Santo:** How many people was that?

**Mike Pen nisi:** Something like 120 or so, I think... Which was actually pretty good, I personally think, for a free software project, at least on the scale of JSHint.

**Jerold Santo:** Sure.

**Mike Pen nisi:** It wasn't as bad as it might seem though, for a few reasons, one of which being that a lot of the people were contributing to files that weren't JSON-licensed, like we talked about; not all the files were JSON-licensed. And further, a lot of the contributions were what you would call -- you know if you were that license nerd, you would say non-substantive. You don't really need permission to change those, because if people fix a typo in a code comment, they're not changing the behaviour of the project; they're actually just reflecting something that's objectively true. That's not really -- you don't necessarily need their permission to change the license, because the way they've contributed is not really...

**Jerold Santo:** Substantive.

**Mike Pen nisi:** Yeah.

**Jerold Santo:** Okay. So how many were there -- you know, take out all of those; take out the ones that were on the files that don't matter, or the ones that weren't substantive, typo fixes etc. Are we talking like 50 people, somewhere in that range? I'm just guessing...

**Mike Pen nisi:** Yeah, that's a little bit harder for me to answer. What I can do...

**Jerold Santo:** I'm trying to figure out how many people you had to email and track down... That's where I'm trying to get.

**Adam Staravia:** What's your cold call list? "Hey, by the way, I've found this free version I want to replay... Can I get your permission?"

**Jerold Santo:** Yeah... It's like when you have Covid, and you have to talk to all the people you were with last week. You're like "Oh, sorry I've got to call you, but by the way..."

**Mike Pen nisi:** Yeah, contact tracing.

**Jerold Santo:** Yeah, that's what it is. It's like contact tracing for a file.

**Adam Staravia:** Contributor tracing.

**Jerold Santo:** "You came in contact with this file. You may have this disease." \[laughs\]

**Mike Pen nisi:** Yeah, yeah... Sometimes the JSON license can feel like a virus... \[laughter\] So I can't say though -- let's see... I can look at the signatures I received. It's a lot of signatures. Yeah, I would say probably 120 or so.

**Jerold Santo:** So what was that process like? Just emailing people?

**Mike Pen nisi:** Yup.

**Jerold Santo:** \[56:00\] There were probably some you were still in touch with, or they were still contributing, so they were probably easier to get a hold of... But what if there was one person that passed away, and they just -- I mean, maybe you didn't come across that, but if that was the case, would it be a blocker? Would that just end it?

**Mike Pen nisi:** Yeah, I didn't know what would happen... But that's what I did - I wrote an email and I spammed everyone on the contributors list. And it doesn't even necessarily need to be that dramatic. A lot of people had changed their email address. There were some people that just configured Git incorrectly, and I didn't know what their email address was... So some people were in some ways almost lost to the sands of time, so I was doing some iffy background searches on people...

**Jerold Santo:** Sleuthing, yeah.

**Mike Pen nisi:** Yeah, trying to find people's identities, and stuff... And telling myself that it was for a good cause.

**Jerold Santo:** Well-intended creepiness...

**Mike Pen nisi:** Yeah, yeah... It was enough, I guess; I don't know. I did it, and I did find most people. And most people were right on board. They said "That's great. Go for it. For sure." And this was, by the way, where I got into the whole CLA thing. CLA stands for Contributor License Agreement. And that's what I introduced into the project - a way for people to bequeath their control over contributions they've made. So I introduced that... And it's a relatively common practice. Well, I wouldn't say that; it's not common, but it's done in open source projects.

So I introduced that, and I was just asking people "Can you sign this?" And this was the paperwork way of getting that done. And most of the developers I talked to got back to me very quickly, and were really encouraging.

Some of them just didn't want to, and they were annoyed, frankly, of me asking. They thought it was my idea of a good time to be doing this...

**Adam Staravia:** \[laughs\] They'll listen to this podcast and be like, "Okay, I was wrong... It was not a good time."

**Jerold Santo:** Do you want to name any names, and shame them publicly? \[laughter\]

**Mike Pen nisi:** No, no, it's alright... And actually, they mostly came around, because you just had to be rational and be like "Listen, I know where you're coming from. I find it just as annoying as you do", and for the most part, they're like "Yeah, okay... I can see you're a person; you're not a lawyer that finds this entertaining..."

But the real sticking point though was for a person that had contributed a lot. And that's important, because there were some people that didn't wanna sign, but they hadn't really contributed that much. But there was one person that contributed a significant amount, and I could not contact... And despite my -- I guess I'm proud to say I'm not a very good creepy internet detective, but despite trying to find more information about them, I found very little. I started to question about their safety. That was kind of tough, because you're reconciling this silly side-project you're doing with the fact that people have real lives, and actual bad things can happen to people out there, and is what you're looking for really important?

At the end of the day though, there wasn't really anything you could do, because I can't find this person, and I certainly can't help them... So I had to just kind of say "I hope they're well, but there's nothing I can really do for that." So I had to turn my attention back to the task at hand, which was "What do I do given that there's a significant contribution and I can't get their permission to relicense?" And the answer was to rewrite that from scratch. It's a little bit trickier than that, because they didn't write just a file, they wrote patches, so I had to work to revert their patches, which other people had patched on top of.

In reverting, I had merged conflicts of -- I had to strangely resolve conflicts that were intended to break the code. But once I had that, I had a version of JSHint that was kind of devoid of that unlicensed contribution. And what I could then do with that is put it in front of another developer that had not seen JSHint before, or seen its source code, and asked them to reimplement it.

**Jerold Santo:** \[01:00:07.05\] I was going to ask, you couldn't just copy what they did, because that is plagiarism at that point, right?

**Mike Pen nisi:** Right, right.

**Jerold Santo:** You have to black-box reimplementation; it's open source, and you have the source, so...

**Mike Pen nisi:** That's right, yeah.

**Jerold Santo:** ...what a weird situation to be in.

**Mike Pen nisi:** Yeah. And my hands were kind of tied, because as much as I would have liked to rewrite it, and I had plenty of ideas for how to rewrite it from having started at the source code for many years... You know, you're always as a maintainer thinking of "Wouldn't it be nice if we did it this way and that way?" I didn't know - at least at the time - if I could really reasonably claim that what my contribution was truly distinct, because you know, you would say that my interpretation and my ideas were in some ways...

**Jerold Santo:** Derivative.

**Mike Pen nisi:** ...informed, yeah. So I had to go look for people that had never worked for this project before, and ask them to reimplement it. And the number of people out there that are interested in JavaScript, that are interested in parsers, that care about free software, and that don't mind contributing to a project that's dwindling in significance - it's a very, very small number, and most of them have already contributed, so they're disqualified.

**Jerold Santo:** Oh, my...

**Mike Pen nisi:** But I went to meetups, I went to software conferences, I posted on Reddit... I don't know if you remember this, but I contacted you folks at one point, to ask if you had ideas of where I could --

**Jerold Santo:** You did?!

**Adam Staravia:** No way...

**Mike Pen nisi:** Yeah, yeah.

**Jerold Santo:** No...

**Mike Pen nisi:** You pointed me to your Slack channel to look for developers. I was looking for just basically developers that wanted to work on this project.

**Jerold Santo:** It sounds like something we would say...

**Mike Pen nisi:** Yeah. I may not have been specific about what the project was, because we talked before about kind of fearing failure and not wanting to fall on your face publicly... So I didn't always talk about, you know, what's this project that had wide industry recognition... But I did try to solicit help from folks.

**Adam Staravia:** Here it is right here. I've got the email, July 10th, 2018.

**Jerold Santo:** Really?

**Adam Staravia:** I responded "Howdy. Thanks for getting in touch. Join the community, hang with us in Slack."

**Jerold Santo:** \[laughs} There you go.

**Adam Staravia:** "We'd love to talk through this with you. You can hang in \#jsparty too, and talk to other JS web folks. Hope to see you there!"

**Jerold Santo:** There you go.

**Mike Pen nisi:** Yeah.

**Jerold Santo:** You didn't take our invitation... Or did you?

**Mike Pen nisi:** I think I might have...

**Jerold Santo:** Okay.

**Mike Pen nisi:** I'm sorry, it's tough to say just because I've got so much silence...

**Jerold Santo:** That's alright.

**Mike Pen nisi:** But I certainly appreciated even the recommendation there, because I was really just looking to expand my network and find folks. The folks eventually showed up, but not through my direct ask. The very first one cam through the Free Software Foundation; an intern working there was -- you know, the Free Software Foundation in some ways provided the resources for some of this work to happen... So this intern, Ethan Dora, spent some of their summer working on rewriting. So that was the impetus to really get me thinking this was actually possible - somebody came up and did this. It was great to see it was the Free Software Foundation, which I've said before, I kind of align with ethically. So it was neat to be able to work with them.

**Jerold Santo:** That's cool.

**Adam Staravia:** There's a lot of work that went into this.

**Jerold Santo:** Yeah, I know.

**Adam Staravia:** You had to chase down people, get signatures...

**Jerold Santo:** Now I'm realizing why it took so long.

**Mike Pen nisi:** Yeah.

**Adam Staravia:** I mean, just the cycles, and the mental cycles alone, let alone the actual time cycles. And it brings up the explicit versus implicit contributor license agreement. So you explicitly asked them to sign one that changed their commits and the license that went with it, right? But you'd mentioned earlier your obligation, and license-wise there was no obligation from you as a maintainer to the open source. But there is, I suppose, some sort of implicit contributor license agreement that you contribute code to this project even though there is not CLA, and you didn't sign it, that you're contributing to that license. So you've got a bunch of people who are like "Why are you reaching out to me, Mike? Come on, are you being serious?" But there's an implicit license agreement there, because there isn't one. And there is a license to the project.

**Mike Pen nisi:** \[01:04:01.17\] Right, yeah. It's actually made me think a lot about my own contributions in other open source projects, and a kind of responsibility that I never really considered. Coming up in open source, just thinking like "Oh, open source is great as a matter of course; free software is great as a matter of course. Just make projects better, and that's that." When you do that, you're kind of accruing a different kind of responsibility that people don't talk about as much... And thinking about this and dealing with this has made me more sensitive to that.

There are interesting things happening in this case, because you know, in the case of when I pass away, if that should happen and someone wants to change the license of the codebase that I contributed to, what happens then? There's some legal standing for people, especially prolific developers, bequeathing their rights as kind of like an inheritance.

**Jerold Santo:** A part of their will, or something.

**Mike Pen nisi:** Yeah, exactly. But it's kind of fraught, because actually, that can be found to have monetary value, and by doing that, you can end up actually making trouble for the person you're giving those rights to.

So really, perfect work is done just in general, but specifically on this topic, by the Software Freedom Conservancy. They have a podcast of their own called Free As In Freedom, that you can listen to and get into the weeds about these kinds of issues, and what real lawyers are doing and thinking about these things. And they work a lot with the Debian project, which is a huge, massive free software project. It's a whole operating system. They work a lot with contributors there and offer them services, so they have a lot to say about this.

**Jerold Santo:** Yeah, we have done a conversation with Karen Sandler, years back.

**Mike Pen nisi:** Oh, great.

**Adam Staravia:** Three years back, at least.

**Jerold Santo:** It looks like it was episode 238 at OSCAN. So I met Karen, and had a great conversation with her. It's on the Changelog. But yeah, they're doing great work... The kind of work that the rest of us, like you said, don't even usually think about these concerns until they're staring us in the face, for some reason... And I would say that I have definitely contributed to open source in a somewhat - we'll just call it willy-nilly fashion... Like "Hey, it's easy... Pull request, merge my bug fix, whatever..." And I don't think about the implications of that necessarily, because it's such a lightweight transaction now. So even just hearing your story makes me think about my contributions, and maybe the responsibility there that I don't always think about when I'm participating in a project...

Or how often do you open up a new repo that maybe you're using as a dependency, and you're going to submit a bug fix, and you think "What's the licensing situation of this software?" I don't usually think about it myself, but I probably should. Like, what exactly am I agreeing to here? What if the license said "You will only use this project for evil." I would have a problem with that. But if I don't read the license... So I think this is a good cautionary tale for all of us, maintainers and contributors.

So you went through all this work, you had a hundred plus people agree, you finally got it out of the weight of the MIT+ or the JSON license... It's now MIT-licensed, August 2020, the blog post out, right? It's officially free open source software now, and anybody can use it. Congratulations on going through it and getting to the other side. Sometimes you wonder if you're going to make to the other side. Well, you made it, so that's cool... What now, and what next?

**Mike Pen nisi:** Well, thank you. Now I'm not so sure. I just want to round out some of my contributions, and finish up some of the work that I've been most recently working on, just because I'm kind of a completions. They've been introducing new features into the JavaScript language in a much more regular rate the past few years, so I'd like to get some of those last few features in.

\[01:08:04.04\] But for the most part, like we've been saying, the project itself isn't really that widely used anymore, so I don't think many people will be too distraught if it goes away... But I am glad that there are a lot of projects out there that rely on it, that depend on it on a technical level, I should say... And what I'm glad to know about those projects is that when we release this software, the free software version that they got is kind of for free.

The way that NPM, which is Node's package manager - the way that it delivers dependencies, in large part, is with semantic versioning, and a lot of people that depend on these packages express their dependencies in ways that can be satisfied by new releases. So there are things that change this - the way that you write your version specifier, whether you use a package-lock file, and all these things... But for a lot of the people that have been relying on this for many years, where those features weren't necessarily available to them, they got this code the moment we've released it, because their automated systems, their CI systems, their deployment systems, all these things just pull from NPM automatically. So that was kind of a benefit; that was kind of satisfying.

Even if new people stopped using JSHint today, I was able to say "Free software is a little more widely proliferated now that we've released this." We didn't release a major version... And actually, that was a whole topic we haven't really gotten into, that you can read about in the blog post, which is why this isn't a major version, and the nursery that goes into that decision...

Next steps for me is just to probably round out these features, and then find a new passion, really. Now we're at that point that Adam was asking about before, which is a more pragmatic scenario of saying "Where do you want to be spending your time?" The ethical component is lifted...

**Jerold Santo:** You resolved that.

**Mike Pen nisi:** Yeah. So now I'm able to ask that question again, and say "Well, now there's not much keeping me here." I don't really necessarily think that I can make JSHint something that has the power of ESLint. And I should say, I introduced ESLint on a sour note, by calling it a competitor, but I should say, really and truly, it's a really impressive software project, and I've never felt otherwise. And also, it's maintained by Nicholas Kakas, who you've had on your show a number of times, and who I have a lot of respect for...

And finally, speaking of maintainer ship, it's maintained in a really impressive way. You know, they have a whole RFC process, and they're taking a lot of new ideas in how you can distribute decision-making in a way that I think is really viable. So really, this is all just to say it would be really hard for a one-man rinky-dink project to offer the same strengths. So I'll be satisfied to leave it in their hands.

**Adam Staravia:** Is there no other maintainers now then? You're the sole maintainer?

**Mike Pen nisi:** There are. I guess you would have to really ask them... I think though at this point that would be Rick Waldron and Caitlin Potter. Furthermore, I think at this point mostly they are to humour me... So in some ways they may be relieved when they no longer have patches to review, which they do, without fail... They'll be relieved to be done with that.

**Adam Staravia:** There you go. Here's a question for you then. So the next time you fire up a new JS project, are you using JSHint, or ESLint?

**Mike Pen nisi:** Hm... All these years I've always do-gooder. But when I'm no longer maintaining it and I no longer see commits going to it, I guess I'll be using ESLint.

**Adam Staravia:** \[01:11:58.17\] Well, this has been a journey for you, for sure... And one, thanks for being a listener, two, thank you for writing in, and... I'm so thankful I didn't have a terrible response to you; at least I'm okay with what I responded with... I really wish we saw you on Slack. But I think what we have also changed in our processes, I suppose thanks to Zoom \[unintelligible 01:12:18.22\] easy meeting people, where it became really easy to use Calendly links and saying "Hey, do you wanna talk, or whatever? Link up." So I wish I would have responded to you in saying "Let's actually talk." Because I think that's the invitation that we try to do with this show. Maintainer Spotlight has been this fun flavour of the Changelog we've done to sort of dig deep into where RFC left off. We can't replace Nadia and Micheal, nor will we try, but to carry on what happened with Request For Commits, that podcast, which was amazing, we continue with Maintainer Spotlight here on the main show, the Changelog.

We want that invitation to be to all maintainers out there. If you're struggling - we may not be able to help everybody, but we're definitely a community to listen, and this is a place you can call home. And hopefully, we can give a slightly better response than that one. I wish I had given a slightly better response to you on that one, to give you more of an invitation in, I suppose, than just simply going to Slack... Which seems kind of cold to me.

**Jerold Santo:** But at least you didn't ghost him.

**Adam Staravia:** That's right. At least I did respond, which... \[laughs\]

**Mike Pen nisi:** Yeah, don't sell yourself short; I think that was a perfect response. It's good to have ideas for how to improve it, but... Yeah, that was great.

**Adam Staravia:** Well, I think it comes back to what you said earlier, which is there's people; there's real people with real lives out there, behind software. And that's what I think Jerold and I really care about most. Sure, progress and tech - it's fun, that's what attracts us, but we're here really for the people. I want that to be the message that resounds whenever we show up into this podcast, or we ship an episode, or we sit and talk with someone like you, or respond to your email. I want that to be what's taken away - that we're here for the humans, not the code. And I think that's what I want to send home - for you too, but more so to say thanks for the ethics behind you, and being a completions, and sticking it through, and delivering. I think you can move on to your next big thing with a happier heart... And thank you for sharing this story with us.

**Jerold Santo:** Yeah. We really enjoyed it.

**Mike Pen nisi:** Thank you.

**Break:** \[01:14:23.11\]

**Adam Staravia:** We should coin that, Jerold, "We're here for the humans, not the code." As I said it, I liked it...

**Jerold Santo:** You just coined it.

**Mike Pen nisi:** I totally know what you're saying, and it's funny, because I think we could have jumped off with what you said at the end there and just gone another hour, if you two weren't already done with me...

**Jerold Santo:** Oh, yeah. \[laughs\]

**Mike Pen nisi:** But I do want to say -- I just want to respond to that a little bit... It's got to be tough; I have a lot of empathy for you, because you're dealing with people all the time, and that's what it comes down to... It just must feel like that, "This is another email I have to deal with." I only have sympathy for being in that position; to maintain the kind of empathy that you want to have is really hard.

**Jerold Santo:** Yeah.

**Mike Pen nisi:** And you have a psychology podcast, which I don't listen to as much as I should, but I'm sure they've talked about how our tendency is just to be complacent, you know?

**Jerold Santo:** Sure.

**Mike Pen nisi:** It's always a fight.

**Adam Staravia:** Yeah. Remove the relation. Well, I can grok my own email, and I can tell that it's a bit robotic... Because I didn't, one, acknowledge at all the challenge that you're facing; I just said thanks for getting in touch. So there was like zero real response to what you'd actually said... So I can tell, in retrospect, that this was a pretty robotic response for me, even though it seems like it's not.

**Jerold Santo:** That's why you didn't feel so great about it.

**Adam Staravia:** Yeah, that's why -- I can tell what I wrote.

**Jerold Santo:** Right. \[unintelligible 01:17:01.13\]

**Adam Staravia:** Normally, we're far more relational, and it bums me out when we're so busy, or... The response was also at 11:45 PM, so it might have been like a nighttime email... Who the heck knows what was happening on July 10th, 2018.

**Mike Pen nisi:** And that's the thing - it's easy to look at that email and be like "Oh, I feel bad about that." But what's hard is to say "What else was going on in my life at that moment?"

**Adam Staravia:** Yeah.

**Jerold Santo:** Right.

**Mike Pen nisi:** And that's something I think a reasonable and mature person like myself would assume when you get a response like that. It's like, people are people.

**Jerold Santo:** Well, it's tough, because your situation is one where we probably could have helped move the needle.

**Adam Staravia:** Yeah.

**Jerold Santo:** But there are lots of situations where people are just asking us for things, whether they're recruiters, or PR people... We get a lot of low-quality emails.

**Adam Staravia:** A lot.

**Jerold Santo:** We read all our emails. So it's hard sometimes, because we're used to dealing with the person who's just trying to take from us, versus somebody who has a legitimate situation, who's in our community, and we could probably help them. And sometimes you can't even discern that, because you just read your email fast... Especially at 11:45 at night.

**Adam Staravia:** Well, I just desire to, I suppose, show up better.

**Jerold Santo:** Yeah, well... We all let ourselves down all the time, so... I thought this was actually -- ironically, I think that was probably the best moment in the show. It was just hilarious, because we were so clueless about it. You're showing all these links you went to, and you're like "I even contacted you guys", and we're just like "What?!" \[laughs\]

**Mike Pen nisi:** Yeah, sorry, I didn't really --

**Jerold Santo:** It was great.

**Mike Pen nisi:** Okay, good. I really didn't \[unintelligible 01:18:28.16\]

**Jerold Santo:** I loved it.

**Adam Staravia:** Me too.

**Jerold Santo:** That was just funny. Because you know, when we speak people, a lot of times we either know you from past interactions, or we assume you don't know who we are, and we barely know who you are... That's why I ask, "Have you ever listened to this show?", because a lot of people are like "No. I'm just here." So we don't assume past relationships if we don't explicitly remember them... So this was just a funny situation where you had tried, and... You know, we didn't ghost you, but...

**Adam Staravia:** But the best part is you got in touch, and that's sometimes the hard part.

**Jerold Santo:** Yup.
