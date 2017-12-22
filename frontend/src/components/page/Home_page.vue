<template>
    <div class="homepage">
        <div style="margin:18% auto;height: 100%;width: 600px;">
          <el-input placeholder="请输入内容" v-model="input5" class="input-with-select" style="width:600px;">
            <el-select v-model="select" slot="prepend" placeholder="全   部" style="width: 120px">
              <el-option label="全   部" value="1"></el-option>
              <el-option label="会议资料" value="2"></el-option>
              <el-option label="视频资料" value="3"></el-option>
              <el-option label="论文期刊" value="4"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return {
            input5: '',
            select: ''
        }
    }
}
</script>
<style scoped>
    .homepage {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 46px;
        background:url('../../assets/background.png') no-repeat;
        background-size: 100% 100%
    }
    .el-select .el-input {
        width: 130px;
    }
    .input-with-select .el-input-group__prepend {
      background-color: #fff;
    }
</style>


