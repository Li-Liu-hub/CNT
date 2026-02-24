package com.cnt.web.controller.system;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.cnt.common.config.CNTConfig;
import com.cnt.common.utils.StringUtils;

/**
 * 首页
 *
 * @author cnt
 */
@RestController
public class SysIndexController
{
    /** 系统基础配置 */
    @Autowired
    private CNTConfig cntConfig;

    /**
     * 访问首页，提示语
     */
    @RequestMapping("/")
    public String index()
    {
        return StringUtils.format("欢迎使用{}通用系统开发框架，当前版本：v{}，请通过前端地址访问。", cntConfig.getName(), cntConfig.getVersion());
    }
}
