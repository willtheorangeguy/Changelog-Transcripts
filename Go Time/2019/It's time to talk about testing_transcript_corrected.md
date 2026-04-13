**Mat Ryder:** Hello, everybody! Welcome to Go Time. I'm [Mat Ryder](https://twitter.com/matryer). Today we're talking about testing, and I'm joined by some great thinkers and tinkerers from around the Go community. I'm joined by [Johnny Tourniquet](https://twitter.com/jboursiquot), [Jana B. Logan](https://twitter.com/rakyll) and the one and only [Jon Calhoun](https://twitter.com/joncalhoun). Hello, everybody!

**Jana Logan:** Hello!

**Johnny Tourniquet:** Hello!

**Jon Calhoun:** Hey, Mat!

**Mat Ryder:** How are you feeling today?

**Jon Calhoun:** Feeling good.

**Johnny Tourniquet:** No complaints.

**Mat Ryder:** Good. Well, if you do have complaints, don't bring them to me, because I can't help... \[laughter\] Especially if it's anything medical. Okay, so... Yeah, testing is such an important subject, I think, so it's great that we get to do a show on it. I noticed whenever I talk about testing, it always creates a lot of debate, and I always wonder why that is.

You hear some people say "TDD is dead", and other people advocating for it... And some very diverse opinions. I think that says something about testing, which hopefully we can uncover today... But perhaps it's worth kicking off with talking a bit about the things we like about testing, and the positivity around testing, because there's definitely lots of negativity around it, too.

First, let's assume that we are joined by some people that are just getting into Go, haven't done much testing before... So what's the point in testing? Why do we do it, and what do we want to get from it?

**Jana Logan:** It's a way to understand myself, I think, especially in the long-term, and a way to express what my code is supposed to do. It's kind of like a summary, you just explain what it's supposed to do, and you have this repeatable way of checking if it's actually doing that.

**Mat Ryder:** Yeah, so you just want it to describe in some form other than the code itself, you want to describe what promises you're making.

**Jana Logan:** It's actually sort of a code that explains itself. When you said it's not a coding way, I just assumed that you were talking more about some specs, or something like "Hey, this is what the project should behave like", more of like a specification. But testing is a spec itself, but it's code as well.

**Mat Ryder:** \[04:05\] Yes, it's code. So just very practically then, in Go, if you write a function, let's say, and it's going to be a greeter function; it's going to take in a name, and it's going to say hello to that name, and return that as a string - you could write a test which passes in some names and makes sure that what gets returned is what was expected. That's essentially a unit test. And then what that gives you is you can look at the test code, and you can just sort of see, at a glance, what promises are being made, or what your function is meant to do.

And of course, one of the goals of good testing and good practices is to have those tests continuously run, such that you can at least assume that they all pass, and that way we get a good feel. It's a great way if you're looking at a new package to get a sense of how you should use that package. You can go and poke around in the test code.

**Jana Logan:** Yeah, totally.

**Johnny Tourniquet:** To piggyback on what Jana has just mentioned, for me the tests take on a different meaning as the project goes. In the beginning I'm trying to think through the problem I'm trying to solve, and I'm basically saying "Okay, let me establish some specs around what I expect it to do." But over time, as the project sort of lives on, and features get added or removed and whatnot, they become more of a guard rail; they are confirming the changes I've been making. The things I assume are still true have remained true throughout the evolution of the software, so they take on a slightly different meaning, I think, as the project evolves.

**Jon Calhoun:** Related to that, I think it's true that tests give you a good chance to clarify on things. A good example is when I play board games, my friends always joke that I'm the person who thinks up the weird edge case and wonders if there's any clarification in the rules for it... But test cases are a great way of saying "If you give me this weird input, this is exactly what you're going to get back."

**Jana Logan:** And this is why coverage is really important, because you basically declare what you expect by covering those cases... And sometimes I'm seeing people just go in over test cases and assuming that "Maybe this package or this function is not supposed to act this way, because it's not represented in the tests." That's one of the reasons why I think coverage is so important.

**Mat Ryder:** Yeah. And I think it's easy to get a little bit obsessed with coverage, too. I've seen people, I've met people who are very proud of it; they have 100% code coverage. And essentially, in Go projects, that means they've tested in some way all the points at which their code could error, for example...

**Jana Logan:** Yeah.

**Mat Ryder:** ...they have test coverage for that.

**Jana Logan:** I would say that for dynamically-typed languages, 100% is definitely required. That is baseline. \[laughter\] Right...? But yeah... 100% doesn't necessarily mean it's good coverage, or it's necessarily important.

**Jon Calhoun:** I think it's important to recognize what coverage actually means, though. Like Mat said, if you're just saying you cover all the code - is that really 100% coverage? Because you didn't try every integer input, you didn't try every string input... So you can have coverage in the sense that it touches all of your code, but that's nowhere near actually having 100% coverage.

**Mat Ryder:** Yeah.

**Jana Logan:** That does mean also you need some fuzzing, or you need to just force it with different inputs and so on, with all the possibilities. You need to be a little bit smarter; maybe you cannot really manually generate all those test cases, right?

**Jon Calhoun:** Yeah. Because for me at least, I would rather work on a codebase with 75% code coverage, but that coverage is actually well-thought-out, and it's good... Versus somebody who's like, "Hey, I've got 100% code coverage", but it's just the simple, really basic inputs for everything, and it doesn't really actually test if things are gonna work when crap hits the fan.

**Johnny Tourniquet:** \[08:07\] Right. The happy path, and everything else, right...?

**Jana Logan:** Yeah...

**Mat Ryder:** Yeah, but if you do have that 100% code coverage, aren't your tests going to be over-fit, really, for the test code? Essentially, your real code, your program code becomes very brittle. Every change, every tweak of the implementation could break these tests, because they've got coverage to that degree. So in that way, I think you can go too far with tests. I think a lot of people probably do. I definitely have in the past, and for me, it's about striking the balance between how much you need to do in order to have the benefits that testing brings you, but no more.

**Jana Logan:** But isn't this a question about compatibility also? If you gave behaviour promises, for example, you may actually want to be able to cover those tiny details, so you don't change the behaviour without -- I mean, you should be informed if your behaviour is changing.

**Mat Ryder:** Yeah, and I suppose that's a good way of putting it - it's about what promises you've made. This is where I think it's quite difficult to have these conversations in the general, because I think this will change depending on the kind of thing you're building. If you're building a binary encoder/decoder, then the test coverage and everything is going to look very different to if you're building an email sending service, or something... Don't you think?

**Jana Logan:** Yeah, true.

**Jon Calhoun:** Yeah. I mean, even if you talk about a website, or something like that... Technically, to have 100% coverage it feels like "Okay, what happens if my hard drive fails." There's all these weird things that you might need to simulate... But is that actually worth doing, versus, like you said, an encoder or something that's much smaller, you don't really have to think about all of that stuff as much.

**Jana Logan:** Yeah, I think unit tests versus integration tests is a huge topic. And it's so complicated to run some of these integration tests that people would rather go to Canary and try to take a look in production... Because the environment and all the glue is really complicated.

**Mat Ryder:** Yeah... So we should just spend a little bit of time just talking a bit about those differences between, say, unit tests and integration tests, and the other types of testing that there are. For sure, unit testing I think is the simplest one to understand, because it's the simplest kind of test. You have some kind of function, usually... [Dave Cheney](https://twitter.com/davecheney) did a talk at a recent Go meetup in London, where he made the case that the unit actually should be the package, and actually that's the boundary at which you should test... And he made some quite interesting points about that.

But essentially, whatever it is you're testing in the unit - that's the unit test; it's the smallest piece. You write the test code, it runs that real code, and checks the outputs. Those are unit tests. Could someone tell us about what's an integration test then, if that's a unit test?

**Johnny Tourniquet:** I've heard different definitions of integration tests. It's almost like whenever I personally start talking about it, I have to sort of give like a preamble, like "When I talk about integration tests within this project, this is what I'm talking about." But the basic idea is that given a solution, given a piece of software that solves a particular problem, are the different components within that solution well-integrated, such that they can solve the problem? Can the components work well together to actually deliver the solution?

You can have just two components, a dozen components, hundreds of components - it doesn't matter. All these pieces within the bounds of your software solution, without talking to external entities - can these things talk to each other?

Now there are others who think, "Well, integration testing means you go outside the boundaries of the immediate piece of software, of the immediate repo, or whatever the project is... Now, can it talk to, say, an external service, like a database? Can it talk to other APIs?" You almost have to qualify what you mean by integration testing, but at least I consider it as within the project you're working on right now, do all the pieces in it fit together well?

**Jon Calhoun:** \[12:24\] Piggybacking on that a little bit, one way that I've heard it described that I think helps sometimes is if you think about it as like I'm testing this one package/component/whatever it is, and it's interacting with other things, and you have to pretend that "I'm not going to be changing that code. So I have to make sure that what I have works correctly with those things."

**Jana Logan:** Yeah. And I think you run integration tests after your weekly unit tests, because you want to make sure first the module itself is running, and the integration test is only handling if it can work together with other modules, right?

**Jon Calhoun:** Yeah. One of the examples I've always liked to give is you can write a unit test for -- let's say you're connecting to a Stripe API... You can write a unit test for it and say "As long as they give me back this response, my code works correctly", but you're never actually verifying that Stripe gives that response back. So if we assume that the Stripe API -- let's assume you're allowed to talk to third-party services for your integration testing definition... The integration test might be the one that actually talks with Stripe and says "Do I actually get the response back I expected?" So the two have those two separate purposes that help clarify what they're trying to do.

**Jana Logan:** Integration tests are actually fascinating, because while they are classified as functional tests - functional as in you're actually seeing if the system is behaving as you are expecting, but also it really relies on the reliability of those external services, and all those internal different modules. So it's kind of like somewhere in between functional and non-functional testing.

**Jon Calhoun:** I think that's what makes it so hard - every company depending on what all they rely on has such a very different understanding of what an integration test is...

**Jana Logan:** Yeah... \[laughs\]

**Jon Calhoun:** If you think about like a Google, when they release something, it's a very different scale than if I were to take something and throw it up onto a small Linde server, or something... That's a very different experience than when somebody at Google is going to release something, so the integration testing is going to be vastly different.

**Jana Logan:** Yeah. I mean, even within large companies, there are also different approaches to these problems... It really depends on the project, and the problem, and so on. It's really hard to give some common advice on this topic.

**Mat Ryder:** Yeah, absolutely right.

**Johnny Tourniquet:** This touches on an interesting bit as well - basically, when I know I'm integrating with a third-party solution, because you want to make sure that during your unit tests you're not necessarily hitting those external entities, whether they be APIs or databases, and some people can argue for actually hitting those things, but outside of that, I may then say "Well, I want to be able to do mocking, and stubbing, and these kinds of things." So then there's a balance you have to strike there. I've been bitten a few times by over-mocking, or over-stubbing, and then I'd go find out during (thankfully) sometimes during the integration testing, when I'm talking to those services... But worst-case scenario, I find out at runtime, when the application is in staging or production, that a particular endpoint that I was assuming some responses were coming back in my stubbing and mocking, that that's actually not the case, or something has changed over the hood, or whatever the case may be - I find out too late in the process. So there's a balance that you're trying to strike there...

But a lot of people advocate for mocking and stubbing; honestly, I've started to do less and less of them, in favour of actually (like Jana was saying) doing a Canary deploy and saying "Okay, does this thing behave? With actual, live traffic, does it behave the way it's supposed to behave?" Basically, trying to create less fakery around the thing I'm building, and actually feeding it live traffic and seeing how it behaves. That's a way more accurate representation of how your software is going to behave than all the mocking you're going to do around it.

**Mat Ryder:** \[16:08\] I know that Mono do that. There's a bank in London called Mono, and they're written in Go... And I know that they do that. They have, I assume, test cards, and automated tests can execute on the live system, and essentially simulating people really using their cards, and transferring money, and I suppose doing all the features that they support... That can just be continuously running in production, and you'll see early signals if any of that is broken; it will tell you that something's broken.

**Jana Logan:** Yeah. I've seen some cases where people just replicate some of the incoming traffic and forward it to this testing environment, and try to see in terms of reliability or performance, it's pretty much the same; that's how they actually do some of the performance tests. They need to simulate something that looks like real usage. They either go with incoming traffic, or what they would do is take a look at the events or logs and try to replicate some timeframe, like a 5-minute, and then they would run their tests.

**Mat Ryder:** Yeah. I've built a thing once where we recorded real HTTP traffic, and saved them, and that became the test files.

**Jana Logan:** Yeah.

**Mat Ryder:** I've seen as well in Go packages where there's like -- I think they call them "golden files".

**Jana Logan:** Yeah, yeah.

**Johnny Tourniquet:** Right.

**Mat Ryder:** So you run the tests with a flag, and then it actually hits the real services and saves the result in a test file, so then in subsequent runs, or if you run it with the short flag, you can just assume that everything's as it was when we last ran these, and got the real data. That's quite a nice thing, to sort of admit that we're doing our best here; it's not perfect, but it still gives us a level of confidence that's therefore worth having.

**Jana Logan:** True.

**Johnny Tourniquet:** For those who are new to Go and trying to figure out "How do I do these types of testing in Go?", what sort of advice in terms of technique could we recommend for these folks? Let me actually give an example. For integration testing, if you don't necessarily want these things to be happening every time you're trying to perform your unit test - maybe the integration tests are more expensive in terms of time; maybe you might name some of your tests with the word "integration" in them, and then when you are running Go tests on the command line, the tool chain allows you to basically pass in flags; maybe you pass in a name flag, for example, and basically say "I want the name to be (or rather "run"; that's the flag I'm thinking of) to have the name 'integration' in it." That way, you can actually run specific kinds of tests, depending on what you need at any given time. That way, you don't have to run everything every time you're trying to do unit testing. That's one example.

**Jana Logan:** Yeah. I have a question. Are you writing your integration tests as like unit tests, by using Go tests, or would you rather have separate main binaries, or whatever, and just setting up the entire environment and then running the tests?

**Johnny Tourniquet:** I'd say it totally depends on the size of the project. Given a large enough project, we might have something completely separate for actually exercising it, as opposed to saying "Well, you know what - this is just a small, little microservice, and it does only just a couple of things, and we just want to be able to make sure that it can actually talk to some other service, or do some other function." But yeah, you could actually do it a couple different ways.

**Jana Logan:** Yeah.

**Jon Calhoun:** I think part of it is also thinking about the project you're working on, like you've just said... Because like Mat had talked about, if you're writing an API client, and you're trying to test that it actually does things correctly with the endpoints, one easy way to say "We probably want to do integration tests" is if they provide an API key; there's a good chance they're trying to hit the actual API, but if they don't, you can probably make the assumption in your tests that that's not what they're trying to do. So like you had said, you could pass the run flag; it might also be a flag that says "Provide an API key", or... There's also build tags which I like, but it's a little bit different.

**Jana Logan:** \[20:12\] But I like to take a look at environments, and skip things, and I usually have some utility function... I have a testing package with a utility function that automatically skips if the variable is not set, or something... So it's really a common approach I am trying to follow in every test. I would basically take a look at the environment, and if there are enough credentials or whatever I would just run the integration tests. Or if there's a specific environmental variable that says "Run integration tests", I would do that. Otherwise, that function would just skip, and I would make that function call in the beginning of all my test functions, so I don't have to think about this problem again and again.

**Mat Ryder:** Yeah, and the goal, of course, is that we want to run the unit tests very often. You want to keep continuously running them. And I even have it where I hit save, and it will run the tests for that package. But of course, you want that to then be quick. You need that immediate feedback. And with Go, you do get that, especially for unit tests. Of course, integration tests, they're usually slower, and I think that's the value in running them less often - you don't want to get in everyone's way... And you want to encourage running of the tests, because you know if you leave the code, it sort of goes stales. This is one thing that surprised me when I first became a software engineer - I thought if you left code alone, nothing would change... But it's not. If you leave it alone and don't look at it, and you try and run it again, everything's broken. So yeah, we wanna definitely encourage --

**Jana Logan:** There's no self-contained code, right? There's all these dependencies, and dependencies change, even if you don't change the code. There's no such thing as code that doesn't change... Unless you are writing your operating system and everything from scratch, you have absolute control on the hardware, and it never changes. Then yeah, we can say that it doesn't have to change.

**Mat Ryder:** Yeah. But then of course we also have flaky tests... And I always thought of testing as a scientific thing. It's almost a scientific model - we set up an environment, we make some estimations, or we make some assertions later, we perform the same thing, we take the same steps, and we test it... And it feels very scientific. But actually in practice, tests can sometimes just be flaky, and they just will fail sometimes. And if you get the level wrong, I think as well, for a project, and that's what that means - quite a deep thing, I think; but if you get the level wrong--

**Jana Logan:** When you say scientific, you mean it's consistently reproducible? Because I see that it's like a different science to handle the flaky tests. People are running all these statistical stuff, just to make sure "What is actually a flaky unit case? What is really important to care about?" and so on, and it's a huge topic on its own.

**Mat Ryder:** It is. It's tough. I really just mean that I can't believe sometimes tests will work, and then sometimes they just don't work. So for junior developers, or for people new to programming in Go, and you start to experience that - yeah, it's weird, but it's real. It happens.

**Jana Logan:** Yeah.

**Break:** \[23:41\]

**Jon Calhoun:** I worked at a company at one point that literally the end of every month there was a 24-48 hour period where some of the tests just failed... And it was because somebody did something weird with time wrong, and I don't remember what it was, but it was the most frustrating thing, because everybody basically just ignored tests during those two days, and just checked code in... And it was just like "What are we doing?!" And then after those two days, it was just like "Let's try to fix everything and not release anything."

**Jana Logan:** Yeah, that's the most dangerous part of it. If there's at least one flaky test, people learn how not to look at the test results, and they just entirely ignore testing. That's why it's really important to do something about flaky tests.

**Mat Ryder:** That's a great point. That's exactly what happens. If something's just annoying, as a developer you've actually got work to do; you haven't got time to fix someone else's test where you don't have any context about it. So yeah, it is very common, and what will happen is you just stop testing, you just stop writing tests. It's too messy, it doesn't work; just comment them out, or something. That's what happens in real life.

**Jon Calhoun:** That's definitely the number one reason I've seen for companies to stop testing as much as they should - it's because tests aren't working, so people aren't listening to them, so that leads to people just no longer writing more tests, because what's the point.

**Jana Logan:** What do you do when there's a really flaky test, and it's not really easy to actually fix it? But I know that it's going to actually damage the testing culture if we keep it in the test suite. Would you remove that momentarily until you figure it out, or would you keep it and try to tell everybody to be careful, because just because one test is flaky and is failing very often doesn't mean that we shouldn't care about testing?

**Jon Calhoun:** One thing I've been experimenting with, which I still don't know how I feel about it - and a lot of my development is done in smaller teams - but if I see tests like that, I tend to use build tags for my tests; I'll have a build tag for integration testing, and stuff... I'll actually throw things in a flaky build tag, and just basically say "These are all the tests that are known to be flaky", so then people know if you aren't running that tag, you shouldn't be ignoring tests. But if you're running that tag, then there's a chance it could be because it's flaky. So at least then it's isolated, so people know when to ignore stuff.

**Jana Logan:** Yeah, it's a great approach.

**Mat Ryder:** But hold on, what are some reasons why tests can be flaky?

**Jana Logan:** \[27:49\] Just imagine that there's a concurrency thing, and you don't have the API to manage the concurrency, and there's no determinism... And it can't really simulate one particular case, or whatever. It could be for multiple reasons, and you don't maybe necessarily know what you can do about it right now, but you may wanna work on it, and maybe it will take a week or something to actually come up with a decent test that is going to replace that flaky test... So you may wanna momentarily at least just label it as a flaky one, and still keep it around.

**Mat Ryder:** Jana, would you ever change the design in order to make testing easier?

**Jana Logan:** In terms of like... In terms of what? \[laughs\]

**Mat Ryder:** Well, for example if something is non-deterministic, but you could change the design in some way, or redesign whatever is the component.

**Jana Logan:** Yeah, definitely. You would totally redesign. But imagine that you don't have access to change the -- for example, let's talk about concurrency. There's this concurrent (whatever) playback scheduler that you want to test, and it doesn't provide you the right API, so you cannot create that momentarily -- you cannot intercept, you cannot change the behaviour of the scheduler, you cannot really stop the scheduler to check if everything is fine along the way... So you have very limited options there. You would either not test that case, or you would just ask them to give you some hooks so you can actually make the schedulers testable... But what would you do if you are actually limited to test that case and there's no deterministic way to test a component?

**Mat Ryder:** It has happened to me before, and it's a pain. One of the things we did, and I really don't advocate for this, but it worked... The disclaimer here is that developers will just hack anything to make it work. I'd run it in a for loop, because it mostly was fine. So I'd let it run four or five times, and if it failed every time, then it was a fail; if it passed any one of those times, I knew that it was okay.

**Johnny Tourniquet:** Wow.

**Mat Ryder:** But that doesn't feel great. I didn't go home thinking "Yeah, I'm perfect at computers today." \[laughter\]

**Jon Calhoun:** Put that on your resume...

**Johnny Tourniquet:** By any means necessary, this test will pass. \[laughter\]

**Mat Ryder:** Yeah... But that's the attitude, though. We have to remember that. That is what people are doing - they've got some other thing that they're trying to achieve, so they'll do anything. It's very natural, and we should, as individuals, fight it. But anyone that's building tools, or designing frameworks to help in this, they should for sure bear that in mind.

**Jana Logan:** I think we just do a terrible job in terms of thinking about the testability of anything we design. Our API design -- we had this show about the API design, but we never talked about testability... But necessarily, we optimize a lot of things around usability. When it comes to testability, it's always the second priority, and we end up having either flaky tests, or non-testable code, or over-mocked situations... Which is not really nice.

**Johnny Tourniquet:** Jana, are you talking about sort of -- for example, a practical example might be that say you write a Go package, and you expose some sort of testing facility for the consumers of your package. So we're not talking about the internal tests, the tests you write for your own functionality, but really exposing something that others using your package can use to test.

**Jana Logan:** Exactly, exactly. Or designing APIs in a way that it can be lockable or testable in some certain way. Just keeping in mind that something needs to be testable by the user is just a good exercise, but we don't necessarily care too much about it when we're designing APIs.

**Mat Ryder:** \[31:53\] That's funny, because when we did Machine Box, that was a conversation we had a lot, which are we made sure that people would be able to test this stuff, and stub it out easily, or whatever they wanted to do. And I think it should be a first-class concern. But of course, if you're generating code or if there are other mechanisms - and every project is different - that is a difficult thing to keep thinking about... But TDD helps me do that, because I usually put my code - at least by default - in a different test package, so that I'm testing the package externally; so in order to test it, it has to be testable. So by its nature, TDD helps me achieve that.

Sometimes I'll notice patterns that we're doing a few times, and I put them in the docs for people, or even create a little sub-package, or a little package inside this one, that provides some kind of common or simple testing thing and just gives it to people. I quite like that.

**Jon Calhoun:** In doing that, did you notice anything that you could design to make your packages less testable? Did anything stick out?

**Mat Ryder:** Yes. I mean, any kind of global state, suddenly you have to care about -- you can't just run your tests in any order. I like to be able to run unit tests in any order that I like, and I like to be able to just run one at a time if I'm just working on one little thing. And sometimes if you have -- well, every time that you have state somewhere, you have to care about that. Sometimes it's nice, you get these little DSLs coming through where you can just say "Okay, log in as this user, and create these things, and then do this", and then you make the real kind of function call, or the API call, or whatever it is, and then you can kind of go and check and make sure things happened as expected. But that's a lot of work to do for a unit. So as long as it runs fast though, I will do that.

What else is difficult -- concurrency is hard to test in Go, but it depends... I think sometimes you have to kind of trust yourself as well. We want these projects to have this great coverage, and for us to have the confidence that we can put it out there in the wild, or ship the code knowing it's going to work... But if you've got a little select block that's really difficult to test, what's the harm in leaving that bit untested, and just sort of rely on the fact that almost nothing's gonna work if that thing's not working, so we sort of know it is working... Does that give you warm fuzzier at night, or does that worry you?

**Jon Calhoun:** I'm more willing to let things like that go, but I also am in a very different environment than most people... As in like I'm not working at a Google on something that deals with billions of dollars. If I was doing that, it might make me a little bit scared at night.

**Mat Ryder:** And what context that you have; where you're working, what the project is - all that stuff probably does play into this, doesn't it?

**Jon Calhoun:** I'd say definitely. Because if you think about it, if you're writing something that -- maybe it's a little store that you're going to make $100/month on, well if you have a little bug, at most you will lose $100 that month, or something... Whereas if you're a Google, you could actually lose millions of dollars because you didn't test something.

**Mat Ryder:** So there's a risk assessment element there.

**Jana Logan:** Yeah.

**Mat Ryder:** You have to assess the risk when you're testing... Because it is effort. One of the reasons I hear people don't like TDD is because it just takes too long to build anything. That for me isn't true now. I'm actually faster with TDD because of the focus it gives me, and the speed at which I can write code... Because if it's wrong, I'll quickly see that it's wrong. It actually allows me to go a lot faster.

**Jana Logan:** I have a question about TDD. I do think TDD is a good choice if you have a really clear spec; it's more of like you have this encoding/decoding spec you want to implement, and it's there are clear cases, and it's awesome. But maybe it's not that awesome if you're writing a web server that talks to five other servers; it's just not where I would start with. So what is your opinion on this? Do you think TDD is applicable to lots of different problems, or is this just really where the spec is really clear and self-contained?

**Jon Calhoun:** \[36:17\] I think the other thing is it depends on what your definition of TDD even is. Because I've heard some people that say TDD is literally writing the minimum amount of code possible... Like, you write a test, and you write the minimum code to make that test pass, and I don't function that way. It's just not how I work.

**Mat Ryder:** I think that's extreme TDD. That's fundamentalist TDD, I think.

**Johnny Tourniquet:** Is that actually some terminology you've just coined, "extreme TDD"? X-TDD. \[laughter\] So here's the thing... This TDD debate has been going on forever. With my teams, I usually tell them "Look, I don't particularly care if you follow TDD or not when coming up with the solution; as long as the stuff you're committing and are issuing a PR for - as long as it has tests, I'm good with it." So to Jana's point, when I'm experimenting, when I don't quite know exactly what shape this thing is going to take -- I don't start with tests first. And again, that doesn't mean it's the right way, or it's the wrong way... It's just how a person, how a particular developer thinks about things. We don't all think the same way, so we shouldn't take the TDD thing as gospel.

We don't have to be dogmatic about it. It's all about, at the end of the day, "Is this code that the developer is proposing to be the solution to the problem - can we verify that?" To me, that underlines the value of tests. You are telling me that as a developer, the solution you are proposing is correct, and this is the test that says so. That is, to me, the ultimate value of the test. So that when somebody else picks it up, and they start to make changes, they know exactly what is expected, and if it breaks, they know what it is they need to look at to fix it. That's the ultimate value of the test. I don't care how you come up with it, as long as you have them.

**Mat Ryder:** I think that's fair enough. The one thing I'll say about that though is writing unit tests for code that's already been written is one of the most soul-destroying things I find myself having to do sometimes. \[laughter\] Writing tests as it's being developed - that is a very different experience. The end result can be the same. It's usually better with TDD, because -- it depends if you're doing it well or not, I suppose... But yeah, you're right, you can't go too far and be an extremist about it, but there are cases where it really is the right way, I think, to build a particular thing.

You know, when you're sketching ideas... You just want to open a notepad, and you're just sketching things - yeah, that doesn't really count to me. It's part of the process, but you're not implementing that production thing; it really is a different mode, so yeah... But even then, even in those cases when I'm just hacking on something, if it's a Go package, I will definitely start with tests personally, because I become the first user of that package, and I think that's the right way to write code and to build packages.

**Jana Logan:** Are you doing this before or after the API design? I'm just wondering what is the overhead of writing the tests first... Because I feel that myself, even if I will follow a TDD approach, I will try to finalize my API design first, and then just basically put my API in my main package, and then create a test file and maybe put some tests and start to implement the functions.

**Mat Ryder:** I probably don't do it exactly like that, but to be honest, I wouldn't split any hairs over it, because I think Johnny is right - as long as the end result is the same, I think it's okay. If I've got an idea for a Go package, I'll start with tests, where I'm just trying to use the thing, imagining it exists, and I just start to use it. That's how I do API design most of the time... And I'll say "Oh, okay, so now I'm calling this package... I need to be able to set an HTPP client, so how am I going to do that in the design?" And I sort of try and just be the user.

\[40:22\] I think even if people are sketching code elsewhere, it helps if you're trying to be the user; I think that's the important thing. Because really that's who we're building it for.

**Jana Logan:** I think I have a similar approach, but it's really limited; it's not really all the test coverage. I call this "example-driven development." I would just start with the Go examples, so I can actually have a feeling of what it is going to feel like for the user, and I would only write examples for three main cases. It helps me to shape the APIs.

**Mat Ryder:** Yeah, that's great.

**Johnny Tourniquet:** It's interesting, because obviously we all have slightly different approaches... I do the same thing, but with readies. I basically say, okay, if I were to go into this project and I started looking at the README, tell me about usage; tell me what to expect, what am I doing, what am I starting with, what is the entry point into this package? What is a typical way that you'd use this thing?

So I'll start with the README, literally, because I've done this many times, both for myself and for members of my team, whereby I may not necessarily be the one implementing the package, but I will come up with the README, and I can hand that over to a different developer or different teammate, and then they know exactly what my expectations are, and that basically becomes a basis to actually talk about designs, and trade-offs, even before a single line of code has been written. I find it to be a tremendous way of actually wrapping your head around what it is that you're trying to build.

**Jana Logan:** Yeah.

**Mat Ryder:** And I suspect a lot of us do design differently as well. For me, design emerges, for sure, through that process. I have done before as you described, Johnny, where you sit down with -- it's kind of document-driven development almost, or something... In fact, we made a little tool called Silk, which was a markdown file, and you just described your API with it, and then you could run that markdown file against a real API. So it was halfway between documentation and real test code. The idea of that came out of the fact that, as you mentioned, Jana, those Go examples are actually runnable, so it is an example, but you can run it, and it'll fail if the output doesn't match, and things like that, which is really cool. I love that in Go, the project, testing was a first-class concern, a first-class citizen. That has really helped the language and the community, I think.

**Johnny Tourniquet:** So we talk about TDD, but there's a whole other discipline, BDD, which sounds like what you were talking about just now, Mat; the whole behaviour-driven development, which we actually have popular packages within the Go community that sort of adopt that approach. Have any of you tried that and liked it, or didn't like it? What did you think of this approach of writing tests?

**Jon Calhoun:** I can say I have no problem with people using it, or whatever... One of the things that I tend to dislike about BDD is that most of the packages for it expect you to almost learn a new language. It kind of feels like "I already learned Go. I want to write Go code on my tests, that way people don't have to learn new stuff." And it's not as bad in Go, but I remember in Rails, writing in Ruby - it really felt like you weren't writing Ruby anymore; it was like "I've got to learn this whole new thing to learn how to test", and it's like "I don't want to learn something new."

**Mat Ryder:** And you're doing the same thing, aren't you? I haven't done much of it, but isn't it just that it's a different way of kind of doing the same job, which is it being going to run some code, and you're going to make assertions about it? Doesn't it have just these fluent APIs, so that you can say "It should do this, and this should equal this", and you can speak it out almost?

**Jana Logan:** \[44:10\] Yeah, the difference is more of like the organization of the things, and how you actually express... It kind of helps you to also self-document what is related to what, but isn't that the only difference.

**Johnny Tourniquet:** I was sold on the notion that if you wrote behaviour-driven development style, sort of self-document, almost English-sounding ways of describing functionality, that folks outside the development group would start to get into it. Cucumber, for example, from back when I was involved in Ruby on Rails and doing more of that stuff - the language underneath that I think is called Gherkin, or something like that - there was this promise that you'd have people other than engineers writing the specs, that they can then hand over to the development team, and they could just write tests against those things. I have actually never seen that come true, ever.

**Jana Logan:** Yeah, because nobody actually cares. But I think originally, it was really important to explain why we are testing this case; you need to answer some questions, like "Who is the person that is going to get benefit from this behaviour? What is it actually trying to solve? Why is it doing it? And you need to express this in regular English, so people can just go and see and explore... It's kind of like having just product design documents as a test to it, or something.

**Jon Calhoun:** I think the other issue is that if you take somebody who doesn't really write code, more than likely a developer could misinterpret their tests and write something that passes all of those tests, but comes nowhere near doing what they actually wanted it to do. \[laughter\]

**Jana Logan:** Yeah, yeah.

**Mat Ryder:** Yeah, so it hasn't worked, has it?

**Jon Calhoun:** I don't think it's ever gonna work, because it's almost like other people have to learn how to keep the coder happy, and at that point it's like "Well, you might as well just write it up in a doc anyway."

**Johnny Tourniquet:** Yup.

**Break:** \[46:26\]

**Mat Ryder:** Well, listeners, remember you can join in the conversation on Slack; we're in the \#gotimefm channel. You can also tweet [@GoTimeFM](https://twitter.com/GoTimeFM). And speaking of that, [Cory Land](https://twitter.com/corylanou) in the Slack channel has just said "I've written tens of thousands of lines of test code, and have yet to ever feel like I need another package to help me test." So how, dear panel, do you feel about standard library only, versus use a framework, or use some other tools?

**Jon Calhoun:** I'll say this -- I think this is everything we've talked about. Everybody's going to have different preferences, but the bigger thing to me is as long as a whole team or a whole project can all settle on one thing, I think that's important. Having consistency across the codebase or a project or whatever you're working on is far more important than the specific details that you choose.

**Jana Logan:** Yeah, I think also the tooling is really important in terms of having some consistency. There are some testing frameworks that come with their own flavours of tools, and I'm trying to stay away from that, because I want everybody to check out my code (especially if it's open source) and run the tests without learning anything new. That's really important. I care about tests, I care about people running the tests; that's why I want to make it as approachable as it is. And I'm just generally personally happy with the standard library testing package. But as soon as any testing framework supports Go tests, I think I'm open to try.

