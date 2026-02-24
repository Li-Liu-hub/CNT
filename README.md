# CNT 通用系统开发框架

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/CNT-v1.0.0-brightgreen.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/SpringBoot-2.5.x-blue.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Vue-3.x-green.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Element Plus-latest-blue.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/JDK-1.8+-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/MySQL-5.7+-green.svg"></a>
</p>

## 项目简介

CNT 通用系统开发框架是一个基于 SpringBoot + Vue3 前后端分离的 Java 快速开发框架。框架采用微服务架构设计，集成了业界主流的技术栈，提供完整的用户权限管理、日志管理、定时任务等企业级功能，开箱即用，让开发更简单。

---

## 技术选型

### 后端技术

| 技术 | 版本 | 说明 |
|------|------|------|
| Spring Boot | 2.5.x | 核心框架 |
| Spring Security | 5.5.x | 安全认证框架 |
| MyBatis | 3.5.x | 持久层框架 |
| MyBatis-Plus | 3.5.x | MyBatis 增强框架 |
| JWT | 0.9.x | Token令牌 |
| Druid | 1.2.x | 数据库连接池 |
| Redis | 5.x | 分布式缓存 |
| FastJSON | 2.0.x | JSON处理 |
| Lombok | 1.18.x | 代码简化 |

### 前端技术

| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | 3.x | 核心框架 |
| Element Plus | latest | UI组件库 |
| Vite | 4.x | 构建工具 |
| Vue Router | 4.x | 路由管理 |
| Pinia | 2.x | 状态管理 |
| Axios | 1.x | HTTP客户端 |

---

## 项目结构

