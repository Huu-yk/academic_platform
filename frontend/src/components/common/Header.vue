<template>
    <div class="header">
        <el-menu :default-active="onRoutes" class="el-menu-demo" mode="horizontal" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title" ><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index" style="line-height: 45px;">{{ subItem.title }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" style="line-height: 45px;">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                items: [
                    {
                        icon: 'el-icon-fa-home fa-fw',
                        index: '/',
                        title: '首页'
                    },
                    {
                        icon: 'el-icon-menu',
                        index: 'page1',
                        title: '测试页1',
                    },
                    {
                        icon: 'el-icon-menu',
                        index: 'page2',
                        title: '测试页2',
                    }
                ]
            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        },
        methods:{

        }
    }
</script>