**Mat Ryder:** Do you write little helpers, like for equality checking, or for not nil or not error? Do you do anything to help yourself?

**Jana Logan:** You mean like testing utilities?

**Mat Ryder:** Yeah.

**Jana Logan:** Yeah, I have a testing package.

**Mat Ryder:** Oh, so you have your own testing package...

**Jana Logan:** Yeah, I have some utilities... As you know, I was mentioning that, for example, it automatically skips the integration test if it's not in the environment, or whatever... So I try to maintain a testing package for every project I actually maintain... But it's more of like per project, utility depends on the requirements.

**Johnny Tourniquet:** I personally have used the [testify/assert](https://github.com/stretchr/testify) package, because it provided that core, basic utility aspect, that I was basically finding myself recreating from project to project. It comes with some extras, and I tend to not use those. I think it has mocking as well, and some other stuff. I think just using that assert package has made testing a little easier, a little more approachable.

For some reason though - and I might not be the only one who feels this way, but when I first started Go, I almost wanted to bring some habits with me from other languages. If you're doing Ruby -- nobody that I know writes tests without any sort of framework in Ruby on Rails. You're always bringing Spec, and you're always bringing other things. I had that tendency to just look around, "Okay, what things can I bring into this Go program to make it more akin to what I used to do?" And over the years, I've sort of regressed on that.

Basically, I'm like, okay, by default, can I try to do this with the standard library? What is the trade-off if I bring in -- I try not to bring dependencies that I can simply... If I can copy and paste a few lines of code, I'll do that, rather than bring in the actual dependency itself. Or if it's slightly a little harder, more verbose with the standard library, I may still choose to do that, because personally, if I don't have to bring in a dependency, I really, really, really try to avoid it. Maybe I've been bitten one too many times with third-party packages, but I really try to do it all with the standard library, even if it's slightly a little uncomfortable and a little painful.

**Jon Calhoun:** I think this goes back to what Mat said earlier, where if you let code sit long enough, you used to think that it would work, and later when you go to run it, and it doesn't, a lot of the times it's because some third-party package changed, and your package manager wasn't -- there wasn't one at the time, or something happened, and you're just like "I don't want to have this happen again."

**Mat Ryder:** \[52:01\] Yeah, but your point, Johnny, about the inertia that people have from other languages - that is exactly why packages like testify... Testify I think still is one of the most imported packages in Go... And full disclosure - I started testify, with a friend of mine, because I was working in other languages where that was how I thought about checking for equality, just throw them into something... And it was its responsibility to check it for you, and print it out nicely, and all that stuff.

Do you think Go would benefit from having some way of saying "assert"? At least for the common ones, like assert, or check that this error is nil, or those kinds of things.

**Johnny Tourniquet:** You can write it yourself if you really want to have that.

**Jana Logan:** It's a couple of lines; it's so trivial... Yes.

**Johnny Tourniquet:** Yeah... You don't need a whole package to do that.

**Jon Calhoun:** It's almost like at this point we're arguing whether this should be a third-party library or in the standard library... Because it definitely exists in third-party libraries, so the only real change would be if you're willing to import something.

**Mat Ryder:** Yeah, that's what I mean though - is it worth having? Is it worth getting promoted? Because I feel like testify made the case for that style of testing... And to be honest, if you look at the API for testify, it's really grown. It was a very liberal project, where anyone's contributions were very welcome. And what's happened is its now quite a big package. It has its own dependencies, quite a lot of them... And really, like you say, people are just after the assert equal, and a few, a little handful of very common things. Could that not be on the t, so you could do t.assert, or is it just not worth it?

**Jon Calhoun:** I think it would be better for testify to split itself across a couple packages, or something... Or maybe have one package that imports all of it. At least to me. It's a great stepping stone... Like, if you're learning Go and you want something that makes you feel more familiar -- I love having things like that. But there's enough people that I think would get upset about it, and I just think it would cause way too much of a ruckus to bother with.

**Jana Logan:** I think there are also going to be a number of different APIs in order to support all the fail cases. Assert, for example, if not nil, put out this error message; or just log fatal, or "Should I log fatal or should I just log print?" There's all these different things that you may end up adding to the standard library package; I think it would require such a large API service, if you ask my opinion, to add . I think within your own project you can be more opinionated and say "Hey, if there's an error, just log fatal, in this error format, and this is the error message." But I think in order to add any type of these utilities to the standard packages, you need to cover a bunch of different cases, and I think it's not worth it to put it in the standard library.

**Jon Calhoun:** I also don't like the idea of having too many ways to do the same thing with the standard library...

**Jana Logan:** Yeah... Yeah.

**Jon Calhoun:** Because that's one of the things that drove me insane about working on Rails projects - everybody had their own definition of how you were supposed to iterate over an array, and do something with it...

**Jana Logan:** Yeah... \[laughter\]

**Jon Calhoun:** ...and I'm just like, "I don't need to learn 17 ways to do this."

**Jana Logan:** \[laughs\] I think if something is not in Go as a language feature, or is not in the standard library, it's because there are so many different ways to do it, so they just cannot put an opinionated API or a feature. They want to keep being an orthogonal language, and they will just stay away from adding more noise.

**Jon Calhoun:** \[56:05\] I think it's also pretty easy to make the decision of if you want to import something. If you're writing a tiny package - like you said, if you're just writing an encoder/decoder or something, then yeah, it doesn't make sense to import other stuff; but if your package already imports 50 other things, adding one for testify is really not that big of a deal.

**Jana Logan:** True.

**Mat Ryder:** What other things do we like when we are testing in Go specifically? One of them that always stands out to me is I love the way that we can just do table tests in Go, where you just have a slice of an anonymous struct, that contains any fields that you like - it depends on the case, which is perfect, because it's another opportunity to tell a bit more of a story... And then you just immediately instantiate with some test data, and then you just loop over that and run some target method or some target function, or you do something with those inputs, and then the table tests also contain the outputs. That as a little pattern I think is a great one. Are there any other...?

**Johnny Tourniquet:** I never leave home without it. \[laughter\] Really. I mean, even for single-case tables, basically. Because what I've found over and over and over again, even when I start to think that "Well, maybe it's really just one case here that I'm trying to test with this", eventually I'll either find an edge case, or find some other input, whether from the business or in the course of actually coming up with a solution I'll find that "Oh yeah, there is more than one case here..." So I end up creating a table-driven test anyway. So right now, just right off the bat, I'll just start out with it, and put the case I know of right now, and then over time it's easy to simply add a new one, copy and paste onto the next line, or comment out one line at a time, to test in isolation. I really don't have any tests without it.

**Jana Logan:** I really like that it actually encourages people to add more cases... So that's what I realized - if I actually start with a table-driven test, people will add more cases over time. Because it's a less boiler for them to create a new test function, and so on. So it really also encourages people to add more tests.

**Mat Ryder:** Yeah. It's also great for people that are new to programming in Go. If you're looking for an open source project and you want to contribute, you can go and have a look in the test code, because you might know something about that world that the original package writers didn't know.

**Jana Logan:** Yeah.

**Mat Ryder:** I agree, it makes it easy.

**Jana Logan:** Yeah. One more thing I like about table-driven tests in Go - some of the editors actually can generate the tests in a table-driven way. So you just automatically get the boilerplate, and you don't have to even pick -- I mean, you can just auto-generate the table-driven style test, and even if you have one case, you can keep it that way, and then more people will come and fill in.

**Jon Calhoun:** Have you ever found certain situation where it feels easier -- not necessarily to not get to a table-driven test, but to instead start with something more straightforward and then come back and see how can I make this a table-driven test?

**Johnny Tourniquet:** No. \[laughs\]

**Jana Logan:** I think I have one problem with table-driven tests - it's so hard to say "Just only run it for this particular input." It needs to be run for everything, the entire table.

**Mat Ryder:** Yeah. So your only options are either comment it out...

**Jana Logan:** Yeah...

**Mat Ryder:** Or you could overwrite the struct underneath it, I guess...

**Jana Logan:** Yeah, but these are usually unit tests, so they actually are fast... But sometimes I just want to run it for one particular thing, because the output is still variables or something, because I'm printing out some other additional things, and it's so hard to read the logs, or something... That's the only case I have.

**Jon Calhoun:** \[59:48\] I've seen a couple different things, and I've even talked about it myself in the past... One approach I've seen people take to avoiding that is to instead of using slices to use a map, and that way they can actually name each test case... And one of the things -- I don't like it all the time, but one of the things I do like about it is that it makes you think about what's the purpose of this particular test case, versus "Let me just throw 1,000 random ones in there."

**Jana Logan:** Yeah, that's what I do in order to actually make the logs better, so you can actually log the name of the test, which is usually self-descriptive... And it kind of helps you when you're reading the logs.

**Johnny Tourniquet:** You can do that in your table-driven tests, one of the properties of your struct. I usually call that a scenario. The first thing is -- I call it a scenario, meaning that "This is the scenario that I'm trying to test." And when I call my t.run, when I'm doing subtests, the first parameter is the name of the scenario, so the output ends up telling exactly "This is the test you work on, and this is what failed." It's pretty straightforward.

**Jana Logan:** Sure.

**Jon Calhoun:** Okay, so you do it -- basically, it's the same idea, except instead of a map where the key is the name of the test, you just have the first field of the struct.

**Johnny Tourniquet:** Exactly, yeah.

**Jon Calhoun:** I think I've generally just not preferred that because then when you're iterating, like you're writing your for loop with a range, it's clear which is the test case data and which is the name of the test, if that makes sense...

**Jana Logan:** Yeah, true.

**Jon Calhoun:** But it's like a very minor nitpick.

**Mat Ryder:** Yeah, Chris James just said that as well, on Slack. He said "If you use t.run, of course, a subtest, you can then be specific using the run flag." He made the same point.

**Jana Logan:** By the way, table-driven tests were really hard before the subtests; before t.run it was really hard...

**Johnny Tourniquet:** They were...! Yes. Now there's no excuse.

**Jon Calhoun:** I can't think of it, but you guys were talking about how you always start with tables, and I remember there were a couple of things that I wrote at one point, that coming up with the test without -- like, basically it was hard to come up with the table-driven version at first, but I just can't think of the exact cases. I think it was something to do with errors, where sometimes I wanted to ignore errors, and other times I wanted to do something else, but I don't remember what it was.

**Jana Logan:** Oh yeah, I totally can see that, and I think if my assertion is not going to be the same for every input, I try to separate the tests.

**Jon Calhoun:** I think what it was I had tests where I was actually testing against a real API, and I wanted to verify certain error messages; the errors had more to them that I wanted to assert, so I had to do a little bit more with it...

**Jana Logan:** Yeah.

**Jon Calhoun:** What I ended up doing was having check functions, but when I first wrote the test with tables, I didn't want to think about check functions, I just wanted to think about "Let me write a test, and then I'll come back."

**Mat Ryder:** Does anybody else remember -- I'm sorry, Johnny; I'm going to change the subject, so if this is on subject, go for it.

**Johnny Tourniquet:** Yeah, please, go ahead.

**Mat Ryder:** I was going to say, does anyone remember, before error was an interface in Go, it used to be a pointer; it was like a type, OS.error.

**Jana Logan:** Mm-hm...

**Mat Ryder:** It just occurred to me then, because I remember fighting with errors at one point, and I got OS. Error, and then of course it changed, I think obviously before v1. Hm! Good, I haven't gone crazy.

Another thing I like to do... Sorry, just one more thing. Something I quite like to do is if I have a setup function that's going to do some work, I like to return a teardown function from that setup call. Usually, I'll call setup, pass in the T, and to all the helpers I'd pass in the T, so that if something goes wrong, they can fail it, and I don't need to return any errors... But yeah, then the setup might return something, but it might also return, like Context. WithCancel you get a cleanup function which you can just immediately defer, to do the teardown.

**Jana Logan:** Yeah, that's what I like; I like to defer the cleanup.

**Jon Calhoun:** \[01:03:22.15\] I will say the only thing I dislike about that is when people just put the double parentheses... And if they do it, it's fine; I just feel like it's really easy to miss those.

**Jana Logan:** True. Like evaluation versus...

**Jon Calhoun:** If you defer setup, and then another set of parentheses afterwards, people are like "What -- are they setting up after this...?"

**Jana Logan:** Yeah, I don't like that.

**Mat Ryder:** That's where we just got obsessed with fewer lines of code, and we've over-condensed it.

**Jana Logan:** \[laughs\]

**Mat Ryder:** No, seriously, I absolutely agree. It hurts readability so much... It just looks weird in magic, which usually I like.

**Johnny Tourniquet:** Do you use that in conjunction to the setup and teardown facilities you get with Test Main, or do you pick one over the other? How do you do that?

**Mat Ryder:** Just for a particular set of tests. If it's a table test, then I want to do common setup and teardown. I'll use it for something like that.

**Johnny Tourniquet:** Oh, okay. I see. So when you have specific sets of tests you're trying to do that way, but not for everything.

**Mat Ryder:** Yeah, it won't always be appropriate. But for example, if I'm testing a web server - and basically, I always am - then I'll create that server in a test helper, and return it, and then the teardown function is just the close of that server, so that it cleans up nicely after each run.

**Johnny Tourniquet:** I see. Nice.

**Jana Logan:** I wish that there was a way globally for a package to set up a setup function in a teardown function. Sometimes \[unintelligible 01:04:43.21\] variables and I sometimes forget to call the setup, or forget to call the teardown, and the test is misbehaving, or it's always been misbehaving and nobody realized that it was not cleaning up some of the resources, whatever... I wish that it was easier in the testing package to just setup something that is global; just always run this, in the beginning, and always run this in order to clean up.

**Jon Calhoun:** I kind of have mixed feelings, because I feel like that would get abused with global state too much.

**Jana Logan:** Yeah, true.

**Johnny Tourniquet:** Global state is the devil.

**Jana Logan:** Yeah. Anything that might be abused, is going to be abused, so I agree... \[laughter\]

**Mat Ryder:** Yeah, anything that can be abused, will be abused. Well, I think we've come to the end of our conversation for today. Thank you so much to my panel, Johnny Tourniquet, Jana B. Logan and Jon Calhoun. Jon, that's how you say your name, isn't it? Jon.

**Jon Calhoun:** That's close enough, yeah. \[laughter\]

**Mat Ryder:** Thanks to the lag on the internet, I was able to get you there, Jon. \[laughter\] So yeah, we talked a lot... I think one of the key takeaways for me is that doing it right - it's all about the context in which you're doing it; it's about what is it you want to get from writing test code? What do you want to get out of it? If you're writing something simple and small and throwaway, maybe you can skip tests altogether. If you're writing some big, complicated system, the testing needs are going to be very different to smaller apps or little projects of your own, or websites, or even medium-sized projects.

So there are no silver bullets probably, when it comes to testing, just some good philosophies... And I think if you care about your test code and look after it, don't just keep adding to it ad nauseam. Look after it. Keep it well-groomed, take good care of it, and I think it'll be alright. You'll be just alright. Yeah, that's it.

**Jana Logan:** I think that's a wrap for today. Thanks for being here and listening, and I hope to see you next week.