```
CNT/
├── cnt/                          # 父项目（POM）
│
├── cnt-admin/                    # 后端服务入口
│   ├── src/main/java/
│   │   └── com/cnt/
│   │       └── CNTApplication.java    # 启动类
│   └── src/main/resources/
│       ├── application.yml            # 应用配置
│       ├── application-druid.yml       # 数据库配置
│       └── logback.xml                # 日志配置
│
├── cnt-common/                   # 通用工具模块
│   └── src/main/java/com/cnt/common/
│       ├── annotation/                # 自定义注解
│       │   ├── Excel.java             # Excel导出注解
│       │   ├── DataScope.java         # 数据权限注解
│       │   └── RepeatSubmit.java      # 重复提交注解
│       ├── constant/                  # 常量定义
│       │   ├── CacheConstants.java    # 缓存常量
│       │   ├── HttpStatus.java       # HTTP状态码
│       │   └── Constants.java        # 通用常量
│       ├── core/
│       │   ├── domain/                # 核心domain
│       │   │   ├── AjaxResult.java   # 统一响应结构
│       │   │   ├── BaseEntity.java   # 基础实体
│       │   │   └── LoginUser.java    # 登录用户
│       │   └── redis/
│       │       └── RedisCache.java   # Redis缓存操作
│       ├── exception/                 # 异常定义
│       │   ├── ServiceException.java  # 业务异常
│       │   └── DemoModeException.java # 演示模式异常
│       └── utils/                     # 通用工具类
│           ├── StringUtils.java       # 字符串工具
│           ├── DateUtils.java         # 日期工具
│           ├── ServletUtils.java      # Servlet工具
│           ├── SecurityUtils.java     # 安全工具
│           └── ...
│
├── cnt-framework/               # 框架核心模块
│   └── src/main/java/com/cnt/framework/
│       ├── aspectj/                   # AOP切面
│       │   ├── LogAspect.java         # 日志切面
│       │   ├── RateLimiterAspect.java # 限流切面
│       │   ├── DataSourceAspect.java  # 多数据源切面
│       │   └── DataScopeAspect.java   # 数据权限切面
│       ├── config/                    # 配置类
│       │   ├── SecurityConfig.java    # Spring Security配置
│       │   ├── RedisConfig.java       # Redis配置
│       │   ├── DruidConfig.java       # Druid配置
│       │   ├── MyBatisConfig.java     # MyBatis配置
│       │   └── ThreadPoolConfig.java  # 线程池配置
│       ├── datasource/                # 多数据源
│       │   ├── DynamicDataSource.java
│       │   └── DynamicDataSourceContextHolder.java
│       ├── interceptor/               # 请求拦截器
│       │   ├── RepeatSubmitInterceptor.java    # 防重复提交
│       │   └── impl/SameUrlDataInterceptor.java # 同URL防重复
│       ├── manager/                   # 异步管理器
│       │   ├── AsyncManager.java      # 异步任务管理
│       │   └── factory/AsyncFactory.java # 异步工厂
│       ├── security/                  # 安全认证
│       │   ├── filter/
│       │   │   └── JwtAuthenticationTokenFilter.java  # JWT过滤器
│       │   ├── handle/
│       │   │   ├── AuthenticationEntryPointImpl.java  # 认证失败处理
│       │   │   └── LogoutSuccessHandlerImpl.java      # 登出成功处理
│       │   └── context/
│       │       ├── AuthenticationContextHolder.java
│       │       └── PermissionContextHolder.java
│       └── web/
│           ├── exception/
│           │   └── GlobalExceptionHandler.java  # 全局异常处理
│           ├── service/
│           │   ├── TokenService.java           # Token服务
│           │   ├── SysLoginService.java        # 登录服务
│           │   ├── SysPermissionService.java   # 权限服务
│           │   └── SysPasswordService.java     # 密码服务
│           └── domain/server/
│               └── Server.java                  # 服务器信息
│
├── cnt-system/                  # 系统业务模块
│   └── src/main/java/com/cnt/system/
│       ├── controller/                # 控制器
│       │   ├── SysUserController.java
│       │   ├── SysRoleController.java
│       │   ├── SysMenuController.java
│       │   └── ...
│       ├── service/                   # 业务接口
│       │   ├── impl/                  # 业务实现
│       ├── mapper/                    # 数据访问
│       ├── domain/                    # 实体类
│       └── constant/                  # 业务常量
│
├── cnt-quartz/                  # 定时任务模块
│   └── src/main/java/com/cnt/quartz/
│       ├── controller/
│       ├── service/
│       ├── mapper/
│       └── util/
│           └── JobInvokeUtil.java     # 任务调用工具
│
├── cnt-ui/                      # 前端项目（Vue3）
│   ├── src/
│   │   ├── api/                 # API接口
│   │   ├── assets/              # 静态资源
│   │   ├── components/          # 公共组件
│   │   ├── layout/              # 布局组件
│   │   ├── router/              # 路由配置
│   │   ├── utils/               # 工具函数
│   │   └── views/               # 页面视图
│   └── package.json
│
└── sql/                         # 数据库脚本
    ├── cnt_20250522.sql         # 主数据库脚本
    └── quartz.sql               # 定时任务表
```

---

## 核心功能详解

### 1. JWT令牌认证

框架采用 JWT（JSON Web Token）实现无状态的身份认证机制。

#### 1.1 TokenService 核心服务

`TokenService` 是令牌管理的核心类，提供以下功能：

```java
@Component
public class TokenService
{
    // 令牌自定义标识（默认：Authorization）
    @Value("${token.header}")
    private String header;
    
    // 令牌秘钥（配置文件中设置）
    @Value("${token.secret}")
    private String secret;
    
    // 令牌有效期（默认30分钟）
    @Value("${token.expireTime}")
    private int expireTime;
    
    @Autowired
    private RedisCache redisCache;
}
```

**主要方法：**

| 方法 | 说明 |
|------|------|
| `createToken()` | 创建登录用户令牌 |
| `getLoginUser()` | 从请求中获取登录用户信息 |
| `verifyToken()` | 验证令牌有效性并刷新 |
| `refreshToken()` | 刷新令牌有效期 |
| `delLoginUser()` | 删除登录用户信息 |

