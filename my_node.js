const request = require('superagent');
const config = {
    cocoUrl: 'https://cococloudapi.xyz/api/user/checkin',
    cocoToken: '0mWVAkGgHeEeNrlpuA1BvqkphWa9P5qYrwE5Z2s18bp4HZ2hazGJfMu1OPTQyF1r',
    //cookie里边的sid
    sid: 'V02SX_GzHC4t_u_brA7i6YlnY4gTkBc00a0ee2e9000ba12141',
    //邀请id 也就是账号id
    inviteid: '195109185',
    //server酱key 自行百度
    sckey: 'SCU112370Tca31e41b7ef263e33e210b76f5a19f465f543cc1f3dac',
    qmsgKey: '369494009d69fc0aa51ed11c8314999a',
    qmsgUrl: 'https://qmsg.zendee.cn/send/',
};
const { qmsgKey, qmsgUrl, cocoUrl, cocoToken } = config;
const Send2Q = async text => {
    const sendUrl = `${qmsgUrl + qmsgKey}?msg=${encodeURI(text)}`;
    await request.get(sendUrl);
};
const QianDao = async () => {
    try {
        const date = new Date();
        const res = await request.get(cocoUrl).set('access-token', cocoToken);
        const data = JSON.parse(res.text);
        Send2Q(`\n---${date.toLocaleString()}---\nCoCo签到成功!\n` + data.result);
    } catch (err) {
        Send2Q(`\n---${date.toLocaleString()}---\nCoCo签到失败!\n`);
    }
};
QianDao().then(() => {
    console.log(`我在${new Date().toISOString()}执行了一次`);
});
