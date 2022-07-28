package json_opt_test

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name string `json:"pName"` // 二次编码，修改在json中的对应的名称
	Age  int8   // 注意，命名必须是大写的，不然外部无法访问
}

type Student struct {
	Person
	Id          int64   `json:"-"`       // 这样表示在json中不会输出
	IsGraduates bool    `json:",string"` // 这样代表在json中将此字段转换为string类型
	Score       int64   `json:"score"`
	TagIds      []int64 `protobuf:"varint,62,rep,name=TagIds,json=tagIds" json:"tag_ids,omitempty" bson:"tag_ids,omitempty"`
}

func Test01() {
	s := Student{Person{"周振武", 18}, 001, true, 100, nil}

	//buf, err := json.Marshal(s)
	buf, err := json.MarshalIndent(&s, "", "	") // 采用格式化编码
	if err != nil {
		fmt.Printf("err = %+v\n", err)
		return
	}

	fmt.Println("buf = ", string(buf))
}

func Test02() {
	jsonBuf := `{
        "pName": "周振武",
        "Age": 18,
        "IsGraduates": "true",
		"haha":86 
}` // 注意最后一定不要有逗号
	var s Student
	err := json.Unmarshal([]byte(jsonBuf), &s) // 这里要传入指针类型
	if err != nil {
		fmt.Println("err :", err)
		return
	}
	println(s.TagIds, len(s.TagIds))
	fmt.Printf("s = %+v\n", s)
}