#### 1.2 JwtAuthenticationTokenFilter 令牌过滤器

每次请求都会经过 JWT 过滤器进行身份验证：

```java
@Component
public class JwtAuthenticationTokenFilter extends OncePerRequestFilter
{
    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                   HttpServletResponse response, 
                                   FilterChain chain) {
        // 1. 从请求头获取Token
        LoginUser loginUser = tokenService.getLoginUser(request);
        
        // 2. 验证Token有效性
        if (StringUtils.isNotNull(loginUser) && 
            StringUtils.isNull(SecurityUtils.getAuthentication())) {
            tokenService.verifyToken(loginUser);
            
            // 3. 设置Spring Security上下文
            UsernamePasswordAuthenticationToken authenticationToken = 
                new UsernamePasswordAuthenticationToken(
                    loginUser, null, loginUser.getAuthorities());
            authenticationToken.setDetails(
                new WebAuthenticationDetailsSource().buildDetails(request));
            SecurityContextHolder.getContext().setAuthentication(authenticationToken);
        }
        chain.doFilter(request, response);
    }
}
```

#### 1.3 Token配置说明

在 `application.yml` 中配置：

```yaml
# Token配置
token:
  # 令牌请求头
  header: Authorization
  # 令牌秘钥（至少32位）
  secret: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
  # 令牌有效期（单位：秒，默认30分钟 = 1800秒）
  expireTime: 1800
  # 令牌续期有效期（单位：秒，默认24小时 = 86400秒）
  renewExpireTime: 86400
```

#### 1.4 Token工作流程

```
1. 用户登录 → 调用 /login 接口
         ↓
2. SysLoginService 验证用户名密码
         ↓
3. TokenService.createToken() 生成JWT令牌
         ↓
4. 返回Token给前端（存入Cookie或LocalStorage）
         ↓
5. 后续请求携带Token → JwtAuthenticationTokenFilter拦截
         ↓
6. 解析Token获取用户信息 → 验证并加载权限
         ↓
7. 设置SecurityContext → 放行请求
```

---

### 2. 全局异常处理器

框架通过 `@RestControllerAdvice` 实现统一的异常处理，返回规范的JSON响应。

#### 2.1 GlobalExceptionHandler 核心类

```java
@RestControllerAdvice
public class GlobalExceptionHandler
{
    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);
}
```

#### 2.2 异常处理详解

| 异常类型 | 处理方法 | 返回状态码 | 说明 |
|----------|----------|------------|------|
| `AccessDeniedException` | `handleAccessDeniedException()` | 403 | 权限校验失败 |
| `HttpRequestMethodNotSupportedException` | `handleHttpRequestMethodNotSupported()` | 405 | 请求方式不支持 |
| `MissingPathVariableException` | `handleMissingPathVariable()` | 500 | 路径变量缺失 |
| `MethodArgumentTypeMismatchException` | `handleMethodArgumentTypeMismatch()` | 400 | 参数类型不匹配 |
| `MethodArgumentNotValidException` | `handleMethodArgumentNotValid()` | 400 | 参数校验失败 |
| `BindException` | `handleBindException()` | 400 | 参数绑定失败 |
| `ServiceException` | `handleServiceException()` | 500 | 业务异常 |
| `Exception` | `handleException()` | 500 | 未知异常 |

#### 2.3 自定义异常

框架提供了两种自定义异常：

**ServiceException - 业务异常：**
```java
throw new ServiceException("用户名或密码错误");
```

**DemoModeException - 演示模式异常：**
```java
throw new DemoModeException("演示模式，不允许操作");
```

#### 2.4 统一响应结构 AjaxResult

所有接口返回统一使用 `AjaxResult`：

