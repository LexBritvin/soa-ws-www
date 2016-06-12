<?php

/* themes/omega/omega/templates/omega-indicator.html.twig */
class __TwigTemplate_f04e3a86480c4826229b052e27d13377a8d3d6e71f640245439c617fac552b9b extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $tags = array();
        $filters = array();
        $functions = array();

        try {
            $this->env->getExtension('sandbox')->checkSecurity(
                array(),
                array(),
                array()
            );
        } catch (Twig_Sandbox_SecurityError $e) {
            $e->setTemplateFile($this->getTemplateName());

            if ($e instanceof Twig_Sandbox_SecurityNotAllowedTagError && isset($tags[$e->getTagName()])) {
                $e->setTemplateLine($tags[$e->getTagName()]);
            } elseif ($e instanceof Twig_Sandbox_SecurityNotAllowedFilterError && isset($filters[$e->getFilterName()])) {
                $e->setTemplateLine($filters[$e->getFilterName()]);
            } elseif ($e instanceof Twig_Sandbox_SecurityNotAllowedFunctionError && isset($functions[$e->getFunctionName()])) {
                $e->setTemplateLine($functions[$e->getFunctionName()]);
            }

            throw $e;
        }

        // line 1
        echo "<div id=\"omega-screen--indicator\" class=\"clearfix\">
  <div class=\"ologo\">
    ";
        // line 3
        echo $this->env->getExtension('sandbox')->ensureToStringAllowed($this->env->getExtension('drupal_core')->escapeFilter($this->env, (isset($context["logo"]) ? $context["logo"] : null), "html", null, true));
        echo "
  </div>
  <div class=\"indicator-data\">
    <div class=\"screen-size\">
      <h5>@screen width:</h5>
      <span class=\"data\"></span>
    </div>
    <div class=\"theme-name\">
      <h5>@theme:</h5>
      <span class=\"data\"></span>
    </div>
    <div class=\"screen-query\">
      <h5>@breakpoints:</h5>
      <span class=\"data\"></span>
    </div>
    <div class=\"screen-layout\">
      <h5>@layout:</h5>
      <span class=\"data\"></span>
    </div>
  </div>
</div>";
    }

    public function getTemplateName()
    {
        return "themes/omega/omega/templates/omega-indicator.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  47 => 3,  43 => 1,);
    }
}
/* <div id="omega-screen--indicator" class="clearfix">*/
/*   <div class="ologo">*/
/*     {{ logo }}*/
/*   </div>*/
/*   <div class="indicator-data">*/
/*     <div class="screen-size">*/
/*       <h5>@screen width:</h5>*/
/*       <span class="data"></span>*/
/*     </div>*/
/*     <div class="theme-name">*/
/*       <h5>@theme:</h5>*/
/*       <span class="data"></span>*/
/*     </div>*/
/*     <div class="screen-query">*/
/*       <h5>@breakpoints:</h5>*/
/*       <span class="data"></span>*/
/*     </div>*/
/*     <div class="screen-layout">*/
/*       <h5>@layout:</h5>*/
/*       <span class="data"></span>*/
/*     </div>*/
/*   </div>*/
/* </div>*/