type PPCtrDcnSlotSt struct {
	Mid           int64 `json:"mid"`
	Gender        int64 `json:"gender"`
	Profession    int64 `json:"profession"`
	Student       int64 `json:"student"`
	IsStudent     int64 `json:"is_student"`
	Age           int64 `json:"age"`
	ZyAge         int64 `json:"zy_age"`
	RegAge        int64 `json:"reg_age"`
	IsReg         int64 `json:"isreg"` // isreg
	Channel       int64 `json:"channel"`
	HistoryLen    int64 `json:"history_len"`
	Pid           int64 `json:"pid"`
	Tid           int64 `json:"tid"`
	PartId        int64 `json:"partid"` // partid
	Source        int64 `json:"source"`
	Ptype         int64 `json:"ptype"`
	Vdur          int64 `json:"vdur"`
	PostAge       int64 `json:"post_age"`
	ExposeWeek    int64 `json:"expose_week"`
	ExposeHour    int64 `json:"expose_hour"`
	ExposeQuarter int64 `json:"expose_quarter"`
	ExposeMinute  int64 `json:"expose_minute"`
	Weekday       int64 `json:"weekday"`
	Rank          int64 `json:"rank"`
	Filter        int64 `json:"filter"`
	Direction     int64 `json:"direction"`
	Nt            int64 `json:"nt"`

	PostNtDetailPostDurDetailRateNorm         float32 `json:"post_nt_detail_post_dur_detail_rate_norm"`
	PostNtLikeAtt3CountRateNorm               float32 `json:"post_nt_like_att3_count_rate_norm"`
	PostNtLikeAtt3CountSumeRateNorm           float32 `json:"post_nt_like_att3_count_sume_rate_norm"`
	PostNtPgodLikeCountDetailRateNorm         float32 `json:"post_nt_pgod_like_count_detail_rate_norm"`
	PostNtPlayRateNorm                        float32 `json:"post_nt_play_rate_norm"`
	PostNtPlayVideoCountRateNorm              float32 `json:"post_nt_play_video_count_rate_norm"`
	PostNtPlayVideoDurRateNorm                float32 `json:"post_nt_play_video_dur_rate_norm"`
	PostNtPlayVideoDurSumeRateNorm            float32 `json:"post_nt_play_video_dur_sume_rate_norm"`
	PostNtPlayVideoDurVideoRateNorm           float32 `json:"post_nt_play_video_dur_video_rate_norm"`
	PostNtPlayVideoRateNorm                   float32 `json:"post_nt_play_video_rate_norm"`
	PostNtShareCountRateNorm                  float32 `json:"post_nt_share_count_rate_norm"`
	PostNtStayTimeSumeRateNorm                float32 `json:"post_nt_stay_time_sume_rate_norm"`
	PostNtSumeCountRateNorm                   float32 `json:"post_nt_sume_count_rate_norm"`
	UserPartidDislikeCountRateNorm            float32 `json:"user_partid_dislike_count_rate_norm"`
	UserPartidDislikeCountSumeRateNorm        float32 `json:"user_partid_dislike_count_sume_rate_norm"`
	UserPartidGsumeCountRateNorm              float32 `json:"user_partid_gsume_count_rate_norm"`
	UserPartidGsumeCountSumeRateNorm          float32 `json:"user_partid_gsume_count_sume_rate_norm"`
	UserPartidLikeAtt2CountRateNorm           float32 `json:"user_partid_like_att2_count_rate_norm"`
	UserPartidLikeAtt2CountSumeRateNorm       float32 `json:"user_partid_like_att2_count_sume_rate_norm"`
	UserPartidLikeAtt4CountRateNorm           float32 `json:"user_partid_like_att4_count_rate_norm"`
	UserPartidLikeAtt4CountSumeRateNorm       float32 `json:"user_partid_like_att4_count_sume_rate_norm"`
	UserPartidLikeCountSumeRateNorm           float32 `json:"user_partid_like_count_sume_rate_norm"`
	UserPartidPlayRateNorm                    float32 `json:"user_partid_play_rate_norm"`
	UserPartidPlayVideoCountRateNorm          float32 `json:"user_partid_play_video_count_rate_norm"`
	UserPartidPlayVideoCountSumeRateNorm      float32 `json:"user_partid_play_video_count_sume_rate_norm"`
	UserPartidPlayVideoDurSumeRateNorm        float32 `json:"user_partid_play_video_dur_sume_rate_norm"`
	UserPartidPlayVideoRateNorm               float32 `json:"user_partid_play_video_rate_norm"`
	UserPartidTediumAllCountRateNorm          float32 `json:"user_partid_tedium_all_count_rate_norm"`
	UserPartidTediumAllCountSumeRateNorm      float32 `json:"user_partid_tedium_all_count_sume_rate_norm"`
	UserPartidTediumCountRateNorm             float32 `json:"user_partid_tedium_count_rate_norm"`
	UserPartidTediumCountSumeRateNorm         float32 `json:"user_partid_tedium_count_sume_rate_norm"`
	UserPartidViewImgCountSumeRateNorm        float32 `json:"user_partid_view_img_count_sume_rate_norm"`
	UserPartidViewImgDurImgRateNorm           float32 `json:"user_partid_view_img_dur_img_rate_norm"`
	UserPtypeDetailCountRateNorm              float32 `json:"user_ptype_detail_count_rate_norm"`
	UserPtypeGsumeCountRateNorm               float32 `json:"user_ptype_gsume_count_rate_norm"`
	UserPtypeGsumeCountSumeRateNorm           float32 `json:"user_ptype_gsume_count_sume_rate_norm"`
	UserPtypePlayRateNorm                     float32 `json:"user_ptype_play_rate_norm"`
	UserPtypePlayReviewVideoDurDetailRateNorm float32 `json:"user_ptype_play_review_video_dur_detail_rate_norm"`
	UserPtypePlayVideoCountRateNorm           float32 `json:"user_ptype_play_video_count_rate_norm"`
	UserPtypePlayVideoCountSumeRateNorm       float32 `json:"user_ptype_play_video_count_sume_rate_norm"`
	UserPtypePlayVideoDurRateNorm             float32 `json:"user_ptype_play_video_dur_rate_norm"`
	UserPtypePlayVideoDurSumeRateNorm         float32 `json:"user_ptype_play_video_dur_sume_rate_norm"`
	UserPtypePlayVideoRateNorm                float32 `json:"user_ptype_play_video_rate_norm"`
	UserPtypeShareCountSumeRateNorm           float32 `json:"user_ptype_share_count_sume_rate_norm"`
	UserPtypeStayTimeSumeRateNorm             float32 `json:"user_ptype_stay_time_sume_rate_norm"`
	UserPtypeSumeCountRateNorm                float32 `json:"user_ptype_sume_count_rate_norm"`
	UserPtypeTediumCountRateNorm              float32 `json:"user_ptype_tedium_count_rate_norm"`
	UserPtypeTediumCountSumeRateNorm          float32 `json:"user_ptype_tedium_count_sume_rate_norm"`
	UserPtypeViewReviewImgCountSumeRateNorm   float32 `json:"user_ptype_view_review_img_count_sume_rate_norm"`
	UserPtypeViewReviewImgDurSumeRateNorm     float32 `json:"user_ptype_view_review_img_dur_sume_rate_norm"`
}

func Test03() {
	jsonBuf := `{"mid":20000004,"pid":20000004,"expose_minute": 10000,"rank": 1000,"gender": 10,"ptype": 1000,"tid": 1000004,"is_student": 10,"nt": 100,"filter": 1000,"channel": 50,"vdur": 1000,"source": 1000,"direction": 10,"profession": 10,"student": 10,"age": 100,"zy_age": 1000,"reg_age": 1000,"isreg": 3,"history_len": 10000,"partid": 100000,"post_age": 1000,"expose_week": 10,"expose_hour": 30,"expose_quarter": 1500,"weekday": 10}`
	var s PPCtrDcnSlotSt
	fmt.Printf("jsonBuf:%v\n", jsonBuf)
	fmt.Printf("PPCtrDcnSlotSt:%v\n", &s)
	err := json.Unmarshal([]byte(jsonBuf), &s) // 这里要传入指针类型
	if err != nil {
		fmt.Println("err :", err)
		return
	}
	fmt.Printf("s = %+v\n", s)
}