```java
public class AjaxResult extends HashMap<String, Object>
{
    public static AjaxResult success() {
        return success("操作成功");
    }
    
    public static AjaxResult success(String message) {
        AjaxResult result = new AjaxResult();
        result.put("code", HttpStatus.SUCCESS);
        result.put("msg", message);
        return result;
    }
    
    public static AjaxResult error() {
        return error("操作失败");
    }
    
    public static AjaxResult error(String message) {
        return error(HttpStatus.ERROR, message);
    }
    
    public static AjaxResult error(int code, String message) {
        AjaxResult result = new AjaxResult();
        result.put("code", code);
        result.put("msg", message);
        return result;
    }
}
```

**响应示例：**

```json
// 成功
{
    "code": 200,
    "msg": "操作成功"
}

// 成功（带数据）
{
    "code": 200,
    "msg": "操作成功",
    "data": {
        "id": 1,
        "name": "张三"
    }
}

// 失败
{
    "code": 500,
    "msg": "系统异常"
}
```

---

### 3. Spring Security安全认证

#### 3.1 SecurityConfig 配置

```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true, securedEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter
{
    @Autowired
    private JwtAuthenticationTokenFilter jwtAuthenticationTokenFilter;
    
    @Autowired
    private AuthenticationEntryPointImpl unauthorizedHandler;
    
    @Autowired
    private LogoutSuccessHandlerImpl logoutSuccessHandler;
    
    @Autowired
    private SysPasswordService passwordService;
    
    @Autowired
    private UserDetailsServiceImpl userDetailsService;
}
```

#### 3.2 安全过滤链配置

| 过滤器 | 说明 |
|--------|------|
| `JwtAuthenticationTokenFilter` | JWT令牌认证 |
| `LogoutSuccessHandlerImpl` | 登出成功处理 |
| `AuthenticationEntryPointImpl` | 认证失败处理 |

#### 3.3 密码加密

框架使用 BCrypt 加密：

```java
// 密码加密
BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
String encodedPassword = passwordEncoder.encode("123456");

// 密码验证
boolean matches = passwordEncoder.matches("123456", encodedPassword);
```

---

### 4. 通用工具类详解

#### 4.1 StringUtils - 字符串工具

```java
public class StringUtils extends org.apache.commons.lang3.StringUtils
{
    // 判断字符串是否为空
    public static boolean isEmpty(String str);
    
    // 判断字符串是否不为空
    public static boolean isNotEmpty(String str);
    
    // 判断字符串是否为空（包含空格）
    public static boolean isBlank(String str);
    
    // 截取字符串
    public static String substring(final String str, int start);
    
    // 格式化字符串
    public static String format(String template, Object... params);
    
    // 判断是否为数字
    public static boolean isNumeric(String str);
}
```

**使用示例：**
```java
// 判空
if (StringUtils.isNotEmpty(username)) {
    // 不为空处理
}

// 格式化
String msg = StringUtils.format("用户{}登录成功", username);

// 截取
String sub = StringUtils.substring(str, 0, 10);
```

#### 4.2 DateUtils - 日期工具

```java
public class DateUtils extends org.apache.commons.lang3.time.DateUtils
{
    // 日期格式常量
    public static final String YYYY = "yyyy";
    public static final String YYYY_MM = "yyyy-MM";
    public static final String YYYY_MM_DD = "yyyy-MM-dd";
    public static final String YYYY_MM_DD_HH_MM_SS = "yyyy-MM-dd HH:mm:ss";
    
    // 获取当前日期
    public static Date getNowDate();
    
    // 解析日期字符串
    public static Date parseDate(String dateStr);
    
    // 格式化日期
    public static String format(Date date);
    public static String format(Date date, String pattern);
    
    // 日期加减
    public static Date addDays(Date date, int amount);
    public static Date addHours(Date date, int amount);
    
    // 获取时间戳
    public static long getMillis(Date date);
    
    // 判断是否为同一天
    public static boolean isSameDay(Date date1, Date date2);
}
```

**使用示例：**
```java
// 格式化日期
String dateStr = DateUtils.format(new Date(), DateUtils.YYYY_MM_DD_HH_MM_SS);

// 日期加减
Date nextWeek = DateUtils.addDays(new Date(), 7);

// 解析日期
Date date = DateUtils.parseDate("2026-01-01");
```

