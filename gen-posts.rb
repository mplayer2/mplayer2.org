class Post
  attr_reader :path

  class << self
    def parsed_attr(attr_name)
      define_method attr_name do
        parse_data
        instance_variable_get "@#{attr_name}"
      end
    end
  end

  parsed_attr :title
  parsed_attr :author
  parsed_attr :abstract
  parsed_attr :body

  def initialize(path)
    @path = path
  end

  def date
    date_array.join("/")
  end

  private
  def parse_data
    abstract_ary, body_ary = [] , []
    in_abstract, in_body = false, false
    File.open(path) do |f|
      f.lines.each do |l|
        if l =~ /^\.\. title: (.*)$/
          @title = $1
        elsif l =~ /^\.\. author: (.*)$/
          @author = $1
        elsif l =~ /^\.\. abstract/
          in_abstract = true
        elsif l =~ /^\.\. body/
          in_abstract = false
          in_body = true
        elsif in_abstract
          abstract_ary << l
        elsif in_body
          body_ary << l
        end
      end

      @abstract = abstract_ary.join.strip
      @body = body_ary.join.strip
    end
  end

  def date_array
    (1..3).reduce([]) do |memo, n|
      date_component = path
      n.times { date_component = File.dirname(date_component) }
      memo << File.basename(date_component)
    end.reverse
  end
end

glob_pattern = File.join(File.dirname(__FILE__), "_posts", "**", "**.rst")
Dir.glob(glob_pattern).each do |post_path|
  p = Post.new(post_path)
  puts p.title
  puts p.author
  puts p.abstract
  puts p.body.strip
end
