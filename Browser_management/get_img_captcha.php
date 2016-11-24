#!/usr/bin/php
<?php

if ($argc > 1)
{
	$ch = curl_init($argv[1]);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
	$ptr = curl_exec($ch);

	preg_match_all('/<img .*src="(.*?)"/', $ptr, $imgs);
	if ($imgs)
	{
		preg_match("/\/\/(.*)/", $argv[1], $tt);
		if (!file_exists('captcha'))
			mkdir('captcha');
	}
	if ($imgs)
	{
		foreach ($imgs[1] as $key => $value) {
			preg_match("/.*\/(.*)$/", $value, $image_name);
			touch('captcha' . "/" . $image_name[1]);
			file_put_contents('captcha/captcha.png', file_get_contents($value));
		}
	}
	curl_close($ch);
}
?>