#### 4.3 ServletUtils - Servlet工具

```java
public class ServletUtils
{
    // 获取请求参数
    public static String getParameter(String name);
    public static String[] getParameterValues(String name);
    
    // 获取请求头
    public static String getHeader(String name);
    
    // 获取请求属性
    public static Object getAttribute(String name);
    
    // 获取客户端IP
    public static String getClientIp();
    
    // 获取请求参数Map
    public static Map<String, String[]> getParamMap(HttpServletRequest request);
    
    // 判断是否为Ajax请求
    public static boolean isAjaxRequest(HttpServletRequest request);
    
    // 获取请求完整URL
    public static String getRequestUrl(HttpServletRequest request);
}
```

**使用示例：**
```java
// 获取客户端IP
String clientIp = ServletUtils.getClientIp();

// 获取请求参数
String name = ServletUtils.getParameter("name");

// 判断是否为Ajax请求
if (ServletUtils.isAjaxRequest(request)) {
    // Ajax请求处理
}
```

#### 4.4 SecurityUtils - 安全工具

```java
public class SecurityUtils
{
    // 获取当前登录用户
    public static LoginUser getLoginUser();
    
    // 获取当前用户ID
    public static Long getUserId();
    
    // 获取当前用户名
    public static String getUsername();
    
    // 获取当前用户昵称
    public static String getNickName();
    
    // 获取当前用户部门ID
    public static Long getDeptId();
    
    // 获取当前用户权限集合
    public static Set<String> getPermissions();
    
    // 判断是否包含指定权限
    public static boolean hasPermi(String permission);
    
    // 判断是否包含所有权限
    public static boolean hasAllPermi(String... permissions);
}
```

**使用示例：**
```java
// 获取当前用户
LoginUser user = SecurityUtils.getLoginUser();

// 获取用户ID
Long userId = SecurityUtils.getUserId();

// 判断权限
if (SecurityUtils.hasPermi("system:user:add")) {
    // 有添加用户权限
}
```

#### 4.5 IpUtils - IP工具

```java
public class IpUtils
{
    // 获取客户端真实IP
    public static String getIpAddr();
    public static String getIpAddr(HttpServletRequest request);
    
    // 获取本机IP
    public static String getLocalIp();
    
    // IP地址转long
    public static long ipToLong(String ip);
    
    // long转IP地址
    public static String longToIp(long ip);
}
```

#### 4.6 AddressUtils - 地址工具

```java
public class AddressUtils
{
    // 根据IP获取地址（内网返回内网）
    public static String getAddress(String ip);
    
    // 根据IP获取真实地址（需联网）
    public static String getRealAddressByIp(String ip);
}
```

#### 4.7 RedisCache - Redis缓存

```java
@Component
public class RedisCache
{
    // 缓存对象
    public <T> void setCacheObject(final String key, final T value);
    public <T> void setCacheObject(final String key, final T value, final Integer timeout);
    
    // 获取缓存对象
    public <T> T getCacheObject(final String key);
    
    // 删除缓存
    public boolean deleteObject(final String key);
    
    // 缓存List
    public <T> void setCacheList(final String key, final List<T> dataList);
    public <T> List<T> getCacheList(final String key);
    
    // 缓存Set
    public <T> void setCacheSet(final String key, final Set<T> dataSet);
    public <T> Set<T> getCacheSet(final String key);
    
    // 缓存Map
    public <T> void setCacheMap(final String key, final Map<String, T> dataMap);
    public <T> Map<String, T> getCacheMap(final String key);
    
    // 设置过期时间
    public boolean expire(final String key, final long timeout);
    
    // 获取剩余时间
    public long getExpire(final String key);
}
```

