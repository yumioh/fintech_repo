import re

text = """/**/
jQuery111103661092026199333_1695051320003({
    "contents": [{
        "serviceId": "ENTERTAIN",
        "contentsId": "ne_001_0014105953",
        "isDisplay": true,
        "categoryId": null,
        "countType": "DEFAULT",
        "reactions": [{
            "reactionType": "like",
            "count": 1,
            "isReacted": false,
            "periodUser": null,
            "reactionTypeCode": {
                "name": "like",
                "messageCode": "reaction.type.like",
                "description": "좋아요"
            }
        }, {
            "reactionType": "congrats",
            "count": 1,
            "isReacted": false,
            "periodUser": null,
            "reactionTypeCode": {
                "name": "congrats",
                "messageCode": "reaction.type.congrats",
                "description": "축하해요"
            }
        }, {
            "reactionType": "expect",
            "count": 0,
            "isReacted": false,
            "periodUser": null,
            "reactionTypeCode": {
                "name": "expect",
                "messageCode": "reaction.type.expect",
                "description": "다음작품원해요"
            }
        }],
        "reactionMap": {
            "com.naver.react.core.nbasearc.common.ReactionType@407b2ee9": {
                "reactionType": "like",
                "count": 1,
                "isReacted": false,
                "periodUser": null,
                "reactionTypeCode": {
                    "name": "like",
                    "messageCode": "reaction.type.like",
                    "description": "좋아요"
                }
            },
            "com.naver.react.core.nbasearc.common.ReactionType@55d9312d": {
                "reactionType": "congrats",
                "count": 1,
                "isReacted": false,
                "periodUser": null,
                "reactionTypeCode": {
                    "name": "congrats",
                    "messageCode": "reaction.type.congrats",
                    "description": "축하해요"
                }
            },
            "com.naver.react.core.nbasearc.common.ReactionType@1aec4fe3": {
                "reactionType": "expect",
                "count": 0,
                "isReacted": false,
                "periodUser": null,
                "reactionTypeCode": {
                    "name": "expect",
                    "messageCode": "reaction.type.expect",
                    "description": "다음작품원해요"
                }
            }
        },
        "reactionTextMap": {
            "ko": {
                "cheer": "응원해요",
                "congrats": "축하해요",
                "expect": "기대해요",
                "like": "좋아요",
                "sad": "슬퍼요",
                "surprise": "놀랐어요"
            },
            "zh-hant": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "zh-tw": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "zh-hans": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "ja": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "en": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "fr": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "zh-cn": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "es": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            },
            "es-mx": {
                "cheer": "cheer",
                "congrats": "congrats",
                "expect": "expect",
                "like": "like",
                "sad": "sad",
                "surprise": "surprise"
            }
        },
        "isLogin": false,
        "customized": false,
        "differentPlatform": false
    }, {
        "serviceId": "JOURNALIST",
        "contentsId": "76915",
        "isDisplay": true,
        "categoryId": null,
        "countType": "PERIOD",
        "reactions": [{
            "reactionType": "cheer",
            "count": 1280,
            "isReacted": false,
            "periodUser": null,
            "reactionTypeCode": {
                "name": "cheer",
                "messageCode": "reaction.type.cheer",
                "description": "응원해요"
            }
        }],
        "reactionMap": {
            "com.naver.react.core.nbasearc.common.ReactionType@536fd80b": {
                "reactionType": "cheer",
                "count": 1280,
                "isReacted": false,
                "periodUser": null,
                "reactionTypeCode": {
                    "name": "cheer",
                    "messageCode": "reaction.type.cheer",
                    "description": "응원해요"
                }
            }
        },
        "reactionTextMap": {
            "ko": {
                "love": "사랑해요",
                "haha": "재밌어요",
                "touched": "감동받았어요",
                "away": "away",
                "analytical": "분석탁월",
                "recommend": "추천해요",
                "fan": "팬이에요",
                "quote": "퍼갈게요",
                "interest": "interest",
                "sad": "슬퍼요",
                "wow": "놀랍네요",
                "surprise": "놀랐어요",
                "normal": "보통이에요",
                "like": "좋아요",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "후속기사원해요",
                "please": "please",
                "angry": "화나요",
                "congrats": "축하해요",
                "cheer": "응원해요",
                "home": "home",
                "yay": "기뻐요",
                "expect": "다음작품원해요",
                "help": "도와주세요",
                "modify": "수정해주세요",
                "warm": "훈훈해요",
                "toobad": "아쉬워요",
                "wantbuy": "사고싶어요",
                "useful": "유익해요",
                "likead": "광고같아요"
            },
            "zh-hant": {
                "love": "love",
                "haha": "haha",
                "touched": "感動",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "驚",
                "surprise": "surprise",
                "normal": "normal",
                "like": "讚",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "期待",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "想買",
                "useful": "useful",
                "likead": "likead"
            },
            "zh-tw": {
                "love": "love",
                "haha": "haha",
                "touched": "touched",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "wow",
                "surprise": "surprise",
                "normal": "normal",
                "like": "like",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "expect",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "wantbuy",
                "useful": "useful",
                "likead": "likead"
            },
            "zh-hans": {
                "love": "love",
                "haha": "haha",
                "touched": "感动",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "惊讶",
                "surprise": "surprise",
                "normal": "normal",
                "like": "喜欢",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "期待",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "想买",
                "useful": "useful",
                "likead": "likead"
            },
            "ja": {
                "love": "大好き",
                "haha": "面白い",
                "touched": "感動した",
                "away": "AWAY",
                "analytical": "analytical",
                "recommend": "お勧め",
                "fan": "ファンです",
                "quote": "お借りします",
                "interest": "interest",
                "sad": "悲しい",
                "wow": "びっくり",
                "surprise": "驚きです",
                "normal": "普通です",
                "like": "いいね",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "続きを教えて",
                "please": "please",
                "angry": "有益",
                "congrats": "おめでとう",
                "cheer": "応援するよ",
                "home": "HOME",
                "yay": "嬉しい",
                "expect": "次回作も期待",
                "help": " ヘルプ",
                "modify": "修正お願い",
                "warm": "いい話だなあ",
                "toobad": "残念",
                "wantbuy": "欲しい",
                "useful": "有益です",
                "likead": "広告みたい"
            },
            "en": {
                "love": "love",
                "haha": "haha",
                "touched": "touched",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "wow",
                "surprise": "surprise",
                "normal": "normal",
                "like": "like",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "expect",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "wantbuy",
                "useful": "useful",
                "likead": "likead"
            },
            "fr": {
                "love": "love",
                "haha": "haha",
                "touched": "Ému",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "wow",
                "surprise": "surprise",
                "normal": "normal",
                "like": "J'aime",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "Je m'attends",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "Je veux acheter",
                "useful": "useful",
                "likead": "likead"
            },
            "zh-cn": {
                "love": "love",
                "haha": "haha",
                "touched": "touched",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "wow",
                "surprise": "surprise",
                "normal": "normal",
                "like": "like",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "expect",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "wantbuy",
                "useful": "useful",
                "likead": "likead"
            },
            "es": {
                "love": "love",
                "haha": "haha",
                "touched": "Me encanta",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "Me asombra",
                "surprise": "surprise",
                "normal": "normal",
                "like": "Me gusta",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "Me espera",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "Quiero comprar",
                "useful": "useful",
                "likead": "likead"
            },
            "es-mx": {
                "love": "love",
                "haha": "haha",
                "touched": "Me encanta",
                "away": "away",
                "analytical": "analytical",
                "recommend": "recommend",
                "fan": "fan",
                "quote": "quote",
                "interest": "interest",
                "sad": "sad",
                "wow": "Me asombra",
                "surprise": "surprise",
                "normal": "normal",
                "like": "Me gusta",
                "relax": "relax",
                "hr_test": "hr_test",
                "want": "want",
                "please": "please",
                "angry": "angry",
                "congrats": "congrats",
                "cheer": "cheer",
                "home": "home",
                "yay": "yay",
                "expect": "Me espera",
                "help": "help",
                "modify": "modify",
                "warm": "warm",
                "toobad": "toobad",
                "wantbuy": "Quiero comprar",
                "useful": "useful",
                "likead": "likead"
            }
        },
        "isLogin": false,
        "customized": true,
        "differentPlatform": false
    }, {
        "serviceId": "ENTERTAIN_MAIN",
        "contentsId": "ne_001_0014105953",
        "isDisplay": true,
        "categoryId": null,
        "countType": "DEFAULT",
        "reactions": [],
        "reactionMap": {},
        "reactionTextMap": {
            "ko": {
                "like": "이 기사를 추천합니다"
            },
            "zh-hant": {
                "like": "讚"
            },
            "zh-tw": {
                "like": "like"
            },
            "zh-hans": {
                "like": "喜欢"
            },
            "ja": {
                "like": "いいね"
            },
            "en": {
                "like": "like"
            },
            "fr": {
                "like": "J'aime"
            },
            "zh-cn": {
                "like": "like"
            },
            "es": {
                "like": "Me gusta"
            },
            "es-mx": {
                "like": "Me gusta"
            }
        },
        "isLogin": false,
        "customized": false,
        "differentPlatform": false
    }],
    "serviceOptionType": {
        "ENTERTAIN_MAIN": {
            "012": false,
            "006": false
        },
        "ENTERTAIN": {
            "012": false,
            "006": false
        },
        "JOURNALIST": {
            "012": false,
            "006": false
        }
    },
    "guestToken": "316e26708b0b66e36ab2fd420295d3bf8d2282d71dfddff199bc5ed20e997385cc45025d214faa331ec0b9f007652707c7d00ba58d68fc3987260021d2902312",
    "timestamp": 1695051321158,
    "isLogin": true,
    "cssConfs": [{
        "cssId": "MULTI_PC",
        "assignId": "80ea98bf-33b2-45a6-81eb-605bda387a93",
        "staticId": "17dfaee1-1102-4053-80a1-30c3db88c225",
        "envType": "PC",
        "applyYn": "Y"
    }, {
        "cssId": "ENTERTAIN_PC",
        "assignId": "0f7c757f-9f9a-4e22-b221-5ea3f1943476",
        "staticId": "9c4b314e-a0a5-46f6-b19f-6798a18761b6",
        "envType": null,
        "applyYn": "Y"
    }]
});
"""
react_json = re.sub('(?<=jQuery.{35}\()(.*)(?=\);)','', text)

print(react_json)

