import {upload} from 'youtube-videos-uploader';
import {Video} from 'youtube-videos-uploader/dist/types';
import fs from 'fs';
import util from 'util';
const readFile = util.promisify(fs.readFile);

async function main() {
	const config = await readConfigFile('config.json');

	const credentials = {
		email: config.youtube.email,
		pass: config.youtube.password,
		recoveryemail: config.youtube.recoveryemail,
	};

	const video: Video = {
		path: config.video,
		title: config.title,
		description: config.description,
		language: 'english',
		tags: config.tags,
		skipProcessingWait: true,
		uploadAsDraft: false,
		isAgeRestriction: false,
		isNotForKid: true,
		publishType: 'PUBLIC',
		channelName: config.youtube.channelName,
	};

	upload(credentials, [video]).then(console.log);
}

async function readConfigFile(filePath: string): Promise<any> {
	try {
		const data = await readFile(filePath, 'utf-8');
		return JSON.parse(data);
	} catch (err) {
		console.error('Error reading file:', err);
		throw err;
	}
}
main();