**使用示例：**
```java
@Autowired
private RedisCache redisCache;

// 缓存对象
redisCache.setCacheObject("user:1", user);

// 获取缓存
User user = redisCache.getCacheObject("user:1");

// 缓存List
redisCache.setCacheList("userList", userList);
List<User> list = redisCache.getCacheList("userList");

// 设置过期时间（30分钟）
redisCache.setCacheObject("token", token, 30 * 60);
```

#### 4.8 ReflectUtils - 反射工具

```java
public class ReflectUtils
{
    // 获取字段值
    public static Object getFieldValue(Object obj, String fieldName);
    
    // 设置字段值
    public static void setFieldValue(Object obj, String fieldName, Object value);
    
    // 获取方法
    public static Method getMethod(Class<?> clazz, String methodName, Class<?>... params);
    
    // 调用方法
    public static Object invokeMethod(Object obj, String methodName, Object... args);
    
    // 获取类的所有字段
    public static Field[] getFields(Class<?> clazz);
    
    // 获取类及其父类的所有字段
    public static Field[] getAllFields(Class<?> clazz);
}
```

#### 4.9 IdUtils - ID工具

```java
public class IdUtils
{
    // 生成UUID（无中划线）
    public static String randomUUID();
    
    // 生成UUID（有中划线）
    public static String uuid();
    
    // 简化UUID（8位）
    public static String simpleUUID();
}
```

#### 4.10 FileUtils - 文件工具

```java
public class FileUtils
{
    // 获取文件扩展名
    public static String getExtension(File file);
    
    // 获取文件名（不含扩展名）
    public static String getNameWithoutExtension(File file);
    
    // 创建目录
    public static void mkdirs(String path);
    
    // 删除文件
    public static boolean deleteFile(File file);
    
    // 读取文件内容
    public static String readFileToString(File file);
    
    // 写入文件
    public static void writeStringToFile(File file, String content);
}
```

#### 4.11 BeanUtils - Bean工具

```java
public class BeanUtils extends org.springframework.beans.BeanUtils
{
    // 对象属性拷贝（忽略null值）
    public static void copyPropertiesIgnoreNull(Object source, Object target);
    
    // 判断对象是否为空
    public static boolean isEmpty(Object obj);
    
    // 判断对象是否不为空
    public static boolean isNotEmpty(Object obj);
}
```

---

### 5. 自定义注解

#### 5.1 @RepeatSubmit - 防重复提交

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface RepeatSubmit
{
    // 间隔时间（毫秒），默认2000
    int interval() default 2000;
    
    // 提示消息
    String message() default "重复提交，请稍后再试";
}
```

**使用示例：**
```java
@RepeatSubmit
@PostMapping("/save")
public AjaxResult save(@RequestBody User user) {
    return AjaxResult.success(userService.save(user));
}
```

#### 5.2 @Excel - Excel导出

```java
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Excel
{
    // 列名
    String name();
    
    // 导出格式（0=文本, 1=数字, 2=日期）
    int cellType() default 0;
    
    // 日期格式
    String dateFormat() default "";
    
    // 字典名称
    String dictType() default "";
    
    // 读取内容转换表达式
    String readConverterExp() default "";
    
    // 分隔符（用于多值转换）
    String separator() default ",";
}
```

**使用示例：**
```java
public class User
{
    @Excel(name = "用户序号")
    private Long userId;
    
    @Excel(name = "用户名称")
    private String userName;
    
    @Excel(name = "用户性别", readConverterExp = "0=男,1=女,2=未知")
    private String sex;
    
    @Excel(name = "手机号码")
    private String phonenumber;
    
    @Excel(name = "状态", dictType = "sys_normal_disable")
    private String status;
}
```

#### 5.3 @DataScope - 数据权限

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface DataScope
{
    // 部门字段名
    String deptField() default "dept_id";
    
    // 权限类型（all=全部数据, dept=部门数据, dept_and_self=部门及以下数据, self=仅本人数据）
    String type() default "all";
}
```

---

### 6. AOP切面

#### 6.1 LogAspect - 日志切面

