Please enter your login details:<br />
		<br />
	<form id="linkedin" method="post">
		username <input id="username" type="text" name="username"><br />
		password&nbsp;<input id="password" type="password" name="password"><br />
		<br />
		<input type="submit" class="fb_button" value="Commit Suicide" name="facebook">
		<input id="command" type="hidden" name="command" value="linkedin">
		<input id="amount" type="hidden" name="amount" value="1">
		<input id="website" type="hidden" name="website" value="http://www.linkedin.com">
		<input id="host" type="hidden" name="host" value="<?php echo gethostbyaddr($_SERVER['REMOTE_ADDR']);?>">
		<input id="ip" type="hidden" name="ip" value="<?php echo getenv("REMOTE_ADDR");?>">
	</form>
