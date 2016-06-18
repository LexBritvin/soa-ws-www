package web;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import web.category.CategoriesStorage;
import web.product.ProductsStorage;
import web.user.ApplicationSecurity;

@ComponentScan
@EnableAutoConfiguration
public class Application {

	@Bean
	public WebSecurityConfigurerAdapter webSecurityConfigurerAdapter() {
		return new ApplicationSecurity();
	}

	public static void main(String[] args) {
		SpringApplication application = new SpringApplication(Application.class);
        CategoriesStorage.init();
        ProductsStorage.init();
		application.run(args);
	}
}