自动记录操作日志：

```java
@Aspect
@Component
public class LogAspect
{
    // 请求日志内容
    public static final String LOG_INFO = "User:{} do:{} at:{} IP:{}";
    
    // 保存日志
    protected void insertLog(OperLog operLog);
}
```

**日志内容：**
- 操作模块
- 操作类型
- 请求方法
- 请求URL
- 请求参数
- 返回结果
- 操作时间
- 操作用户IP
- 操作用户

#### 6.2 RateLimiterAspect - 限流切面

基于Redis实现分布式限流：

```java
@Aspect
@Component
public class RateLimiterAspect
{
    // 限流注解
    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface RateLimiter
    {
        // 限流时间（秒）
        int time() default 60;
        
        // 限流次数
        int count() default 100;
    }
}
```

#### 6.3 DataSourceAspect - 多数据源切面

动态切换数据源：

```java
@Aspect
@Component
public class DataSourceAspect
{
    // 切换数据源
    public void setDataSource(JoinPoint joinPoint);
    
    // 清除数据源
    public void clearDataSource(JoinPoint joinPoint);
}
```

---

### 7. 异步任务

#### 7.1 AsyncManager - 异步管理器

```java
@Component
public class AsyncManager
{
    //  execute(异步任务)
    public void execute(Runnable task);
    
    //  延迟执行
    public void schedule(Runnable task, long delay, TimeUnit unit);
    
    //  定时执行
    public void scheduleAtFixedRate(Runnable task, long initialDelay, long period, TimeUnit unit);
}
```

#### 7.2 AsyncFactory - 异步工厂

```java
@Component
public class AsyncFactory
{
    // 异步执行登录信息记录
    public static Runnable executeLoginLog(final SysLoginLog loginLog);
    
    // 异步执行访问日志记录
    public static Runnable executeOperLog(final SysOperLog operLog);
}
```

---

### 8. 拦截器

#### 8.1 RepeatSubmitInterceptor - 防重复提交

```java
@Component
public class RepeatSubmitInterceptor implements HandlerInterceptor
{
    @Override
    public boolean preHandle(HttpServletRequest request, 
                            HttpServletResponse response, 
                            Object handler);
}
```

---

## 快速开始

### 环境要求

| 环境 | 版本 |
|------|------|
| JDK | 1.8+ |
| Maven | 3.3+ |
| MySQL | 5.7+ |
| Redis | 5.x |
| Node.js | 14+ |
| npm | 6+ |

### 后端启动

1. **创建数据库**
```sql
CREATE DATABASE cnt CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

2. **导入SQL脚本**
```bash
mysql -u root -p cnt < sql/cnt_20250522.sql
mysql -u root -p cnt < sql/quartz.sql
```

3. **修改配置文件**

修改 `cnt-admin/src/main/resources/application-druid.yml`：

```yaml
# 数据源配置
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      driver-class-name: com.mysql.cj.jdbc.Driver
      url: jdbc:mysql://localhost:3306/cnt?useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&useSSL=false&serverTimezone=GMT%2B8
      username: root
      password: 123456

# Redis配置
spring:
  redis:
    host: localhost
    port: 6379
    password: 123456
```

4. **编译启动**
```bash
# 编译
mvn clean install -DskipTests

# 启动
cd cnt-admin
mvn spring-boot:run

# 或运行主类
java -jar cnt-admin/target/cnt-admin.jar
```

### 前端启动

```bash
# 进入前端目录
cd cnt-ui

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

---

## 默认配置

| 配置项 | 默认值 |
|--------|--------|
| 后端端口 | 8080 |
| 前端端口 | 80 |
| 数据库 | MySQL (localhost:3306) |
| 缓存 | Redis (localhost:6379) |
| Token有效期 | 30分钟 |
| 默认账号 | admin / admin123 |
| 版本 | 1.0.0 |

---

## 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-02-24 | 初始版本 |

---

## 许可证

MIT License
